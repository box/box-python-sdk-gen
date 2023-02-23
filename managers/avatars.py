from typing import Union

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

from base_object import BaseObject

from schemas import ClientError

from schemas import UserAvatar

class AvatarsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getUsersIdAvatar(self, userId: str):
        """
        Retrieves an image of a the user's avatar.
        :param userId: The ID of the user.
            Example: "12345"
        :type userId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users/', userId, '/avatar']), FetchOptions(method='GET', auth=self.auth))
        return response.content
    def deleteUsersIdAvatar(self, userId: str):
        """
        Removes an existing user avatar.
        
        You cannot reverse this operation.

        :param userId: The ID of the user.
            Example: "12345"
        :type userId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users/', userId, '/avatar']), FetchOptions(method='DELETE', auth=self.auth))
        return response.content