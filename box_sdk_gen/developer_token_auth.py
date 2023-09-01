from typing import Optional

from .auth import Authentication
from .network import NetworkSession
from .schemas import AccessToken


class DeveloperTokenAuth(Authentication):
    def __init__(self, token: str):
        self.token: AccessToken = AccessToken(access_token=token)

    def retrieve_token(
        self, network_session: Optional[NetworkSession] = None
    ) -> AccessToken:
        return self.token

    def refresh_token(
        self, network_session: Optional[NetworkSession] = None
    ) -> AccessToken:
        raise Exception("Developer token has expired. Please provide a new one.")
