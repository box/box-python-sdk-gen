import pytest

from box_sdk.utils import decode_base_64

from box_sdk.utils import get_env_var

from box_sdk.utils import get_uuid

from box_sdk.schemas import FolderBaseTypeField

from box_sdk.managers.folders import CreateFolderRequestBodyArg

from box_sdk.managers.folders import CopyFolderRequestBodyArgParentField

from box_sdk.managers.folders import RestoreFolderFromTrashRequestBodyArg

from box_sdk.managers.folders import UpdateFolderByIdRequestBodyArgParentField

from box_sdk.managers.folders import CopyFolderRequestBodyArg

from box_sdk.managers.folders import CreateFolderRequestBodyArgParentField

from box_sdk.managers.folders import UpdateFolderByIdRequestBodyArg

from box_sdk.client import Client

from box_sdk.jwt_auth import JWTAuth

from box_sdk.jwt_auth import JWTConfig

jwt_config = JWTConfig.from_config_json_string(decode_base_64(get_env_var('JWT_CONFIG_BASE_64')))

auth: JWTAuth = JWTAuth(config=jwt_config)

client: Client = Client(auth=auth)

def test_get_folder_info():
    root_folder = client.folders.get_folder_by_id('0')
    assert root_folder.id == '0'
    assert root_folder.name == 'All Files'
    assert root_folder.type == FolderBaseTypeField.FOLDER.value

def test_create_delete_folder_and_restore_folder():
    new_folder_name = get_uuid()
    new_folder = client.folders.create_folder(CreateFolderRequestBodyArg(name=new_folder_name, parent=CreateFolderRequestBodyArgParentField(id='0')))
    assert client.folders.get_folder_by_id(new_folder.id).name == new_folder_name
    client.folders.delete_folder_by_id(new_folder.id)
    with pytest.raises(Exception):
        client.folders.get_folder_by_id(new_folder.id)
    client.folders.restore_folder_from_trash(new_folder.id, RestoreFolderFromTrashRequestBodyArg())
    assert client.folders.get_folder_by_id(new_folder.id).name == new_folder_name
    client.folders.delete_folder_by_id(new_folder.id)

def test_update_folder():
    folder_to_update_name = get_uuid()
    folder_to_update = client.folders.create_folder(CreateFolderRequestBodyArg(name=folder_to_update_name, parent=CreateFolderRequestBodyArgParentField(id='0')))
    updated_name = get_uuid()
    updated_folder = client.folders.update_folder_by_id(folder_to_update.id, UpdateFolderByIdRequestBodyArg(name=updated_name, description='Updated description'))
    assert updated_folder.name == updated_name
    assert updated_folder.description == 'Updated description'
    client.folders.delete_folder_by_id(updated_folder.id)

def test_copy_move_folder_and_list_folder_items():
    folder_origin_name = get_uuid()
    folder_origin = client.folders.create_folder(CreateFolderRequestBodyArg(name=folder_origin_name, parent=CreateFolderRequestBodyArgParentField(id='0')))
    copied_folder_name = get_uuid()
    copied_folder = client.folders.copy_folder(folder_origin.id, CopyFolderRequestBodyArg(parent=CopyFolderRequestBodyArgParentField(id='0'), name=copied_folder_name))
    assert copied_folder.parent.id == '0'
    moved_folder_name = get_uuid()
    moved_folder = client.folders.update_folder_by_id(copied_folder.id, UpdateFolderByIdRequestBodyArg(parent=UpdateFolderByIdRequestBodyArgParentField(id=folder_origin.id), name=moved_folder_name))
    assert moved_folder.parent.id == folder_origin.id
    folder_items = client.folders.get_folder_items(folder_origin.id)
    assert folder_items.entries[0].id == moved_folder.id
    assert folder_items.entries[0].name == moved_folder_name
    client.folders.delete_folder_by_id(moved_folder.id)
    client.folders.delete_folder_by_id(folder_origin.id)