from box_sdk_gen.utils import to_string

import pytest

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import UserFull

from box_sdk_gen.schemas import GroupMemberships

from box_sdk_gen.schemas import GroupFull

from box_sdk_gen.schemas import GroupMembership

from box_sdk_gen.managers.memberships import CreateGroupMembershipUserArg

from box_sdk_gen.managers.memberships import CreateGroupMembershipGroupArg

from box_sdk_gen.managers.memberships import UpdateGroupMembershipByIdRoleArg

from box_sdk_gen.utils import get_uuid

from test.commons import get_default_client

client: BoxClient = get_default_client()


def testMemberships():
    user: UserFull = client.users.create_user(
        name=get_uuid(), login=''.join([get_uuid(), '@boxdemo.com'])
    )
    user_memberships: GroupMemberships = client.memberships.get_user_memberships(
        user_id=user.id
    )
    assert user_memberships.total_count == 0
    group: GroupFull = client.groups.create_group(name=get_uuid())
    group_memberships: GroupMemberships = client.memberships.get_group_memberships(
        group_id=group.id
    )
    assert group_memberships.total_count == 0
    group_membership: GroupMembership = client.memberships.create_group_membership(
        user=CreateGroupMembershipUserArg(id=user.id),
        group=CreateGroupMembershipGroupArg(id=group.id),
    )
    assert group_membership.user.id == user.id
    assert group_membership.group.id == group.id
    assert to_string(group_membership.role) == 'member'
    get_group_membership: GroupMembership = (
        client.memberships.get_group_membership_by_id(
            group_membership_id=group_membership.id
        )
    )
    assert get_group_membership.id == group_membership.id
    updated_group_membership: GroupMembership = (
        client.memberships.update_group_membership_by_id(
            group_membership_id=group_membership.id,
            role=UpdateGroupMembershipByIdRoleArg.ADMIN.value,
        )
    )
    assert updated_group_membership.id == group_membership.id
    assert to_string(updated_group_membership.role) == 'admin'
    client.memberships.delete_group_membership_by_id(
        group_membership_id=group_membership.id
    )
    with pytest.raises(Exception):
        client.memberships.get_group_membership_by_id(
            group_membership_id=group_membership.id
        )
    client.groups.delete_group_by_id(group_id=group.id)
    client.users.delete_user_by_id(user_id=user.id)
