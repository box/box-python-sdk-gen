from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import UserFull

from box_sdk_gen.schemas import FolderFull

from box_sdk_gen.managers.transfer import TransferOwnedFolderOwnedByArg

from box_sdk_gen.utils import get_uuid

from test.commons import get_default_client

client: BoxClient = get_default_client()


def testTransferUserContent():
    new_user_name: str = get_uuid()
    new_user: UserFull = client.users.create_user(
        name=new_user_name, is_platform_access_only=True
    )
    current_user: UserFull = client.users.get_user_me()
    transfered_folder: FolderFull = client.transfer.transfer_owned_folder(
        user_id=new_user.id,
        owned_by=TransferOwnedFolderOwnedByArg(id=current_user.id),
        notify=False,
    )
    assert transfered_folder.owned_by.id == current_user.id
    client.folders.delete_folder_by_id(folder_id=transfered_folder.id, recursive=True)
    client.users.delete_user_by_id(user_id=new_user.id, notify=False, force=True)
