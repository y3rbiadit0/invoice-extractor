# Invoice - Extractor
Extract data from invoices in PDF format. This is a small project to demonstrate the concept of using models like OpenAI to assist in parsing and normalizing data.

This project make use of four main libraries:
1. [`pdf2image`](https://github.com/Belval/pdf2image) - Transform PDF to an image
2. [`pytesseract`](https://github.com/madmaze/pytesseract) - Use OCR to get text from image (Also [easyocr](https://github.com/JaidedAI/EasyOCR) could be used as well)
3. [`openai`](https://github.com/openai/openai-python) - Process text and format data (`model: gpt-4o`)
4. [`openpyxl`](https://openpyxl.readthedocs.io/en/stable/tutorial.html) - Export it in a `.xslx` format

## 1. Setup - Dev Environment

You can install the required libraries using `poetry`:
1. Clone the project - `git clone https://github.com/y3rbiadit0/invoice-extractor`
2. Install [PyPoetry](https://python-poetry.org/docs/#installation) 
3. Install Dependencies
```bash
poetry install
```
4. Create your `.env` file with the following format:
```dotenv
INV_EXTRACTOR_INPUT_DATA=input_data     # Input path folder
INV_EXTRACTOR_OUTPUT_DATA=output        # Output path folder
OPENAI_API_KEY=FILL_ME_WITH_YOUR_API_KEY
```

5. Run the project! -> Go to `#Usage` section

## 2. Usage
```bash
poetry run python main.py
```