from dataclasses import dataclass
from typing import Literal


@dataclass
class OpenAIConfig:
    role: Literal["user", "system"] = "system"
    model: str = "gpt-4o"
    temperature: float = 0.7
    prompt_text: str = (
        f"You are a parser of italian invoices. You will receive text that is being parsed from pdf images. You will attempt extract the following data:"
        f"invoice_id, invoice_issue_date, item_code, item_description, measure_unit, quantity, unit_price, total amount, supplier vat number, suppplier name"
        f"Each item in the invoice must be transformed into a row that will refer to the same invoice_id"
        "##############################"
        "Considerations for data types:"
            f"For quantities or prices, always set them as type float, to make them compatible for JSON format, so they can be serialized/deserialized."
            f"For dates, always set them as type string using the YYYY-MM-DD format, so they can be serialized/deserialized."
            f"For descriptions, always set them as uppercase string"
            f"For total amount, only in case is not explicit, multiply `quantity` for `unit_price`, if not, take the value from parsing"
        f"############################"
        f"Task: extract the following data into the following response format:"
        "["
        '{"file_name": "invoice_1234.pdf", "invoice_id": "INV-2024-001", "issue_date": "2024-12-06", "item_code": "ITEM-001", "description": "Laptop", "measure_unit": "pcs", "quantity": "1", "unit_price": "1000.00", "total_amount": "1000.00", "supplier_name": "Tech Supplies Inc.", "supplier_vat_number": "123456789"}'
        '{"file_name": "invoice_1234.pdf", "invoice_id": "INV-2024-001", "issue_date": "2024-12-06", "item_code": "ITEM-002", "description": "Laptop", "measure_unit": "pcs", "quantity": "1", "unit_price": "1000.00", "total_amount": "1000.00", "supplier_name": "Tech Supplies Inc.", "supplier_vat_number": "123456789"}'
        "]."
    )
