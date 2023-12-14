import pytest

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import FolderFull

from box_sdk_gen.managers.folders import CreateFolderParent

from box_sdk_gen.schemas import TrashFolder

from box_sdk_gen.schemas import TrashFolderRestored

from box_sdk_gen.utils import get_uuid

from test.commons import get_default_client

client: BoxClient = get_default_client()


def testTrashedFolders():
    folder: FolderFull = client.folders.create_folder(
        name=get_uuid(), parent=CreateFolderParent(id='0')
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
