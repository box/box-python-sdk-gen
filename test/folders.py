import pytest

from box_sdk_gen.managers.folders import CreateFolderParentArg

from box_sdk_gen.managers.folders import CopyFolderParentArg

from box_sdk_gen.managers.folders import UpdateFolderByIdParentArg

from box_sdk_gen.utils import decode_base_64

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.client import Client

from box_sdk_gen.jwt_auth import JWTAuth

from box_sdk_gen.jwt_auth import JWTConfig

jwt_config = JWTConfig.from_config_json_string(decode_base_64(get_env_var('JWT_CONFIG_BASE_64')))

auth: JWTAuth = JWTAuth(config=jwt_config)

client: Client = Client(auth=auth)

def test_get_folder_info():
    root_folder: FolderFull = client.folders.get_folder_by_id(folder_id='0')
    assert root_folder.id == '0'
    assert root_folder.name == 'All Files'

def test_get_folder_full_info_with_extra_fields():
    root_folder: FolderFull = client.folders.get_folder_by_id(folder_id='0', fields='has_collaborations,tags')
    assert root_folder.id == '0'
    assert root_folder.has_collaborations == False
    tags_length: int = len(root_folder.tags)
    assert tags_length == 0

def test_create_and_delete_folder():
    new_folder_name: str = get_uuid()
    new_folder: FolderFull = client.folders.create_folder(name=new_folder_name, parent=CreateFolderParentArg(id='0'))
    created_folder: FolderFull = client.folders.get_folder_by_id(folder_id=new_folder.id)
    assert created_folder.name == new_folder_name
    client.folders.delete_folder_by_id(folder_id=new_folder.id)
    with pytest.raises(Exception):
        client.folders.get_folder_by_id(folder_id=new_folder.id)

def test_update_folder():
    folder_to_update_name: str = get_uuid()
    folder_to_update: FolderFull = client.folders.create_folder(name=folder_to_update_name, parent=CreateFolderParentArg(id='0'))
    updated_name: str = get_uuid()
    updated_folder: FolderFull = client.folders.update_folder_by_id(folder_id=folder_to_update.id, name=updated_name, description='Updated description')
    assert updated_folder.name == updated_name
    assert updated_folder.description == 'Updated description'
    client.folders.delete_folder_by_id(folder_id=updated_folder.id)

def test_copy_move_folder_and_list_folder_items():
    folder_origin_name: str = get_uuid()
    folder_origin: FolderFull = client.folders.create_folder(name=folder_origin_name, parent=CreateFolderParentArg(id='0'))
    copied_folder_name: str = get_uuid()
    copied_folder: FolderFull = client.folders.copy_folder(folder_id=folder_origin.id, name=copied_folder_name, parent=CopyFolderParentArg(id='0'))
    assert copied_folder.parent.id == '0'
    moved_folder_name: str = get_uuid()
    moved_folder: FolderFull = client.folders.update_folder_by_id(folder_id=copied_folder.id, name=moved_folder_name, parent=UpdateFolderByIdParentArg(id=folder_origin.id))
    assert moved_folder.parent.id == folder_origin.id
    folder_items: Items = client.folders.get_folder_items(folder_id=folder_origin.id)
    assert folder_items.entries[0].id == moved_folder.id
    assert folder_items.entries[0].name == moved_folder_name
    client.folders.delete_folder_by_id(folder_id=moved_folder.id)
    client.folders.delete_folder_by_id(folder_id=folder_origin.id)