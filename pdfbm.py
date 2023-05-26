import argparse
import os
import PyPDF2
import pytesseract
from PIL import Image
import io
import re
import multiprocessing

# Create an argument parser
parser = argparse.ArgumentParser(description='Extract text from an image-based PDF file')
parser.add_argument('input_file', type=str, help='Path to the input PDF file')
parser.add_argument('-o', '--output_dir', type=str, default='output', help='Directory for bulk exports')
parser.add_argument('-t', '--output_type', type=str, default='txt', choices=['pdf', 'txt', 'rtc'],
                    help='Type of output file (pdf, txt, rtc)')
args = parser.parse_args()

# Set the Tesseract OCR executable path
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'  # Update with the correct path

# Regular expression pattern to filter out non-standard characters
non_standard_chars_pattern = re.compile(r'[^a-zA-Z0-9\s.,?!]')

# Create the output file name based on the input file name and output type
input_filename = os.path.basename(args.input_file)
output_filename = f"{os.path.splitext(input_filename)[0]}_update.{args.output_type}"

# Determine the output file path based on the provided output directory
output_dir = os.path.join(os.getcwd(), args.output_dir)
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, output_filename)

# Define the worker function for parallel processing
def process_page(page_num):
    # Open the PDF file
    with open(args.input_file, 'rb') as pdf_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Extract the xobjects (including images) from the page
        xobjects = pdf_reader.pages[page_num]['/Resources']['/XObject'].get_object()

        # Iterate through each xobject
        extracted_text = []
        for obj in xobjects:
            if xobjects[obj]['/Subtype'] == '/Image':
                # Get the image data
                image_data = xobjects[obj]._data

                # Convert the image data to a PIL Image object
                image_obj = Image.open(io.BytesIO(image_data))

                # Apply OCR using pytesseract
                text = pytesseract.image_to_string(image_obj)

                # Filter out non-standard characters using regular expressions
                filtered_text = non_standard_chars_pattern.sub('', text)

                # Append the extracted text to the list
                extracted_text.append(filtered_text)

        return extracted_text

# Entry point of the script
if __name__ == '__main__':
    # Get the total number of pages in the PDF
    with open(args.input_file, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)

    # Create a multiprocessing pool with the number of CPU cores available
    pool = multiprocessing.Pool()

    # Process pages in parallel
    extracted_text_list = pool.map(process_page, range(num_pages))

    # Close the pool
    pool.close()
    pool.join()

    # Flatten the extracted text list
    extracted_text = [text for page_text in extracted_text_list for text in page_text]

    # Write the extracted text to the output file
    with open(output_path, 'w') as output_file:
        output_file.write('\n\n'.join(extracted_text))

    print(f"Text extracted successfully. Output file: {output_path}")
