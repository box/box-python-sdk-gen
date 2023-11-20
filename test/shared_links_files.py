from box_sdk_gen.utils import to_string

import pytest

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import Files

from box_sdk_gen.managers.uploads import UploadFileAttributesArg

from box_sdk_gen.managers.uploads import UploadFileAttributesArgParentField

from box_sdk_gen.managers.shared_links_files import UpdateFileAddSharedLinkSharedLinkArg

from box_sdk_gen.managers.shared_links_files import (
    UpdateFileAddSharedLinkSharedLinkArgAccessField,
)

from box_sdk_gen.schemas import FileFull

from box_sdk_gen.managers.shared_links_files import (
    UpdateFileUpdateSharedLinkSharedLinkArg,
)

from box_sdk_gen.managers.shared_links_files import (
    UpdateFileUpdateSharedLinkSharedLinkArgAccessField,
)

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.utils import generate_byte_stream

from box_sdk_gen.utils import get_env_var

from test.commons import get_default_client

from test.commons import get_default_client_as_user

client: BoxClient = get_default_client()


def testSharedLinksFiles():
    uploaded_files: Files = client.uploads.upload_file(
        attributes=UploadFileAttributesArg(
            name=get_uuid(), parent=UploadFileAttributesArgParentField(id='0')
        ),
        file=generate_byte_stream(10),
    )
    file_id: str = uploaded_files.entries[0].id
    client.shared_links_files.update_file_add_shared_link(
        file_id=file_id,
        shared_link=UpdateFileAddSharedLinkSharedLinkArg(
            access=UpdateFileAddSharedLinkSharedLinkArgAccessField.OPEN.value,
            password='Secret123@',
        ),
        fields='shared_link',
    )
    file_from_api: FileFull = client.shared_links_files.get_file_get_shared_link(
        file_id=file_id, fields='shared_link'
    )
    assert to_string(file_from_api.shared_link.access) == 'open'
    user_id: str = get_env_var('USER_ID')
    user_client: BoxClient = get_default_client_as_user(user_id)
    file_from_shared_link_password: FileFull = (
        user_client.shared_links_files.get_shared_items(
            boxapi=''.join([
                'shared_link=',
                file_from_api.shared_link.url,
                '&shared_link_password=Secret123@',
            ])
        )
    )
    assert file_id == file_from_shared_link_password.id
    with pytest.raises(Exception):
        user_client.shared_links_files.get_shared_items(
            boxapi=''.join([
                'shared_link=',
                file_from_api.shared_link.url,
                '&shared_link_password=incorrectPassword',
            ])
        )
    updated_file: FileFull = client.shared_links_files.update_file_update_shared_link(
        file_id=file_id,
        shared_link=UpdateFileUpdateSharedLinkSharedLinkArg(
            access=UpdateFileUpdateSharedLinkSharedLinkArgAccessField.COLLABORATORS.value
        ),
        fields='shared_link',
    )
    assert to_string(updated_file.shared_link.access) == 'collaborators'
    client.files.delete_file_by_id(file_id=file_id)
