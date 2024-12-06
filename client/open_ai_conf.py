from dataclasses import dataclass
from typing import Literal


@dataclass
class OpenAIConfig:
    role: Literal["user", "system"] = "system"
    model: str = "gpt-4o-2024-08-06"
    temperature: float = 0.2
    prompt_text: str = (
        f"You are a parser of invoices. You will receive text that is being parsed from pdf images."
        f"Consider that each item in the invoice must be transformed into a row, so if the invoice has 5 items, the excel must contain 5 rows."
        f"You need to extract the following data:"
        f"Here is the response "
        "format: {"
        '{"file_name": "invoice_1234.pdf", "doc_id": "INV-2024-001", "issue_date": "2024-12-06", "item_code": "ITEM-001", "description": "Laptop", "measure_unit": "pcs", "quantity": "1", "unit_price": "1000.00", "total_amount": "1000.00", "supplier_name": "Tech Supplies Inc.", "supplier_vat_number": "123456789"}'
        "}."
    )
