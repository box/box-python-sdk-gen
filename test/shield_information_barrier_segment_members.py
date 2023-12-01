import pytest

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import ShieldInformationBarrier

from box_sdk_gen.schemas import ShieldInformationBarrierSegment

from box_sdk_gen.schemas import ShieldInformationBarrierBase

from box_sdk_gen.schemas import ShieldInformationBarrierBaseTypeField

from box_sdk_gen.schemas import ShieldInformationBarrierSegmentMember

from box_sdk_gen.managers.shield_information_barrier_segment_members import (
    CreateShieldInformationBarrierSegmentMemberShieldInformationBarrierSegmentArg,
)

from box_sdk_gen.managers.shield_information_barrier_segment_members import (
    CreateShieldInformationBarrierSegmentMemberShieldInformationBarrierSegmentArgTypeField,
)

from box_sdk_gen.schemas import UserBase

from box_sdk_gen.schemas import UserBaseTypeField

from box_sdk_gen.schemas import ShieldInformationBarrierSegmentMembers

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.utils import get_uuid

from test.commons import get_default_client_as_user

from test.commons import get_or_create_shield_information_barrier


def testShieldInformationBarrierSegmentMembers():
    client: BoxClient = get_default_client_as_user(get_env_var('USER_ID'))
    enterprise_id: str = get_env_var('ENTERPRISE_ID')
    barrier: ShieldInformationBarrier = get_or_create_shield_information_barrier(
        client, enterprise_id
    )
    barrier_id: str = barrier.id
    segment_name: str = get_uuid()
    segment: ShieldInformationBarrierSegment = (
        client.shield_information_barrier_segments.create_shield_information_barrier_segment(
            shield_information_barrier=ShieldInformationBarrierBase(
                id=barrier_id,
                type=ShieldInformationBarrierBaseTypeField.SHIELD_INFORMATION_BARRIER.value,
            ),
            name=segment_name,
        )
    )
    assert segment.name == segment_name
    segment_member: ShieldInformationBarrierSegmentMember = (
        client.shield_information_barrier_segment_members.create_shield_information_barrier_segment_member(
            shield_information_barrier_segment=CreateShieldInformationBarrierSegmentMemberShieldInformationBarrierSegmentArg(
                id=segment.id,
                type=CreateShieldInformationBarrierSegmentMemberShieldInformationBarrierSegmentArgTypeField.SHIELD_INFORMATION_BARRIER_SEGMENT.value,
            ),
            user=UserBase(id=get_env_var('USER_ID'), type=UserBaseTypeField.USER.value),
        )
    )
    assert segment_member.user.id == get_env_var('USER_ID')
    assert segment_member.shield_information_barrier_segment.id == segment.id
    segment_members: ShieldInformationBarrierSegmentMembers = (
        client.shield_information_barrier_segment_members.get_shield_information_barrier_segment_members(
            shield_information_barrier_segment_id=segment.id
        )
    )
    assert len(segment_members.entries) > 0
    segment_member_get: ShieldInformationBarrierSegmentMember = (
        client.shield_information_barrier_segment_members.get_shield_information_barrier_segment_member_by_id(
            shield_information_barrier_segment_member_id=segment_member.id
        )
    )
    assert segment_member_get.id == segment_member.id
    client.shield_information_barrier_segment_members.delete_shield_information_barrier_segment_member_by_id(
        shield_information_barrier_segment_member_id=segment_member.id
    )
    with pytest.raises(Exception):
        client.shield_information_barrier_segment_members.get_shield_information_barrier_segment_member_by_id(
            shield_information_barrier_segment_member_id=segment_member.id
        )
    client.shield_information_barrier_segments.delete_shield_information_barrier_segment_by_id(
        shield_information_barrier_segment_id=segment.id
    )
