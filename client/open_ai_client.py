import os
from typing import Dict

from openai import AsyncOpenAI, AsyncStream

from models import GenericInvoiceModel
from .base_api_client import BaseAsyncClient
from .open_ai_conf import OpenAIConfig


class OpenAPIClient(BaseAsyncClient):

    __open_ai_client: AsyncOpenAI

    def __init__(self):
        api_key = os.getenv("OPEN_AI_API_KEY")
        self.__open_ai_client = AsyncOpenAI(api_key=api_key)

    async def parsing_prompt(
        self,
        open_ai_config: OpenAIConfig,
    ) -> AsyncStream:
        completion = self.__open_ai_client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": open_ai_config.prompt_text},
                {"role": "user", "content": "how can I solve 8x + 7 = -23"},
            ],
            response_format=GenericInvoiceModel,
        )
        return await completion
