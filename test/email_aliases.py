from box_sdk_gen.utils import decode_base_64

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.client import Client

from box_sdk_gen.jwt_auth import JWTAuth

from box_sdk_gen.jwt_auth import JWTConfig

jwt_config = JWTConfig.from_config_json_string(decode_base_64(get_env_var('JWT_CONFIG_BASE_64')))

auth: JWTAuth = JWTAuth(config=jwt_config)

client: Client = Client(auth=auth)

def testEmailAliases():
    new_user_name: str = get_uuid()
    new_user_login: str = ''.join([get_uuid(), '@boxdemo.com'])
    new_user: User = client.users.create_user(name=new_user_name, login=new_user_login)
    aliases: EmailAliases = client.email_aliases.get_user_email_aliases(user_id=new_user.id)
    assert aliases.total_count == 0
    new_alias_email: str = ''.join([new_user.id, '@boxdemo.com'])
    new_alias: EmailAlias = client.email_aliases.create_user_email_alias(user_id=new_user.id, email=new_alias_email)
    updated_aliases: EmailAliases = client.email_aliases.get_user_email_aliases(user_id=new_user.id)
    assert updated_aliases.total_count == 1
    assert updated_aliases.entries[0].email == new_alias_email
    client.email_aliases.delete_user_email_alias_by_id(user_id=new_user.id, email_alias_id=new_alias.id)
    final_aliases: EmailAliases = client.email_aliases.get_user_email_aliases(user_id=new_user.id)
    assert final_aliases.total_count == 0
    client.users.delete_user_by_id(user_id=new_user.id)