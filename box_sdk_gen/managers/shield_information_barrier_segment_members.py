from enum import Enum

from typing import Optional

from box_sdk_gen.base_object import BaseObject

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.serialization import serialize

from box_sdk_gen.schemas import ShieldInformationBarrierSegmentMember

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import ShieldInformationBarrierSegmentMembers

from box_sdk_gen.schemas import ShieldInformationBarrierBase

from box_sdk_gen.schemas import UserBase

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse

from box_sdk_gen.json import sd_to_json

from box_sdk_gen.json import SerializedData


class CreateShieldInformationBarrierSegmentMemberTypeArg(str, Enum):
    SHIELD_INFORMATION_BARRIER_SEGMENT_MEMBER = (
        'shield_information_barrier_segment_member'
    )


class CreateShieldInformationBarrierSegmentMemberShieldInformationBarrierSegmentArgTypeField(
    str, Enum
):
    SHIELD_INFORMATION_BARRIER_SEGMENT = 'shield_information_barrier_segment'


class CreateShieldInformationBarrierSegmentMemberShieldInformationBarrierSegmentArg(
    BaseObject
):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[
            CreateShieldInformationBarrierSegmentMemberShieldInformationBarrierSegmentArgTypeField
        ] = None,
        **kwargs
    ):
        """
        :param id: The ID reference of the
            requesting shield information barrier segment.
        :type id: Optional[str], optional
        :param type: The type of the shield barrier segment for this member.
        :type type: Optional[CreateShieldInformationBarrierSegmentMemberShieldInformationBarrierSegmentArgTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class ShieldInformationBarrierSegmentMembersManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def get_shield_information_barrier_segment_member_by_id(
        self,
        shield_information_barrier_segment_member_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> ShieldInformationBarrierSegmentMember:
        """
        Retrieves a shield information barrier

        segment member by its ID.

        :param shield_information_barrier_segment_member_id: The ID of the shield information barrier segment Member.
            Example: "7815"
        :type shield_information_barrier_segment_member_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/shield_information_barrier_segment_members/',
                to_string(shield_information_barrier_segment_member_id),
            ]),
            FetchOptions(
                method='GET',
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, ShieldInformationBarrierSegmentMember)

    def delete_shield_information_barrier_segment_member_by_id(
        self,
        shield_information_barrier_segment_member_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> None:
        """
        Deletes a shield information barrier

        segment member based on provided ID.

        :param shield_information_barrier_segment_member_id: The ID of the shield information barrier segment Member.
            Example: "7815"
        :type shield_information_barrier_segment_member_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/shield_information_barrier_segment_members/',
                to_string(shield_information_barrier_segment_member_id),
            ]),
            FetchOptions(
                method='DELETE',
                headers=headers_map,
                response_format=None,
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return None

    def get_shield_information_barrier_segment_members(
        self,
        shield_information_barrier_segment_id: str,
        marker: Optional[str] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> ShieldInformationBarrierSegmentMembers:
        """
        Lists shield information barrier segment members

        based on provided segment IDs.

        :param shield_information_barrier_segment_id: The ID of the shield information barrier segment.
        :type shield_information_barrier_segment_id: str
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
        query_params_map: Dict[str, str] = prepare_params({
            'shield_information_barrier_segment_id': to_string(
                shield_information_barrier_segment_id
            ),
            'marker': to_string(marker),
            'limit': to_string(limit),
        })
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/shield_information_barrier_segment_members'
            ]),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, ShieldInformationBarrierSegmentMembers)

    def create_shield_information_barrier_segment_member(
        self,
        shield_information_barrier_segment: CreateShieldInformationBarrierSegmentMemberShieldInformationBarrierSegmentArg,
        user: UserBase,
        type: Optional[CreateShieldInformationBarrierSegmentMemberTypeArg] = None,
        shield_information_barrier: Optional[ShieldInformationBarrierBase] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> ShieldInformationBarrierSegmentMember:
        """
        Creates a new shield information barrier segment member.
        :param shield_information_barrier_segment: The `type` and `id` of the
            requested shield information barrier segment.
        :type shield_information_barrier_segment: CreateShieldInformationBarrierSegmentMemberShieldInformationBarrierSegmentArg
        :param user: User to which restriction will be applied.
        :type user: UserBase
        :param type: -| A type of the shield barrier segment member.
        :type type: Optional[CreateShieldInformationBarrierSegmentMemberTypeArg], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {
            'type': type,
            'shield_information_barrier': shield_information_barrier,
            'shield_information_barrier_segment': shield_information_barrier_segment,
            'user': user,
        }
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/shield_information_barrier_segment_members'
            ]),
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
        return deserialize(response.data, ShieldInformationBarrierSegmentMember)
