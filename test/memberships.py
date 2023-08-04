import pytest

from box_sdk_gen.managers.memberships import UpdateGroupMembershipByIdRoleArg

from box_sdk_gen.utils import decode_base_64

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.client import Client

from box_sdk_gen.jwt_auth import JWTAuth

from box_sdk_gen.jwt_auth import JWTConfig

jwt_config = JWTConfig.from_config_json_string(decode_base_64(get_env_var('JWT_CONFIG_BASE_64')))

auth: JWTAuth = JWTAuth(config=jwt_config)

client: Client = Client(auth=auth)


def testMemberships():
    user: User = client.users.create_user(name=get_uuid(), login=''.join([get_uuid(), '@boxdemo.com']))
    user_memberships: GroupMemberships = client.memberships.get_user_memberships(user_id=user.id)
    assert user_memberships.total_count == 0
    group: Group = client.groups.create_group(name=get_uuid())
    group_memberships: GroupMemberships = client.memberships.get_group_memberships(group_id=group.id)
    assert group_memberships.total_count == 0
    group_membership: GroupMembership = client.memberships.create_group_membership(user=user, group=group)
    assert group_membership.user.id == user.id
    assert group_membership.group.id == group.id
    assert group_membership.role == 'member'
    assert client.memberships.get_group_membership_by_id(group_membership_id=group_membership.id)
    updated_group_membership: GroupMembership = client.memberships.update_group_membership_by_id(group_membership_id=group_membership.id, role=UpdateGroupMembershipByIdRoleArg.ADMIN.value)
    assert updated_group_membership.id == group_membership.id
    assert updated_group_membership.role == 'admin'
    client.memberships.delete_group_membership_by_id(group_membership.id)
    with pytest.raises(Exception):
        client.memberships.get_group_membership_by_id(group_membership_id=group_membership.id)
    client.groups.delete_group_by_id(group.id)
    client.users.delete_user_by_id(user_id=user.id)