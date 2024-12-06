import os

import pytesseract
from pdf2image import convert_from_path


def _get_files_from_input_data(folder_path: str = "input_data"):
    return [
        f
        for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]


def main():
    files = _get_files_from_input_data()
    for file in files:
        extract_text(f"input_data/{file}")


def extract_text(file_path: str = "input_data") -> str:
    images = convert_from_path(file_path)
    text_data = ""
    for image in images:
        text = pytesseract.image_to_string(image)
        text_data += text + "\n"
    return text_data


if __name__ == "__main__":
    main()
