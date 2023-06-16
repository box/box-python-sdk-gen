from typing import Optional

from .auth import Authentication
from .network import NetworkSession


class DeveloperTokenAuth(Authentication):
    def __init__(self, token: str):
        self.token: str = token

    def retrieve_token(self, network_session: Optional[NetworkSession] = None) -> str:
        return self.token

    def refresh(self, network_session: Optional[NetworkSession] = None) -> str:
        raise Exception("Developer token has expired. Please provide a new one.")