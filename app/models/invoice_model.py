import abc
import json
import logging
from typing import Optional, List, Dict

import pandas as pd
from pydantic import BaseModel

logger = logging.getLogger(__name__)

class InvoiceModelInterface(abc.ABC):
    @abc.abstractmethod
    def to_json(self, path: str):
        pass

    @abc.abstractmethod
    def to_xlsx(self, path: str):
        pass


class InvoiceItemModel(BaseModel):
    item_code: Optional[str]
    description: Optional[str]
    measure_unit: Optional[str]
    quantity: Optional[str]
    unit_price: Optional[str]
    total_amount: Optional[str]


class GenericInvoiceModel(BaseModel, InvoiceModelInterface):
    file_name: str
    invoice_id: Optional[str]
    issue_date: Optional[str]
    invoice_items: List[InvoiceItemModel]
    supplier_name: Optional[str]
    supplier_vat_number: Optional[str]

    def invoice_lines(self) -> List[Dict]:
        invoice_lines = []
        for invoice_item in self.invoice_items:
            entry = self.model_dump(exclude={"invoice_items", "file_name"})
            entry.update(invoice_item.model_dump())
            invoice_lines.append(entry)
        return invoice_lines

    def to_xlsx(self, output_folder: str):
        output_filename = f"{output_folder}/{self.file_name.split('.')[0]}.xlsx"
        df = pd.DataFrame(self.invoice_lines())

        # Save to Excel
        df.to_excel(output_filename, index=False, engine="openpyxl")
        logger.info(f"Wrote {output_filename}")

    def to_json(self, output_folder: str):
        file_path = f"{output_folder}/{self.file_name.split('.')[0]}.json"
        with open(file_path, "w") as file:
            file.write(json.dumps(self.invoice_lines(), indent=4))
            logger.info(f"Wrote {file_path}")
