import pytest

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import FolderFull

from box_sdk_gen.managers.folders import CreateFolderParentArg

from box_sdk_gen.schemas import FolderLocks

from box_sdk_gen.schemas import FolderLock

from box_sdk_gen.managers.folder_locks import CreateFolderLockLockedOperationsArg

from box_sdk_gen.managers.folder_locks import CreateFolderLockFolderArg

from box_sdk_gen.utils import get_uuid

from test.commons import get_default_client

client: BoxClient = get_default_client()


def testFolderLocks():
    folder: FolderFull = client.folders.create_folder(
        name=get_uuid(), parent=CreateFolderParentArg(id='0')
    )
    folder_locks: FolderLocks = client.folder_locks.get_folder_locks(
        folder_id=folder.id
    )
    assert len(folder_locks.entries) == 0
    folder_lock: FolderLock = client.folder_locks.create_folder_lock(
        locked_operations=CreateFolderLockLockedOperationsArg(move=True, delete=True),
        folder=CreateFolderLockFolderArg(id=folder.id, type='folder'),
    )
    assert folder_lock.folder.id == folder.id
    assert folder_lock.locked_operations.move == True
    assert folder_lock.locked_operations.delete == True
    client.folder_locks.delete_folder_lock_by_id(folder_lock_id=folder_lock.id)
    with pytest.raises(Exception):
        client.folder_locks.delete_folder_lock_by_id(folder_lock_id=folder_lock.id)
    new_folder_locks: FolderLocks = client.folder_locks.get_folder_locks(
        folder_id=folder.id
    )
    assert len(new_folder_locks.entries) == 0
    client.folders.delete_folder_by_id(folder_id=folder.id)
