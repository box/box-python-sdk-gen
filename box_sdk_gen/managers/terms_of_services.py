from enum import Enum

from typing import Optional

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.serialization import serialize

from box_sdk_gen.schemas import TermsOfServices

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import Task

from box_sdk_gen.schemas import TermsOfService

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.json import sd_to_json

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse

from box_sdk_gen.json import SerializedData


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
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def get_term_of_services(
        self,
        tos_type: Optional[GetTermOfServicesTosTypeArg] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> TermsOfServices:
        """
        Returns the current terms of service text and settings

        for the enterprise.

        :param tos_type: Limits the results to the terms of service of the given type.
        :type tos_type: Optional[GetTermOfServicesTosTypeArg], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params({
            'tos_type': to_string(tos_type)
        })
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/terms_of_services']),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, TermsOfServices)

    def create_term_of_service(
        self,
        status: CreateTermOfServiceStatusArg,
        text: str,
        tos_type: Optional[CreateTermOfServiceTosTypeArg] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> Task:
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
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {'status': status, 'tos_type': tos_type, 'text': text}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/terms_of_services']),
            FetchOptions(
                method='POST',
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, Task)

    def get_term_of_service_by_id(
        self,
        terms_of_service_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> TermsOfService:
        """
        Fetches a specific terms of service.
        :param terms_of_service_id: The ID of the terms of service.
            Example: "324234"
        :type terms_of_service_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/terms_of_services/',
                to_string(terms_of_service_id),
            ]),
            FetchOptions(
                method='GET',
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, TermsOfService)

    def update_term_of_service_by_id(
        self,
        terms_of_service_id: str,
        status: UpdateTermOfServiceByIdStatusArg,
        text: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> TermsOfService:
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
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {'status': status, 'text': text}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/terms_of_services/',
                to_string(terms_of_service_id),
            ]),
            FetchOptions(
                method='PUT',
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, TermsOfService)
