from abc import abstractmethod
from typing import Optional

from .network import NetworkSession
from .schemas import AccessToken


class Authentication:
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
