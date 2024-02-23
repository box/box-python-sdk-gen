from box_sdk_gen.internal.utils import to_string

import pytest

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import Files

from box_sdk_gen.managers.uploads import UploadFileAttributes

from box_sdk_gen.managers.uploads import UploadFileAttributesParentField

from box_sdk_gen.managers.shared_links_files import AddShareLinkToFileSharedLink

from box_sdk_gen.managers.shared_links_files import (
    AddShareLinkToFileSharedLinkAccessField,
)

from box_sdk_gen.schemas import FileFull

from box_sdk_gen.managers.shared_links_files import UpdateSharedLinkOnFileSharedLink

from box_sdk_gen.managers.shared_links_files import (
    UpdateSharedLinkOnFileSharedLinkAccessField,
)

from box_sdk_gen.internal.utils import get_uuid

from box_sdk_gen.internal.utils import generate_byte_stream

from box_sdk_gen.internal.utils import get_env_var

from test.commons import get_default_client

from test.commons import get_default_client_as_user

client: BoxClient = get_default_client()


def testSharedLinksFiles():
    uploaded_files: Files = client.uploads.upload_file(
        attributes=UploadFileAttributes(
            name=get_uuid(), parent=UploadFileAttributesParentField(id='0')
        ),
        file=generate_byte_stream(10),
    )
    file_id: str = uploaded_files.entries[0].id
    client.shared_links_files.add_share_link_to_file(
        file_id=file_id,
        shared_link=AddShareLinkToFileSharedLink(
            access=AddShareLinkToFileSharedLinkAccessField.OPEN.value,
            password='Secret123@',
        ),
        fields='shared_link',
    )
    file_from_api: FileFull = client.shared_links_files.get_shared_link_for_file(
        file_id=file_id, fields='shared_link'
    )
    assert to_string(file_from_api.shared_link.access) == 'open'
    user_id: str = get_env_var('USER_ID')
    user_client: BoxClient = get_default_client_as_user(user_id)
    file_from_shared_link_password: FileFull = (
        user_client.shared_links_files.find_file_for_shared_link(
            boxapi=''.join(
                [
                    'shared_link=',
                    file_from_api.shared_link.url,
                    '&shared_link_password=Secret123@',
                ]
            )
        )
    )
    assert file_id == file_from_shared_link_password.id
    with pytest.raises(Exception):
        user_client.shared_links_files.find_file_for_shared_link(
            boxapi=''.join(
                [
                    'shared_link=',
                    file_from_api.shared_link.url,
                    '&shared_link_password=incorrectPassword',
                ]
            )
        )
    updated_file: FileFull = client.shared_links_files.update_shared_link_on_file(
        file_id=file_id,
        shared_link=UpdateSharedLinkOnFileSharedLink(
            access=UpdateSharedLinkOnFileSharedLinkAccessField.COLLABORATORS.value
        ),
        fields='shared_link',
    )
    assert to_string(updated_file.shared_link.access) == 'collaborators'
    client.files.delete_file_by_id(file_id=file_id)
