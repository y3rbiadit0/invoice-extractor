from dataclasses import dataclass
from typing import Literal


@dataclass
class OpenAIConfig:
    role: Literal["user", "system"] = "system"
    model: str = "gpt-4o"
    temperature: float = 0.7
    prompt_text: str = (
        "You are a parser of Italian invoices. You will receive text that is being parsed from PDF images. "
        "Your task is to extract the following fields for all items in the invoice:"
        "\n- invoice_id\n- invoice_issue_date\n- item_code\n- item_description\n- measure_unit\n- quantity\n- unit_price\n- total_amount\n- supplier_vat_number\n- supplier_name"
        "\n##############################"
        "\n**Considerations for data types:**"
        "\n- Quantities and prices should be floats. (Check for 'prezzo', 'quantita')"
        "\n- Dates should be strings in the format YYYY-MM-DD."
        "\n- Descriptions should be uppercase strings."
        "\n- For total_amount, calculate it as quantity * unit_price if not explicit."
        "\n##############################"
        "\n**Output JSON format:** The JSON should include an array of items when an invoice contains multiple items. Example output for two items:"
        "["
        '{"file_name": "invoice_1234.pdf", "invoice_id": "INV-2024-001", "issue_date": "2024-12-06", "item_code": "ITEM-001", "description": "LAPTOP", "measure_unit": "PCS", "quantity": 1.0, "unit_price": 1000.0, "total_amount": 1000.0, "supplier_name": "TECH SUPPLIES INC.", "supplier_vat_number": "123456789"},'
        '{"file_name": "invoice_1234.pdf", "invoice_id": "INV-2024-001", "issue_date": "2024-12-06", "item_code": "ITEM-002", "description": "MOUSE", "measure_unit": "PCS", "quantity": 2.0, "unit_price": 25.0, "total_amount": 50.0, "supplier_name": "TECH SUPPLIES INC.", "supplier_vat_number": "123456789"}'
        "]"
    )
