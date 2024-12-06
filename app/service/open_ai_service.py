from typing import List

from ..client.open_ai_client import OpenAPIClient
from ..client.open_ai_conf import OpenAIConfig
from ..models import GenericInvoiceModel


class OpenAIService:

    _client: OpenAPIClient
    _config: OpenAIConfig

    def __init__(self):
        self._client = OpenAPIClient()
        self._config = OpenAIConfig()

    def parse_invoice(self, raw_invoice_text: str) -> List[GenericInvoiceModel]:
        data = self._client.parsing_prompt(
            open_ai_config=self._config, raw_invoice_text=raw_invoice_text
        )
        return [data.choices[0].message.parsed]
