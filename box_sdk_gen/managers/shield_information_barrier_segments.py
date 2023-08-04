from typing import Optional

import json

from typing import Dict

from box_sdk_gen.base_object import BaseObject

from box_sdk_gen.schemas import ShieldInformationBarrierSegment

from box_sdk_gen.schemas import ClientError

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
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session

    def get_shield_information_barrier_segment_by_id(self, shield_information_barrier_segment_id: str) -> ShieldInformationBarrierSegment:
        """
        Retrieves shield information barrier segment based on provided ID..
        :param shield_information_barrier_segment_id: The ID of the shield information barrier segment.
            Example: "3423"
        :type shield_information_barrier_segment_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segments/', shield_information_barrier_segment_id]), FetchOptions(method='GET', response_format='json', auth=self.auth, network_session=self.network_session))
        return ShieldInformationBarrierSegment.from_dict(json.loads(response.text))

    def update_shield_information_barrier_segment_by_id(self, shield_information_barrier_segment_id: str, name: Optional[str] = None, description: Optional[str] = None) -> ShieldInformationBarrierSegment:
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
        """
        request_body: BaseObject = BaseObject(name=name, description=description)
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segments/', shield_information_barrier_segment_id]), FetchOptions(method='PUT', body=json.dumps(request_body.to_dict()), content_type='application/json', response_format='json', auth=self.auth, network_session=self.network_session))
        return ShieldInformationBarrierSegment.from_dict(json.loads(response.text))

    def delete_shield_information_barrier_segment_by_id(self, shield_information_barrier_segment_id: str) -> None:
        """
        Deletes the shield information barrier segment

        based on provided ID.

        :param shield_information_barrier_segment_id: The ID of the shield information barrier segment.
            Example: "3423"
        :type shield_information_barrier_segment_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segments/', shield_information_barrier_segment_id]), FetchOptions(method='DELETE', response_format=None, auth=self.auth, network_session=self.network_session))
        return None

    def get_shield_information_barrier_segments(self, shield_information_barrier_id: str, marker: Optional[str] = None, limit: Optional[int] = None) -> None:
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
        """
        query_params_map: Dict[str, str] = prepare_params({'shield_information_barrier_id': to_string(shield_information_barrier_id), 'marker': to_string(marker), 'limit': to_string(limit)})
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segments']), FetchOptions(method='GET', params=query_params_map, response_format='json', auth=self.auth, network_session=self.network_session))
        return None

    def create_shield_information_barrier_segment(self, shield_information_barrier: ShieldInformationBarrierBase, name: str, description: Optional[str] = None) -> ShieldInformationBarrierSegment:
        """
        Creates a shield information barrier segment.
        :param name: Name of the shield information barrier segment
        :type name: str
        :param description: Description of the shield information barrier segment
        :type description: Optional[str], optional
        """
        request_body: BaseObject = BaseObject(shield_information_barrier=shield_information_barrier, name=name, description=description)
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segments']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', response_format='json', auth=self.auth, network_session=self.network_session))
        return ShieldInformationBarrierSegment.from_dict(json.loads(response.text))