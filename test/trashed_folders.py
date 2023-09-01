import pytest

from box_sdk_gen.schemas import FolderFull

from box_sdk_gen.managers.folders import CreateFolderParentArg

from box_sdk_gen.schemas import TrashFolder

from box_sdk_gen.schemas import TrashFolderRestored

from box_sdk_gen.utils import decode_base_64

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.client import Client

from box_sdk_gen.jwt_auth import JWTAuth

from box_sdk_gen.jwt_auth import JWTConfig

jwt_config: JWTConfig = JWTConfig.from_config_json_string(
    decode_base_64(get_env_var('JWT_CONFIG_BASE_64'))
)

auth: JWTAuth = JWTAuth(config=jwt_config)

client: Client = Client(auth=auth)


def testTrashedFolders():
    folder: FolderFull = client.folders.create_folder(
        name=get_uuid(), parent=CreateFolderParentArg(id='0')
    )
    client.folders.delete_folder_by_id(folder_id=folder.id)
    from_trash: TrashFolder = client.trashed_folders.get_folder_trash(
        folder_id=folder.id
    )
    assert from_trash.id == folder.id
    assert from_trash.name == folder.name
    with pytest.raises(Exception):
        client.folders.get_folder_by_id(folder_id=folder.id)
    restored_folder: TrashFolderRestored = (
        client.trashed_folders.restore_folder_from_trash(folder_id=folder.id)
    )
    from_api: FolderFull = client.folders.get_folder_by_id(folder_id=folder.id)
    assert restored_folder.id == from_api.id
    assert restored_folder.name == from_api.name
    client.folders.delete_folder_by_id(folder_id=folder.id)
    client.trashed_folders.delete_folder_trash(folder_id=folder.id)
    with pytest.raises(Exception):
        client.trashed_folders.get_folder_trash(folder_id=folder.id)
