from typing import Dict

import aiohttp


class BaseAsyncClient:
    base_url = "insert_base_url"
    request_headers: Dict = {}
    session: aiohttp.ClientSession = aiohttp.ClientSession()
