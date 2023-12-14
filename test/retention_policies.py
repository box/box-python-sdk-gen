from box_sdk_gen.schemas import RetentionPolicy

from box_sdk_gen.managers.retention_policies import CreateRetentionPolicyPolicyType

from box_sdk_gen.managers.retention_policies import (
    CreateRetentionPolicyDispositionAction,
)

from box_sdk_gen.managers.retention_policies import CreateRetentionPolicyRetentionType

from box_sdk_gen.schemas import RetentionPolicies

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.client import BoxClient

from test.commons import get_default_client

client: BoxClient = get_default_client()


def testCreateUpdateGetDeleteRetentionPolicy():
    retention_policy_name: str = get_uuid()
    retention_description: str = 'test description'
    retention_policy: RetentionPolicy = (
        client.retention_policies.create_retention_policy(
            policy_name=retention_policy_name,
            description=retention_description,
            policy_type=CreateRetentionPolicyPolicyType.FINITE.value,
            disposition_action=CreateRetentionPolicyDispositionAction.REMOVE_RETENTION.value,
            retention_length='1',
            retention_type=CreateRetentionPolicyRetentionType.MODIFIABLE.value,
            can_owner_extend_retention=True,
            are_owners_notified=True,
        )
    )
    assert retention_policy.policy_name == retention_policy_name
    assert retention_policy.description == retention_description
    retention_policy_by_id: RetentionPolicy = (
        client.retention_policies.get_retention_policy_by_id(
            retention_policy_id=retention_policy.id
        )
    )
    assert retention_policy_by_id.id == retention_policy.id
    retention_policies: RetentionPolicies = (
        client.retention_policies.get_retention_policies()
    )
    assert len(retention_policies.entries) > 0
    updated_retention_policy_name: str = get_uuid()
    updated_retention_policy: RetentionPolicy = (
        client.retention_policies.update_retention_policy_by_id(
            retention_policy_id=retention_policy.id,
            policy_name=updated_retention_policy_name,
        )
    )
    assert updated_retention_policy.policy_name == updated_retention_policy_name
    client.retention_policies.delete_retention_policy_by_id(
        retention_policy_id=retention_policy.id
    )
