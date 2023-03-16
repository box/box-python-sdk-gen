from enum import Enum

from typing import Union

from box_sdk.base_object import BaseObject

import json

from box_sdk.schemas import TermsOfServices

from box_sdk.schemas import ClientError

from box_sdk.schemas import Task

from box_sdk.schemas import TermsOfService

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetTermsOfServicesOptionsArgTosTypeField(str, Enum):
    EXTERNAL = 'external'
    MANAGED = 'managed'

class GetTermsOfServicesOptionsArg(BaseObject):
    def __init__(self, tos_type: Union[None, GetTermsOfServicesOptionsArgTosTypeField] = None, **kwargs):
        """
        :param tos_type: Limits the results to the terms of service of the given type.
        :type tos_type: Union[None, GetTermsOfServicesOptionsArgTosTypeField], optional
        """
        super().__init__(**kwargs)
        self.tos_type = tos_type

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
    def get_terms_of_services(self, options: GetTermsOfServicesOptionsArg = None) -> TermsOfServices:
        """
        Returns the current terms of service text and settings
        
        for the enterprise.

        """
        if options is None:
            options = GetTermsOfServicesOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_services']), FetchOptions(method='GET', params={'tos_type': options.tosType}, auth=self.auth))
        return TermsOfServices.from_dict(json.loads(response.text))
    def post_terms_of_services(self, request_body: PostTermsOfServicesRequestBodyArg) -> Task:
        """
        Creates a terms of service for a given enterprise
        
        and type of user.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_services']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), auth=self.auth))
        return Task.from_dict(json.loads(response.text))
    def get_terms_of_services_id(self, terms_of_service_id: str) -> TermsOfService:
        """
        Fetches a specific terms of service.
        :param terms_of_service_id: The ID of the terms of service.
            Example: "324234"
        :type terms_of_service_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_services/', terms_of_service_id]), FetchOptions(method='GET', auth=self.auth))
        return TermsOfService.from_dict(json.loads(response.text))
    def put_terms_of_services_id(self, terms_of_service_id: str, request_body: PutTermsOfServicesIdRequestBodyArg) -> TermsOfService:
        """
        Updates a specific terms of service.
        :param terms_of_service_id: The ID of the terms of service.
            Example: "324234"
        :type terms_of_service_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_services/', terms_of_service_id]), FetchOptions(method='PUT', body=json.dumps(request_body.to_dict()), auth=self.auth))
        return TermsOfService.from_dict(json.loads(response.text))