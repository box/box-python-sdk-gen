from enum import Enum

from typing import Optional

from box_sdk_gen.base_object import BaseObject

from typing import List

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.serialization import serialize

from box_sdk_gen.schemas import FolderFull

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import Items

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse


class GetFolderByIdSortArg(str, Enum):
    ID = 'id'
    NAME = 'name'
    DATE = 'date'
    SIZE = 'size'


class GetFolderByIdDirectionArg(str, Enum):
    ASC = 'ASC'
    DESC = 'DESC'


class UpdateFolderByIdSyncStateArg(str, Enum):
    SYNCED = 'synced'
    NOT_SYNCED = 'not_synced'
    PARTIALLY_SYNCED = 'partially_synced'


class UpdateFolderByIdParentArg(BaseObject):
    def __init__(self, id: Optional[str] = None, **kwargs):
        """
        :param id: The ID of the new parent folder
        :type id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id


class UpdateFolderByIdSharedLinkArgAccessField(str, Enum):
    OPEN = 'open'
    COMPANY = 'company'
    COLLABORATORS = 'collaborators'


class UpdateFolderByIdSharedLinkArgPermissionsField(BaseObject):
    def __init__(self, can_download: Optional[bool] = None, **kwargs):
        """
        :param can_download: If the shared link allows for downloading of files.
            This can only be set when `access` is set to
            `open` or `company`.
        :type can_download: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.can_download = can_download


class UpdateFolderByIdSharedLinkArg(BaseObject):
    def __init__(
        self,
        access: Optional[UpdateFolderByIdSharedLinkArgAccessField] = None,
        password: Optional[str] = None,
        vanity_name: Optional[str] = None,
        unshared_at: Optional[str] = None,
        permissions: Optional[UpdateFolderByIdSharedLinkArgPermissionsField] = None,
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
        :type access: Optional[UpdateFolderByIdSharedLinkArgAccessField], optional
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


class UpdateFolderByIdFolderUploadEmailArgAccessField(str, Enum):
    OPEN = 'open'
    COLLABORATORS = 'collaborators'


class UpdateFolderByIdFolderUploadEmailArg(BaseObject):
    def __init__(
        self,
        access: Optional[UpdateFolderByIdFolderUploadEmailArgAccessField] = None,
        **kwargs
    ):
        """
        :param access: When this parameter has been set, users can email files
            to the email address that has been automatically
            created for this folder.
            To create an email address, set this property either when
            creating or updating the folder.
            When set to `collaborators`, only emails from registered email
            addresses for collaborators will be accepted. This includes
            any email aliases a user might have registered.
            When set to `open` it will accept emails from any email
            address.
        :type access: Optional[UpdateFolderByIdFolderUploadEmailArgAccessField], optional
        """
        super().__init__(**kwargs)
        self.access = access


class UpdateFolderByIdCollectionsArg(BaseObject):
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


class GetFolderItemsSortArg(str, Enum):
    ID = 'id'
    NAME = 'name'
    DATE = 'date'
    SIZE = 'size'


class GetFolderItemsDirectionArg(str, Enum):
    ASC = 'ASC'
    DESC = 'DESC'


class CreateFolderParentArg(BaseObject):
    def __init__(self, id: str, **kwargs):
        """
        :param id: The ID of parent folder
        :type id: str
        """
        super().__init__(**kwargs)
        self.id = id


class CreateFolderFolderUploadEmailArgAccessField(str, Enum):
    OPEN = 'open'
    COLLABORATORS = 'collaborators'


class CreateFolderFolderUploadEmailArg(BaseObject):
    def __init__(
        self,
        access: Optional[CreateFolderFolderUploadEmailArgAccessField] = None,
        **kwargs
    ):
        """
        :param access: When this parameter has been set, users can email files
            to the email address that has been automatically
            created for this folder.
            To create an email address, set this property either when
            creating or updating the folder.
            When set to `collaborators`, only emails from registered email
            addresses for collaborators will be accepted. This includes
            any email aliases a user might have registered.
            When set to `open` it will accept emails from any email
            address.
        :type access: Optional[CreateFolderFolderUploadEmailArgAccessField], optional
        """
        super().__init__(**kwargs)
        self.access = access


class CreateFolderSyncStateArg(str, Enum):
    SYNCED = 'synced'
    NOT_SYNCED = 'not_synced'
    PARTIALLY_SYNCED = 'partially_synced'


class CopyFolderParentArg(BaseObject):
    def __init__(self, id: str, **kwargs):
        """
        :param id: The ID of parent folder
        :type id: str
        """
        super().__init__(**kwargs)
        self.id = id


class FoldersManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def get_folder_by_id(
        self,
        folder_id: str,
        fields: Optional[List[str]] = None,
        sort: Optional[GetFolderByIdSortArg] = None,
        direction: Optional[GetFolderByIdDirectionArg] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        if_none_match: Optional[str] = None,
        boxapi: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> FolderFull:
        """
        Retrieves details for a folder, including the first 100 entries

        in the folder.


        Passing `sort`, `direction`, `offset`, and `limit`


        parameters in query allows you to manage the


        list of returned


        [folder items](r://folder--full#param-item-collection).


        To fetch more items within the folder, use the


        [Get items in a folder](#get-folders-id-items) endpoint.

        :param folder_id: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folder_id: str
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
        :param sort: Defines the **second** attribute by which items
            are sorted.
            The folder type affects the way the items
            are sorted:
              * **Standard folder**:
              Items are always sorted by
              their `type` first, with
              folders listed before files,
              and files listed
              before web links.
              * **Root folder**:
              This parameter is not supported
              for marker-based pagination
              on the root folder
              (the folder with an `id` of `0`).
              * **Shared folder with parent path
              to the associated folder visible to
              the collaborator**:
              Items are always sorted by
              their `type` first, with
              folders listed before files,
              and files listed
              before web links.
        :type sort: Optional[GetFolderByIdSortArg], optional
        :param direction: The direction to sort results in. This can be either in alphabetical ascending
            (`ASC`) or descending (`DESC`) order.
        :type direction: Optional[GetFolderByIdDirectionArg], optional
        :param offset: The offset of the item at which to begin the response.
            Queries with offset parameter value
            exceeding 10000 will be rejected
            with a 400 response.
        :type offset: Optional[int], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
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
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params(
            {
                'fields': to_string(fields),
                'sort': to_string(sort),
                'direction': to_string(direction),
                'offset': to_string(offset),
                'limit': to_string(limit),
            }
        )
        headers_map: Dict[str, str] = prepare_params(
            {
                'if-none-match': to_string(if_none_match),
                'boxapi': to_string(boxapi),
                **extra_headers,
            }
        )
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/folders/', to_string(folder_id)]),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, FolderFull)

    def update_folder_by_id(
        self,
        folder_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        sync_state: Optional[UpdateFolderByIdSyncStateArg] = None,
        can_non_owners_invite: Optional[bool] = None,
        parent: Optional[UpdateFolderByIdParentArg] = None,
        shared_link: Optional[UpdateFolderByIdSharedLinkArg] = None,
        folder_upload_email: Optional[UpdateFolderByIdFolderUploadEmailArg] = None,
        tags: Optional[List[str]] = None,
        is_collaboration_restricted_to_enterprise: Optional[bool] = None,
        collections: Optional[List[UpdateFolderByIdCollectionsArg]] = None,
        can_non_owners_view_collaborators: Optional[bool] = None,
        fields: Optional[List[str]] = None,
        if_match: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> FolderFull:
        """
        Updates a folder. This can be also be used to move the folder,

        create shared links, update collaborations, and more.

        :param folder_id: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folder_id: str
        :param name: The optional new name for this folder.
        :type name: Optional[str], optional
        :param description: The optional description of this folder
        :type description: Optional[str], optional
        :param sync_state: Specifies whether a folder should be synced to a
            user's device or not. This is used by Box Sync
            (discontinued) and is not used by Box Drive.
        :type sync_state: Optional[UpdateFolderByIdSyncStateArg], optional
        :param can_non_owners_invite: Specifies if users who are not the owner
            of the folder can invite new collaborators to the folder.
        :type can_non_owners_invite: Optional[bool], optional
        :param parent: The parent folder for this folder. Use this to move
            the folder or to restore it out of the trash.
        :type parent: Optional[UpdateFolderByIdParentArg], optional
        :param tags: The tags for this item. These tags are shown in
            the Box web app and mobile apps next to an item.
            To add or remove a tag, retrieve the item's current tags,
            modify them, and then update this field.
            There is a limit of 100 tags per item, and 10,000
            unique tags per enterprise.
        :type tags: Optional[List[str]], optional
        :param is_collaboration_restricted_to_enterprise: Specifies if new invites to this folder are restricted to users
            within the enterprise. This does not affect existing
            collaborations.
        :type is_collaboration_restricted_to_enterprise: Optional[bool], optional
        :param collections: An array of collections to make this folder
            a member of. Currently
            we only support the `favorites` collection.
            To get the ID for a collection, use the
            [List all collections][1] endpoint.
            Passing an empty array `[]` or `null` will remove
            the folder from all collections.
            [1]: e://get-collections
        :type collections: Optional[List[UpdateFolderByIdCollectionsArg]], optional
        :param can_non_owners_view_collaborators: Restricts collaborators who are not the owner of
            this folder from viewing other collaborations on
            this folder.
            It also restricts non-owners from inviting new
            collaborators.
            When setting this field to `false`, it is required
            to also set `can_non_owners_invite_collaborators` to
            `false` if it has not already been set.
        :type can_non_owners_view_collaborators: Optional[bool], optional
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
            'sync_state': sync_state,
            'can_non_owners_invite': can_non_owners_invite,
            'parent': parent,
            'shared_link': shared_link,
            'folder_upload_email': folder_upload_email,
            'tags': tags,
            'is_collaboration_restricted_to_enterprise': (
                is_collaboration_restricted_to_enterprise
            ),
            'collections': collections,
            'can_non_owners_view_collaborators': can_non_owners_view_collaborators,
        }
        query_params_map: Dict[str, str] = prepare_params({'fields': to_string(fields)})
        headers_map: Dict[str, str] = prepare_params(
            {'if-match': to_string(if_match), **extra_headers}
        )
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/folders/', to_string(folder_id)]),
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
        return deserialize(response.text, FolderFull)

    def delete_folder_by_id(
        self,
        folder_id: str,
        recursive: Optional[bool] = None,
        if_match: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> None:
        """
        Deletes a folder, either permanently or by moving it to

        the trash.

        :param folder_id: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folder_id: str
        :param recursive: Delete a folder that is not empty by recursively deleting the
            folder and all of its content.
        :type recursive: Optional[bool], optional
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
        query_params_map: Dict[str, str] = prepare_params(
            {'recursive': to_string(recursive)}
        )
        headers_map: Dict[str, str] = prepare_params(
            {'if-match': to_string(if_match), **extra_headers}
        )
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/folders/', to_string(folder_id)]),
            FetchOptions(
                method='DELETE',
                params=query_params_map,
                headers=headers_map,
                response_format=None,
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return None

    def get_folder_items(
        self,
        folder_id: str,
        fields: Optional[List[str]] = None,
        usemarker: Optional[bool] = None,
        marker: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[GetFolderItemsSortArg] = None,
        direction: Optional[GetFolderItemsDirectionArg] = None,
        boxapi: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> Items:
        """
        Retrieves a page of items in a folder. These items can be files,

        folders, and web links.


        To request more information about the folder itself, like its size,


        use the [Get a folder](#get-folders-id) endpoint instead.

        :param folder_id: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folder_id: str
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
        :param usemarker: Specifies whether to use marker-based pagination instead of
            offset-based pagination. Only one pagination method can
            be used at a time.
            By setting this value to true, the API will return a `marker` field
            that can be passed as a parameter to this endpoint to get the next
            page of the response.
        :type usemarker: Optional[bool], optional
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        :param offset: The offset of the item at which to begin the response.
            Queries with offset parameter value
            exceeding 10000 will be rejected
            with a 400 response.
        :type offset: Optional[int], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        :param sort: Defines the **second** attribute by which items
            are sorted.
            The folder type affects the way the items
            are sorted:
              * **Standard folder**:
              Items are always sorted by
              their `type` first, with
              folders listed before files,
              and files listed
              before web links.
              * **Root folder**:
              This parameter is not supported
              for marker-based pagination
              on the root folder
              (the folder with an `id` of `0`).
              * **Shared folder with parent path
              to the associated folder visible to
              the collaborator**:
              Items are always sorted by
              their `type` first, with
              folders listed before files,
              and files listed
              before web links.
        :type sort: Optional[GetFolderItemsSortArg], optional
        :param direction: The direction to sort results in. This can be either in alphabetical ascending
            (`ASC`) or descending (`DESC`) order.
        :type direction: Optional[GetFolderItemsDirectionArg], optional
        :param boxapi: The URL, and optional password, for the shared link of this item.
            This header can be used to access items that have not been
            explicitly shared with a user.
            Use the format `shared_link=[link]` or if a password is required then
            use `shared_link=[link]&shared_link_password=[password]`.
            This header can be used on the file or folder shared, as well as on any files
            or folders nested within the item.
        :type boxapi: Optional[str], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params(
            {
                'fields': to_string(fields),
                'usemarker': to_string(usemarker),
                'marker': to_string(marker),
                'offset': to_string(offset),
                'limit': to_string(limit),
                'sort': to_string(sort),
                'direction': to_string(direction),
            }
        )
        headers_map: Dict[str, str] = prepare_params(
            {'boxapi': to_string(boxapi), **extra_headers}
        )
        response: FetchResponse = fetch(
            ''.join(
                ['https://api.box.com/2.0/folders/', to_string(folder_id), '/items']
            ),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, Items)

    def create_folder(
        self,
        name: str,
        parent: CreateFolderParentArg,
        folder_upload_email: Optional[CreateFolderFolderUploadEmailArg] = None,
        sync_state: Optional[CreateFolderSyncStateArg] = None,
        fields: Optional[List[str]] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> FolderFull:
        """
        Creates a new empty folder within the specified parent folder.
        :param name: The name for the new folder.
            There are some restrictions to the file name. Names containing
            non-printable ASCII characters, forward and backward slashes
            (`/`, `\`), as well as names with trailing spaces are
            prohibited.
            Additionally, the names `.` and `..` are
            not allowed either.
        :type name: str
        :param parent: The parent folder to create the new folder within.
        :type parent: CreateFolderParentArg
        :param sync_state: Specifies whether a folder should be synced to a
            user's device or not. This is used by Box Sync
            (discontinued) and is not used by Box Drive.
        :type sync_state: Optional[CreateFolderSyncStateArg], optional
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
        request_body = {
            'name': name,
            'parent': parent,
            'folder_upload_email': folder_upload_email,
            'sync_state': sync_state,
        }
        query_params_map: Dict[str, str] = prepare_params({'fields': to_string(fields)})
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/folders']),
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
        return deserialize(response.text, FolderFull)

    def copy_folder(
        self,
        folder_id: str,
        parent: CopyFolderParentArg,
        name: Optional[str] = None,
        fields: Optional[List[str]] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> FolderFull:
        """
        Creates a copy of a folder within a destination folder.

        The original folder will not be changed.

        :param folder_id: The unique identifier of the folder to copy.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder with the ID `0` can not be copied.
            Example: "0"
        :type folder_id: str
        :param parent: The destination folder to copy the folder to.
        :type parent: CopyFolderParentArg
        :param name: An optional new name for the copied folder.
            There are some restrictions to the file name. Names containing
            non-printable ASCII characters, forward and backward slashes
            (`/`, `\`), as well as names with trailing spaces are
            prohibited.
            Additionally, the names `.` and `..` are
            not allowed either.
        :type name: Optional[str], optional
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
        request_body = {'name': name, 'parent': parent}
        query_params_map: Dict[str, str] = prepare_params({'fields': to_string(fields)})
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                ['https://api.box.com/2.0/folders/', to_string(folder_id), '/copy']
            ),
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
        return deserialize(response.text, FolderFull)
