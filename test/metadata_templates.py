import pytest

from box_sdk_gen.client import BoxClient

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

from box_sdk_gen.utils import get_uuid

from test.commons import get_default_client

client: BoxClient = get_default_client()


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
    get_metadata_template: MetadataTemplate = (
        client.metadata_templates.get_metadata_template_by_id(template_id=template.id)
    )
    assert get_metadata_template.id == template.id
    get_metadata_template_schema: MetadataTemplate = (
        client.metadata_templates.get_metadata_template_schema(
            scope=GetMetadataTemplateSchemaScopeArg.ENTERPRISE.value,
            template_key=template.template_key,
        )
    )
    assert get_metadata_template_schema.id == template.id
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
