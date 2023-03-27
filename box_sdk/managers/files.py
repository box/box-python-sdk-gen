from typing import Union

from box_sdk.base_object import BaseObject

from enum import Enum

from typing import List

import json

from box_sdk.schemas import File

from box_sdk.schemas import ClientError

from box_sdk.schemas import TrashFileRestored

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetFilesIdOptionsArg(BaseObject):
    def __init__(self, fields: Union[None, str] = None, if_none_match: Union[None, str] = None, boxapi: Union[None, str] = None, x_rep_hints: Union[None, str] = None, **kwargs):
        """
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
            Additionally this field can be used to query any metadata
            applied to the file by specifying the `metadata` field as well
            as the scope and key of the template to retrieve, for example
            `?field=metadata.enterprise_12345.contractTemplate`.
        :type fields: Union[None, str], optional
        :param if_none_match: Ensures an item is only returned if it has changed.
            Pass in the item's last observed `etag` value
            into this header and the endpoint will fail
            with a `304 Not Modified` if the item has not
            changed since.
        :type if_none_match: Union[None, str], optional
        :param boxapi: The URL, and optional password, for the shared link of this item.
            This header can be used to access items that have not been
            explicitly shared with a user.
            Use the format `shared_link=[link]` or if a password is required then
            use `shared_link=[link]&shared_link_password=[password]`.
            This header can be used on the file or folder shared, as well as on any files
            or folders nested within the item.
        :type boxapi: Union[None, str], optional
        :param x_rep_hints: A header required to request specific `representations`
            of a file. Use this in combination with the `fields` query
            parameter to request a specific file representation.
            The general format for these representations is
            `X-Rep-Hints: [...]` where `[...]` is one or many
            hints in the format `[fileType?query]`.
            For example, to request a `png` representation in `32x32`
            as well as `64x64` pixel dimensions provide the following
            hints.
            `x-rep-hints: [jpg?dimensions=32x32][jpg?dimensions=64x64]`
            Additionally, a `text` representation is available for all
            document file types in Box using the `[extracted_text]`
            representation.
            `x-rep-hints: [extracted_text]`
        :type x_rep_hints: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.fields = fields
        self.if_none_match = if_none_match
        self.boxapi = boxapi
        self.x_rep_hints = x_rep_hints

class PostFilesIdRequestBodyArgParentField(BaseObject):
    def __init__(self, id: Union[None, str] = None, **kwargs):
        """
        :param id: The ID of parent item
        :type id: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.id = id

class PostFilesIdRequestBodyArg(BaseObject):
    def __init__(self, name: Union[None, str] = None, parent: Union[None, PostFilesIdRequestBodyArgParentField] = None, **kwargs):
        """
        :param name: An optional new name for the file.
        :type name: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.name = name
        self.parent = parent

class PostFilesIdOptionsArg(BaseObject):
    def __init__(self, fields: Union[None, str] = None, **kwargs):
        """
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
        self.fields = fields

class PutFilesIdRequestBodyArgParentField(BaseObject):
    def __init__(self, id: Union[None, str] = None, **kwargs):
        """
        :param id: The ID of parent item
        :type id: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.id = id

class PutFilesIdRequestBodyArgSharedLinkFieldAccessField(str, Enum):
    OPEN = 'open'
    COMPANY = 'company'
    COLLABORATORS = 'collaborators'

class PutFilesIdRequestBodyArgSharedLinkFieldPermissionsField(BaseObject):
    def __init__(self, can_download: Union[None, bool] = None, **kwargs):
        """
        :param can_download: If the shared link allows for downloading of files.
            This can only be set when `access` is set to
            `open` or `company`.
        :type can_download: Union[None, bool], optional
        """
        super().__init__(**kwargs)
        self.can_download = can_download

class PutFilesIdRequestBodyArgSharedLinkField(BaseObject):
    def __init__(self, access: Union[None, PutFilesIdRequestBodyArgSharedLinkFieldAccessField] = None, password: Union[None, str] = None, vanity_name: Union[None, str] = None, unshared_at: Union[None, str] = None, permissions: Union[None, PutFilesIdRequestBodyArgSharedLinkFieldPermissionsField] = None, **kwargs):
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
        :type access: Union[None, PutFilesIdRequestBodyArgSharedLinkFieldAccessField], optional
        :param password: The password required to access the shared link. Set the
            password to `null` to remove it.
            A password can only be set when `access` is set to `open`.
        :type password: Union[None, str], optional
        :param vanity_name: Defines a custom vanity name to use in the shared link URL,
            for example `https://app.box.com/v/my-shared-link`.
            Custom URLs should not be used when sharing sensitive content
            as vanity URLs are a lot easier to guess than regular shared links.
        :type vanity_name: Union[None, str], optional
        :param unshared_at: The timestamp at which this shared link will
            expire. This field can only be set by
            users with paid accounts.
        :type unshared_at: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.access = access
        self.password = password
        self.vanity_name = vanity_name
        self.unshared_at = unshared_at
        self.permissions = permissions

class PutFilesIdRequestBodyArgLockFieldAccessField(str, Enum):
    LOCK = 'lock'

class PutFilesIdRequestBodyArgLockField(BaseObject):
    def __init__(self, access: Union[None, PutFilesIdRequestBodyArgLockFieldAccessField] = None, expires_at: Union[None, str] = None, is_download_prevented: Union[None, bool] = None, **kwargs):
        """
        :param access: The type of this object.
        :type access: Union[None, PutFilesIdRequestBodyArgLockFieldAccessField], optional
        :param expires_at: Defines the time at which the lock expires.
        :type expires_at: Union[None, str], optional
        :param is_download_prevented: Defines if the file can be downloaded while it is locked.
        :type is_download_prevented: Union[None, bool], optional
        """
        super().__init__(**kwargs)
        self.access = access
        self.expires_at = expires_at
        self.is_download_prevented = is_download_prevented

class PutFilesIdRequestBodyArgPermissionsFieldCanDownloadField(str, Enum):
    OPEN = 'open'
    COMPANY = 'company'

class PutFilesIdRequestBodyArgPermissionsField(BaseObject):
    def __init__(self, can_download: Union[None, PutFilesIdRequestBodyArgPermissionsFieldCanDownloadField] = None, **kwargs):
        """
        :param can_download: Defines who is allowed to download this file. The possible
            values are either `open` for everyone or `company` for
            the other members of the user's enterprise.
            This setting overrides the download permissions that are
            normally part of the `role` of a collaboration. When set to
            `company`, this essentially removes the download option for
            external users with `viewer` or `editor` a roles.
        :type can_download: Union[None, PutFilesIdRequestBodyArgPermissionsFieldCanDownloadField], optional
        """
        super().__init__(**kwargs)
        self.can_download = can_download

class PutFilesIdRequestBodyArg(BaseObject):
    def __init__(self, name: Union[None, str] = None, description: Union[None, str] = None, parent: Union[None, PutFilesIdRequestBodyArgParentField] = None, shared_link: Union[None, PutFilesIdRequestBodyArgSharedLinkField] = None, lock: Union[None, PutFilesIdRequestBodyArgLockField] = None, disposition_at: Union[None, str] = None, permissions: Union[None, PutFilesIdRequestBodyArgPermissionsField] = None, tags: Union[None, List[str]] = None, **kwargs):
        """
        :param name: An optional different name for the file. This can be used to
            rename the file.
        :type name: Union[None, str], optional
        :param description: The description for a file. This can be seen in the right-hand sidebar panel
            when viewing a file in the Box web app. Additionally, this index is used in
            the search index of the file, allowing users to find the file by the content
            in the description.
        :type description: Union[None, str], optional
        :param lock: Defines a lock on an item. This prevents the item from being
            moved, renamed, or otherwise changed by anyone other than the user
            who created the lock.
            Set this to `null` to remove the lock.
        :type lock: Union[None, PutFilesIdRequestBodyArgLockField], optional
        :param disposition_at: The retention expiration timestamp for the given file. This
            date cannot be shortened once set on a file.
        :type disposition_at: Union[None, str], optional
        :param permissions: Defines who can download a file.
        :type permissions: Union[None, PutFilesIdRequestBodyArgPermissionsField], optional
        :param tags: The tags for this item. These tags are shown in
            the Box web app and mobile apps next to an item.
            To add or remove a tag, retrieve the item's current tags,
            modify them, and then update this field.
            There is a limit of 100 tags per item, and 10,000
            unique tags per enterprise.
        :type tags: Union[None, List[str]], optional
        """
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self.parent = parent
        self.shared_link = shared_link
        self.lock = lock
        self.disposition_at = disposition_at
        self.permissions = permissions
        self.tags = tags

class PutFilesIdOptionsArg(BaseObject):
    def __init__(self, fields: Union[None, str] = None, if_match: Union[None, str] = None, **kwargs):
        """
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Union[None, str], optional
        :param if_match: Ensures this item hasn't recently changed before
            making changes.
            Pass in the item's last observed `etag` value
            into this header and the endpoint will fail
            with a `412 Precondition Failed` if it
            has changed since.
        :type if_match: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.fields = fields
        self.if_match = if_match

class DeleteFilesIdOptionsArg(BaseObject):
    def __init__(self, if_match: Union[None, str] = None, **kwargs):
        """
        :param if_match: Ensures this item hasn't recently changed before
            making changes.
            Pass in the item's last observed `etag` value
            into this header and the endpoint will fail
            with a `412 Precondition Failed` if it
            has changed since.
        :type if_match: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.if_match = if_match

class PostFilesIdCopyRequestBodyArgParentField(BaseObject):
    def __init__(self, id: str, **kwargs):
        """
        :param id: The ID of folder to copy the file to.
        :type id: str
        """
        super().__init__(**kwargs)
        self.id = id

class PostFilesIdCopyRequestBodyArg(BaseObject):
    def __init__(self, parent: PostFilesIdCopyRequestBodyArgParentField, name: Union[None, str] = None, version: Union[None, str] = None, **kwargs):
        """
        :param parent: The destination folder to copy the file to.
        :type parent: PostFilesIdCopyRequestBodyArgParentField
        :param name: An optional new name for the copied file.
            There are some restrictions to the file name. Names containing
            non-printable ASCII characters, forward and backward slashes
            (`/`, `\`), and protected names like `.` and `..` are
            automatically sanitized by removing the non-allowed
            characters.
        :type name: Union[None, str], optional
        :param version: An optional ID of the specific file version to copy.
        :type version: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.parent = parent
        self.name = name
        self.version = version

class PostFilesIdCopyOptionsArg(BaseObject):
    def __init__(self, fields: Union[None, str] = None, **kwargs):
        """
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
        self.fields = fields

class GetFilesIdThumbnailIdExtensionArg(str, Enum):
    PNG = 'png'
    JPG = 'jpg'

class GetFilesIdThumbnailIdOptionsArg(BaseObject):
    def __init__(self, min_height: Union[None, int] = None, min_width: Union[None, int] = None, max_height: Union[None, int] = None, max_width: Union[None, int] = None, **kwargs):
        """
        :param min_height: The minimum height of the thumbnail
        :type min_height: Union[None, int], optional
        :param min_width: The minimum width of the thumbnail
        :type min_width: Union[None, int], optional
        :param max_height: The maximum height of the thumbnail
        :type max_height: Union[None, int], optional
        :param max_width: The maximum width of the thumbnail
        :type max_width: Union[None, int], optional
        """
        super().__init__(**kwargs)
        self.min_height = min_height
        self.min_width = min_width
        self.max_height = max_height
        self.max_width = max_width

class FilesManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_files_id(self, file_id: str, options: GetFilesIdOptionsArg = None) -> File:
        """
        Retrieves the details about a file.
        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        """
        if options is None:
            options = GetFilesIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id]), FetchOptions(method='GET', params={'fields': options.fields}, headers={'if-none-match': options.if_none_match, 'boxapi': options.boxapi, 'x-rep-hints': options.x_rep_hints}, auth=self.auth))
        return File.from_dict(json.loads(response.text))
    def post_files_id(self, file_id: str, request_body: PostFilesIdRequestBodyArg, options: PostFilesIdOptionsArg = None) -> TrashFileRestored:
        """
        Restores a file that has been moved to the trash.
        
        An optional new parent ID can be provided to restore the file to in case the

        
        original folder has been deleted.

        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        """
        if options is None:
            options = PostFilesIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id]), FetchOptions(method='POST', params={'fields': options.fields}, body=json.dumps(request_body.to_dict()), auth=self.auth))
        return TrashFileRestored.from_dict(json.loads(response.text))
    def put_files_id(self, file_id: str, request_body: PutFilesIdRequestBodyArg, options: PutFilesIdOptionsArg = None) -> File:
        """
        Updates a file. This can be used to rename or move a file,
        
        create a shared link, or lock a file.

        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        """
        if options is None:
            options = PutFilesIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id]), FetchOptions(method='PUT', params={'fields': options.fields}, headers={'if-match': options.if_match}, body=json.dumps(request_body.to_dict()), auth=self.auth))
        return File.from_dict(json.loads(response.text))
    def delete_files_id(self, file_id: str, options: DeleteFilesIdOptionsArg = None):
        """
        Deletes a file, either permanently or by moving it to
        
        the trash.

        
        The the enterprise settings determine whether the item will

        
        be permanently deleted from Box or moved to the trash.

        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        """
        if options is None:
            options = DeleteFilesIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id]), FetchOptions(method='DELETE', headers={'if-match': options.if_match}, auth=self.auth))
        return response.content
    def post_files_id_copy(self, file_id: str, request_body: PostFilesIdCopyRequestBodyArg, options: PostFilesIdCopyOptionsArg = None) -> File:
        """
        Creates a copy of a file.
        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        """
        if options is None:
            options = PostFilesIdCopyOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/copy']), FetchOptions(method='POST', params={'fields': options.fields}, body=json.dumps(request_body.to_dict()), auth=self.auth))
        return File.from_dict(json.loads(response.text))
    def get_files_id_thumbnail_id(self, file_id: str, extension: GetFilesIdThumbnailIdExtensionArg, options: GetFilesIdThumbnailIdOptionsArg = None):
        """
        Retrieves a thumbnail, or smaller image representation, of a file.
        
        Sizes of `32x32`,`64x64`, `128x128`, and `256x256` can be returned in

        
        the `.png` format and sizes of `32x32`, `160x160`, and `320x320`

        
        can be returned in the `.jpg` format.

        
        Thumbnails can be generated for the image and video file formats listed

        
        [found on our community site][1].

        
        [1]: https://community.box.com/t5/Migrating-and-Previewing-Content/File-Types-and-Fonts-Supported-in-Box-Content-Preview/ta-p/327

        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        :param extension: The file format for the thumbnail
            Example: "png"
        :type extension: GetFilesIdThumbnailIdExtensionArg
        """
        if options is None:
            options = GetFilesIdThumbnailIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/thumbnail.', extension]), FetchOptions(method='GET', params={'min_height': options.minHeight, 'min_width': options.minWidth, 'max_height': options.maxHeight, 'max_width': options.maxWidth}, auth=self.auth))
        return response.content