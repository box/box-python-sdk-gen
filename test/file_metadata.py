from box_sdk_gen.internal.utils import to_string

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

from box_sdk_gen.internal.utils import generate_byte_stream

from box_sdk_gen.internal.utils import get_uuid

from test.commons import get_default_client

from test.commons import upload_new_file

client: BoxClient = get_default_client()


def testFileMetadata():
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
