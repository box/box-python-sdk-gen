from box_sdk.utils import decode_base_64

from box_sdk.utils import get_env_var

from box_sdk.utils import get_uuid

from box_sdk.client import Client

from box_sdk.jwt_auth import JWTAuth

from box_sdk.jwt_auth import JWTConfig

jwt_config = JWTConfig.from_config_json_string(decode_base_64(get_env_var('JWT_CONFIG_BASE_64')))

auth: JWTAuth = JWTAuth(config=jwt_config)

client: Client = Client(auth=auth)

def test_get_groups():
    groups: Groups = client.groups.get_groups()
    assert groups.total_count >= 0

def test_create_get_delete_group():
    group_name: str = get_uuid()
    group_description: str = 'Group description'
    group: Group = client.groups.create_group(name=group_name, description=group_description)
    assert group.name == group_name
    group_by_id: GroupFull = client.groups.get_group_by_id(group.id, 'id,name,description,group_type')
    assert group_by_id.id == group.id
    assert group_by_id.description == group_description
    updated_group_name: str = get_uuid()
    updated_group: GroupFull = client.groups.update_group_by_id(group_id=group.id, name=updated_group_name)
    assert updated_group.name == updated_group_name
    client.groups.delete_group_by_id(group.id)