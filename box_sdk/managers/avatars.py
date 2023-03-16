from typing import Union

from box_sdk.base_object import BaseObject

from box_sdk.schemas import ClientError

from box_sdk.schemas import UserAvatar

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class AvatarsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_users_id_avatar(self, user_id: str):
        """
        Retrieves an image of a the user's avatar.
        :param user_id: The ID of the user.
            Example: "12345"
        :type user_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users/', user_id, '/avatar']), FetchOptions(method='GET', auth=self.auth))
        return response.content
    def delete_users_id_avatar(self, user_id: str):
        """
        Removes an existing user avatar.
        
        You cannot reverse this operation.

        :param user_id: The ID of the user.
            Example: "12345"
        :type user_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users/', user_id, '/avatar']), FetchOptions(method='DELETE', auth=self.auth))
        return response.content