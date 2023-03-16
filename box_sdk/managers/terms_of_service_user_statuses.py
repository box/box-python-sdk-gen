from typing import Union

from box_sdk.base_object import BaseObject

import json

from box_sdk.schemas import TermsOfServiceUserStatuses

from box_sdk.schemas import ClientError

from box_sdk.schemas import TermsOfServiceUserStatus

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetTermsOfServiceUserStatusesOptionsArg(BaseObject):
    def __init__(self, user_id: Union[None, str] = None, **kwargs):
        """
        :param user_id: Limits results to the given user ID.
        :type user_id: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.user_id = user_id

class PostTermsOfServiceUserStatusesRequestBodyArgTosFieldTypeField:
    pass

class PostTermsOfServiceUserStatusesRequestBodyArgTosField(BaseObject):
    def __init__(self, type: PostTermsOfServiceUserStatusesRequestBodyArgTosFieldTypeField, id: str, **kwargs):
        """
        :param type: The type of object.
        :type type: PostTermsOfServiceUserStatusesRequestBodyArgTosFieldTypeField
        :param id: The ID of terms of service
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class PostTermsOfServiceUserStatusesRequestBodyArgUserFieldTypeField:
    pass

class PostTermsOfServiceUserStatusesRequestBodyArgUserField(BaseObject):
    def __init__(self, type: PostTermsOfServiceUserStatusesRequestBodyArgUserFieldTypeField, id: str, **kwargs):
        """
        :param type: The type of object.
        :type type: PostTermsOfServiceUserStatusesRequestBodyArgUserFieldTypeField
        :param id: The ID of user
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class PostTermsOfServiceUserStatusesRequestBodyArg(BaseObject):
    def __init__(self, tos: PostTermsOfServiceUserStatusesRequestBodyArgTosField, user: PostTermsOfServiceUserStatusesRequestBodyArgUserField, is_accepted: bool, **kwargs):
        """
        :param tos: The terms of service to set the status for.
        :type tos: PostTermsOfServiceUserStatusesRequestBodyArgTosField
        :param user: The user to set the status for.
        :type user: PostTermsOfServiceUserStatusesRequestBodyArgUserField
        :param is_accepted: Whether the user has accepted the terms.
        :type is_accepted: bool
        """
        super().__init__(**kwargs)
        self.tos = tos
        self.user = user
        self.is_accepted = is_accepted

class PutTermsOfServiceUserStatusesIdRequestBodyArg(BaseObject):
    def __init__(self, is_accepted: bool, **kwargs):
        """
        :param is_accepted: Whether the user has accepted the terms.
        :type is_accepted: bool
        """
        super().__init__(**kwargs)
        self.is_accepted = is_accepted

class TermsOfServiceUserStatusesManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_terms_of_service_user_statuses(self, tos_id: str, options: GetTermsOfServiceUserStatusesOptionsArg = None) -> TermsOfServiceUserStatuses:
        """
        Retrieves an overview of users and their status for a
        
        terms of service, including Whether they have accepted

        
        the terms and when.

        :param tos_id: The ID of the terms of service.
            Example: "324234"
        :type tos_id: str
        """
        if options is None:
            options = GetTermsOfServiceUserStatusesOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_service_user_statuses']), FetchOptions(method='GET', params={'tos_id': tos_id, 'user_id': options.userId}, auth=self.auth))
        return TermsOfServiceUserStatuses.from_dict(json.loads(response.text))
    def post_terms_of_service_user_statuses(self, request_body: PostTermsOfServiceUserStatusesRequestBodyArg) -> TermsOfServiceUserStatus:
        """
        Sets the status for a terms of service for a user.
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_service_user_statuses']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), auth=self.auth))
        return TermsOfServiceUserStatus.from_dict(json.loads(response.text))
    def put_terms_of_service_user_statuses_id(self, terms_of_service_user_status_id: str, request_body: PutTermsOfServiceUserStatusesIdRequestBodyArg) -> TermsOfServiceUserStatus:
        """
        Updates the status for a terms of service for a user.
        :param terms_of_service_user_status_id: The ID of the terms of service status.
            Example: "324234"
        :type terms_of_service_user_status_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_service_user_statuses/', terms_of_service_user_status_id]), FetchOptions(method='PUT', body=json.dumps(request_body.to_dict()), auth=self.auth))
        return TermsOfServiceUserStatus.from_dict(json.loads(response.text))