from box_sdk_gen.utils import to_string

import pytest

from box_sdk_gen.schemas import FolderFull

from box_sdk_gen.schemas import WebLink

from box_sdk_gen.managers.web_links import CreateWebLinkParentArg

from box_sdk_gen.schemas import TrashWebLink

from box_sdk_gen.schemas import TrashWebLinkRestored

from box_sdk_gen.utils import decode_base_64

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.client import BoxClient

from box_sdk_gen.jwt_auth import BoxJWTAuth

from box_sdk_gen.jwt_auth import JWTConfig

jwt_config: JWTConfig = JWTConfig.from_config_json_string(
    decode_base_64(get_env_var('JWT_CONFIG_BASE_64'))
)

auth: BoxJWTAuth = BoxJWTAuth(config=jwt_config)

client: BoxClient = BoxClient(auth=auth)


def testTrashedWebLinks():
    url: str = 'https://www.box.com'
    parent: FolderFull = client.folders.get_folder_by_id(folder_id='0')
    name: str = get_uuid()
    description: str = 'Weblink description'
    weblink: WebLink = client.web_links.create_web_link(
        url=url,
        parent=CreateWebLinkParentArg(id=parent.id),
        name=name,
        description=description,
    )
    client.web_links.delete_web_link_by_id(web_link_id=weblink.id)
    from_trash: TrashWebLink = client.trashed_web_links.get_web_link_trash(
        web_link_id=weblink.id
    )
    assert from_trash.id == weblink.id
    assert from_trash.name == weblink.name
    from_api_after_trashed: WebLink = client.web_links.get_web_link_by_id(
        web_link_id=weblink.id
    )
    assert to_string(from_api_after_trashed.item_status) == 'trashed'
    restored_weblink: TrashWebLinkRestored = (
        client.trashed_web_links.restore_weblink_from_trash(web_link_id=weblink.id)
    )
    from_api: WebLink = client.web_links.get_web_link_by_id(web_link_id=weblink.id)
    assert restored_weblink.id == from_api.id
    assert restored_weblink.name == from_api.name
    client.web_links.delete_web_link_by_id(web_link_id=weblink.id)
    client.trashed_web_links.delete_web_link_trash(web_link_id=weblink.id)
    with pytest.raises(Exception):
        client.trashed_web_links.get_web_link_trash(web_link_id=weblink.id)
