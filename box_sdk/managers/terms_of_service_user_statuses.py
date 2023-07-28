from enum import Enum

from box_sdk.base_object import BaseObject

from typing import Optional

from typing import Dict

import json

from box_sdk.base_object import BaseObject

from box_sdk.schemas import TermsOfServiceUserStatuses

from box_sdk.schemas import ClientError

from box_sdk.schemas import TermsOfServiceUserStatus

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.utils import prepare_params

from box_sdk.utils import to_string

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class CreateTermOfServiceUserStatusTosArgTypeField(str, Enum):
    TERMS_OF_SERVICE = 'terms_of_service'

class CreateTermOfServiceUserStatusTosArg(BaseObject):
    def __init__(self, type: CreateTermOfServiceUserStatusTosArgTypeField, id: str, **kwargs):
        """
        :param type: The type of object.
        :type type: CreateTermOfServiceUserStatusTosArgTypeField
        :param id: The ID of terms of service
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class CreateTermOfServiceUserStatusUserArgTypeField(str, Enum):
    USER = 'user'

class CreateTermOfServiceUserStatusUserArg(BaseObject):
    def __init__(self, type: CreateTermOfServiceUserStatusUserArgTypeField, id: str, **kwargs):
        """
        :param type: The type of object.
        :type type: CreateTermOfServiceUserStatusUserArgTypeField
        :param id: The ID of user
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class TermsOfServiceUserStatusesManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def get_term_of_service_user_statuses(self, tos_id: str, user_id: Optional[str] = None) -> TermsOfServiceUserStatuses:
        """
        Retrieves an overview of users and their status for a
        
        terms of service, including Whether they have accepted

        
        the terms and when.

        :param tos_id: The ID of the terms of service.
        :type tos_id: str
        :param user_id: Limits results to the given user ID.
        :type user_id: Optional[str], optional
        """
        query_params_map: Dict[str, str] = prepare_params({'tos_id': to_string(tos_id), 'user_id': to_string(user_id)})
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_service_user_statuses']), FetchOptions(method='GET', params=query_params_map, auth=self.auth, network_session=self.network_session))
        return TermsOfServiceUserStatuses.from_dict(json.loads(response.text))
    def create_term_of_service_user_status(self, tos: CreateTermOfServiceUserStatusTosArg, user: CreateTermOfServiceUserStatusUserArg, is_accepted: bool) -> TermsOfServiceUserStatus:
        """
        Sets the status for a terms of service for a user.
        :param tos: The terms of service to set the status for.
        :type tos: CreateTermOfServiceUserStatusTosArg
        :param user: The user to set the status for.
        :type user: CreateTermOfServiceUserStatusUserArg
        :param is_accepted: Whether the user has accepted the terms.
        :type is_accepted: bool
        """
        request_body: BaseObject = BaseObject(tos=tos, user=user, is_accepted=is_accepted)
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_service_user_statuses']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return TermsOfServiceUserStatus.from_dict(json.loads(response.text))
    def update_term_of_service_user_status_by_id(self, terms_of_service_user_status_id: str, is_accepted: bool) -> TermsOfServiceUserStatus:
        """
        Updates the status for a terms of service for a user.
        :param terms_of_service_user_status_id: The ID of the terms of service status.
            Example: "324234"
        :type terms_of_service_user_status_id: str
        :param is_accepted: Whether the user has accepted the terms.
        :type is_accepted: bool
        """
        request_body: BaseObject = BaseObject(is_accepted=is_accepted)
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_service_user_statuses/', terms_of_service_user_status_id]), FetchOptions(method='PUT', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return TermsOfServiceUserStatus.from_dict(json.loads(response.text))