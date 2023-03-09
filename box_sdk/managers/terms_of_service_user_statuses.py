from typing import Union

from box_sdk.base_object import BaseObject

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch, FetchOptions, FetchResponse

import json

from box_sdk.schemas import TermsOfServiceUserStatuses

from box_sdk.schemas import ClientError

from box_sdk.schemas import TermsOfServiceUserStatus

class GetTermsOfServiceUserStatusesOptionsArg(BaseObject):
    def __init__(self, userId: Union[None, str] = None, **kwargs):
        """
        :param userId: Limits results to the given user ID.
        :type userId: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.userId = userId

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
    def getTermsOfServiceUserStatuses(self, tosId: str, options: GetTermsOfServiceUserStatusesOptionsArg = None) -> TermsOfServiceUserStatuses:
        """
        Retrieves an overview of users and their status for a
        
        terms of service, including Whether they have accepted

        
        the terms and when.

        :param tosId: The ID of the terms of service.
            Example: "324234"
        :type tosId: str
        """
        if options is None:
            options = GetTermsOfServiceUserStatusesOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_service_user_statuses']), FetchOptions(method='GET', params={'tos_id': tosId, 'user_id': options.userId}, auth=self.auth))
        return TermsOfServiceUserStatuses.from_dict(json.loads(response.text))
    def postTermsOfServiceUserStatuses(self, requestBody: PostTermsOfServiceUserStatusesRequestBodyArg) -> TermsOfServiceUserStatus:
        """
        Sets the status for a terms of service for a user.
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_service_user_statuses']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return TermsOfServiceUserStatus.from_dict(json.loads(response.text))
    def putTermsOfServiceUserStatusesId(self, termsOfServiceUserStatusId: str, requestBody: PutTermsOfServiceUserStatusesIdRequestBodyArg) -> TermsOfServiceUserStatus:
        """
        Updates the status for a terms of service for a user.
        :param termsOfServiceUserStatusId: The ID of the terms of service status.
            Example: "324234"
        :type termsOfServiceUserStatusId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_service_user_statuses/', termsOfServiceUserStatusId]), FetchOptions(method='PUT', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return TermsOfServiceUserStatus.from_dict(json.loads(response.text))