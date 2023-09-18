import pytest

from box_sdk_gen.schemas import CollaborationAllowlistEntries

from box_sdk_gen.schemas import CollaborationAllowlistEntry

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


def collaborationAllowlistEntries():
    allowlist: CollaborationAllowlistEntries = (
        client.collaboration_allowlist_entries.get_collaboration_whitelist_entries()
    )
    assert len(allowlist.entries) >= 0
    direction: str = 'inbound'
    domain: str = 'example.com'
    new_entry: CollaborationAllowlistEntry = (
        client.collaboration_allowlist_entries.create_collaboration_whitelist_entry(
            domain=domain, direction=direction
        )
    )
    assert new_entry.type == 'collaboration_whitelist_entry'
    assert new_entry.direction == direction
    assert new_entry.domain == domain
    entry: CollaborationAllowlistEntry = (
        client.collaboration_allowlist_entries.get_collaboration_whitelist_entry_by_id(
            collaboration_whitelist_entry_id=new_entry.id
        )
    )
    assert entry.id == new_entry.id
    assert entry.direction == direction
    assert entry.domain == domain
    client.collaboration_allowlist_entries.delete_collaboration_whitelist_entry_by_id(
        collaboration_whitelist_entry_id=entry.id
    )
    with pytest.raises(Exception):
        client.collaboration_allowlist_entries.get_collaboration_whitelist_entry_by_id(
            collaboration_whitelist_entry_id=entry.id
        )
