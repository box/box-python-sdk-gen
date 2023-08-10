import pytest

from box_sdk_gen.managers.folders import CreateFolderParentArg

from box_sdk_gen.managers.folder_locks import CreateFolderLockLockedOperationsArg

from box_sdk_gen.managers.folder_locks import CreateFolderLockFolderArg

from box_sdk_gen.utils import decode_base_64

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.client import Client

from box_sdk_gen.jwt_auth import JWTAuth

from box_sdk_gen.jwt_auth import JWTConfig

jwt_config = JWTConfig.from_config_json_string(decode_base_64(get_env_var('JWT_CONFIG_BASE_64')))

auth: JWTAuth = JWTAuth(config=jwt_config)

client: Client = Client(auth=auth)

def testFolderLocks():
    folder: FolderFull = client.folders.create_folder(name=get_uuid(), parent=CreateFolderParentArg(id='0'))
    folder_locks: FolderLocks = client.folder_locks.get_folder_locks(folder_id=folder.id)
    assert len(folder_locks.entries) == 0
    folder_lock: FolderLock = client.folder_locks.create_folder_lock(locked_operations=CreateFolderLockLockedOperationsArg(move=True, delete=True), folder=CreateFolderLockFolderArg(id=folder.id, type='folder'))
    assert folder_lock.folder.id == folder.id
    assert folder_lock.locked_operations.move == True
    assert folder_lock.locked_operations.delete == True
    with pytest.raises(Exception):
        client.folders.delete_folder_by_id(folder_id=folder.id)
    client.folder_locks.delete_folder_lock_by_id(folder_lock_id=folder_lock.id)
    with pytest.raises(Exception):
        client.folder_locks.delete_folder_lock_by_id(folder_lock_id=folder_lock.id)
    new_folder_locks: FolderLocks = client.folder_locks.get_folder_locks(folder_id=folder.id)
    assert len(new_folder_locks.entries) == 0
    client.folders.delete_folder_by_id(folder_id=folder.id)