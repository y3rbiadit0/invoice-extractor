from openai import OpenAI
from openai.types.chat import ParsedChatCompletion

from models import GenericInvoiceModel
from .open_ai_conf import OpenAIConfig


class OpenAPIClient:

    __open_ai_client: OpenAI

    def __init__(self):
        self.__open_ai_client = OpenAI()

    def parsing_prompt(
        self,
        open_ai_config: OpenAIConfig,
        raw_invoice_text: str,
    ) -> ParsedChatCompletion:
        completion = self.__open_ai_client.beta.chat.completions.parse(
            model=open_ai_config.model,
            messages=[
                {"role": open_ai_config.role, "content": open_ai_config.prompt_text},
                {"role": "user", "content": raw_invoice_text},
            ],
            response_format=GenericInvoiceModel,
        )
        return completion
