from enum import Enum

from typing import Union

from base_object import BaseObject

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

import json

from schemas import TermsOfServices

from schemas import ClientError

from schemas import Task

from schemas import TermsOfService

class GetTermsOfServicesOptionsArgTosTypeField(str, Enum):
    EXTERNAL = 'external'
    MANAGED = 'managed'

class GetTermsOfServicesOptionsArg(BaseObject):
    def __init__(self, tosType: Union[None, GetTermsOfServicesOptionsArgTosTypeField] = None, **kwargs):
        """
        :param tosType: Limits the results to the terms of service of the given type.
        :type tosType: Union[None, GetTermsOfServicesOptionsArgTosTypeField], optional
        """
        super().__init__(**kwargs)
        self.tosType = tosType

class PostTermsOfServicesRequestBodyArgStatusField(str, Enum):
    ENABLED = 'enabled'
    DISABLED = 'disabled'

class PostTermsOfServicesRequestBodyArgTosTypeField(str, Enum):
    EXTERNAL = 'external'
    MANAGED = 'managed'

class PostTermsOfServicesRequestBodyArg(BaseObject):
    def __init__(self, status: PostTermsOfServicesRequestBodyArgStatusField, text: str, tos_type: Union[None, PostTermsOfServicesRequestBodyArgTosTypeField] = None, **kwargs):
        """
        :param status: Whether this terms of service is active.
        :type status: PostTermsOfServicesRequestBodyArgStatusField
        :param text: The terms of service text to display to users.
            The text can be set to empty if the `status` is set to `disabled`.
        :type text: str
        :param tos_type: The type of user to set the terms of
            service for.
        :type tos_type: Union[None, PostTermsOfServicesRequestBodyArgTosTypeField], optional
        """
        super().__init__(**kwargs)
        self.status = status
        self.text = text
        self.tos_type = tos_type

class PutTermsOfServicesIdRequestBodyArgStatusField(str, Enum):
    ENABLED = 'enabled'
    DISABLED = 'disabled'

class PutTermsOfServicesIdRequestBodyArg(BaseObject):
    def __init__(self, status: PutTermsOfServicesIdRequestBodyArgStatusField, text: str, **kwargs):
        """
        :param status: Whether this terms of service is active.
        :type status: PutTermsOfServicesIdRequestBodyArgStatusField
        :param text: The terms of service text to display to users.
            The text can be set to empty if the `status` is set to `disabled`.
        :type text: str
        """
        super().__init__(**kwargs)
        self.status = status
        self.text = text

class TermsOfServicesManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getTermsOfServices(self, options: GetTermsOfServicesOptionsArg = None) -> TermsOfServices:
        """
        Returns the current terms of service text and settings
        
        for the enterprise.

        """
        if options is None:
            options = GetTermsOfServicesOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_services']), FetchOptions(method='GET', params={'tos_type': options.tosType}, auth=self.auth))
        return TermsOfServices.from_dict(json.loads(response.text))
    def postTermsOfServices(self, requestBody: PostTermsOfServicesRequestBodyArg) -> Task:
        """
        Creates a terms of service for a given enterprise
        
        and type of user.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_services']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return Task.from_dict(json.loads(response.text))
    def getTermsOfServicesId(self, termsOfServiceId: str) -> TermsOfService:
        """
        Fetches a specific terms of service.
        :param termsOfServiceId: The ID of the terms of service.
            Example: "324234"
        :type termsOfServiceId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_services/', termsOfServiceId]), FetchOptions(method='GET', auth=self.auth))
        return TermsOfService.from_dict(json.loads(response.text))
    def putTermsOfServicesId(self, termsOfServiceId: str, requestBody: PutTermsOfServicesIdRequestBodyArg) -> TermsOfService:
        """
        Updates a specific terms of service.
        :param termsOfServiceId: The ID of the terms of service.
            Example: "324234"
        :type termsOfServiceId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_services/', termsOfServiceId]), FetchOptions(method='PUT', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return TermsOfService.from_dict(json.loads(response.text))