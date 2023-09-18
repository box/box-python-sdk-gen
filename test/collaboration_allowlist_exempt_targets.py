import pytest

from box_sdk_gen.schemas import CollaborationAllowlistExemptTargets

from box_sdk_gen.schemas import User

from box_sdk_gen.schemas import CollaborationAllowlistExemptTarget

from box_sdk_gen.managers.collaboration_allowlist_exempt_targets import (
    CreateCollaborationWhitelistExemptTargetUserArg,
)

from box_sdk_gen.utils import decode_base_64

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.client import BoxClient

from box_sdk_gen.jwt_auth import BoxJWTAuth

from box_sdk_gen.jwt_auth import JWTConfig

client: BoxClient = BoxClient(
    auth=BoxJWTAuth(
        config=JWTConfig.from_config_json_string(
            decode_base_64(get_env_var('JWT_CONFIG_BASE_64'))
        )
    )
)


def collaborationAllowlistExemptTargets():
    exempt_targets: CollaborationAllowlistExemptTargets = (
        client.collaboration_allowlist_exempt_targets.get_collaboration_whitelist_exempt_targets()
    )
    assert len(exempt_targets.entries) >= 0
    user: User = client.users.create_user(
        name=get_uuid(),
        login=''.join([get_uuid(), '@boxdemo.com']),
        is_platform_access_only=True,
    )
    new_exempt_target: CollaborationAllowlistExemptTarget = client.collaboration_allowlist_exempt_targets.create_collaboration_whitelist_exempt_target(
        user=CreateCollaborationWhitelistExemptTargetUserArg(id=user.id)
    )
    assert new_exempt_target.type == 'collaboration_whitelist_exempt_target'
    assert new_exempt_target.user.id == user.id
    exempt_target: CollaborationAllowlistExemptTarget = client.collaboration_allowlist_exempt_targets.get_collaboration_whitelist_exempt_target_by_id(
        collaboration_whitelist_exempt_target_id=new_exempt_target.id
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
