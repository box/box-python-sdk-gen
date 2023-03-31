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

from box_sdk.jwt_auth import JWTAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetTermOfServicesOptionsArgTosTypeField(str, Enum):
    EXTERNAL = 'external'
    MANAGED = 'managed'

class GetTermOfServicesOptionsArg(BaseObject):
    def __init__(self, tos_type: Union[None, GetTermOfServicesOptionsArgTosTypeField] = None, **kwargs):
        """
        :param tos_type: Limits the results to the terms of service of the given type.
        :type tos_type: Union[None, GetTermOfServicesOptionsArgTosTypeField], optional
        """
        super().__init__(**kwargs)
        self.tos_type = tos_type

class CreateTermOfServiceRequestBodyArgStatusField(str, Enum):
    ENABLED = 'enabled'
    DISABLED = 'disabled'

class CreateTermOfServiceRequestBodyArgTosTypeField(str, Enum):
    EXTERNAL = 'external'
    MANAGED = 'managed'

class CreateTermOfServiceRequestBodyArg(BaseObject):
    def __init__(self, status: CreateTermOfServiceRequestBodyArgStatusField, text: str, tos_type: Union[None, CreateTermOfServiceRequestBodyArgTosTypeField] = None, **kwargs):
        """
        :param status: Whether this terms of service is active.
        :type status: CreateTermOfServiceRequestBodyArgStatusField
        :param text: The terms of service text to display to users.
            The text can be set to empty if the `status` is set to `disabled`.
        :type text: str
        :param tos_type: The type of user to set the terms of
            service for.
        :type tos_type: Union[None, CreateTermOfServiceRequestBodyArgTosTypeField], optional
        """
        super().__init__(**kwargs)
        self.status = status
        self.text = text
        self.tos_type = tos_type

class UpdateTermOfServiceByIdRequestBodyArgStatusField(str, Enum):
    ENABLED = 'enabled'
    DISABLED = 'disabled'

class UpdateTermOfServiceByIdRequestBodyArg(BaseObject):
    def __init__(self, status: UpdateTermOfServiceByIdRequestBodyArgStatusField, text: str, **kwargs):
        """
        :param status: Whether this terms of service is active.
        :type status: UpdateTermOfServiceByIdRequestBodyArgStatusField
        :param text: The terms of service text to display to users.
            The text can be set to empty if the `status` is set to `disabled`.
        :type text: str
        """
        super().__init__(**kwargs)
        self.status = status
        self.text = text

class TermsOfServicesManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth, JWTAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_term_of_services(self, options: GetTermOfServicesOptionsArg = None) -> TermsOfServices:
        """
        Returns the current terms of service text and settings
        
        for the enterprise.

        """
        if options is None:
            options = GetTermOfServicesOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_services']), FetchOptions(method='GET', params={'tos_type': options.tosType}, auth=self.auth))
        return TermsOfServices.from_dict(json.loads(response.text))
    def create_term_of_service(self, request_body: CreateTermOfServiceRequestBodyArg) -> Task:
        """
        Creates a terms of service for a given enterprise
        
        and type of user.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_services']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), auth=self.auth))
        return Task.from_dict(json.loads(response.text))
    def get_term_of_service_by_id(self, terms_of_service_id: str) -> TermsOfService:
        """
        Fetches a specific terms of service.
        :param terms_of_service_id: The ID of the terms of service.
            Example: "324234"
        :type terms_of_service_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_services/', terms_of_service_id]), FetchOptions(method='GET', auth=self.auth))
        return TermsOfService.from_dict(json.loads(response.text))
    def update_term_of_service_by_id(self, terms_of_service_id: str, request_body: UpdateTermOfServiceByIdRequestBodyArg) -> TermsOfService:
        """
        Updates a specific terms of service.
        :param terms_of_service_id: The ID of the terms of service.
            Example: "324234"
        :type terms_of_service_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_services/', terms_of_service_id]), FetchOptions(method='PUT', body=json.dumps(request_body.to_dict()), auth=self.auth))
        return TermsOfService.from_dict(json.loads(response.text))