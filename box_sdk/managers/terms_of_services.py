from enum import Enum

from typing import Optional

from typing import Dict

import json

from box_sdk.base_object import BaseObject

from box_sdk.schemas import TermsOfServices

from box_sdk.schemas import ClientError

from box_sdk.schemas import Task

from box_sdk.schemas import TermsOfService

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.utils import prepare_params

from box_sdk.utils import to_string

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetTermOfServicesTosTypeArg(str, Enum):
    EXTERNAL = 'external'
    MANAGED = 'managed'

class CreateTermOfServiceStatusArg(str, Enum):
    ENABLED = 'enabled'
    DISABLED = 'disabled'

class CreateTermOfServiceTosTypeArg(str, Enum):
    EXTERNAL = 'external'
    MANAGED = 'managed'

class UpdateTermOfServiceByIdStatusArg(str, Enum):
    ENABLED = 'enabled'
    DISABLED = 'disabled'

class TermsOfServicesManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def get_term_of_services(self, tos_type: Optional[GetTermOfServicesTosTypeArg] = None) -> TermsOfServices:
        """
        Returns the current terms of service text and settings
        
        for the enterprise.

        :param tos_type: Limits the results to the terms of service of the given type.
        :type tos_type: Optional[GetTermOfServicesTosTypeArg], optional
        """
        query_params_map: Dict[str, str] = prepare_params({'tos_type': to_string(tos_type)})
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_services']), FetchOptions(method='GET', params=query_params_map, auth=self.auth, network_session=self.network_session))
        return TermsOfServices.from_dict(json.loads(response.text))
    def create_term_of_service(self, status: CreateTermOfServiceStatusArg, text: str, tos_type: Optional[CreateTermOfServiceTosTypeArg] = None) -> Task:
        """
        Creates a terms of service for a given enterprise
        
        and type of user.

        :param status: Whether this terms of service is active.
        :type status: CreateTermOfServiceStatusArg
        :param text: The terms of service text to display to users.
            The text can be set to empty if the `status` is set to `disabled`.
        :type text: str
        :param tos_type: The type of user to set the terms of
            service for.
        :type tos_type: Optional[CreateTermOfServiceTosTypeArg], optional
        """
        request_body: BaseObject = BaseObject(status=status, tos_type=tos_type, text=text)
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
    def update_term_of_service_by_id(self, terms_of_service_id: str, status: UpdateTermOfServiceByIdStatusArg, text: str) -> TermsOfService:
        """
        Updates a specific terms of service.
        :param terms_of_service_id: The ID of the terms of service.
            Example: "324234"
        :type terms_of_service_id: str
        :param status: Whether this terms of service is active.
        :type status: UpdateTermOfServiceByIdStatusArg
        :param text: The terms of service text to display to users.
            The text can be set to empty if the `status` is set to `disabled`.
        :type text: str
        """
        request_body: BaseObject = BaseObject(status=status, text=text)
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/terms_of_services/', terms_of_service_id]), FetchOptions(method='PUT', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return TermsOfService.from_dict(json.loads(response.text))