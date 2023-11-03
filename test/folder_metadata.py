from typing import Dict

import pytest

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import FolderFull

from box_sdk_gen.managers.folders import CreateFolderParentArg

from box_sdk_gen.schemas import Metadatas

from box_sdk_gen.schemas import Metadata

from box_sdk_gen.schemas import MetadataFull

from box_sdk_gen.managers.folder_metadata import UpdateFolderMetadataByIdRequestBodyArg

from box_sdk_gen.managers.folder_metadata import (
    UpdateFolderMetadataByIdRequestBodyArgOpField,
)

from box_sdk_gen.utils import get_uuid

from test.commons import get_default_client

client: BoxClient = get_default_client()


def testFolderMetadata():
    folder: FolderFull = client.folders.create_folder(
        name=get_uuid(), parent=CreateFolderParentArg(id='0')
    )
    folder_metadata: Metadatas = client.folder_metadata.get_folder_metadata(
        folder_id=folder.id
    )
    assert len(folder_metadata.entries) == 0
    scope: str = 'global'
    template: str = 'properties'
    data: Dict[str, str] = {'abc': 'xyz'}
    created_metadata: Metadata = client.folder_metadata.create_folder_metadata_by_id(
        folder_id=folder.id, scope=scope, template_key=template, request_body=data
    )
    assert created_metadata.template == template
    assert created_metadata.scope == scope
    assert created_metadata.version == 0
    received_metadata: MetadataFull = client.folder_metadata.get_folder_metadata_by_id(
        folder_id=folder.id, scope=scope, template_key=template
    )
    assert received_metadata.extra_data['abc'] == data['abc']
    new_value: str = 'bar'
    updated_metadata: Metadata = client.folder_metadata.update_folder_metadata_by_id(
        folder_id=folder.id,
        scope=scope,
        template_key=template,
        request_body=[
            UpdateFolderMetadataByIdRequestBodyArg(
                op=UpdateFolderMetadataByIdRequestBodyArgOpField.REPLACE.value,
                path='/abc',
                value=new_value,
            )
        ],
    )
    received_updated_metadata: MetadataFull = (
        client.folder_metadata.get_folder_metadata_by_id(
            folder_id=folder.id, scope=scope, template_key=template
        )
    )
    assert received_updated_metadata.extra_data['abc'] == new_value
    client.folder_metadata.delete_folder_metadata_by_id(
        folder_id=folder.id, scope=scope, template_key=template
    )
    with pytest.raises(Exception):
        client.folder_metadata.get_folder_metadata_by_id(
            folder_id=folder.id, scope=scope, template_key=template
        )
    client.folders.delete_folder_by_id(folder_id=folder.id)
