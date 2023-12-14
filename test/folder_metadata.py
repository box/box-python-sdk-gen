from box_sdk_gen.utils import to_string

import pytest

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import FolderFull

from box_sdk_gen.schemas import Metadatas

from box_sdk_gen.schemas import MetadataFull

from box_sdk_gen.managers.folder_metadata import CreateFolderMetadataByIdScope

from box_sdk_gen.managers.folder_metadata import GetFolderMetadataByIdScope

from box_sdk_gen.managers.folder_metadata import UpdateFolderMetadataByIdScope

from box_sdk_gen.managers.folder_metadata import UpdateFolderMetadataByIdRequestBody

from box_sdk_gen.managers.folder_metadata import (
    UpdateFolderMetadataByIdRequestBodyOpField,
)

from box_sdk_gen.managers.folder_metadata import DeleteFolderMetadataByIdScope

from box_sdk_gen.utils import get_uuid

from test.commons import get_default_client

from test.commons import create_new_folder

client: BoxClient = get_default_client()


def testFolderMetadata():
    folder: FolderFull = create_new_folder()
    folder_metadata: Metadatas = client.folder_metadata.get_folder_metadata(
        folder_id=folder.id
    )
    assert len(folder_metadata.entries) == 0
    created_metadata: MetadataFull = (
        client.folder_metadata.create_folder_metadata_by_id(
            folder_id=folder.id,
            scope=CreateFolderMetadataByIdScope.GLOBAL.value,
            template_key='properties',
            request_body={'abc': 'xyz'},
        )
    )
    assert to_string(created_metadata.template) == 'properties'
    assert to_string(created_metadata.scope) == 'global'
    assert created_metadata.version == 0
    received_metadata: MetadataFull = client.folder_metadata.get_folder_metadata_by_id(
        folder_id=folder.id,
        scope=GetFolderMetadataByIdScope.GLOBAL.value,
        template_key='properties',
    )
    assert received_metadata.extra_data['abc'] == 'xyz'
    new_value: str = 'bar'
    updated_metadata: MetadataFull = (
        client.folder_metadata.update_folder_metadata_by_id(
            folder_id=folder.id,
            scope=UpdateFolderMetadataByIdScope.GLOBAL.value,
            template_key='properties',
            request_body=[
                UpdateFolderMetadataByIdRequestBody(
                    op=UpdateFolderMetadataByIdRequestBodyOpField.REPLACE.value,
                    path='/abc',
                    value=new_value,
                )
            ],
        )
    )
    received_updated_metadata: MetadataFull = (
        client.folder_metadata.get_folder_metadata_by_id(
            folder_id=folder.id,
            scope=GetFolderMetadataByIdScope.GLOBAL.value,
            template_key='properties',
        )
    )
    assert received_updated_metadata.extra_data['abc'] == new_value
    client.folder_metadata.delete_folder_metadata_by_id(
        folder_id=folder.id,
        scope=DeleteFolderMetadataByIdScope.GLOBAL.value,
        template_key='properties',
    )
    with pytest.raises(Exception):
        client.folder_metadata.get_folder_metadata_by_id(
            folder_id=folder.id,
            scope=GetFolderMetadataByIdScope.GLOBAL.value,
            template_key='properties',
        )
    client.folders.delete_folder_by_id(folder_id=folder.id)
