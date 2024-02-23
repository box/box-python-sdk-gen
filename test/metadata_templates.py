import pytest

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import MetadataTemplate

from box_sdk_gen.managers.metadata_templates import CreateMetadataTemplateFields

from box_sdk_gen.managers.metadata_templates import (
    CreateMetadataTemplateFieldsTypeField,
)

from box_sdk_gen.managers.metadata_templates import UpdateMetadataTemplateScope

from box_sdk_gen.managers.metadata_templates import UpdateMetadataTemplateRequestBody

from box_sdk_gen.managers.metadata_templates import (
    UpdateMetadataTemplateRequestBodyOpField,
)

from box_sdk_gen.managers.metadata_templates import GetMetadataTemplateScope

from box_sdk_gen.schemas import MetadataTemplates

from box_sdk_gen.managers.metadata_templates import DeleteMetadataTemplateScope

from box_sdk_gen.schemas import FileFull

from box_sdk_gen.schemas import MetadataFull

from box_sdk_gen.managers.file_metadata import CreateFileMetadataByIdScope

from box_sdk_gen.managers.file_metadata import DeleteFileMetadataByIdScope

from box_sdk_gen.internal.utils import get_uuid

from test.commons import get_default_client

from test.commons import upload_new_file

client: BoxClient = get_default_client()


def testMetadataTemplates():
    template_key: str = ''.join(['key', get_uuid()])
    template: MetadataTemplate = client.metadata_templates.create_metadata_template(
        scope='enterprise',
        template_key=template_key,
        display_name=template_key,
        fields=[
            CreateMetadataTemplateFields(
                type=CreateMetadataTemplateFieldsTypeField.STRING.value,
                key='testName',
                display_name='testName',
            )
        ],
    )
    assert template.template_key == template_key
    assert template.display_name == template_key
    assert len(template.fields) == 1
    assert template.fields[0].key == 'testName'
    assert template.fields[0].display_name == 'testName'
    updated_template: MetadataTemplate = (
        client.metadata_templates.update_metadata_template(
            scope=UpdateMetadataTemplateScope.ENTERPRISE.value,
            template_key=template_key,
            request_body=[
                UpdateMetadataTemplateRequestBody(
                    op=UpdateMetadataTemplateRequestBodyOpField.ADDFIELD.value,
                    field_key='newfieldname',
                    data={'type': 'string', 'displayName': 'newFieldName'},
                )
            ],
        )
    )
    assert len(updated_template.fields) == 2
    assert updated_template.fields[1].key == 'newfieldname'
    assert updated_template.fields[1].display_name == 'newFieldName'
    get_metadata_template: MetadataTemplate = (
        client.metadata_templates.get_metadata_template_by_id(template_id=template.id)
    )
    assert get_metadata_template.id == template.id
    get_metadata_template_schema: MetadataTemplate = (
        client.metadata_templates.get_metadata_template(
            scope=GetMetadataTemplateScope.ENTERPRISE.value,
            template_key=template.template_key,
        )
    )
    assert get_metadata_template_schema.id == template.id
    enterprise_metadata_templates: MetadataTemplates = (
        client.metadata_templates.get_enterprise_metadata_templates()
    )
    assert len(enterprise_metadata_templates.entries) > 0
    global_metadata_templates: MetadataTemplates = (
        client.metadata_templates.get_global_metadata_templates()
    )
    assert len(global_metadata_templates.entries) > 0
    client.metadata_templates.delete_metadata_template(
        scope=DeleteMetadataTemplateScope.ENTERPRISE.value,
        template_key=template.template_key,
    )
    with pytest.raises(Exception):
        client.metadata_templates.delete_metadata_template(
            scope=DeleteMetadataTemplateScope.ENTERPRISE.value,
            template_key=template.template_key,
        )


def testGetMetadataTemplateByInstance():
    file: FileFull = upload_new_file()
    template_key: str = ''.join(['key', get_uuid()])
    template: MetadataTemplate = client.metadata_templates.create_metadata_template(
        scope='enterprise',
        template_key=template_key,
        display_name=template_key,
        fields=[
            CreateMetadataTemplateFields(
                type=CreateMetadataTemplateFieldsTypeField.STRING.value,
                key='testName',
                display_name='testName',
            )
        ],
    )
    created_metadata_instance: MetadataFull = (
        client.file_metadata.create_file_metadata_by_id(
            file_id=file.id,
            scope=CreateFileMetadataByIdScope.ENTERPRISE.value,
            template_key=template_key,
            request_body={'testName': 'xyz'},
        )
    )
    metadata_templates: MetadataTemplates = (
        client.metadata_templates.get_metadata_templates_by_instance_id(
            metadata_instance_id=created_metadata_instance.id
        )
    )
    assert len(metadata_templates.entries) == 1
    assert metadata_templates.entries[0].display_name == template_key
    assert metadata_templates.entries[0].template_key == template_key
    client.file_metadata.delete_file_metadata_by_id(
        file_id=file.id,
        scope=DeleteFileMetadataByIdScope.ENTERPRISE.value,
        template_key=template_key,
    )
    client.metadata_templates.delete_metadata_template(
        scope=DeleteMetadataTemplateScope.ENTERPRISE.value,
        template_key=template.template_key,
    )
    client.files.delete_file_by_id(file_id=file.id)
