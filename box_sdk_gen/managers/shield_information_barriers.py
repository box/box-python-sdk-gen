from enum import Enum

from typing import Optional

from typing import Dict

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.serialization import serialize

from box_sdk_gen.base_object import BaseObject

from box_sdk_gen.schemas import EnterpriseBase

from box_sdk_gen.schemas import UserBase

from box_sdk_gen.schemas import ShieldInformationBarrier

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse


class CreateShieldInformationBarrierChangeStatusStatusArg(str, Enum):
    PENDING = 'pending'
    DISABLED = 'disabled'


class CreateShieldInformationBarrierTypeArg(str, Enum):
    SHIELD_INFORMATION_BARRIER = 'shield_information_barrier'


class CreateShieldInformationBarrierStatusArg(str, Enum):
    DRAFT = 'draft'
    PENDING = 'pending'
    DISABLED = 'disabled'
    ENABLED = 'enabled'
    INVALID = 'invalid'


class ShieldInformationBarriersManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def get_shield_information_barrier_by_id(
        self,
        shield_information_barrier_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> ShieldInformationBarrier:
        """
        Get shield information barrier based on provided ID..
        :param shield_information_barrier_id: The ID of the shield information barrier.
            Example: "1910967"
        :type shield_information_barrier_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    'https://api.box.com/2.0/shield_information_barriers/',
                    shield_information_barrier_id,
                ]
            ),
            FetchOptions(
                method='GET',
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, ShieldInformationBarrier)

    def create_shield_information_barrier_change_status(
        self,
        id: str,
        status: CreateShieldInformationBarrierChangeStatusStatusArg,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> ShieldInformationBarrier:
        """
        Change status of shield information barrier with the specified ID.
        :param id: The ID of the shield information barrier.
        :type id: str
        :param status: The desired status for the shield information barrier.
        :type status: CreateShieldInformationBarrierChangeStatusStatusArg
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body = BaseObject(id=id, status=status)
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                ['https://api.box.com/2.0/shield_information_barriers/change_status']
            ),
            FetchOptions(
                method='POST',
                headers=headers_map,
                body=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, ShieldInformationBarrier)

    def get_shield_information_barriers(
        self,
        marker: Optional[str] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> None:
        """
        Retrieves a list of shield information barrier objects

        for the enterprise of JWT.

        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params(
            {'marker': to_string(marker), 'limit': to_string(limit)}
        )
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/shield_information_barriers']),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return None

    def create_shield_information_barrier(
        self,
        id: Optional[str] = None,
        type: Optional[CreateShieldInformationBarrierTypeArg] = None,
        enterprise: Optional[EnterpriseBase] = None,
        status: Optional[CreateShieldInformationBarrierStatusArg] = None,
        created_at: Optional[str] = None,
        created_by: Optional[UserBase] = None,
        updated_at: Optional[str] = None,
        updated_by: Optional[UserBase] = None,
        enabled_at: Optional[str] = None,
        enabled_by: Optional[UserBase] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> ShieldInformationBarrier:
        """
        Creates a shield information barrier to

        separate individuals/groups within the same


        firm and prevents confidential information passing between them.

        :param id: The unique identifier for the shield information barrier
        :type id: Optional[str], optional
        :param type: The type of the shield information barrier
        :type type: Optional[CreateShieldInformationBarrierTypeArg], optional
        :param status: Status of the shield information barrier
        :type status: Optional[CreateShieldInformationBarrierStatusArg], optional
        :param created_at: ISO date time string when this
            shield information barrier object was created.
        :type created_at: Optional[str], optional
        :param updated_at: ISO date time string when this shield information barrier was updated.
        :type updated_at: Optional[str], optional
        :param enabled_at: ISO date time string when this shield information barrier was enabled.
        :type enabled_at: Optional[str], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body = BaseObject(
            id=id,
            type=type,
            enterprise=enterprise,
            status=status,
            created_at=created_at,
            created_by=created_by,
            updated_at=updated_at,
            updated_by=updated_by,
            enabled_at=enabled_at,
            enabled_by=enabled_by,
        )
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/shield_information_barriers']),
            FetchOptions(
                method='POST',
                headers=headers_map,
                body=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, ShieldInformationBarrier)
