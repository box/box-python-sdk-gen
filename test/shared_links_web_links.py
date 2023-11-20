from box_sdk_gen.utils import to_string

import pytest

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import FolderFull

from box_sdk_gen.schemas import WebLink

from box_sdk_gen.managers.web_links import CreateWebLinkParentArg

from box_sdk_gen.managers.shared_links_web_links import (
    UpdateWebLinkAddSharedLinkSharedLinkArg,
)

from box_sdk_gen.managers.shared_links_web_links import (
    UpdateWebLinkAddSharedLinkSharedLinkArgAccessField,
)

from box_sdk_gen.managers.shared_links_web_links import (
    UpdateWebLinkUpdateSharedLinkSharedLinkArg,
)

from box_sdk_gen.managers.shared_links_web_links import (
    UpdateWebLinkUpdateSharedLinkSharedLinkArgAccessField,
)

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.utils import generate_byte_stream

from box_sdk_gen.utils import get_env_var

from test.commons import get_default_client

from test.commons import get_default_client_as_user

client: BoxClient = get_default_client()


def testSharedLinksWebLinks():
    parent: FolderFull = client.folders.get_folder_by_id(folder_id='0')
    web_link: WebLink = client.web_links.create_web_link(
        url='https://www.box.com',
        parent=CreateWebLinkParentArg(id=parent.id),
        name=get_uuid(),
        description='Weblink description',
    )
    web_link_id: str = web_link.id
    client.shared_links_web_links.update_web_link_add_shared_link(
        web_link_id=web_link_id,
        shared_link=UpdateWebLinkAddSharedLinkSharedLinkArg(
            access=UpdateWebLinkAddSharedLinkSharedLinkArgAccessField.OPEN.value,
            password='Secret123@',
        ),
        fields='shared_link',
    )
    web_link_from_api: WebLink = (
        client.shared_links_web_links.get_web_link_get_shared_link(
            web_link_id=web_link_id, fields='shared_link'
        )
    )
    assert to_string(web_link_from_api.shared_link.access) == 'open'
    user_id: str = get_env_var('USER_ID')
    user_client: BoxClient = get_default_client_as_user(user_id)
    web_link_from_shared_link_password: WebLink = (
        user_client.shared_links_web_links.get_shared_item_web_links(
            boxapi=''.join([
                'shared_link=',
                web_link_from_api.shared_link.url,
                '&shared_link_password=Secret123@',
            ])
        )
    )
    assert web_link_id == web_link_from_shared_link_password.id
    with pytest.raises(Exception):
        user_client.shared_links_web_links.get_shared_item_web_links(
            boxapi=''.join([
                'shared_link=',
                web_link_from_api.shared_link.url,
                '&shared_link_password=incorrectPassword',
            ])
        )
    updated_web_link: WebLink = (
        client.shared_links_web_links.update_web_link_update_shared_link(
            web_link_id=web_link_id,
            shared_link=UpdateWebLinkUpdateSharedLinkSharedLinkArg(
                access=UpdateWebLinkUpdateSharedLinkSharedLinkArgAccessField.COLLABORATORS.value
            ),
            fields='shared_link',
        )
    )
    assert to_string(updated_web_link.shared_link.access) == 'collaborators'
    client.web_links.delete_web_link_by_id(web_link_id=web_link_id)
