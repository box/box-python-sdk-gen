from enum import Enum

from typing import Optional

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.serialization import serialize

from box_sdk_gen.schemas import ShieldInformationBarrier

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import ShieldInformationBarriers

from box_sdk_gen.schemas import EnterpriseBase

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse

from box_sdk_gen.json_data import sd_to_json

from box_sdk_gen.json_data import SerializedData


class UpdateShieldInformationBarrierStatusStatus(str, Enum):
    PENDING = 'pending'
    DISABLED = 'disabled'


class ShieldInformationBarriersManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: NetworkSession = None,
    ):
        if network_session is None:
            network_session = NetworkSession()
        self.auth = auth
        self.network_session = network_session

    def get_shield_information_barrier_by_id(
        self,
        shield_information_barrier_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> ShieldInformationBarrier:
        """
        Get shield information barrier based on provided ID.
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
                    self.network_session.base_urls.base_url,
                    '/shield_information_barriers/',
                    to_string(shield_information_barrier_id),
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
        return deserialize(response.data, ShieldInformationBarrier)

    def update_shield_information_barrier_status(
        self,
        id: str,
        status: UpdateShieldInformationBarrierStatusStatus,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> ShieldInformationBarrier:
        """
        Change status of shield information barrier with the specified ID.
        :param id: The ID of the shield information barrier.
        :type id: str
        :param status: The desired status for the shield information barrier.
        :type status: UpdateShieldInformationBarrierStatusStatus
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {'id': id, 'status': status}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    self.network_session.base_urls.base_url,
                    '/shield_information_barriers/change_status',
                ]
            ),
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
        return deserialize(response.data, ShieldInformationBarrier)

    def get_shield_information_barriers(
        self,
        marker: Optional[str] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> ShieldInformationBarriers:
        """
        Retrieves a list of shield information barrier objects

        for the enterprise of JWT.

        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
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
            ''.join(
                [
                    self.network_session.base_urls.base_url,
                    '/shield_information_barriers',
                ]
            ),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, ShieldInformationBarriers)

    def create_shield_information_barrier(
        self,
        enterprise: EnterpriseBase,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> ShieldInformationBarrier:
        """
        Creates a shield information barrier to

        separate individuals/groups within the same


        firm and prevents confidential information passing between them.

        :param enterprise: The `type` and `id` of enterprise this barrier is under.
        :type enterprise: EnterpriseBase
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {'enterprise': enterprise}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    self.network_session.base_urls.base_url,
                    '/shield_information_barriers',
                ]
            ),
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
        return deserialize(response.data, ShieldInformationBarrier)
