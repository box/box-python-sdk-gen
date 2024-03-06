import pytest

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import CollaborationAllowlistEntries

from box_sdk_gen.schemas import CollaborationAllowlistEntry

from test.commons import get_default_client

client: BoxClient = get_default_client()


def collaborationAllowlistEntries():
    allowlist: CollaborationAllowlistEntries = (
        client.collaboration_allowlist_entries.get_collaboration_whitelist_entries()
    )
    assert len(allowlist.entries) >= 0
    direction: str = 'inbound'
    domain: str = 'example.com'
    new_entry: CollaborationAllowlistEntry = (
        client.collaboration_allowlist_entries.create_collaboration_whitelist_entry(
            domain, direction
        )
    )
    assert new_entry.type == 'collaboration_whitelist_entry'
    assert new_entry.direction == direction
    assert new_entry.domain == domain
    entry: CollaborationAllowlistEntry = (
        client.collaboration_allowlist_entries.get_collaboration_whitelist_entry_by_id(
            new_entry.id
        )
    )
    assert entry.id == new_entry.id
    assert entry.direction == direction
    assert entry.domain == domain
    client.collaboration_allowlist_entries.delete_collaboration_whitelist_entry_by_id(
        entry.id
    )
    with pytest.raises(Exception):
        client.collaboration_allowlist_entries.get_collaboration_whitelist_entry_by_id(
            entry.id
        )
