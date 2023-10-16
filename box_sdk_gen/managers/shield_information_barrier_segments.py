from typing import Optional

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.serialization import serialize

from box_sdk_gen.schemas import ShieldInformationBarrierSegment

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import ShieldInformationBarrierSegments

from box_sdk_gen.schemas import ShieldInformationBarrierBase

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse


class ShieldInformationBarrierSegmentsManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def get_shield_information_barrier_segment_by_id(
        self,
        shield_information_barrier_segment_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> ShieldInformationBarrierSegment:
        """
        Retrieves shield information barrier segment based on provided ID..
        :param shield_information_barrier_segment_id: The ID of the shield information barrier segment.
            Example: "3423"
        :type shield_information_barrier_segment_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    'https://api.box.com/2.0/shield_information_barrier_segments/',
                    to_string(shield_information_barrier_segment_id),
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
        return deserialize(response.text, ShieldInformationBarrierSegment)

    def update_shield_information_barrier_segment_by_id(
        self,
        shield_information_barrier_segment_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> ShieldInformationBarrierSegment:
        """
        Updates the shield information barrier segment based on provided ID..
        :param shield_information_barrier_segment_id: The ID of the shield information barrier segment.
            Example: "3423"
        :type shield_information_barrier_segment_id: str
        :param name: The updated name for the shield information barrier segment.
        :type name: Optional[str], optional
        :param description: The updated description for
            the shield information barrier segment.
        :type description: Optional[str], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body = {'name': name, 'description': description}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    'https://api.box.com/2.0/shield_information_barrier_segments/',
                    to_string(shield_information_barrier_segment_id),
                ]
            ),
            FetchOptions(
                method='PUT',
                headers=headers_map,
                body=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, ShieldInformationBarrierSegment)

    def delete_shield_information_barrier_segment_by_id(
        self,
        shield_information_barrier_segment_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> None:
        """
        Deletes the shield information barrier segment

        based on provided ID.

        :param shield_information_barrier_segment_id: The ID of the shield information barrier segment.
            Example: "3423"
        :type shield_information_barrier_segment_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    'https://api.box.com/2.0/shield_information_barrier_segments/',
                    to_string(shield_information_barrier_segment_id),
                ]
            ),
            FetchOptions(
                method='DELETE',
                headers=headers_map,
                response_format=None,
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return None

    def get_shield_information_barrier_segments(
        self,
        shield_information_barrier_id: str,
        marker: Optional[str] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> ShieldInformationBarrierSegments:
        """
        Retrieves a list of shield information barrier segment objects

        for the specified Information Barrier ID.

        :param shield_information_barrier_id: The ID of the shield information barrier.
        :type shield_information_barrier_id: str
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
            {
                'shield_information_barrier_id': to_string(
                    shield_information_barrier_id
                ),
                'marker': to_string(marker),
                'limit': to_string(limit),
            }
        )
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/shield_information_barrier_segments']),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, ShieldInformationBarrierSegments)

    def create_shield_information_barrier_segment(
        self,
        shield_information_barrier: ShieldInformationBarrierBase,
        name: str,
        description: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> ShieldInformationBarrierSegment:
        """
        Creates a shield information barrier segment.
        :param name: Name of the shield information barrier segment
        :type name: str
        :param description: Description of the shield information barrier segment
        :type description: Optional[str], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body = {
            'shield_information_barrier': shield_information_barrier,
            'name': name,
            'description': description,
        }
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/shield_information_barrier_segments']),
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
        return deserialize(response.text, ShieldInformationBarrierSegment)
