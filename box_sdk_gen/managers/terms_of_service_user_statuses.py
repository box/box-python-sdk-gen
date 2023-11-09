from enum import Enum

from box_sdk_gen.base_object import BaseObject

from typing import Optional

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.serialization import serialize

from box_sdk_gen.schemas import TermsOfServiceUserStatuses

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import TermsOfServiceUserStatus

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


class CreateTermOfServiceUserStatusTosArgTypeField(str, Enum):
    TERMS_OF_SERVICE = 'terms_of_service'


class CreateTermOfServiceUserStatusTosArg(BaseObject):
    def __init__(
        self, type: CreateTermOfServiceUserStatusTosArgTypeField, id: str, **kwargs
    ):
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
    def __init__(
        self, type: CreateTermOfServiceUserStatusUserArgTypeField, id: str, **kwargs
    ):
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
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def get_term_of_service_user_statuses(
        self,
        tos_id: str,
        user_id: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> TermsOfServiceUserStatuses:
        """
        Retrieves an overview of users and their status for a

        terms of service, including Whether they have accepted


        the terms and when.

        :param tos_id: The ID of the terms of service.
        :type tos_id: str
        :param user_id: Limits results to the given user ID.
        :type user_id: Optional[str], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params({
            'tos_id': to_string(tos_id), 'user_id': to_string(user_id)
        })
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/terms_of_service_user_statuses']),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, TermsOfServiceUserStatuses)

    def create_term_of_service_user_status(
        self,
        tos: CreateTermOfServiceUserStatusTosArg,
        user: CreateTermOfServiceUserStatusUserArg,
        is_accepted: bool,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> TermsOfServiceUserStatus:
        """
        Sets the status for a terms of service for a user.
        :param tos: The terms of service to set the status for.
        :type tos: CreateTermOfServiceUserStatusTosArg
        :param user: The user to set the status for.
        :type user: CreateTermOfServiceUserStatusUserArg
        :param is_accepted: Whether the user has accepted the terms.
        :type is_accepted: bool
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {'tos': tos, 'user': user, 'is_accepted': is_accepted}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/terms_of_service_user_statuses']),
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
        return deserialize(response.data, TermsOfServiceUserStatus)

    def update_term_of_service_user_status_by_id(
        self,
        terms_of_service_user_status_id: str,
        is_accepted: bool,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> TermsOfServiceUserStatus:
        """
        Updates the status for a terms of service for a user.
        :param terms_of_service_user_status_id: The ID of the terms of service status.
            Example: "324234"
        :type terms_of_service_user_status_id: str
        :param is_accepted: Whether the user has accepted the terms.
        :type is_accepted: bool
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {'is_accepted': is_accepted}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/terms_of_service_user_statuses/',
                to_string(terms_of_service_user_status_id),
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
        return deserialize(response.data, TermsOfServiceUserStatus)
