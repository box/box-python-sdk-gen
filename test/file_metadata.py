from box_sdk_gen.internal.utils import to_string

import pytest

from typing import List

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import FileFull

from box_sdk_gen.schemas import Metadatas

from box_sdk_gen.schemas import MetadataFull

from box_sdk_gen.managers.file_metadata import CreateFileMetadataByIdScope

from box_sdk_gen.managers.file_metadata import GetFileMetadataByIdScope

from box_sdk_gen.managers.file_metadata import UpdateFileMetadataByIdScope

from box_sdk_gen.managers.file_metadata import UpdateFileMetadataByIdRequestBody

from box_sdk_gen.managers.file_metadata import UpdateFileMetadataByIdRequestBodyOpField

from box_sdk_gen.managers.file_metadata import DeleteFileMetadataByIdScope

from box_sdk_gen.schemas import MetadataTemplate

from box_sdk_gen.managers.metadata_templates import CreateMetadataTemplateFields

from box_sdk_gen.managers.metadata_templates import (
    CreateMetadataTemplateFieldsTypeField,
)

from box_sdk_gen.managers.metadata_templates import (
    CreateMetadataTemplateFieldsOptionsField,
)

from box_sdk_gen.managers.metadata_templates import DeleteMetadataTemplateScope

from box_sdk_gen.internal.utils import generate_byte_stream

from box_sdk_gen.internal.utils import get_uuid

from test.commons import get_default_client

from test.commons import upload_new_file

client: BoxClient = get_default_client()


def testGlobalFileMetadata():
    file: FileFull = upload_new_file()
    file_metadata: Metadatas = client.file_metadata.get_file_metadata(file.id)
    assert len(file_metadata.entries) == 0
    created_metadata: MetadataFull = client.file_metadata.create_file_metadata_by_id(
        file.id, CreateFileMetadataByIdScope.GLOBAL.value, 'properties', {'abc': 'xyz'}
    )
    assert to_string(created_metadata.template) == 'properties'
    assert to_string(created_metadata.scope) == 'global'
    assert created_metadata.version == 0
    received_metadata: MetadataFull = client.file_metadata.get_file_metadata_by_id(
        file.id, GetFileMetadataByIdScope.GLOBAL.value, 'properties'
    )
    assert received_metadata.extra_data['abc'] == 'xyz'
    new_value: str = 'bar'
    updated_metadata: MetadataFull = client.file_metadata.update_file_metadata_by_id(
        file.id,
        UpdateFileMetadataByIdScope.GLOBAL.value,
        'properties',
        [
            UpdateFileMetadataByIdRequestBody(
                op=UpdateFileMetadataByIdRequestBodyOpField.REPLACE.value,
                path='/abc',
                value=new_value,
            )
        ],
    )
    received_updated_metadata: MetadataFull = (
        client.file_metadata.get_file_metadata_by_id(
            file.id, GetFileMetadataByIdScope.GLOBAL.value, 'properties'
        )
    )
    assert received_updated_metadata.extra_data['abc'] == new_value
    client.file_metadata.delete_file_metadata_by_id(
        file.id, DeleteFileMetadataByIdScope.GLOBAL.value, 'properties'
    )
    with pytest.raises(Exception):
        client.file_metadata.get_file_metadata_by_id(
            file.id, GetFileMetadataByIdScope.GLOBAL.value, 'properties'
        )
    client.files.delete_file_by_id(file.id)


def testEnterpriseFileMetadata():
    file: FileFull = upload_new_file()
    template_key: str = ''.join(['key', get_uuid()])
    template: MetadataTemplate = client.metadata_templates.create_metadata_template(
        'enterprise',
        template_key,
        template_key=template_key,
        fields=[
            CreateMetadataTemplateFields(
                type=CreateMetadataTemplateFieldsTypeField.STRING.value,
                key='name',
                display_name='name',
            ),
            CreateMetadataTemplateFields(
                type=CreateMetadataTemplateFieldsTypeField.FLOAT.value,
                key='age',
                display_name='age',
            ),
            CreateMetadataTemplateFields(
                type=CreateMetadataTemplateFieldsTypeField.DATE.value,
                key='birthDate',
                display_name='birthDate',
            ),
            CreateMetadataTemplateFields(
                type=CreateMetadataTemplateFieldsTypeField.ENUM.value,
                key='countryCode',
                display_name='countryCode',
                options=[
                    CreateMetadataTemplateFieldsOptionsField(key='US'),
                    CreateMetadataTemplateFieldsOptionsField(key='CA'),
                ],
            ),
            CreateMetadataTemplateFields(
                type=CreateMetadataTemplateFieldsTypeField.MULTISELECT.value,
                key='sports',
                display_name='sports',
                options=[
                    CreateMetadataTemplateFieldsOptionsField(key='basketball'),
                    CreateMetadataTemplateFieldsOptionsField(key='football'),
                    CreateMetadataTemplateFieldsOptionsField(key='tennis'),
                ],
            ),
        ],
    )
    created_metadata: MetadataFull = client.file_metadata.create_file_metadata_by_id(
        file.id,
        CreateFileMetadataByIdScope.ENTERPRISE.value,
        template_key,
        {
            'name': 'John',
            'age': 23,
            'birthDate': '2001-01-03T02:20:50.520Z',
            'countryCode': 'US',
            'sports': ['basketball', 'tennis'],
        },
    )
    assert to_string(created_metadata.template) == template_key
    assert created_metadata.extra_data['name'] == 'John'
    assert created_metadata.extra_data['age'] == 23
    assert created_metadata.extra_data['birthDate'] == '2001-01-03T02:20:50.520Z'
    assert created_metadata.extra_data['countryCode'] == 'US'
    sports: List[str] = created_metadata.extra_data['sports']
    assert sports[0] == 'basketball'
    assert sports[1] == 'tennis'
    client.file_metadata.delete_file_metadata_by_id(
        file.id, DeleteFileMetadataByIdScope.ENTERPRISE.value, template_key
    )
    client.metadata_templates.delete_metadata_template(
        DeleteMetadataTemplateScope.ENTERPRISE.value, template_key
    )
    client.files.delete_file_by_id(file.id)
