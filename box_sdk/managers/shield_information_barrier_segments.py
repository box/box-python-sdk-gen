from typing import Union

from box_sdk.base_object import BaseObject

import json

from box_sdk.schemas import ShieldInformationBarrierSegment

from box_sdk.schemas import ClientError

from box_sdk.schemas import ShieldInformationBarrierBase

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.jwt_auth import JWTAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class UpdateShieldInformationBarrierSegmentByIdRequestBodyArg(BaseObject):
    def __init__(self, name: Union[None, str] = None, description: Union[None, str] = None, **kwargs):
        """
        :param name: The updated name for the shield information barrier segment.
        :type name: Union[None, str], optional
        :param description: The updated description for
            the shield information barrier segment.
        :type description: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.name = name
        self.description = description

class GetShieldInformationBarrierSegmentsOptionsArg(BaseObject):
    def __init__(self, marker: Union[None, str] = None, limit: Union[None, int] = None, **kwargs):
        """
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Union[None, str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        """
        super().__init__(**kwargs)
        self.marker = marker
        self.limit = limit

class CreateShieldInformationBarrierSegmentRequestBodyArg(BaseObject):
    def __init__(self, shield_information_barrier: ShieldInformationBarrierBase, name: str, description: Union[None, str] = None, **kwargs):
        """
        :param name: Name of the shield information barrier segment
        :type name: str
        :param description: Description of the shield information barrier segment
        :type description: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.shield_information_barrier = shield_information_barrier
        self.name = name
        self.description = description

class ShieldInformationBarrierSegmentsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth, JWTAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_shield_information_barrier_segment_by_id(self, shield_information_barrier_segment_id: str) -> ShieldInformationBarrierSegment:
        """
        Retrieves shield information barrier segment based on provided ID..
        :param shield_information_barrier_segment_id: The ID of the shield information barrier segment.
            Example: "3423"
        :type shield_information_barrier_segment_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segments/', shield_information_barrier_segment_id]), FetchOptions(method='GET', auth=self.auth))
        return ShieldInformationBarrierSegment.from_dict(json.loads(response.text))
    def update_shield_information_barrier_segment_by_id(self, shield_information_barrier_segment_id: str, request_body: UpdateShieldInformationBarrierSegmentByIdRequestBodyArg) -> ShieldInformationBarrierSegment:
        """
        Updates the shield information barrier segment based on provided ID..
        :param shield_information_barrier_segment_id: The ID of the shield information barrier segment.
            Example: "3423"
        :type shield_information_barrier_segment_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segments/', shield_information_barrier_segment_id]), FetchOptions(method='PUT', body=json.dumps(request_body.to_dict()), auth=self.auth))
        return ShieldInformationBarrierSegment.from_dict(json.loads(response.text))
    def delete_shield_information_barrier_segment_by_id(self, shield_information_barrier_segment_id: str):
        """
        Deletes the shield information barrier segment
        
        based on provided ID.

        :param shield_information_barrier_segment_id: The ID of the shield information barrier segment.
            Example: "3423"
        :type shield_information_barrier_segment_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segments/', shield_information_barrier_segment_id]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content
    def get_shield_information_barrier_segments(self, shield_information_barrier_id: str, options: GetShieldInformationBarrierSegmentsOptionsArg = None) -> None:
        """
        Retrieves a list of shield information barrier segment objects
        
        for the specified Information Barrier ID.

        :param shield_information_barrier_id: The ID of the shield information barrier.
            Example: "1910967"
        :type shield_information_barrier_id: str
        """
        if options is None:
            options = GetShieldInformationBarrierSegmentsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segments']), FetchOptions(method='GET', params={'shield_information_barrier_id': shield_information_barrier_id, 'marker': options.marker, 'limit': options.limit}, auth=self.auth))
        return None
    def create_shield_information_barrier_segment(self, request_body: CreateShieldInformationBarrierSegmentRequestBodyArg) -> ShieldInformationBarrierSegment:
        """
        Creates a shield information barrier segment.
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segments']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), auth=self.auth))
        return ShieldInformationBarrierSegment.from_dict(json.loads(response.text))