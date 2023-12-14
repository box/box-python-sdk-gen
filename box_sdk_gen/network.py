import requests
from typing import Dict
from .base_urls import BaseUrls


class NetworkSession:
    MAX_ATTEMPTS = 5

    def __init__(
        self, additional_headers: Dict[str, str] = None, base_urls: BaseUrls = None
    ):
        if additional_headers is None:
            additional_headers = {}
        if base_urls is None:
            base_urls = BaseUrls()
        self.requests_session = requests.Session()
        self.additional_headers = additional_headers
        self.base_urls = base_urls

    def with_additional_headers(
        self, additional_headers: Dict[str, str] = None
    ) -> 'NetworkSession':
        """
        Generate a fresh network session by duplicating the existing configuration and network parameters,
        while also including additional headers to be attached to every API call.
        :param additional_headers: Dict of headers, which are appended to each API request
        :return: a new instance of NetworkSession
        """
        return NetworkSession(
            {**self.additional_headers, **additional_headers}, self.base_urls
        )

    def with_custom_base_urls(self, base_urls: BaseUrls) -> 'NetworkSession':
        """
        Generate a fresh network session by duplicating the existing configuration and network parameters,
        while also including additional base urls to be used for each API call.
        :param base_urls: Dict of base urls, which are appended to each API request
        :return: a new instance of NetworkSession
        """
        return NetworkSession(self.additional_headers, base_urls)
