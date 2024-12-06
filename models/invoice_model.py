import abc
from typing import Optional

import pandas as pd
from pydantic import BaseModel


class InvoiceModelInterface(abc.ABC):
    @abc.abstractmethod
    def to_json(self):
        pass

    @abc.abstractmethod
    def to_xlsx(self):
        pass


class GenericInvoiceModel(BaseModel, InvoiceModelInterface):
    file_name: str
    doc_id: Optional[str]
    issue_date: Optional[str]
    item_code: Optional[str]
    description: Optional[str]
    measure_unit: Optional[str]
    quantity: Optional[str]
    unit_price: Optional[str]
    total_amount: Optional[str]
    supplier_name: Optional[str]
    supplier_vat_number: Optional[str]

    def to_xlsx(self):
        # Create a DataFrame
        output_filename = f"{self.file_name.split('.')[0]}"

        df = pd.DataFrame([self.model_dump_json()])

        # Save to Excel
        df.to_excel(output_filename, index=False, engine="openpyxl")

    def to_json(self):
        df = pd.DataFrame([self.model_dump_json()])
        df.to_json(path_or_buf=f"{self.file_name.split('.')[0]}.json")
