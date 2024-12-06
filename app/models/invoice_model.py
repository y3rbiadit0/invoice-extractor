import abc
from typing import Optional, List

import pandas as pd
from pydantic import BaseModel


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

    def to_xlsx(self, output_folder: str):
        # Create a DataFrame
        output_filename = f"{output_folder}/{self.file_name.split('.')[0]}.xlsx"

        df = pd.DataFrame([self.model_dump()])

        # Save to Excel
        df.to_excel(output_filename, index=False, engine="openpyxl")

    def to_json(self, output_folder: str):
        file_path = f"{output_folder}/{self.file_name.split('.')[0]}.json"
        with open(file_path, "w") as file:
            file.write(self.model_dump_json(indent=4))
