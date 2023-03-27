import os

import uuid

import pytest

from box_sdk.schemas import FolderBaseTypeField

from box_sdk.managers.folders import PostFoldersRequestBodyArg

from box_sdk.managers.folders import PostFoldersIdRequestBodyArg

from box_sdk.managers.folders import PutFoldersIdRequestBodyArg

from box_sdk.managers.folders import PostFoldersIdCopyRequestBodyArgParentField

from box_sdk.managers.folders import PutFoldersIdRequestBodyArgParentField

from box_sdk.managers.folders import PostFoldersIdCopyRequestBodyArg

from box_sdk.managers.folders import PostFoldersRequestBodyArgParentField

from box_sdk.client import Client

from box_sdk.developer_token_auth import DeveloperTokenAuth

auth: DeveloperTokenAuth = DeveloperTokenAuth(token=os.getenv('DEVELOPER_TOKEN'))

client: Client = Client(auth=auth)

def test_get_folder_info():
    root_folder = client.folders.get_folders_id('0')
    assert root_folder.id == '0'
    assert root_folder.name == 'All Files'
    assert root_folder.type == FolderBaseTypeField.FOLDER.value

def test_create_delete_folder_and_restore_folder():
    new_folder_name: str = str(uuid.uuid1())
    new_folder = client.folders.post_folders(PostFoldersRequestBodyArg(name=new_folder_name, parent=PostFoldersRequestBodyArgParentField(id='0')))
    assert client.folders.get_folders_id(new_folder.id).name == new_folder_name
    client.folders.delete_folders_id(new_folder.id)
    with pytest.raises(Exception):
        client.folders.get_folders_id(new_folder.id)
    client.folders.post_folders_id(new_folder.id, PostFoldersIdRequestBodyArg())
    assert client.folders.get_folders_id(new_folder.id).name == new_folder_name
    client.folders.delete_folders_id(new_folder.id)

def test_update_folder():
    folder_to_update_name: str = str(uuid.uuid1())
    folder_to_update = client.folders.post_folders(PostFoldersRequestBodyArg(name=folder_to_update_name, parent=PostFoldersRequestBodyArgParentField(id='0')))
    updated_name: str = str(uuid.uuid1())
    updated_folder = client.folders.put_folders_id(folder_to_update.id, PutFoldersIdRequestBodyArg(name=updated_name, description='Updated description'))
    assert updated_folder.name == updated_name
    assert updated_folder.description == 'Updated description'
    client.folders.delete_folders_id(updated_folder.id)

def test_copy_move_folder_and_list_folder_items():
    folder_origin_name: str = str(uuid.uuid1())
    folder_origin = client.folders.post_folders(PostFoldersRequestBodyArg(name=folder_origin_name, parent=PostFoldersRequestBodyArgParentField(id='0')))
    copied_folder_name: str = str(uuid.uuid1())
    copied_folder = client.folders.post_folders_id_copy(folder_origin.id, PostFoldersIdCopyRequestBodyArg(parent=PostFoldersIdCopyRequestBodyArgParentField(id='0'), name=copied_folder_name))
    assert copied_folder.parent.id == '0'
    moved_folder_name: str = str(uuid.uuid1())
    moved_folder = client.folders.put_folders_id(copied_folder.id, PutFoldersIdRequestBodyArg(parent=PutFoldersIdRequestBodyArgParentField(id=folder_origin.id), name=moved_folder_name))
    assert moved_folder.parent.id == folder_origin.id
    folder_items = client.folders.get_folders_id_items(folder_origin.id)
    assert folder_items.entries[0].id == moved_folder.id
    assert folder_items.entries[0].name == moved_folder_name
    client.folders.delete_folders_id(moved_folder.id)
    client.folders.delete_folders_id(folder_origin.id)