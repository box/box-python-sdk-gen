from box_sdk_gen.managers.retention_policies import CreateRetentionPolicyPolicyTypeArg

from box_sdk_gen.managers.retention_policies import CreateRetentionPolicyDispositionActionArg

from box_sdk_gen.managers.retention_policies import CreateRetentionPolicyRetentionTypeArg

from box_sdk_gen.utils import decode_base_64

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.client import Client

from box_sdk_gen.jwt_auth import JWTAuth

from box_sdk_gen.jwt_auth import JWTConfig

jwt_config = JWTConfig.from_config_json_string(decode_base_64(get_env_var('JWT_CONFIG_BASE_64')))

auth: JWTAuth = JWTAuth(config=jwt_config)

client: Client = Client(auth=auth)

def testCreateUpdateGetDeleteRetentionPolicy():
    retention_policy_name: str = get_uuid()
    retention_description: str = 'test description'
    retention_policy: RetentionPolicy = client.retention_policies.create_retention_policy(policy_name=retention_policy_name, description=retention_description, policy_type=CreateRetentionPolicyPolicyTypeArg.FINITE.value, disposition_action=CreateRetentionPolicyDispositionActionArg.REMOVE_RETENTION.value, retention_length='1', retention_type=CreateRetentionPolicyRetentionTypeArg.MODIFIABLE.value, can_owner_extend_retention=True, are_owners_notified=True)
    assert retention_policy.policy_name == retention_policy_name
    assert retention_policy.description == retention_description
    retention_policy_by_id: RetentionPolicy = client.retention_policies.get_retention_policy_by_id(retention_policy_id=retention_policy.id)
    assert retention_policy_by_id.id == retention_policy.id
    retention_policies: RetentionPolicies = client.retention_policies.get_retention_policies()
    assert len(retention_policies.entries) > 0
    updated_retention_policy_name: str = get_uuid()
    updated_retention_policy: RetentionPolicy = client.retention_policies.update_retention_policy_by_id(retention_policy_id=retention_policy.id, policy_name=updated_retention_policy_name)
    assert updated_retention_policy.policy_name == updated_retention_policy_name
    client.retention_policies.delete_retention_policy_by_id(retention_policy_id=retention_policy.id)