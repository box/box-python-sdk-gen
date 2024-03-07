from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import FolderFull

from box_sdk_gen.schemas import WebLink

from box_sdk_gen.managers.web_links import CreateWebLinkParent

from box_sdk_gen.managers.web_links import UpdateWebLinkByIdSharedLink

from box_sdk_gen.internal.utils import get_uuid

from test.commons import get_default_client

client: BoxClient = get_default_client()


def test_create_get_delete_weblink():
    url: str = 'https://www.box.com'
    parent: FolderFull = client.folders.get_folder_by_id('0')
    name: str = get_uuid()
    description: str = 'Weblink description'
    shared_access: str = 'open'
    password: str = 'super-secret-password'
    weblink: WebLink = client.web_links.create_web_link(
        url, CreateWebLinkParent(id=parent.id), name=name, description=description
    )
    assert weblink.url == url
    assert weblink.parent.id == parent.id
    assert weblink.name == name
    assert weblink.description == description
    weblink_by_id: WebLink = client.web_links.get_web_link_by_id(weblink.id)
    assert weblink_by_id.id == weblink.id
    assert weblink_by_id.url == url
    updated_name: str = get_uuid()
    updated_weblink: WebLink = client.web_links.update_web_link_by_id(
        weblink.id,
        name=updated_name,
        shared_link=UpdateWebLinkByIdSharedLink(
            access=shared_access, password=password
        ),
    )
    assert updated_weblink.name == updated_name
    assert updated_weblink.shared_link.access == shared_access
    client.web_links.delete_web_link_by_id(weblink.id)
    deleted_weblink: WebLink = client.web_links.get_web_link_by_id(weblink.id)
    assert deleted_weblink.item_status == 'trashed'
