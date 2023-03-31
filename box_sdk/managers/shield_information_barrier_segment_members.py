from typing import Union

from box_sdk.base_object import BaseObject

from enum import Enum

import json

from box_sdk.schemas import ShieldInformationBarrierSegmentMember

from box_sdk.schemas import ClientError

from box_sdk.schemas import ShieldInformationBarrierBase

from box_sdk.schemas import UserBase

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.jwt_auth import JWTAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetShieldInformationBarrierSegmentMembersOptionsArg(BaseObject):
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

class CreateShieldInformationBarrierSegmentMemberRequestBodyArgTypeField(str, Enum):
    SHIELD_INFORMATION_BARRIER_SEGMENT_MEMBER = 'shield_information_barrier_segment_member'

class CreateShieldInformationBarrierSegmentMemberRequestBodyArgShieldInformationBarrierSegmentFieldTypeField(str, Enum):
    SHIELD_INFORMATION_BARRIER_SEGMENT = 'shield_information_barrier_segment'

class CreateShieldInformationBarrierSegmentMemberRequestBodyArgShieldInformationBarrierSegmentField(BaseObject):
    def __init__(self, id: Union[None, str] = None, type: Union[None, CreateShieldInformationBarrierSegmentMemberRequestBodyArgShieldInformationBarrierSegmentFieldTypeField] = None, **kwargs):
        """
        :param id: The ID reference of the
            requesting shield information barrier segment.
        :type id: Union[None, str], optional
        :param type: The type of the shield barrier segment for this member.
        :type type: Union[None, CreateShieldInformationBarrierSegmentMemberRequestBodyArgShieldInformationBarrierSegmentFieldTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type

class CreateShieldInformationBarrierSegmentMemberRequestBodyArg(BaseObject):
    def __init__(self, shield_information_barrier_segment: CreateShieldInformationBarrierSegmentMemberRequestBodyArgShieldInformationBarrierSegmentField, user: UserBase, type: Union[None, CreateShieldInformationBarrierSegmentMemberRequestBodyArgTypeField] = None, shield_information_barrier: Union[None, ShieldInformationBarrierBase] = None, **kwargs):
        """
        :param shield_information_barrier_segment: The `type` and `id` of the
            requested shield information barrier segment.
        :type shield_information_barrier_segment: CreateShieldInformationBarrierSegmentMemberRequestBodyArgShieldInformationBarrierSegmentField
        :param type: -| A type of the shield barrier segment member.
        :type type: Union[None, CreateShieldInformationBarrierSegmentMemberRequestBodyArgTypeField], optional
        """
        super().__init__(**kwargs)
        self.shield_information_barrier_segment = shield_information_barrier_segment
        self.user = user
        self.type = type
        self.shield_information_barrier = shield_information_barrier

class ShieldInformationBarrierSegmentMembersManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth, JWTAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_shield_information_barrier_segment_member_by_id(self, shield_information_barrier_segment_member_id: str) -> ShieldInformationBarrierSegmentMember:
        """
        Retrieves a shield information barrier
        
        segment member by its ID.

        :param shield_information_barrier_segment_member_id: The ID of the shield information barrier segment Member.
            Example: "7815"
        :type shield_information_barrier_segment_member_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segment_members/', shield_information_barrier_segment_member_id]), FetchOptions(method='GET', auth=self.auth))
        return ShieldInformationBarrierSegmentMember.from_dict(json.loads(response.text))
    def delete_shield_information_barrier_segment_member_by_id(self, shield_information_barrier_segment_member_id: str):
        """
        Deletes a shield information barrier
        
        segment member based on provided ID.

        :param shield_information_barrier_segment_member_id: The ID of the shield information barrier segment Member.
            Example: "7815"
        :type shield_information_barrier_segment_member_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segment_members/', shield_information_barrier_segment_member_id]), FetchOptions(method='DELETE', auth=self.auth))
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
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segment_members']), FetchOptions(method='GET', params={'shield_information_barrier_segment_id': shield_information_barrier_segment_id, 'marker': options.marker, 'limit': options.limit}, auth=self.auth))
        return None
    def create_shield_information_barrier_segment_member(self, request_body: CreateShieldInformationBarrierSegmentMemberRequestBodyArg) -> ShieldInformationBarrierSegmentMember:
        """
        Creates a new shield information barrier segment member.
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segment_members']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), auth=self.auth))
        return ShieldInformationBarrierSegmentMember.from_dict(json.loads(response.text))