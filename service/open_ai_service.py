import asyncio
from typing import List

from client.open_ai_client import OpenAPIClient
from client.open_ai_conf import OpenAIConfig
from models import GenericInvoiceModel


class OpenAIService:

    _client: OpenAPIClient
    _config: OpenAIConfig

    def __init__(self):
        self._client = OpenAPIClient()
        self._config = OpenAIConfig()

    def parse_invoice(self) -> List[GenericInvoiceModel]:
        data = asyncio.run(self._client.parsing_prompt(open_ai_config=self._config))
        import ipdb

        ipdb.set_trace()
        return data
