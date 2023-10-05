from typing import Optional

from box_sdk_gen.base_object import BaseObject

from enum import Enum

from typing import List

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.serialization import serialize

from box_sdk_gen.schemas import FileFull

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse


class UpdateFileByIdParentArg(BaseObject):
    def __init__(self, id: Optional[str] = None, **kwargs):
        """
        :param id: The ID of parent item
        :type id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id


class UpdateFileByIdSharedLinkArgAccessField(str, Enum):
    OPEN = 'open'
    COMPANY = 'company'
    COLLABORATORS = 'collaborators'


class UpdateFileByIdSharedLinkArgPermissionsField(BaseObject):
    def __init__(self, can_download: Optional[bool] = None, **kwargs):
        """
        :param can_download: If the shared link allows for downloading of files.
            This can only be set when `access` is set to
            `open` or `company`.
        :type can_download: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.can_download = can_download


class UpdateFileByIdSharedLinkArg(BaseObject):
    def __init__(
        self,
        access: Optional[UpdateFileByIdSharedLinkArgAccessField] = None,
        password: Optional[str] = None,
        vanity_name: Optional[str] = None,
        unshared_at: Optional[str] = None,
        permissions: Optional[UpdateFileByIdSharedLinkArgPermissionsField] = None,
        **kwargs
    ):
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
        :type access: Optional[UpdateFileByIdSharedLinkArgAccessField], optional
        :param password: The password required to access the shared link. Set the
            password to `null` to remove it.
            Passwords must now be at least eight characters
            long and include a number, upper case letter, or
            a non-numeric or non-alphabetic character.
            A password can only be set when `access` is set to `open`.
        :type password: Optional[str], optional
        :param vanity_name: Defines a custom vanity name to use in the shared link URL,
            for example `https://app.box.com/v/my-shared-link`.
            Custom URLs should not be used when sharing sensitive content
            as vanity URLs are a lot easier to guess than regular shared links.
        :type vanity_name: Optional[str], optional
        :param unshared_at: The timestamp at which this shared link will
            expire. This field can only be set by
            users with paid accounts.
        :type unshared_at: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.access = access
        self.password = password
        self.vanity_name = vanity_name
        self.unshared_at = unshared_at
        self.permissions = permissions


class UpdateFileByIdLockArgAccessField(str, Enum):
    LOCK = 'lock'


class UpdateFileByIdLockArg(BaseObject):
    def __init__(
        self,
        access: Optional[UpdateFileByIdLockArgAccessField] = None,
        expires_at: Optional[str] = None,
        is_download_prevented: Optional[bool] = None,
        **kwargs
    ):
        """
        :param access: The type of this object.
        :type access: Optional[UpdateFileByIdLockArgAccessField], optional
        :param expires_at: Defines the time at which the lock expires.
        :type expires_at: Optional[str], optional
        :param is_download_prevented: Defines if the file can be downloaded while it is locked.
        :type is_download_prevented: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.access = access
        self.expires_at = expires_at
        self.is_download_prevented = is_download_prevented


class UpdateFileByIdPermissionsArgCanDownloadField(str, Enum):
    OPEN = 'open'
    COMPANY = 'company'


class UpdateFileByIdPermissionsArg(BaseObject):
    def __init__(
        self,
        can_download: Optional[UpdateFileByIdPermissionsArgCanDownloadField] = None,
        **kwargs
    ):
        """
        :param can_download: Defines who is allowed to download this file. The possible
            values are either `open` for everyone or `company` for
            the other members of the user's enterprise.
            This setting overrides the download permissions that are
            normally part of the `role` of a collaboration. When set to
            `company`, this essentially removes the download option for
            external users with `viewer` or `editor` a roles.
        :type can_download: Optional[UpdateFileByIdPermissionsArgCanDownloadField], optional
        """
        super().__init__(**kwargs)
        self.can_download = can_download


class UpdateFileByIdCollectionsArg(BaseObject):
    def __init__(self, id: Optional[str] = None, type: Optional[str] = None, **kwargs):
        """
        :param id: The unique identifier for this object
        :type id: Optional[str], optional
        :param type: The type for this object
        :type type: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class CopyFileParentArg(BaseObject):
    def __init__(self, id: str, **kwargs):
        """
        :param id: The ID of folder to copy the file to.
        :type id: str
        """
        super().__init__(**kwargs)
        self.id = id


class GetFileThumbnailByIdExtensionArg(str, Enum):
    PNG = 'png'
    JPG = 'jpg'


class FilesManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def get_file_by_id(
        self,
        file_id: str,
        fields: Optional[List[str]] = None,
        if_none_match: Optional[str] = None,
        boxapi: Optional[str] = None,
        x_rep_hints: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> FileFull:
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
        :type fields: Optional[List[str]], optional
        :param if_none_match: Ensures an item is only returned if it has changed.
            Pass in the item's last observed `etag` value
            into this header and the endpoint will fail
            with a `304 Not Modified` if the item has not
            changed since.
        :type if_none_match: Optional[str], optional
        :param boxapi: The URL, and optional password, for the shared link of this item.
            This header can be used to access items that have not been
            explicitly shared with a user.
            Use the format `shared_link=[link]` or if a password is required then
            use `shared_link=[link]&shared_link_password=[password]`.
            This header can be used on the file or folder shared, as well as on any files
            or folders nested within the item.
        :type boxapi: Optional[str], optional
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
        :type x_rep_hints: Optional[str], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params({'fields': to_string(fields)})
        headers_map: Dict[str, str] = prepare_params(
            {
                'if-none-match': to_string(if_none_match),
                'boxapi': to_string(boxapi),
                'x-rep-hints': to_string(x_rep_hints),
                **extra_headers,
            }
        )
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/files/', to_string(file_id)]),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, FileFull)

    def update_file_by_id(
        self,
        file_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        parent: Optional[UpdateFileByIdParentArg] = None,
        shared_link: Optional[UpdateFileByIdSharedLinkArg] = None,
        lock: Optional[UpdateFileByIdLockArg] = None,
        disposition_at: Optional[str] = None,
        permissions: Optional[UpdateFileByIdPermissionsArg] = None,
        collections: Optional[List[UpdateFileByIdCollectionsArg]] = None,
        tags: Optional[List[str]] = None,
        fields: Optional[List[str]] = None,
        if_match: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> FileFull:
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
        :param name: An optional different name for the file. This can be used to
            rename the file.
        :type name: Optional[str], optional
        :param description: The description for a file. This can be seen in the right-hand sidebar panel
            when viewing a file in the Box web app. Additionally, this index is used in
            the search index of the file, allowing users to find the file by the content
            in the description.
        :type description: Optional[str], optional
        :param lock: Defines a lock on an item. This prevents the item from being
            moved, renamed, or otherwise changed by anyone other than the user
            who created the lock.
            Set this to `null` to remove the lock.
        :type lock: Optional[UpdateFileByIdLockArg], optional
        :param disposition_at: The retention expiration timestamp for the given file. This
            date cannot be shortened once set on a file.
        :type disposition_at: Optional[str], optional
        :param permissions: Defines who can download a file.
        :type permissions: Optional[UpdateFileByIdPermissionsArg], optional
        :param collections: An array of collections to make this file
            a member of. Currently
            we only support the `favorites` collection.
            To get the ID for a collection, use the
            [List all collections][1] endpoint.
            Passing an empty array `[]` or `null` will remove
            the file from all collections.
            [1]: e://get-collections
        :type collections: Optional[List[UpdateFileByIdCollectionsArg]], optional
        :param tags: The tags for this item. These tags are shown in
            the Box web app and mobile apps next to an item.
            To add or remove a tag, retrieve the item's current tags,
            modify them, and then update this field.
            There is a limit of 100 tags per item, and 10,000
            unique tags per enterprise.
        :type tags: Optional[List[str]], optional
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[List[str]], optional
        :param if_match: Ensures this item hasn't recently changed before
            making changes.
            Pass in the item's last observed `etag` value
            into this header and the endpoint will fail
            with a `412 Precondition Failed` if it
            has changed since.
        :type if_match: Optional[str], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body = {
            'name': name,
            'description': description,
            'parent': parent,
            'shared_link': shared_link,
            'lock': lock,
            'disposition_at': disposition_at,
            'permissions': permissions,
            'collections': collections,
            'tags': tags,
        }
        query_params_map: Dict[str, str] = prepare_params({'fields': to_string(fields)})
        headers_map: Dict[str, str] = prepare_params(
            {'if-match': to_string(if_match), **extra_headers}
        )
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/files/', to_string(file_id)]),
            FetchOptions(
                method='PUT',
                params=query_params_map,
                headers=headers_map,
                body=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, FileFull)

    def delete_file_by_id(
        self,
        file_id: str,
        if_match: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> None:
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
        :param if_match: Ensures this item hasn't recently changed before
            making changes.
            Pass in the item's last observed `etag` value
            into this header and the endpoint will fail
            with a `412 Precondition Failed` if it
            has changed since.
        :type if_match: Optional[str], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params(
            {'if-match': to_string(if_match), **extra_headers}
        )
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/files/', to_string(file_id)]),
            FetchOptions(
                method='DELETE',
                headers=headers_map,
                response_format=None,
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return None

    def copy_file(
        self,
        file_id: str,
        parent: CopyFileParentArg,
        name: Optional[str] = None,
        version: Optional[str] = None,
        fields: Optional[List[str]] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> FileFull:
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
        :param parent: The destination folder to copy the file to.
        :type parent: CopyFileParentArg
        :param name: An optional new name for the copied file.
            There are some restrictions to the file name. Names containing
            non-printable ASCII characters, forward and backward slashes
            (`/`, `\`), and protected names like `.` and `..` are
            automatically sanitized by removing the non-allowed
            characters.
        :type name: Optional[str], optional
        :param version: An optional ID of the specific file version to copy.
        :type version: Optional[str], optional
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[List[str]], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body = {'name': name, 'version': version, 'parent': parent}
        query_params_map: Dict[str, str] = prepare_params({'fields': to_string(fields)})
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/files/', to_string(file_id), '/copy']),
            FetchOptions(
                method='POST',
                params=query_params_map,
                headers=headers_map,
                body=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, FileFull)

    def get_file_thumbnail_by_id(
        self,
        file_id: str,
        extension: GetFileThumbnailByIdExtensionArg,
        min_height: Optional[int] = None,
        min_width: Optional[int] = None,
        max_height: Optional[int] = None,
        max_width: Optional[int] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> ByteStream:
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
        :type extension: GetFileThumbnailByIdExtensionArg
        :param min_height: The minimum height of the thumbnail
        :type min_height: Optional[int], optional
        :param min_width: The minimum width of the thumbnail
        :type min_width: Optional[int], optional
        :param max_height: The maximum height of the thumbnail
        :type max_height: Optional[int], optional
        :param max_width: The maximum width of the thumbnail
        :type max_width: Optional[int], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params(
            {
                'min_height': to_string(min_height),
                'min_width': to_string(min_width),
                'max_height': to_string(max_height),
                'max_width': to_string(max_width),
            }
        )
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    'https://api.box.com/2.0/files/',
                    to_string(file_id),
                    '/thumbnail.',
                    to_string(extension),
                ]
            ),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='binary',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return response.content
