from box_sdk_gen.schemas import LegalHoldPolicy

from box_sdk_gen.schemas import LegalHoldPolicies

from box_sdk_gen.internal.utils import get_uuid

from box_sdk_gen.client import BoxClient

from test.commons import get_default_client

client: BoxClient = get_default_client()


def testCreateUpdateGetDeleteLegalHoldPolicy():
    legal_hold_policy_name: str = get_uuid()
    legal_hold_description: str = 'test description'
    legal_hold_policy: LegalHoldPolicy = (
        client.legal_hold_policies.create_legal_hold_policy(
            legal_hold_policy_name, description=legal_hold_description, is_ongoing=True
        )
    )
    assert legal_hold_policy.policy_name == legal_hold_policy_name
    assert legal_hold_policy.description == legal_hold_description
    legal_hold_policy_id: str = legal_hold_policy.id
    legal_hold_policy_by_id: LegalHoldPolicy = (
        client.legal_hold_policies.get_legal_hold_policy_by_id(legal_hold_policy_id)
    )
    assert legal_hold_policy_by_id.id == legal_hold_policy_id
    legal_hold_policies: LegalHoldPolicies = (
        client.legal_hold_policies.get_legal_hold_policies()
    )
    assert len(legal_hold_policies.entries) > 0
    updated_legal_hold_policy_name: str = get_uuid()
    updated_legal_hold_policy: LegalHoldPolicy = (
        client.legal_hold_policies.update_legal_hold_policy_by_id(
            legal_hold_policy_id, policy_name=updated_legal_hold_policy_name
        )
    )
    assert updated_legal_hold_policy.policy_name == updated_legal_hold_policy_name
    client.legal_hold_policies.delete_legal_hold_policy_by_id(legal_hold_policy_id)
