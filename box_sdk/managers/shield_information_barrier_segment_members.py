from typing import Optional

from box_sdk.base_object import BaseObject

from enum import Enum

import json

from typing import Dict

from box_sdk.schemas import ShieldInformationBarrierSegmentMember

from box_sdk.schemas import ClientError

from box_sdk.schemas import ShieldInformationBarrierBase

from box_sdk.schemas import UserBase

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetShieldInformationBarrierSegmentMembersOptionsArg(BaseObject):
    def __init__(self, marker: Optional[str] = None, limit: Optional[int] = None, **kwargs):
        """
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.marker = marker
        self.limit = limit

class CreateShieldInformationBarrierSegmentMemberRequestBodyArgTypeField(str, Enum):
    SHIELD_INFORMATION_BARRIER_SEGMENT_MEMBER = 'shield_information_barrier_segment_member'

class CreateShieldInformationBarrierSegmentMemberRequestBodyArgShieldInformationBarrierSegmentFieldTypeField(str, Enum):
    SHIELD_INFORMATION_BARRIER_SEGMENT = 'shield_information_barrier_segment'

class CreateShieldInformationBarrierSegmentMemberRequestBodyArgShieldInformationBarrierSegmentField(BaseObject):
    def __init__(self, id: Optional[str] = None, type: Optional[CreateShieldInformationBarrierSegmentMemberRequestBodyArgShieldInformationBarrierSegmentFieldTypeField] = None, **kwargs):
        """
        :param id: The ID reference of the
            requesting shield information barrier segment.
        :type id: Optional[str], optional
        :param type: The type of the shield barrier segment for this member.
        :type type: Optional[CreateShieldInformationBarrierSegmentMemberRequestBodyArgShieldInformationBarrierSegmentFieldTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type

class CreateShieldInformationBarrierSegmentMemberRequestBodyArg(BaseObject):
    def __init__(self, shield_information_barrier_segment: CreateShieldInformationBarrierSegmentMemberRequestBodyArgShieldInformationBarrierSegmentField, user: UserBase, type: Optional[CreateShieldInformationBarrierSegmentMemberRequestBodyArgTypeField] = None, shield_information_barrier: Optional[ShieldInformationBarrierBase] = None, **kwargs):
        """
        :param shield_information_barrier_segment: The `type` and `id` of the
            requested shield information barrier segment.
        :type shield_information_barrier_segment: CreateShieldInformationBarrierSegmentMemberRequestBodyArgShieldInformationBarrierSegmentField
        :param type: -| A type of the shield barrier segment member.
        :type type: Optional[CreateShieldInformationBarrierSegmentMemberRequestBodyArgTypeField], optional
        """
        super().__init__(**kwargs)
        self.shield_information_barrier_segment = shield_information_barrier_segment
        self.user = user
        self.type = type
        self.shield_information_barrier = shield_information_barrier

class ShieldInformationBarrierSegmentMembersManager(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {'network_session': 'networkSession', **BaseObject._fields_to_json_mapping}
    _json_to_fields_mapping: Dict[str, str] = {'networkSession': 'network_session', **BaseObject._json_to_fields_mapping}
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None, **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
        self.network_session = network_session
    def get_shield_information_barrier_segment_member_by_id(self, shield_information_barrier_segment_member_id: str) -> ShieldInformationBarrierSegmentMember:
        """
        Retrieves a shield information barrier
        
        segment member by its ID.

        :param shield_information_barrier_segment_member_id: The ID of the shield information barrier segment Member.
            Example: "7815"
        :type shield_information_barrier_segment_member_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segment_members/', shield_information_barrier_segment_member_id]), FetchOptions(method='GET', auth=self.auth, network_session=self.network_session))
        return ShieldInformationBarrierSegmentMember.from_dict(json.loads(response.text))
    def delete_shield_information_barrier_segment_member_by_id(self, shield_information_barrier_segment_member_id: str):
        """
        Deletes a shield information barrier
        
        segment member based on provided ID.

        :param shield_information_barrier_segment_member_id: The ID of the shield information barrier segment Member.
            Example: "7815"
        :type shield_information_barrier_segment_member_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segment_members/', shield_information_barrier_segment_member_id]), FetchOptions(method='DELETE', auth=self.auth, network_session=self.network_session))
        return response.content
    def get_shield_information_barrier_segment_members(self, shield_information_barrier_segment_id: str, options: GetShieldInformationBarrierSegmentMembersOptionsArg = None) -> None:
        """
        Lists shield information barrier segment members
        
        based on provided segment IDs.

        :param shield_information_barrier_segment_id: The ID of the shield information barrier segment.
            Example: "3423"
        :type shield_information_barrier_segment_id: str
        """
        if options is None:
            options = GetShieldInformationBarrierSegmentMembersOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segment_members']), FetchOptions(method='GET', params={'shield_information_barrier_segment_id': shield_information_barrier_segment_id, 'marker': options.marker, 'limit': options.limit}, auth=self.auth, network_session=self.network_session))
        return None
    def create_shield_information_barrier_segment_member(self, request_body: CreateShieldInformationBarrierSegmentMemberRequestBodyArg) -> ShieldInformationBarrierSegmentMember:
        """
        Creates a new shield information barrier segment member.
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segment_members']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return ShieldInformationBarrierSegmentMember.from_dict(json.loads(response.text))