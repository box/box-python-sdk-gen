from typing import Optional

from box_sdk.base_object import BaseObject

from enum import Enum

from typing import List

import json

from box_sdk.schemas import FolderFull

from box_sdk.schemas import ClientError

from box_sdk.schemas import Items

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetFolderByIdOptionsArg(BaseObject):
    def __init__(self, fields: Optional[str] = None, if_none_match: Optional[str] = None, boxapi: Optional[str] = None, **kwargs):
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
        :type fields: Optional[str], optional
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
        """
        super().__init__(**kwargs)
        self.fields = fields
        self.if_none_match = if_none_match
        self.boxapi = boxapi

class UpdateFolderByIdRequestBodyArgSyncStateField(str, Enum):
    SYNCED = 'synced'
    NOT_SYNCED = 'not_synced'
    PARTIALLY_SYNCED = 'partially_synced'

class UpdateFolderByIdRequestBodyArgParentField(BaseObject):
    def __init__(self, id: Optional[str] = None, **kwargs):
        """
        :param id: The ID of the new parent folder
        :type id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id

class UpdateFolderByIdRequestBodyArgSharedLinkFieldAccessField(str, Enum):
    OPEN = 'open'
    COMPANY = 'company'
    COLLABORATORS = 'collaborators'

class UpdateFolderByIdRequestBodyArgSharedLinkFieldPermissionsField(BaseObject):
    def __init__(self, can_download: Optional[bool] = None, **kwargs):
        """
        :param can_download: If the shared link allows for downloading of files.
            This can only be set when `access` is set to
            `open` or `company`.
        :type can_download: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.can_download = can_download

class UpdateFolderByIdRequestBodyArgSharedLinkField(BaseObject):
    def __init__(self, access: Optional[UpdateFolderByIdRequestBodyArgSharedLinkFieldAccessField] = None, password: Optional[str] = None, vanity_name: Optional[str] = None, unshared_at: Optional[str] = None, permissions: Optional[UpdateFolderByIdRequestBodyArgSharedLinkFieldPermissionsField] = None, **kwargs):
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
        :type access: Optional[UpdateFolderByIdRequestBodyArgSharedLinkFieldAccessField], optional
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

class UpdateFolderByIdRequestBodyArgFolderUploadEmailFieldAccessField(str, Enum):
    OPEN = 'open'
    COLLABORATORS = 'collaborators'

class UpdateFolderByIdRequestBodyArgFolderUploadEmailField(BaseObject):
    def __init__(self, access: Optional[UpdateFolderByIdRequestBodyArgFolderUploadEmailFieldAccessField] = None, **kwargs):
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
        :type access: Optional[UpdateFolderByIdRequestBodyArgFolderUploadEmailFieldAccessField], optional
        """
        super().__init__(**kwargs)
        self.access = access

class UpdateFolderByIdRequestBodyArgCollectionsField(BaseObject):
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

class UpdateFolderByIdRequestBodyArg(BaseObject):
    def __init__(self, name: Optional[str] = None, description: Optional[str] = None, sync_state: Optional[UpdateFolderByIdRequestBodyArgSyncStateField] = None, can_non_owners_invite: Optional[bool] = None, parent: Optional[UpdateFolderByIdRequestBodyArgParentField] = None, shared_link: Optional[UpdateFolderByIdRequestBodyArgSharedLinkField] = None, folder_upload_email: Optional[UpdateFolderByIdRequestBodyArgFolderUploadEmailField] = None, tags: Optional[List[str]] = None, is_collaboration_restricted_to_enterprise: Optional[bool] = None, collections: Optional[List[UpdateFolderByIdRequestBodyArgCollectionsField]] = None, can_non_owners_view_collaborators: Optional[bool] = None, **kwargs):
        """
        :param name: The optional new name for this folder.
        :type name: Optional[str], optional
        :param description: The optional description of this folder
        :type description: Optional[str], optional
        :param sync_state: Specifies whether a folder should be synced to a
            user's device or not. This is used by Box Sync
            (discontinued) and is not used by Box Drive.
        :type sync_state: Optional[UpdateFolderByIdRequestBodyArgSyncStateField], optional
        :param can_non_owners_invite: Specifies if users who are not the owner
            of the folder can invite new collaborators to the folder.
        :type can_non_owners_invite: Optional[bool], optional
        :param parent: The parent folder for this folder. Use this to move
            the folder or to restore it out of the trash.
        :type parent: Optional[UpdateFolderByIdRequestBodyArgParentField], optional
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
            [1]: ../advanced-files-and-folders/#get-collections
        :type collections: Optional[List[UpdateFolderByIdRequestBodyArgCollectionsField]], optional
        :param can_non_owners_view_collaborators: Restricts collaborators who are not the owner of
            this folder from viewing other collaborations on
            this folder.
            It also restricts non-owners from inviting new
            collaborators.
            When setting this field to `false`, it is required
            to also set `can_non_owners_invite_collaborators` to
            `false` if it has not already been set.
        :type can_non_owners_view_collaborators: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self.sync_state = sync_state
        self.can_non_owners_invite = can_non_owners_invite
        self.parent = parent
        self.shared_link = shared_link
        self.folder_upload_email = folder_upload_email
        self.tags = tags
        self.is_collaboration_restricted_to_enterprise = is_collaboration_restricted_to_enterprise
        self.collections = collections
        self.can_non_owners_view_collaborators = can_non_owners_view_collaborators

class UpdateFolderByIdOptionsArg(BaseObject):
    def __init__(self, fields: Optional[str] = None, if_match: Optional[str] = None, **kwargs):
        """
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[str], optional
        :param if_match: Ensures this item hasn't recently changed before
            making changes.
            Pass in the item's last observed `etag` value
            into this header and the endpoint will fail
            with a `412 Precondition Failed` if it
            has changed since.
        :type if_match: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.fields = fields
        self.if_match = if_match

class DeleteFolderByIdOptionsArg(BaseObject):
    def __init__(self, if_match: Optional[str] = None, recursive: Optional[bool] = None, **kwargs):
        """
        :param if_match: Ensures this item hasn't recently changed before
            making changes.
            Pass in the item's last observed `etag` value
            into this header and the endpoint will fail
            with a `412 Precondition Failed` if it
            has changed since.
        :type if_match: Optional[str], optional
        :param recursive: Delete a folder that is not empty by recursively deleting the
            folder and all of its content.
        :type recursive: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.if_match = if_match
        self.recursive = recursive

class GetFolderItemsOptionsArgSortField(str, Enum):
    ID = 'id'
    NAME = 'name'
    DATE = 'date'
    SIZE = 'size'

class GetFolderItemsOptionsArgDirectionField(str, Enum):
    ASC = 'ASC'
    DESC = 'DESC'

class GetFolderItemsOptionsArg(BaseObject):
    def __init__(self, fields: Optional[str] = None, usemarker: Optional[bool] = None, marker: Optional[str] = None, offset: Optional[int] = None, limit: Optional[int] = None, boxapi: Optional[str] = None, sort: Optional[GetFolderItemsOptionsArgSortField] = None, direction: Optional[GetFolderItemsOptionsArgDirectionField] = None, **kwargs):
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
        :type fields: Optional[str], optional
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
        :param boxapi: The URL, and optional password, for the shared link of this item.
            This header can be used to access items that have not been
            explicitly shared with a user.
            Use the format `shared_link=[link]` or if a password is required then
            use `shared_link=[link]&shared_link_password=[password]`.
            This header can be used on the file or folder shared, as well as on any files
            or folders nested within the item.
        :type boxapi: Optional[str], optional
        :param sort: Defines the **second** attribute by which items
            are sorted.
            The folder type affects the way the items
            are sorted:
            * **Standard folder**:
              Items are always sorted by their `type` first, with
              folders listed before files, and files listed
              before web links.
            * **Root folder**:
              This parameter is not supported for marker-based pagination
              on the root folder (the folder with an `id` of `0`).
            * **Shared folder with parent path to the associated folder visible to the collaborator**:
              Items are always sorted by their `type` first, with
              folders listed before files, and files listed
              before web links.
        :type sort: Optional[GetFolderItemsOptionsArgSortField], optional
        :param direction: The direction to sort results in. This can be either in alphabetical ascending
            (`ASC`) or descending (`DESC`) order.
        :type direction: Optional[GetFolderItemsOptionsArgDirectionField], optional
        """
        super().__init__(**kwargs)
        self.fields = fields
        self.usemarker = usemarker
        self.marker = marker
        self.offset = offset
        self.limit = limit
        self.boxapi = boxapi
        self.sort = sort
        self.direction = direction

class CreateFolderRequestBodyArgParentField(BaseObject):
    def __init__(self, id: str, **kwargs):
        """
        :param id: The ID of parent folder
        :type id: str
        """
        super().__init__(**kwargs)
        self.id = id

class CreateFolderRequestBodyArgFolderUploadEmailFieldAccessField(str, Enum):
    OPEN = 'open'
    COLLABORATORS = 'collaborators'

class CreateFolderRequestBodyArgFolderUploadEmailField(BaseObject):
    def __init__(self, access: Optional[CreateFolderRequestBodyArgFolderUploadEmailFieldAccessField] = None, **kwargs):
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
        :type access: Optional[CreateFolderRequestBodyArgFolderUploadEmailFieldAccessField], optional
        """
        super().__init__(**kwargs)
        self.access = access

class CreateFolderRequestBodyArgSyncStateField(str, Enum):
    SYNCED = 'synced'
    NOT_SYNCED = 'not_synced'
    PARTIALLY_SYNCED = 'partially_synced'

class CreateFolderRequestBodyArg(BaseObject):
    def __init__(self, name: str, parent: CreateFolderRequestBodyArgParentField, folder_upload_email: Optional[CreateFolderRequestBodyArgFolderUploadEmailField] = None, sync_state: Optional[CreateFolderRequestBodyArgSyncStateField] = None, **kwargs):
        """
        :param name: The name for the new folder.
            There are some restrictions to the file name. Names containing
            non-printable ASCII characters, forward and backward slashes
            (`/`, `\`), as well as names with trailing spaces are
            prohibited.
            Additionally, the names `.` and `..` are
            not allowed either.
        :type name: str
        :param parent: The parent folder to create the new folder within.
        :type parent: CreateFolderRequestBodyArgParentField
        :param sync_state: Specifies whether a folder should be synced to a
            user's device or not. This is used by Box Sync
            (discontinued) and is not used by Box Drive.
        :type sync_state: Optional[CreateFolderRequestBodyArgSyncStateField], optional
        """
        super().__init__(**kwargs)
        self.name = name
        self.parent = parent
        self.folder_upload_email = folder_upload_email
        self.sync_state = sync_state

class CreateFolderOptionsArg(BaseObject):
    def __init__(self, fields: Optional[str] = None, **kwargs):
        """
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
        self.fields = fields

class CopyFolderRequestBodyArgParentField(BaseObject):
    def __init__(self, id: str, **kwargs):
        """
        :param id: The ID of parent folder
        :type id: str
        """
        super().__init__(**kwargs)
        self.id = id

class CopyFolderRequestBodyArg(BaseObject):
    def __init__(self, parent: CopyFolderRequestBodyArgParentField, name: Optional[str] = None, **kwargs):
        """
        :param parent: The destination folder to copy the folder to.
        :type parent: CopyFolderRequestBodyArgParentField
        :param name: An optional new name for the copied folder.
            There are some restrictions to the file name. Names containing
            non-printable ASCII characters, forward and backward slashes
            (`/`, `\`), as well as names with trailing spaces are
            prohibited.
            Additionally, the names `.` and `..` are
            not allowed either.
        :type name: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.parent = parent
        self.name = name

class CopyFolderOptionsArg(BaseObject):
    def __init__(self, fields: Optional[str] = None, **kwargs):
        """
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
        self.fields = fields

class FoldersManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def get_folder_by_id(self, folder_id: str, options: GetFolderByIdOptionsArg = None) -> FolderFull:
        """
        Retrieves details for a folder, including the first 100 entries
        
        in the folder.

        
        To fetch more items within the folder, please use the

        
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
        """
        if options is None:
            options = GetFolderByIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id]), FetchOptions(method='GET', params={'fields': options.fields}, headers={'if-none-match': options.if_none_match, 'boxapi': options.boxapi}, auth=self.auth, network_session=self.network_session))
        return FolderFull.from_dict(json.loads(response.text))
    def update_folder_by_id(self, folder_id: str, request_body: UpdateFolderByIdRequestBodyArg, options: UpdateFolderByIdOptionsArg = None) -> FolderFull:
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
        """
        if options is None:
            options = UpdateFolderByIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id]), FetchOptions(method='PUT', params={'fields': options.fields}, headers={'if-match': options.if_match}, body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return FolderFull.from_dict(json.loads(response.text))
    def delete_folder_by_id(self, folder_id: str, options: DeleteFolderByIdOptionsArg = None):
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
        """
        if options is None:
            options = DeleteFolderByIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id]), FetchOptions(method='DELETE', params={'recursive': options.recursive}, headers={'if-match': options.if_match}, auth=self.auth, network_session=self.network_session))
        return response.content
    def get_folder_items(self, folder_id: str, options: GetFolderItemsOptionsArg = None) -> Items:
        """
        Retrieves a page of items in a folder. These items can be files,
        
        folders, and web links.

        
        To request more information about the folder itself, like its size,

        
        please use the [Get a folder](#get-folders-id) endpoint instead.

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
        """
        if options is None:
            options = GetFolderItemsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/items']), FetchOptions(method='GET', params={'fields': options.fields, 'usemarker': options.usemarker, 'marker': options.marker, 'offset': options.offset, 'limit': options.limit, 'sort': options.sort, 'direction': options.direction}, headers={'boxapi': options.boxapi}, auth=self.auth, network_session=self.network_session))
        return Items.from_dict(json.loads(response.text))
    def create_folder(self, request_body: CreateFolderRequestBodyArg, options: CreateFolderOptionsArg = None) -> FolderFull:
        """
        Creates a new empty folder within the specified parent folder.
        """
        if options is None:
            options = CreateFolderOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders']), FetchOptions(method='POST', params={'fields': options.fields}, body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return FolderFull.from_dict(json.loads(response.text))
    def copy_folder(self, folder_id: str, request_body: CopyFolderRequestBodyArg, options: CopyFolderOptionsArg = None) -> FolderFull:
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
        """
        if options is None:
            options = CopyFolderOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/copy']), FetchOptions(method='POST', params={'fields': options.fields}, body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return FolderFull.from_dict(json.loads(response.text))