from box_sdk_gen.schemas import FolderFull

from box_sdk_gen.schemas import WebLink

from box_sdk_gen.managers.web_links import UpdateWebLinkByIdSharedLinkArg

from box_sdk_gen.utils import decode_base_64

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.client import Client

from box_sdk_gen.jwt_auth import JWTAuth

from box_sdk_gen.jwt_auth import JWTConfig

jwt_config: JWTConfig = JWTConfig.from_config_json_string(
    decode_base_64(get_env_var('JWT_CONFIG_BASE_64'))
)

auth: JWTAuth = JWTAuth(config=jwt_config)

client: Client = Client(auth=auth)


def test_create_get_delete_weblink():
    url: str = 'https://www.box.com'
    parent: FolderFull = client.folders.get_folder_by_id(folder_id='0')
    name: str = get_uuid()
    description: str = 'Weblink description'
    shared_access: str = 'open'
    password: str = 'super-secret-password'
    weblink: WebLink = client.web_links.create_web_link(
        url=url, parent=parent, name=name, description=description
    )
    assert weblink.url == url
    assert weblink.parent.id == parent.id
    assert weblink.name == name
    assert weblink.description == description
    weblink_by_id: WebLink = client.web_links.get_web_link_by_id(web_link_id=weblink.id)
    assert weblink_by_id.id == weblink.id
    assert weblink_by_id.url == url
    updated_name: str = get_uuid()
    updated_weblink: WebLink = client.web_links.update_web_link_by_id(
        web_link_id=weblink.id,
        name=updated_name,
        shared_link=UpdateWebLinkByIdSharedLinkArg(
            access=shared_access, password=password
        ),
    )
    assert updated_weblink.name == updated_name
    assert updated_weblink.shared_link.access == shared_access
    client.web_links.delete_web_link_by_id(web_link_id=weblink.id)
    deleted_weblink: WebLink = client.web_links.get_web_link_by_id(
        web_link_id=weblink.id
    )
    assert deleted_weblink.item_status == 'trashed'
