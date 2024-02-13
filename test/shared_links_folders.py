from box_sdk_gen.utils import to_string

import pytest

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import FolderFull

from box_sdk_gen.managers.folders import CreateFolderParent

from box_sdk_gen.managers.shared_links_folders import AddShareLinkToFolderSharedLink

from box_sdk_gen.managers.shared_links_folders import (
    AddShareLinkToFolderSharedLinkAccessField,
)

from box_sdk_gen.managers.shared_links_folders import UpdateSharedLinkOnFolderSharedLink

from box_sdk_gen.managers.shared_links_folders import (
    UpdateSharedLinkOnFolderSharedLinkAccessField,
)

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.utils import generate_byte_stream

from box_sdk_gen.utils import get_env_var

from test.commons import get_default_client

from test.commons import get_default_client_as_user

client: BoxClient = get_default_client()


def testSharedLinksFolders():
    folder: FolderFull = client.folders.create_folder(
        name=get_uuid(), parent=CreateFolderParent(id='0')
    )
    client.shared_links_folders.add_share_link_to_folder(
        folder_id=folder.id,
        shared_link=AddShareLinkToFolderSharedLink(
            access=AddShareLinkToFolderSharedLinkAccessField.OPEN.value,
            password='Secret123@',
        ),
        fields='shared_link',
    )
    folder_from_api: FolderFull = (
        client.shared_links_folders.get_shared_link_for_folder(
            folder_id=folder.id, fields='shared_link'
        )
    )
    assert to_string(folder_from_api.shared_link.access) == 'open'
    user_id: str = get_env_var('USER_ID')
    user_client: BoxClient = get_default_client_as_user(user_id)
    folder_from_shared_link_password: FolderFull = (
        user_client.shared_links_folders.find_folder_for_shared_link(
            boxapi=''.join(
                [
                    'shared_link=',
                    folder_from_api.shared_link.url,
                    '&shared_link_password=Secret123@',
                ]
            )
        )
    )
    assert folder.id == folder_from_shared_link_password.id
    with pytest.raises(Exception):
        user_client.shared_links_folders.find_folder_for_shared_link(
            boxapi=''.join(
                [
                    'shared_link=',
                    folder_from_api.shared_link.url,
                    '&shared_link_password=incorrectPassword',
                ]
            )
        )
    updated_folder: FolderFull = (
        client.shared_links_folders.update_shared_link_on_folder(
            folder_id=folder.id,
            shared_link=UpdateSharedLinkOnFolderSharedLink(
                access=UpdateSharedLinkOnFolderSharedLinkAccessField.COLLABORATORS.value
            ),
            fields='shared_link',
        )
    )
    assert to_string(updated_folder.shared_link.access) == 'collaborators'
    client.folders.delete_folder_by_id(folder_id=folder.id)
