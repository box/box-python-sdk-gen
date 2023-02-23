from typing import Union

from base_object import BaseObject

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

import json

from schemas import ShieldInformationBarrierSegmentMember

from schemas import ClientError

from schemas import ShieldInformationBarrierBase

from schemas import UserBase

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

class PostShieldInformationBarrierSegmentMembersRequestBodyArgTypeField:
    pass

class PostShieldInformationBarrierSegmentMembersRequestBodyArgShieldInformationBarrierSegmentFieldTypeField:
    pass

class PostShieldInformationBarrierSegmentMembersRequestBodyArgShieldInformationBarrierSegmentField(BaseObject):
    def __init__(self, id: Union[None, str] = None, type: Union[None, PostShieldInformationBarrierSegmentMembersRequestBodyArgShieldInformationBarrierSegmentFieldTypeField] = None, **kwargs):
        """
        :param id: The ID reference of the
            requesting shield information barrier segment.
        :type id: Union[None, str], optional
        :param type: The type of the shield barrier segment for this member.
        :type type: Union[None, PostShieldInformationBarrierSegmentMembersRequestBodyArgShieldInformationBarrierSegmentFieldTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type

class PostShieldInformationBarrierSegmentMembersRequestBodyArg(BaseObject):
    def __init__(self, shield_information_barrier_segment: PostShieldInformationBarrierSegmentMembersRequestBodyArgShieldInformationBarrierSegmentField, user: UserBase, type: Union[None, PostShieldInformationBarrierSegmentMembersRequestBodyArgTypeField] = None, shield_information_barrier: Union[None, ShieldInformationBarrierBase] = None, **kwargs):
        """
        :param shield_information_barrier_segment: The `type` and `id` of the
            requested shield information barrier segment.
        :type shield_information_barrier_segment: PostShieldInformationBarrierSegmentMembersRequestBodyArgShieldInformationBarrierSegmentField
        :param type: -| A type of the shield barrier segment member.
        :type type: Union[None, PostShieldInformationBarrierSegmentMembersRequestBodyArgTypeField], optional
        """
        super().__init__(**kwargs)
        self.shield_information_barrier_segment = shield_information_barrier_segment
        self.user = user
        self.type = type
        self.shield_information_barrier = shield_information_barrier

class ShieldInformationBarrierSegmentMembersManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getShieldInformationBarrierSegmentMembersId(self, shieldInformationBarrierSegmentMemberId: str) -> ShieldInformationBarrierSegmentMember:
        """
        Retrieves a shield information barrier
        
        segment member by its ID.

        :param shieldInformationBarrierSegmentMemberId: The ID of the shield information barrier segment Member.
            Example: "7815"
        :type shieldInformationBarrierSegmentMemberId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segment_members/', shieldInformationBarrierSegmentMemberId]), FetchOptions(method='GET', auth=self.auth))
        return ShieldInformationBarrierSegmentMember.from_dict(json.loads(response.text))
    def deleteShieldInformationBarrierSegmentMembersId(self, shieldInformationBarrierSegmentMemberId: str):
        """
        Deletes a shield information barrier
        
        segment member based on provided ID.

        :param shieldInformationBarrierSegmentMemberId: The ID of the shield information barrier segment Member.
            Example: "7815"
        :type shieldInformationBarrierSegmentMemberId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segment_members/', shieldInformationBarrierSegmentMemberId]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content
    def getShieldInformationBarrierSegmentMembers(self, shieldInformationBarrierSegmentId: str, options: GetShieldInformationBarrierSegmentMembersOptionsArg = None) -> None:
        """
        Lists shield information barrier segment members
        
        based on provided segment IDs.

        :param shieldInformationBarrierSegmentId: The ID of the shield information barrier segment.
            Example: "3423"
        :type shieldInformationBarrierSegmentId: str
        """
        if options is None:
            options = GetShieldInformationBarrierSegmentMembersOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segment_members']), FetchOptions(method='GET', params={'shield_information_barrier_segment_id': shieldInformationBarrierSegmentId, 'marker': options.marker, 'limit': options.limit}, auth=self.auth))
        return None
    def postShieldInformationBarrierSegmentMembers(self, requestBody: PostShieldInformationBarrierSegmentMembersRequestBodyArg) -> ShieldInformationBarrierSegmentMember:
        """
        Creates a new shield information barrier segment member.
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segment_members']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return ShieldInformationBarrierSegmentMember.from_dict(json.loads(response.text))