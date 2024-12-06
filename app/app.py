import logging
import os
from tkinter import Image
from typing import List

import dotenv
import pytesseract
from pdf2image import convert_from_path

from .models import GenericInvoiceModel
from .service.open_ai_service import OpenAIService

logger = logging.getLogger(__name__)


class App:
    _input_folder: str
    _output_folder: str

    def __init__(self):
        self._set_logger_config()
        self._load_environment_variables()

        self._input_folder = os.getenv("INV_EXTRACTOR_INPUT_DATA")
        self._output_folder = os.getenv("INV_EXTRACTOR_OUTPUT_DATA")
        if not os.path.exists(self._output_folder):
            os.makedirs(self._output_folder)

    def _load_environment_variables(self):
        dotenv.load_dotenv()

    def _set_logger_config(self):
        logging.basicConfig(
            level=logging.INFO,
            format='[%(asctime)s - %(levelname)s]: %(message)s',
        )

    def process_files(self):
        input_files = self._get_input_files(self._input_folder)

        for input_file in input_files:
            file_name = input_file.split(".")[0]
            raw_data = self._extract_text(f"{self._input_folder}/{input_file}")
            logger.info("Processing file: %s", input_file)

            invoice_model = self._parse_invoice(raw_data)[0]

            invoice_model.file_name = file_name
            invoice_model.to_json(output_folder=f"{self._output_folder}")
            invoice_model.to_xlsx(output_folder=f"{self._output_folder}")

    def _get_input_files(self, folder_path: str) -> List[str]:
        return [
            input_file
            for input_file in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, input_file))
        ]

    def _extract_text(self, file_path: str = "input_data") -> str:
        images: List[Image] = convert_from_path(file_path)
        text_data = ""
        for image in images:
            text = pytesseract.image_to_string(image)
            text_data += text + "\n"
        return text_data

    def _parse_invoice(self, invoice_raw_data: str) -> List[GenericInvoiceModel]:
        invoice_articles = OpenAIService().parse_invoice(invoice_raw_data)
        return invoice_articles
