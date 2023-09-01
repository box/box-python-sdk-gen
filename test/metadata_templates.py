import pytest

from box_sdk_gen.schemas import MetadataTemplate

from box_sdk_gen.managers.metadata_templates import (
    CreateMetadataTemplateSchemaFieldsArg,
)

from box_sdk_gen.managers.metadata_templates import (
    CreateMetadataTemplateSchemaFieldsArgTypeField,
)

from box_sdk_gen.managers.metadata_templates import GetMetadataTemplateSchemaScopeArg

from box_sdk_gen.schemas import MetadataTemplates

from box_sdk_gen.managers.metadata_templates import DeleteMetadataTemplateSchemaScopeArg

from box_sdk_gen.utils import decode_base_64

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.client import Client

from box_sdk_gen.jwt_auth import JWTAuth

from box_sdk_gen.jwt_auth import JWTConfig

jwt_config: JWTConfig = JWTConfig.from_config_json_string(
    decode_base_64(get_env_var('JWT_CONFIG_BASE_64'))
)

auth: JWTAuth = JWTAuth(config=jwt_config)

client: Client = Client(auth=auth)


def testMetadataTemplates():
    template_key: str = ''.join(['key', get_uuid()])
    template: MetadataTemplate = (
        client.metadata_templates.create_metadata_template_schema(
            scope='enterprise',
            template_key=template_key,
            display_name=template_key,
            fields=[
                CreateMetadataTemplateSchemaFieldsArg(
                    type=CreateMetadataTemplateSchemaFieldsArgTypeField.STRING.value,
                    key='testName',
                    display_name='testName',
                )
            ],
        )
    )
    assert template.template_key == template_key
    assert template.display_name == template_key
    assert len(template.fields) == 1
    assert template.fields[0].key == 'testName'
    assert template.fields[0].display_name == 'testName'
    assert client.metadata_templates.get_metadata_template_by_id(
        template_id=template.id
    )
    assert client.metadata_templates.get_metadata_template_schema(
        scope=GetMetadataTemplateSchemaScopeArg.ENTERPRISE.value,
        template_key=template.template_key,
    )
    enterprise_metadata_templates: MetadataTemplates = (
        client.metadata_templates.get_metadata_template_enterprise()
    )
    assert len(enterprise_metadata_templates.entries) > 0
    global_metadata_templates: MetadataTemplates = (
        client.metadata_templates.get_metadata_template_global()
    )
    assert len(global_metadata_templates.entries) > 0
    client.metadata_templates.delete_metadata_template_schema(
        scope=DeleteMetadataTemplateSchemaScopeArg.ENTERPRISE.value,
        template_key=template.template_key,
    )
    with pytest.raises(Exception):
        client.metadata_templates.delete_metadata_template_schema(
            scope=DeleteMetadataTemplateSchemaScopeArg.ENTERPRISE.value,
            template_key=template.template_key,
        )
