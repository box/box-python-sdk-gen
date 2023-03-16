from typing import List

from box_sdk.base_object import BaseObject

from typing import Union

import json

from box_sdk.schemas import SessionTerminationMessage

from box_sdk.schemas import ClientError

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class PostUsersTerminateSessionsRequestBodyArg(BaseObject):
    def __init__(self, user_ids: List[str], user_logins: List[str], **kwargs):
        """
        :param user_ids: A list of user IDs
        :type user_ids: List[str]
        :param user_logins: A list of user logins
        :type user_logins: List[str]
        """
        super().__init__(**kwargs)
        self.user_ids = user_ids
        self.user_logins = user_logins

class PostGroupsTerminateSessionsRequestBodyArg(BaseObject):
    def __init__(self, group_ids: List[str], **kwargs):
        """
        :param group_ids: A list of group IDs
        :type group_ids: List[str]
        """
        super().__init__(**kwargs)
        self.group_ids = group_ids

class SessionTerminationManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def post_users_terminate_sessions(self, request_body: PostUsersTerminateSessionsRequestBodyArg) -> SessionTerminationMessage:
        """
        Validates the roles and permissions of the user,
        
        and creates asynchronous jobs

        
        to terminate the user's sessions.

        
        Returns the status for the POST request.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users/terminate_sessions']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), auth=self.auth))
        return SessionTerminationMessage.from_dict(json.loads(response.text))
    def post_groups_terminate_sessions(self, request_body: PostGroupsTerminateSessionsRequestBodyArg) -> SessionTerminationMessage:
        """
        Validates the roles and permissions of the group,
        
        and creates asynchronous jobs

        
        to terminate the group's sessions.

        
        Returns the status for the POST request.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/groups/terminate_sessions']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), auth=self.auth))
        return SessionTerminationMessage.from_dict(json.loads(response.text))