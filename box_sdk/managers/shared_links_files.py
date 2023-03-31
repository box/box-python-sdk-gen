from typing import Union

from box_sdk.base_object import BaseObject

from enum import Enum

import json

from box_sdk.schemas import File

from box_sdk.schemas import ClientError

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.jwt_auth import JWTAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetSharedItemsOptionsArg(BaseObject):
    def __init__(self, if_none_match: Union[None, str] = None, fields: Union[None, str] = None, **kwargs):
        """
        :param if_none_match: Ensures an item is only returned if it has changed.
            Pass in the item's last observed `etag` value
            into this header and the endpoint will fail
            with a `304 Not Modified` if the item has not
            changed since.
        :type if_none_match: Union[None, str], optional
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.if_none_match = if_none_match
        self.fields = fields

class UpdateFileAddSharedLinkRequestBodyArgSharedLinkFieldAccessField(str, Enum):
    OPEN = 'open'
    COMPANY = 'company'
    COLLABORATORS = 'collaborators'

class UpdateFileAddSharedLinkRequestBodyArgSharedLinkFieldPermissionsField(BaseObject):
    def __init__(self, can_download: Union[None, bool] = None, can_preview: Union[None, bool] = None, can_edit: Union[None, bool] = None, **kwargs):
        """
        :param can_download: If the shared link allows for downloading of files.
            This can only be set when `access` is set to
            `open` or `company`.
        :type can_download: Union[None, bool], optional
        :param can_preview: If the shared link allows for previewing of files.
            This value is always `true`. For shared links on folders
            this also applies to any items in the folder.
        :type can_preview: Union[None, bool], optional
        :param can_edit: If the shared link allows for editing of files.
            This can only be set when `access` is set to
            `open` or `company`.
            This value can only be `true` is `can_download` is
            also `true`.
        :type can_edit: Union[None, bool], optional
        """
        super().__init__(**kwargs)
        self.can_download = can_download
        self.can_preview = can_preview
        self.can_edit = can_edit

class UpdateFileAddSharedLinkRequestBodyArgSharedLinkField(BaseObject):
    def __init__(self, access: Union[None, UpdateFileAddSharedLinkRequestBodyArgSharedLinkFieldAccessField] = None, password: Union[None, str] = None, vanity_name: Union[None, str] = None, unshared_at: Union[None, str] = None, permissions: Union[None, UpdateFileAddSharedLinkRequestBodyArgSharedLinkFieldPermissionsField] = None, **kwargs):
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
        :type access: Union[None, UpdateFileAddSharedLinkRequestBodyArgSharedLinkFieldAccessField], optional
        :param password: The password required to access the shared link. Set the
            password to `null` to remove it.
            A password can only be set when `access` is set to `open`.
        :type password: Union[None, str], optional
        :param vanity_name: Defines a custom vanity name to use in the shared link URL,
            for example `https://app.box.com/v/my-shared-link`.
            Custom URLs should not be used when sharing sensitive content
            as vanity URLs are a lot easier to guess than regular shared
            links.
        :type vanity_name: Union[None, str], optional
        :param unshared_at: The timestamp at which this shared link will
            expire. This field can only be set by
            users with paid accounts. The value must be greater than the
            current date and time.
        :type unshared_at: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.access = access
        self.password = password
        self.vanity_name = vanity_name
        self.unshared_at = unshared_at
        self.permissions = permissions

class UpdateFileAddSharedLinkRequestBodyArg(BaseObject):
    def __init__(self, shared_link: Union[None, UpdateFileAddSharedLinkRequestBodyArgSharedLinkField] = None, **kwargs):
        """
        :param shared_link: The settings for the shared link to create on the file.
            Use an empty object (`{}`) to use the default settings for shared
            links.
        :type shared_link: Union[None, UpdateFileAddSharedLinkRequestBodyArgSharedLinkField], optional
        """
        super().__init__(**kwargs)
        self.shared_link = shared_link

class UpdateFileUpdateSharedLinkRequestBodyArgSharedLinkFieldAccessField(str, Enum):
    OPEN = 'open'
    COMPANY = 'company'
    COLLABORATORS = 'collaborators'

class UpdateFileUpdateSharedLinkRequestBodyArgSharedLinkFieldPermissionsField(BaseObject):
    def __init__(self, can_download: Union[None, bool] = None, can_preview: Union[None, bool] = None, can_edit: Union[None, bool] = None, **kwargs):
        """
        :param can_download: If the shared link allows for downloading of files.
            This can only be set when `access` is set to
            `open` or `company`.
        :type can_download: Union[None, bool], optional
        :param can_preview: If the shared link allows for previewing of files.
            This value is always `true`. For shared links on folders
            this also applies to any items in the folder.
        :type can_preview: Union[None, bool], optional
        :param can_edit: If the shared link allows for editing of files.
            This can only be set when `access` is set to
            `open` or `company`.
            This value can only be `true` is `can_download` is
            also `true`.
        :type can_edit: Union[None, bool], optional
        """
        super().__init__(**kwargs)
        self.can_download = can_download
        self.can_preview = can_preview
        self.can_edit = can_edit

class UpdateFileUpdateSharedLinkRequestBodyArgSharedLinkField(BaseObject):
    def __init__(self, access: Union[None, UpdateFileUpdateSharedLinkRequestBodyArgSharedLinkFieldAccessField] = None, password: Union[None, str] = None, vanity_name: Union[None, str] = None, unshared_at: Union[None, str] = None, permissions: Union[None, UpdateFileUpdateSharedLinkRequestBodyArgSharedLinkFieldPermissionsField] = None, **kwargs):
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
        :type access: Union[None, UpdateFileUpdateSharedLinkRequestBodyArgSharedLinkFieldAccessField], optional
        :param password: The password required to access the shared link. Set the
            password to `null` to remove it.
            A password can only be set when `access` is set to `open`.
        :type password: Union[None, str], optional
        :param vanity_name: Defines a custom vanity name to use in the shared link URL,
            for example `https://app.box.com/v/my-shared-link`.
            Custom URLs should not be used when sharing sensitive content
            as vanity URLs are a lot easier to guess than regular shared
            links.
        :type vanity_name: Union[None, str], optional
        :param unshared_at: The timestamp at which this shared link will
            expire. This field can only be set by
            users with paid accounts. The value must be greater than the
            current date and time.
        :type unshared_at: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.access = access
        self.password = password
        self.vanity_name = vanity_name
        self.unshared_at = unshared_at
        self.permissions = permissions

class UpdateFileUpdateSharedLinkRequestBodyArg(BaseObject):
    def __init__(self, shared_link: Union[None, UpdateFileUpdateSharedLinkRequestBodyArgSharedLinkField] = None, **kwargs):
        """
        :param shared_link: The settings for the shared link to update.
        :type shared_link: Union[None, UpdateFileUpdateSharedLinkRequestBodyArgSharedLinkField], optional
        """
        super().__init__(**kwargs)
        self.shared_link = shared_link

class UpdateFileRemoveSharedLinkRequestBodyArgSharedLinkField(BaseObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class UpdateFileRemoveSharedLinkRequestBodyArg(BaseObject):
    def __init__(self, shared_link: Union[None, UpdateFileRemoveSharedLinkRequestBodyArgSharedLinkField] = None, **kwargs):
        """
        :param shared_link: By setting this value to `null`, the shared link
            is removed from the file.
        :type shared_link: Union[None, UpdateFileRemoveSharedLinkRequestBodyArgSharedLinkField], optional
        """
        super().__init__(**kwargs)
        self.shared_link = shared_link

class SharedLinksFilesManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth, JWTAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_shared_items(self, boxapi: str, options: GetSharedItemsOptionsArg = None) -> File:
        """
        Returns the file represented by a shared link.
        
        A shared file can be represented by a shared link,

        
        which can originate within the current enterprise or within another.

        
        This endpoint allows an application to retrieve information about a

        
        shared file when only given a shared link.

        
        The `shared_link_permission_options` array field can be returned

        
        by requesting it in the `fields` query parameter.

        :param boxapi: A header containing the shared link and optional password for the
            shared link.
            The format for this header is as follows.
            `shared_link=[link]&shared_link_password=[password]`
            Example: "shared_link=[link]&shared_link_password=[password]"
        :type boxapi: str
        """
        if options is None:
            options = GetSharedItemsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shared_items']), FetchOptions(method='GET', params={'fields': options.fields}, headers={'if-none-match': options.if_none_match, 'boxapi': boxapi}, auth=self.auth))
        return File.from_dict(json.loads(response.text))
    def get_file_get_shared_link(self, file_id: str, fields: str) -> File:
        """
        Gets the information for a shared link on a file.
        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        :param fields: Explicitly request the `shared_link` fields
            to be returned for this item.
            Example: "shared_link"
        :type fields: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '#get_shared_link']), FetchOptions(method='GET', params={'fields': fields}, auth=self.auth))
        return File.from_dict(json.loads(response.text))
    def update_file_add_shared_link(self, file_id: str, fields: str, request_body: UpdateFileAddSharedLinkRequestBodyArg) -> File:
        """
        Adds a shared link to a file.
        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        :param fields: Explicitly request the `shared_link` fields
            to be returned for this item.
            Example: "shared_link"
        :type fields: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '#add_shared_link']), FetchOptions(method='PUT', params={'fields': fields}, body=json.dumps(request_body.to_dict()), auth=self.auth))
        return File.from_dict(json.loads(response.text))
    def update_file_update_shared_link(self, file_id: str, fields: str, request_body: UpdateFileUpdateSharedLinkRequestBodyArg) -> File:
        """
        Updates a shared link on a file.
        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        :param fields: Explicitly request the `shared_link` fields
            to be returned for this item.
            Example: "shared_link"
        :type fields: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '#update_shared_link']), FetchOptions(method='PUT', params={'fields': fields}, body=json.dumps(request_body.to_dict()), auth=self.auth))
        return File.from_dict(json.loads(response.text))
    def update_file_remove_shared_link(self, file_id: str, fields: str, request_body: UpdateFileRemoveSharedLinkRequestBodyArg) -> File:
        """
        Removes a shared link from a file.
        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        :param fields: Explicitly request the `shared_link` fields
            to be returned for this item.
            Example: "shared_link"
        :type fields: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '#remove_shared_link']), FetchOptions(method='PUT', params={'fields': fields}, body=json.dumps(request_body.to_dict()), auth=self.auth))
        return File.from_dict(json.loads(response.text))