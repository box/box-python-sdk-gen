import requests
from typing import Dict

from .proxy_config import ProxyConfig
from .base_urls import BaseUrls


class NetworkSession:
    MAX_ATTEMPTS = 5

    def __init__(
        self,
        additional_headers: Dict[str, str] = None,
        base_urls: BaseUrls = None,
        proxy_url: str = None,
    ):
        if additional_headers is None:
            additional_headers = {}
        if base_urls is None:
            base_urls = BaseUrls()
        self.requests_session = requests.Session()
        self.additional_headers = additional_headers
        self.base_urls = base_urls
        self.proxy_url = proxy_url

        proxies = {'http': proxy_url, 'https': proxy_url} if proxy_url else {}
        self.requests_session.proxies = proxies

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
            {**self.additional_headers, **additional_headers},
            self.base_urls,
            self.proxy_url,
        )

    def with_custom_base_urls(self, base_urls: BaseUrls) -> 'NetworkSession':
        """
        Generate a fresh network session by duplicating the existing configuration and network parameters,
        while also including additional base urls to be used for each API call.
        :param base_urls: Dict of base urls, which are appended to each API request
        :return: a new instance of NetworkSession
        """
        return NetworkSession(self.additional_headers, base_urls, self.proxy_url)

    def with_proxy(self, config: ProxyConfig) -> 'NetworkSession':
        """
        Generate a fresh network session by duplicating the existing configuration and network parameters,
        while also including a proxy to be used for each API call.
        :param config: ProxyConfig object, which contains the proxy url, username, and password
        :return: a new instance of NetworkSession
        """
        if not config.url or not config.url.startswith("http"):
            raise ValueError("Invalid proxy URL provided")

        proxy_host = config.url.split("//")[1]
        proxy_auth = (
            f'{config.username}:{config.password}@'
            if config.username and config.password
            else ''
        )
        proxy_url = f'http://{proxy_auth}{proxy_host}'
        return NetworkSession(self.additional_headers, self.base_urls, proxy_url)
