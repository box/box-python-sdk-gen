from box_sdk_gen.utils import to_string

import pytest

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import CollaborationAllowlistExemptTargets

from box_sdk_gen.schemas import UserFull

from box_sdk_gen.schemas import CollaborationAllowlistExemptTarget

from box_sdk_gen.managers.collaboration_allowlist_exempt_targets import (
    CreateCollaborationWhitelistExemptTargetUser,
)

from box_sdk_gen.utils import get_uuid

from test.commons import get_default_client

client: BoxClient = get_default_client()


def collaborationAllowlistExemptTargets():
    exempt_targets: CollaborationAllowlistExemptTargets = (
        client.collaboration_allowlist_exempt_targets.get_collaboration_whitelist_exempt_targets()
    )
    assert len(exempt_targets.entries) >= 0
    user: UserFull = client.users.create_user(
        name=get_uuid(),
        login=''.join([get_uuid(), '@boxdemo.com']),
        is_platform_access_only=True,
    )
    new_exempt_target: CollaborationAllowlistExemptTarget = (
        client.collaboration_allowlist_exempt_targets.create_collaboration_whitelist_exempt_target(
            user=CreateCollaborationWhitelistExemptTargetUser(id=user.id)
        )
    )
    assert to_string(new_exempt_target.type) == 'collaboration_whitelist_exempt_target'
    assert new_exempt_target.user.id == user.id
    exempt_target: CollaborationAllowlistExemptTarget = (
        client.collaboration_allowlist_exempt_targets.get_collaboration_whitelist_exempt_target_by_id(
            collaboration_whitelist_exempt_target_id=new_exempt_target.id
        )
    )
    assert exempt_target.id == new_exempt_target.id
    assert exempt_target.user.id == user.id
    client.collaboration_allowlist_exempt_targets.delete_collaboration_whitelist_exempt_target_by_id(
        collaboration_whitelist_exempt_target_id=exempt_target.id
    )
    with pytest.raises(Exception):
        client.collaboration_allowlist_exempt_targets.get_collaboration_whitelist_exempt_target_by_id(
            collaboration_whitelist_exempt_target_id=exempt_target.id
        )
    client.users.delete_user_by_id(user_id=user.id)
