import os
from tkinter import Image
from typing import List

import pytesseract
from pdf2image import convert_from_path

from models import GenericInvoiceModel
from service.open_ai_service import OpenAIService


def main():
    files = files_to_process()
    for file in files:
        raw_data = extract_text(f"input_data/{file}")
        invoice_model = parse_invoice(raw_data)
        invoice_model.to_json()
        invoice_model.to_xlsx()


def files_to_process(folder_path: str = "input_data"):
    return [
        f
        for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]


def extract_text(file_path: str = "input_data") -> str:
    images: List[Image] = convert_from_path(file_path)
    text_data = ""
    for image in images:
        text = pytesseract.image_to_string(image)
        text_data += text + "\n"
    return text_data


def parse_invoice(invoice_raw_data: str) -> GenericInvoiceModel:
    open_ai_service = OpenAIService()
    return GenericInvoiceModel()


if __name__ == "__main__":
    main()
