
# PDFBeMine - Text Extraction Solution

PDFBeMine is an innovative application designed to streamline the process of extracting text from PDF files. It provides a user-friendly and efficient solution for obtaining text content from image-based PDFs, utilizing advanced OCR technology.

## Key Features

- Accurate Text Extraction: PDFBeMine employs intelligent Optical Character Recognition (OCR) algorithms to accurately extract text from image-based PDF files.
- PDF Parsing: The app parses the structure of PDF files, identifying images and text elements to ensure precise extraction of targeted content.
- Text Filtering: PDFBeMine applies sophisticated filtering techniques to remove non-standard characters and enhance the quality of extracted text.
- Bulk Processing: Users can extract text from multiple PDF files simultaneously, saving time and effort.
- Customizable Output: PDFBeMine allows users to choose their preferred output format, including PDF, plain text, or rich text format (RTC), catering to diverse use cases.

## Installation

To use PDFBeMine, follow these steps:

1. Clone the repository:

`git clone https://github.com/jbrenan/PDFBeMine.git`

2. Install the required dependencies:

`pip install -r requirements.txt`

3. Set the path to the Tesseract OCR executable in the config.py file:

`OCR_EXECUTABLE_PATH = '/opt/homebrew/bin/tesseract'`

4. Run the app:

`python pdfbm.py -i input.pdf -o output.txt`

Replace input.pdf with the path to your input PDF file, and output.txt with the desired output file.

## Usage
PDFBeMine offers a simple command-line interface. Here's an example usage:

`python pdfbm.py -i input.pdf -o output.txt`

` -i or --input: Path to the input PDF file `
` -o or --output: Path to the output file `

Additional options:

`-t or --output-type: Type of output file (pdf, txt, rtc). Default: txt`
`-d or --output-dir: Directory for bulk exports. Default: output`

## Examples
Extract text from a PDF file and save it as plain text:
`python pdfbm.py -i input.pdf -o output.txt`

Extract text from a PDF file and save it as a PDF:
`python pdfbm.py -i input.pdf -o output.pdf -t pdf`

Bulk extraction from a directory and save as plain text:
`python pdfbm.py -i directory_path -o output.txt -d bulk_output`


License
This project is licensed under the MIT License.
