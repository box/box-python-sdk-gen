import requests
from typing import Dict

from .network_client import NetworkClient
from .box_network_client import BoxNetworkClient
from .proxy_config import ProxyConfig
from .base_urls import BaseUrls
from .retries import RetryStrategy, BoxRetryStrategy


class NetworkSession:
    def __init__(
        self,
        *,
        network_client: NetworkClient = None,
        retry_strategy: RetryStrategy = None,
        additional_headers: Dict[str, str] = None,
        base_urls: BaseUrls = None,
        proxy_url: str = None,
    ):
        if additional_headers is None:
            additional_headers = {}
        if base_urls is None:
            base_urls = BaseUrls()
        if retry_strategy is None:
            retry_strategy = BoxRetryStrategy()
        if network_client is None:
            network_client = BoxNetworkClient()
        self.requests_session = requests.Session()
        self.additional_headers = additional_headers
        self.base_urls = base_urls
        self.proxy_url = proxy_url
        self.network_client = network_client
        self.retry_strategy = retry_strategy

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
            network_client=self.network_client,
            additional_headers={**self.additional_headers, **additional_headers},
            base_urls=self.base_urls,
            proxy_url=self.proxy_url,
            retry_strategy=self.retry_strategy,
        )

    def with_custom_base_urls(self, base_urls: BaseUrls) -> 'NetworkSession':
        """
        Generate a fresh network session by duplicating the existing configuration and network parameters,
        while also including additional base urls to be used for each API call.
        :param base_urls: Dict of base urls, which are appended to each API request
        :return: a new instance of NetworkSession
        """
        return NetworkSession(
            network_client=self.network_client,
            additional_headers=self.additional_headers,
            base_urls=base_urls,
            proxy_url=self.proxy_url,
            retry_strategy=self.retry_strategy,
        )

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
        return NetworkSession(
            network_client=self.network_client,
            additional_headers=self.additional_headers,
            base_urls=self.base_urls,
            proxy_url=proxy_url,
            retry_strategy=self.retry_strategy,
        )

    def with_network_client(self, network_client: NetworkClient) -> 'NetworkSession':
        """
        Generate a fresh network session by duplicating the existing configuration and network parameters,
        while also including a new network client to be used for each API call.
        :param network_client: NetworkClient object, which contains the fetch method
        :return: a new instance of NetworkSession
        """
        return NetworkSession(
            network_client=network_client,
            additional_headers=self.additional_headers,
            base_urls=self.base_urls,
            proxy_url=self.proxy_url,
            retry_strategy=self.retry_strategy,
        )

    def with_retry_strategy(self, retry_strategy: RetryStrategy) -> 'NetworkSession':
        """
        Generate a fresh network session by duplicating the existing configuration and network parameters,
        while also including a new retry options to be used for each API call.
        :param retry_options: RetryOptions object, which contains the retry logic
        :return: a new instance of NetworkSession
        """
        return NetworkSession(
            network_client=self.network_client,
            additional_headers=self.additional_headers,
            base_urls=self.base_urls,
            proxy_url=self.proxy_url,
            retry_strategy=retry_strategy,
        )
