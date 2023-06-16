from enum import Enum

from typing import Optional

from box_sdk.base_object import BaseObject

import json

from typing import Dict

from box_sdk.schemas import TermsOfServices

from box_sdk.schemas import ClientError

from box_sdk.schemas import Task

from box_sdk.schemas import TermsOfService

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetTermOfServicesOptionsArgTosTypeField(str, Enum):
    EXTERNAL = 'external'
    MANAGED = 'managed'

class GetTermOfServicesOptionsArg(BaseObject):
    def __init__(self, tos_type: Optional[GetTermOfServicesOptionsArgTosTypeField] = None, **kwargs):
        """
        :param tos_type: Limits the results to the terms of service of the given type.
        :type tos_type: Optional[GetTermOfServicesOptionsArgTosTypeField], optional
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
    def __init__(self, status: CreateTermOfServiceRequestBodyArgStatusField, text: str, tos_type: Optional[CreateTermOfServiceRequestBodyArgTosTypeField] = None, **kwargs):
        """
        :param status: Whether this terms of service is active.
        :type status: CreateTermOfServiceRequestBodyArgStatusField
        :param text: The terms of service text to display to users.
            The text can be set to empty if the `status` is set to `disabled`.
        :type text: str
        :param tos_type: The type of user to set the terms of
            service for.
        :type tos_type: Optional[CreateTermOfServiceRequestBodyArgTosTypeField], optional
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
    _fields_to_json_mapping: Dict[str, str] = {'network_session': 'networkSession', **BaseObject._fields_to_json_mapping}
    _json_to_fields_mapping: Dict[str, str] = {'networkSession': 'network_session', **BaseObject._json_to_fields_mapping}
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None, **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
        self.network_session = network_session
    def get_term_of_services(self, options: GetTermOfServicesOptionsArg = None) -> TermsOfServices:
        """
        Returns the current terms of service text and settings
        
        for the enterprise.

        """
        if options is None:
            options = GetTermOfServicesOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_services']), FetchOptions(method='GET', params={'tos_type': options.tos_type}, auth=self.auth, network_session=self.network_session))
        return TermsOfServices.from_dict(json.loads(response.text))
    def create_term_of_service(self, request_body: CreateTermOfServiceRequestBodyArg) -> Task:
        """
        Creates a terms of service for a given enterprise
        
        and type of user.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_services']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return Task.from_dict(json.loads(response.text))
    def get_term_of_service_by_id(self, terms_of_service_id: str) -> TermsOfService:
        """
        Fetches a specific terms of service.
        :param terms_of_service_id: The ID of the terms of service.
            Example: "324234"
        :type terms_of_service_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_services/', terms_of_service_id]), FetchOptions(method='GET', auth=self.auth, network_session=self.network_session))
        return TermsOfService.from_dict(json.loads(response.text))
    def update_term_of_service_by_id(self, terms_of_service_id: str, request_body: UpdateTermOfServiceByIdRequestBodyArg) -> TermsOfService:
        """
        Updates a specific terms of service.
        :param terms_of_service_id: The ID of the terms of service.
            Example: "324234"
        :type terms_of_service_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_services/', terms_of_service_id]), FetchOptions(method='PUT', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return TermsOfService.from_dict(json.loads(response.text))