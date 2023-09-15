from typing import Optional

from .auth import Authentication
from .network import NetworkSession
from .schemas import AccessToken


class BoxDeveloperTokenAuth(Authentication):
    def __init__(self, token: str):
        self.token: AccessToken = AccessToken(access_token=token)

    def retrieve_token(
        self, network_session: Optional[NetworkSession] = None
    ) -> AccessToken:
        """
        Retrieves stored developer token
        :param network_session: An object to keep network session state
        :return: Return a current token
        """
        return self.token

    def refresh_token(self, network_session: Optional[NetworkSession] = None):
        """
        Developer token cannot be refreshed
        :param network_session: An object to keep network session state
        """
        raise Exception("Developer token has expired. Please provide a new one.")
