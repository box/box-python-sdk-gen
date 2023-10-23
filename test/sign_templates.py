from box_sdk_gen.schemas import SignTemplates

from box_sdk_gen.schemas import SignTemplate

from box_sdk_gen.utils import decode_base_64

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.client import BoxClient

from box_sdk_gen.jwt_auth import BoxJWTAuth

from box_sdk_gen.jwt_auth import JWTConfig

jwt_config: JWTConfig = JWTConfig.from_config_json_string(
    decode_base_64(get_env_var('JWT_CONFIG_BASE_64'))
)

auth: BoxJWTAuth = BoxJWTAuth(config=jwt_config)

client: BoxClient = BoxClient(auth=auth)


def testGetSignTemplates():
    auth.as_user(get_env_var('USER_ID'))
    sign_templates: SignTemplates = client.sign_templates.get_sign_templates(limit=2)
    assert len(sign_templates.entries) >= 0


def testGetSignTemplate():
    auth.as_user(get_env_var('USER_ID'))
    sign_templates: SignTemplates = client.sign_templates.get_sign_templates(limit=2)
    assert len(sign_templates.entries) >= 0
    if len(sign_templates.entries) > 0:
        sign_template: SignTemplate = client.sign_templates.get_sign_template_by_id(
            template_id=sign_templates.entries[0].id
        )
        assert sign_template.id == sign_templates.entries[0].id
        assert len(sign_template.source_files) > 0
        assert not sign_template.name == ''
        assert not sign_template.parent_folder.id == ''
