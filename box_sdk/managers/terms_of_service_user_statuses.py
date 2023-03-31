from typing import Union

from box_sdk.base_object import BaseObject

from enum import Enum

import json

from box_sdk.schemas import TermsOfServiceUserStatuses

from box_sdk.schemas import ClientError

from box_sdk.schemas import TermsOfServiceUserStatus

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.jwt_auth import JWTAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetTermOfServiceUserStatusesOptionsArg(BaseObject):
    def __init__(self, user_id: Union[None, str] = None, **kwargs):
        """
        :param user_id: Limits results to the given user ID.
        :type user_id: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.user_id = user_id

class CreateTermOfServiceUserStatusRequestBodyArgTosFieldTypeField(str, Enum):
    TERMS_OF_SERVICE = 'terms_of_service'

class CreateTermOfServiceUserStatusRequestBodyArgTosField(BaseObject):
    def __init__(self, type: CreateTermOfServiceUserStatusRequestBodyArgTosFieldTypeField, id: str, **kwargs):
        """
        :param type: The type of object.
        :type type: CreateTermOfServiceUserStatusRequestBodyArgTosFieldTypeField
        :param id: The ID of terms of service
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class CreateTermOfServiceUserStatusRequestBodyArgUserFieldTypeField(str, Enum):
    USER = 'user'

class CreateTermOfServiceUserStatusRequestBodyArgUserField(BaseObject):
    def __init__(self, type: CreateTermOfServiceUserStatusRequestBodyArgUserFieldTypeField, id: str, **kwargs):
        """
        :param type: The type of object.
        :type type: CreateTermOfServiceUserStatusRequestBodyArgUserFieldTypeField
        :param id: The ID of user
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class CreateTermOfServiceUserStatusRequestBodyArg(BaseObject):
    def __init__(self, tos: CreateTermOfServiceUserStatusRequestBodyArgTosField, user: CreateTermOfServiceUserStatusRequestBodyArgUserField, is_accepted: bool, **kwargs):
        """
        :param tos: The terms of service to set the status for.
        :type tos: CreateTermOfServiceUserStatusRequestBodyArgTosField
        :param user: The user to set the status for.
        :type user: CreateTermOfServiceUserStatusRequestBodyArgUserField
        :param is_accepted: Whether the user has accepted the terms.
        :type is_accepted: bool
        """
        super().__init__(**kwargs)
        self.tos = tos
        self.user = user
        self.is_accepted = is_accepted

class UpdateTermOfServiceUserStatusByIdRequestBodyArg(BaseObject):
    def __init__(self, is_accepted: bool, **kwargs):
        """
        :param is_accepted: Whether the user has accepted the terms.
        :type is_accepted: bool
        """
        super().__init__(**kwargs)
        self.is_accepted = is_accepted

class TermsOfServiceUserStatusesManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth, JWTAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_term_of_service_user_statuses(self, tos_id: str, options: GetTermOfServiceUserStatusesOptionsArg = None) -> TermsOfServiceUserStatuses:
        """
        Retrieves an overview of users and their status for a
        
        terms of service, including Whether they have accepted

        
        the terms and when.

        :param tos_id: The ID of the terms of service.
            Example: "324234"
        :type tos_id: str
        """
        if options is None:
            options = GetTermOfServiceUserStatusesOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_service_user_statuses']), FetchOptions(method='GET', params={'tos_id': tos_id, 'user_id': options.userId}, auth=self.auth))
        return TermsOfServiceUserStatuses.from_dict(json.loads(response.text))
    def create_term_of_service_user_status(self, request_body: CreateTermOfServiceUserStatusRequestBodyArg) -> TermsOfServiceUserStatus:
        """
        Sets the status for a terms of service for a user.
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_service_user_statuses']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), auth=self.auth))
        return TermsOfServiceUserStatus.from_dict(json.loads(response.text))
    def update_term_of_service_user_status_by_id(self, terms_of_service_user_status_id: str, request_body: UpdateTermOfServiceUserStatusByIdRequestBodyArg) -> TermsOfServiceUserStatus:
        """
        Updates the status for a terms of service for a user.
        :param terms_of_service_user_status_id: The ID of the terms of service status.
            Example: "324234"
        :type terms_of_service_user_status_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_service_user_statuses/', terms_of_service_user_status_id]), FetchOptions(method='PUT', body=json.dumps(request_body.to_dict()), auth=self.auth))
        return TermsOfServiceUserStatus.from_dict(json.loads(response.text))