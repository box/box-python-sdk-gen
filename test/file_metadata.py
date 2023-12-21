from box_sdk_gen.utils import to_string

import pytest

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

from box_sdk_gen.utils import generate_byte_stream

from box_sdk_gen.utils import get_uuid

from test.commons import get_default_client

from test.commons import upload_new_file

client: BoxClient = get_default_client()


def testFileMetadata():
    file: FileFull = upload_new_file()
    file_metadata: Metadatas = client.file_metadata.get_file_metadata(file_id=file.id)
    assert len(file_metadata.entries) == 0
    created_metadata: MetadataFull = client.file_metadata.create_file_metadata_by_id(
        file_id=file.id,
        scope=CreateFileMetadataByIdScope.GLOBAL.value,
        template_key='properties',
        request_body={'abc': 'xyz'},
    )
    assert to_string(created_metadata.template) == 'properties'
    assert to_string(created_metadata.scope) == 'global'
    assert created_metadata.version == 0
    received_metadata: MetadataFull = client.file_metadata.get_file_metadata_by_id(
        file_id=file.id,
        scope=GetFileMetadataByIdScope.GLOBAL.value,
        template_key='properties',
    )
    assert received_metadata.extra_data['abc'] == 'xyz'
    new_value: str = 'bar'
    updated_metadata: MetadataFull = client.file_metadata.update_file_metadata_by_id(
        file_id=file.id,
        scope=UpdateFileMetadataByIdScope.GLOBAL.value,
        template_key='properties',
        request_body=[
            UpdateFileMetadataByIdRequestBody(
                op=UpdateFileMetadataByIdRequestBodyOpField.REPLACE.value,
                path='/abc',
                value=new_value,
            )
        ],
    )
    received_updated_metadata: MetadataFull = (
        client.file_metadata.get_file_metadata_by_id(
            file_id=file.id,
            scope=GetFileMetadataByIdScope.GLOBAL.value,
            template_key='properties',
        )
    )
    assert received_updated_metadata.extra_data['abc'] == new_value
    client.file_metadata.delete_file_metadata_by_id(
        file_id=file.id,
        scope=DeleteFileMetadataByIdScope.GLOBAL.value,
        template_key='properties',
    )
    with pytest.raises(Exception):
        client.file_metadata.get_file_metadata_by_id(
            file_id=file.id,
            scope=GetFileMetadataByIdScope.GLOBAL.value,
            template_key='properties',
        )
    client.files.delete_file_by_id(file_id=file.id)
