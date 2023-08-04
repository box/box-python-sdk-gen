from abc import abstractmethod
from typing import Optional

from .network import NetworkSession


class Authentication:
    @abstractmethod
    def retrieve_token(self, network_session: Optional[NetworkSession] = None) -> str:
        pass

    @abstractmethod
    def refresh(self, network_session: Optional[NetworkSession] = None) -> str:
        pass
