from typing import List

from box_sdk.base_object import BaseObject

from typing import Optional

import json

from typing import Dict

from box_sdk.schemas import SessionTerminationMessage

from box_sdk.schemas import ClientError

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class CreateUserTerminateSessionRequestBodyArg(BaseObject):
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

class CreateGroupTerminateSessionRequestBodyArg(BaseObject):
    def __init__(self, group_ids: List[str], **kwargs):
        """
        :param group_ids: A list of group IDs
        :type group_ids: List[str]
        """
        super().__init__(**kwargs)
        self.group_ids = group_ids

class SessionTerminationManager(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {'network_session': 'networkSession', **BaseObject._fields_to_json_mapping}
    _json_to_fields_mapping: Dict[str, str] = {'networkSession': 'network_session', **BaseObject._json_to_fields_mapping}
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None, **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
        self.network_session = network_session
    def create_user_terminate_session(self, request_body: CreateUserTerminateSessionRequestBodyArg) -> SessionTerminationMessage:
        """
        Validates the roles and permissions of the user,
        
        and creates asynchronous jobs

        
        to terminate the user's sessions.

        
        Returns the status for the POST request.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users/terminate_sessions']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return SessionTerminationMessage.from_dict(json.loads(response.text))
    def create_group_terminate_session(self, request_body: CreateGroupTerminateSessionRequestBodyArg) -> SessionTerminationMessage:
        """
        Validates the roles and permissions of the group,
        
        and creates asynchronous jobs

        
        to terminate the group's sessions.

        
        Returns the status for the POST request.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/groups/terminate_sessions']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return SessionTerminationMessage.from_dict(json.loads(response.text))