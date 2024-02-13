from typing import Optional

from box_sdk_gen.schemas import AccessToken

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.errors import BoxSDKError


class BoxDeveloperTokenAuth(Authentication):
    def __init__(self, token: str, **kwargs):
        super().__init__(**kwargs)
        self.token = token

    def retrieve_token(
        self, network_session: Optional[NetworkSession] = None
    ) -> AccessToken:
        """
        Retrieves stored developer token
        :param network_session: An object to keep network session state
        :type network_session: Optional[NetworkSession], optional
        """
        return AccessToken(access_token=self.token)

    def refresh_token(
        self, network_session: Optional[NetworkSession] = None
    ) -> AccessToken:
        """
        Developer token cannot be refreshed
        :param network_session: An object to keep network session state
        :type network_session: Optional[NetworkSession], optional
        """
        raise BoxSDKError(
            message='Developer token has expired. Please provide a new one.'
        )
