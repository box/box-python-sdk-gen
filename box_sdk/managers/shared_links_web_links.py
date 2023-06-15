from typing import Optional

from box_sdk.base_object import BaseObject

from enum import Enum

import json

from typing import Dict

from box_sdk.schemas import WebLink

from box_sdk.schemas import ClientError

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetSharedItemWebLinksOptionsArg(BaseObject):
    def __init__(self, if_none_match: Optional[str] = None, fields: Optional[str] = None, **kwargs):
        """
        :param if_none_match: Ensures an item is only returned if it has changed.
            Pass in the item's last observed `etag` value
            into this header and the endpoint will fail
            with a `304 Not Modified` if the item has not
            changed since.
        :type if_none_match: Optional[str], optional
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.if_none_match = if_none_match
        self.fields = fields

class UpdateWebLinkAddSharedLinkRequestBodyArgSharedLinkFieldAccessField(str, Enum):
    OPEN = 'open'
    COMPANY = 'company'
    COLLABORATORS = 'collaborators'

class UpdateWebLinkAddSharedLinkRequestBodyArgSharedLinkFieldPermissionsField(BaseObject):
    def __init__(self, can_download: Optional[bool] = None, can_preview: Optional[bool] = None, can_edit: Optional[bool] = None, **kwargs):
        """
        :param can_download: If the shared link allows for downloading of files.
            This can only be set when `access` is set to
            `open` or `company`.
        :type can_download: Optional[bool], optional
        :param can_preview: If the shared link allows for previewing of files.
            This value is always `true`. For shared links on folders
            this also applies to any items in the folder.
        :type can_preview: Optional[bool], optional
        :param can_edit: This value can only be `true` is `type` is `file`.
        :type can_edit: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.can_download = can_download
        self.can_preview = can_preview
        self.can_edit = can_edit

class UpdateWebLinkAddSharedLinkRequestBodyArgSharedLinkField(BaseObject):
    def __init__(self, access: Optional[UpdateWebLinkAddSharedLinkRequestBodyArgSharedLinkFieldAccessField] = None, password: Optional[str] = None, vanity_name: Optional[str] = None, unshared_at: Optional[str] = None, permissions: Optional[UpdateWebLinkAddSharedLinkRequestBodyArgSharedLinkFieldPermissionsField] = None, **kwargs):
        """
        :param access: The level of access for the shared link. This can be
            restricted to anyone with the link (`open`), only people
            within the company (`company`) and only those who
            have been invited to the file (`collaborators`).
            If not set, this field defaults to the access level specified
            by the enterprise admin. To create a shared link with this
            default setting pass the `shared_link` object with
            no `access` field, for example `{ "shared_link": {} }`.
            The `company` access level is only available to paid
            accounts.
        :type access: Optional[UpdateWebLinkAddSharedLinkRequestBodyArgSharedLinkFieldAccessField], optional
        :param password: The password required to access the shared link. Set the
            password to `null` to remove it.
            Passwords must now be at least eight characters
            long and include a number, upper case letter, or
            a non-numeric or non-alphabetical character.
            A password can only be set when `access` is set to `open`.
        :type password: Optional[str], optional
        :param vanity_name: Defines a custom vanity name to use in the shared link URL,
            for example `https://app.box.com/v/my-shared-link`.
            Custom URLs should not be used when sharing sensitive content
            as vanity URLs are a lot easier to guess than regular shared
            links.
        :type vanity_name: Optional[str], optional
        :param unshared_at: The timestamp at which this shared link will
            expire. This field can only be set by
            users with paid accounts. The value must be greater than the
            current date and time.
        :type unshared_at: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.access = access
        self.password = password
        self.vanity_name = vanity_name
        self.unshared_at = unshared_at
        self.permissions = permissions

class UpdateWebLinkAddSharedLinkRequestBodyArg(BaseObject):
    def __init__(self, shared_link: Optional[UpdateWebLinkAddSharedLinkRequestBodyArgSharedLinkField] = None, **kwargs):
        """
        :param shared_link: The settings for the shared link to create on the web link.
            Use an empty object (`{}`) to use the default settings for shared
            links.
        :type shared_link: Optional[UpdateWebLinkAddSharedLinkRequestBodyArgSharedLinkField], optional
        """
        super().__init__(**kwargs)
        self.shared_link = shared_link

class UpdateWebLinkUpdateSharedLinkRequestBodyArgSharedLinkFieldAccessField(str, Enum):
    OPEN = 'open'
    COMPANY = 'company'
    COLLABORATORS = 'collaborators'

class UpdateWebLinkUpdateSharedLinkRequestBodyArgSharedLinkFieldPermissionsField(BaseObject):
    def __init__(self, can_download: Optional[bool] = None, can_preview: Optional[bool] = None, can_edit: Optional[bool] = None, **kwargs):
        """
        :param can_download: If the shared link allows for downloading of files.
            This can only be set when `access` is set to
            `open` or `company`.
        :type can_download: Optional[bool], optional
        :param can_preview: If the shared link allows for previewing of files.
            This value is always `true`. For shared links on folders
            this also applies to any items in the folder.
        :type can_preview: Optional[bool], optional
        :param can_edit: This value can only be `true` is `type` is `file`.
        :type can_edit: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.can_download = can_download
        self.can_preview = can_preview
        self.can_edit = can_edit

class UpdateWebLinkUpdateSharedLinkRequestBodyArgSharedLinkField(BaseObject):
    def __init__(self, access: Optional[UpdateWebLinkUpdateSharedLinkRequestBodyArgSharedLinkFieldAccessField] = None, password: Optional[str] = None, vanity_name: Optional[str] = None, unshared_at: Optional[str] = None, permissions: Optional[UpdateWebLinkUpdateSharedLinkRequestBodyArgSharedLinkFieldPermissionsField] = None, **kwargs):
        """
        :param access: The level of access for the shared link. This can be
            restricted to anyone with the link (`open`), only people
            within the company (`company`) and only those who
            have been invited to the folder (`collaborators`).
            If not set, this field defaults to the access level specified
            by the enterprise admin. To create a shared link with this
            default setting pass the `shared_link` object with
            no `access` field, for example `{ "shared_link": {} }`.
            The `company` access level is only available to paid
            accounts.
        :type access: Optional[UpdateWebLinkUpdateSharedLinkRequestBodyArgSharedLinkFieldAccessField], optional
        :param password: The password required to access the shared link. Set the
            password to `null` to remove it.
            Passwords must now be at least eight characters
            long and include a number, upper case letter, or
            a non-numeric or non-alphabetical character.
            A password can only be set when `access` is set to `open`.
        :type password: Optional[str], optional
        :param vanity_name: Defines a custom vanity name to use in the shared link URL,
            for example `https://app.box.com/v/my-shared-link`.
            Custom URLs should not be used when sharing sensitive content
            as vanity URLs are a lot easier to guess than regular shared
            links.
        :type vanity_name: Optional[str], optional
        :param unshared_at: The timestamp at which this shared link will
            expire. This field can only be set by
            users with paid accounts. The value must be greater than the
            current date and time.
        :type unshared_at: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.access = access
        self.password = password
        self.vanity_name = vanity_name
        self.unshared_at = unshared_at
        self.permissions = permissions

class UpdateWebLinkUpdateSharedLinkRequestBodyArg(BaseObject):
    def __init__(self, shared_link: Optional[UpdateWebLinkUpdateSharedLinkRequestBodyArgSharedLinkField] = None, **kwargs):
        """
        :param shared_link: The settings for the shared link to update.
        :type shared_link: Optional[UpdateWebLinkUpdateSharedLinkRequestBodyArgSharedLinkField], optional
        """
        super().__init__(**kwargs)
        self.shared_link = shared_link

class UpdateWebLinkRemoveSharedLinkRequestBodyArgSharedLinkField(BaseObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class UpdateWebLinkRemoveSharedLinkRequestBodyArg(BaseObject):
    def __init__(self, shared_link: Optional[UpdateWebLinkRemoveSharedLinkRequestBodyArgSharedLinkField] = None, **kwargs):
        """
        :param shared_link: By setting this value to `null`, the shared link
            is removed from the web link.
        :type shared_link: Optional[UpdateWebLinkRemoveSharedLinkRequestBodyArgSharedLinkField], optional
        """
        super().__init__(**kwargs)
        self.shared_link = shared_link

class SharedLinksWebLinksManager(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {'network_session': 'networkSession', **BaseObject._fields_to_json_mapping}
    _json_to_fields_mapping: Dict[str, str] = {'networkSession': 'network_session', **BaseObject._json_to_fields_mapping}
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None, **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
        self.network_session = network_session
    def get_shared_item_web_links(self, boxapi: str, options: GetSharedItemWebLinksOptionsArg = None) -> WebLink:
        """
        Returns the web link represented by a shared link.
        
        A shared web link can be represented by a shared link,

        
        which can originate within the current enterprise or within another.

        
        This endpoint allows an application to retrieve information about a

        
        shared web link when only given a shared link.

        :param boxapi: A header containing the shared link and optional password for the
            shared link.
            The format for this header is as follows.
            `shared_link=[link]&shared_link_password=[password]`
            Example: "shared_link=[link]&shared_link_password=[password]"
        :type boxapi: str
        """
        if options is None:
            options = GetSharedItemWebLinksOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shared_items#web_links']), FetchOptions(method='GET', params={'fields': options.fields}, headers={'if-none-match': options.if_none_match, 'boxapi': boxapi}, auth=self.auth, network_session=self.network_session))
        return WebLink.from_dict(json.loads(response.text))
    def get_web_link_get_shared_link(self, web_link_id: str, fields: str) -> WebLink:
        """
        Gets the information for a shared link on a web link.
        :param web_link_id: The ID of the web link.
            Example: "12345"
        :type web_link_id: str
        :param fields: Explicitly request the `shared_link` fields
            to be returned for this item.
            Example: "shared_link"
        :type fields: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/web_links/', web_link_id, '#get_shared_link']), FetchOptions(method='GET', params={'fields': fields}, auth=self.auth, network_session=self.network_session))
        return WebLink.from_dict(json.loads(response.text))
    def update_web_link_add_shared_link(self, web_link_id: str, fields: str, request_body: UpdateWebLinkAddSharedLinkRequestBodyArg) -> WebLink:
        """
        Adds a shared link to a web link.
        :param web_link_id: The ID of the web link.
            Example: "12345"
        :type web_link_id: str
        :param fields: Explicitly request the `shared_link` fields
            to be returned for this item.
            Example: "shared_link"
        :type fields: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/web_links/', web_link_id, '#add_shared_link']), FetchOptions(method='PUT', params={'fields': fields}, body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return WebLink.from_dict(json.loads(response.text))
    def update_web_link_update_shared_link(self, web_link_id: str, fields: str, request_body: UpdateWebLinkUpdateSharedLinkRequestBodyArg) -> WebLink:
        """
        Updates a shared link on a web link.
        :param web_link_id: The ID of the web link.
            Example: "12345"
        :type web_link_id: str
        :param fields: Explicitly request the `shared_link` fields
            to be returned for this item.
            Example: "shared_link"
        :type fields: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/web_links/', web_link_id, '#update_shared_link']), FetchOptions(method='PUT', params={'fields': fields}, body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return WebLink.from_dict(json.loads(response.text))
    def update_web_link_remove_shared_link(self, web_link_id: str, fields: str, request_body: UpdateWebLinkRemoveSharedLinkRequestBodyArg) -> WebLink:
        """
        Removes a shared link from a web link.
        :param web_link_id: The ID of the web link.
            Example: "12345"
        :type web_link_id: str
        :param fields: Explicitly request the `shared_link` fields
            to be returned for this item.
            Example: "shared_link"
        :type fields: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/web_links/', web_link_id, '#remove_shared_link']), FetchOptions(method='PUT', params={'fields': fields}, body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return WebLink.from_dict(json.loads(response.text))