import requests
from typing import Dict


class NetworkSession:
    MAX_ATTEMPTS = 5

    def __init__(self, additional_headers: Dict[str, str] = None):
        if additional_headers is None:
            additional_headers = {}
        self.requests_session = requests.Session()
        self.additional_headers = additional_headers

    def with_additional_headers(
        self, additional_headers: Dict[str, str] = None
    ) -> 'NetworkSession':
        """
        Generate a fresh network session by duplicating the existing configuration and network parameters,
        while also including additional headers to be attached to every API call.
        :param additional_headers: Dict of headers, which are appended to each API request
        :return: a new instance of NetworkSession
        """
        return NetworkSession({**self.additional_headers, **additional_headers})
