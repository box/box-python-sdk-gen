from typing import Optional

from abc import abstractmethod

from box_sdk_gen.schemas import AccessToken

from box_sdk_gen.network import NetworkSession


class Authentication:
    def __init__(self):
        pass

    @abstractmethod
    def retrieve_token(
        self, network_session: Optional[NetworkSession] = None
    ) -> AccessToken:
        pass

    @abstractmethod
    def refresh_token(
        self, network_session: Optional[NetworkSession] = None
    ) -> AccessToken:
        pass
