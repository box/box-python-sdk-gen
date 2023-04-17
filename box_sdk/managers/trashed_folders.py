from typing import Union

from box_sdk.base_object import BaseObject

from enum import Enum

from typing import List

import json

from box_sdk.schemas import FolderFull

from box_sdk.schemas import ClientError

from box_sdk.schemas import TrashFolderRestored

from box_sdk.schemas import TrashFolder

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.jwt_auth import JWTAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetFolderByIdOptionsArg(BaseObject):
    def __init__(self, fields: Union[None, str] = None, if_none_match: Union[None, str] = None, boxapi: Union[None, str] = None, **kwargs):
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
        """
        super().__init__(**kwargs)
        self.fields = fields
        self.if_none_match = if_none_match
        self.boxapi = boxapi

class RestoreFolderFromTrashRequestBodyArgParentField(BaseObject):
    def __init__(self, id: Union[None, str] = None, **kwargs):
        """
        :param id: The ID of parent item
        :type id: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.id = id

class RestoreFolderFromTrashRequestBodyArg(BaseObject):
    def __init__(self, name: Union[None, str] = None, parent: Union[None, RestoreFolderFromTrashRequestBodyArgParentField] = None, **kwargs):
        """
        :param name: An optional new name for the folder.
        :type name: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.name = name
        self.parent = parent

class RestoreFolderFromTrashOptionsArg(BaseObject):
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

class UpdateFolderByIdRequestBodyArgSyncStateField(str, Enum):
    SYNCED = 'synced'
    NOT_SYNCED = 'not_synced'
    PARTIALLY_SYNCED = 'partially_synced'

class UpdateFolderByIdRequestBodyArgParentField(BaseObject):
    def __init__(self, id: Union[None, str] = None, **kwargs):
        """
        :param id: The ID of the new parent folder
        :type id: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.id = id

class UpdateFolderByIdRequestBodyArgSharedLinkFieldAccessField(str, Enum):
    OPEN = 'open'
    COMPANY = 'company'
    COLLABORATORS = 'collaborators'

class UpdateFolderByIdRequestBodyArgSharedLinkFieldPermissionsField(BaseObject):
    def __init__(self, can_download: Union[None, bool] = None, **kwargs):
        """
        :param can_download: If the shared link allows for downloading of files.
            This can only be set when `access` is set to
            `open` or `company`.
        :type can_download: Union[None, bool], optional
        """
        super().__init__(**kwargs)
        self.can_download = can_download

class UpdateFolderByIdRequestBodyArgSharedLinkField(BaseObject):
    def __init__(self, access: Union[None, UpdateFolderByIdRequestBodyArgSharedLinkFieldAccessField] = None, password: Union[None, str] = None, vanity_name: Union[None, str] = None, unshared_at: Union[None, str] = None, permissions: Union[None, UpdateFolderByIdRequestBodyArgSharedLinkFieldPermissionsField] = None, **kwargs):
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
        :type access: Union[None, UpdateFolderByIdRequestBodyArgSharedLinkFieldAccessField], optional
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

class UpdateFolderByIdRequestBodyArgFolderUploadEmailFieldAccessField(str, Enum):
    OPEN = 'open'
    COLLABORATORS = 'collaborators'

class UpdateFolderByIdRequestBodyArgFolderUploadEmailField(BaseObject):
    def __init__(self, access: Union[None, UpdateFolderByIdRequestBodyArgFolderUploadEmailFieldAccessField] = None, **kwargs):
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
        :type access: Union[None, UpdateFolderByIdRequestBodyArgFolderUploadEmailFieldAccessField], optional
        """
        super().__init__(**kwargs)
        self.access = access

class UpdateFolderByIdRequestBodyArgCollectionsField(BaseObject):
    def __init__(self, id: Union[None, str] = None, type: Union[None, str] = None, **kwargs):
        """
        :param id: The unique identifier for this object
        :type id: Union[None, str], optional
        :param type: The type for this object
        :type type: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type

class UpdateFolderByIdRequestBodyArg(BaseObject):
    def __init__(self, name: Union[None, str] = None, description: Union[None, str] = None, sync_state: Union[None, UpdateFolderByIdRequestBodyArgSyncStateField] = None, can_non_owners_invite: Union[None, bool] = None, parent: Union[None, UpdateFolderByIdRequestBodyArgParentField] = None, shared_link: Union[None, UpdateFolderByIdRequestBodyArgSharedLinkField] = None, folder_upload_email: Union[None, UpdateFolderByIdRequestBodyArgFolderUploadEmailField] = None, tags: Union[None, List[str]] = None, is_collaboration_restricted_to_enterprise: Union[None, bool] = None, collections: Union[None, List[UpdateFolderByIdRequestBodyArgCollectionsField]] = None, can_non_owners_view_collaborators: Union[None, bool] = None, **kwargs):
        """
        :param name: The optional new name for this folder.
        :type name: Union[None, str], optional
        :param description: The optional description of this folder
        :type description: Union[None, str], optional
        :param sync_state: Specifies whether a folder should be synced to a
            user's device or not. This is used by Box Sync
            (discontinued) and is not used by Box Drive.
        :type sync_state: Union[None, UpdateFolderByIdRequestBodyArgSyncStateField], optional
        :param can_non_owners_invite: Specifies if users who are not the owner
            of the folder can invite new collaborators to the folder.
        :type can_non_owners_invite: Union[None, bool], optional
        :param parent: The parent folder for this folder. Use this to move
            the folder or to restore it out of the trash.
        :type parent: Union[None, UpdateFolderByIdRequestBodyArgParentField], optional
        :param tags: The tags for this item. These tags are shown in
            the Box web app and mobile apps next to an item.
            To add or remove a tag, retrieve the item's current tags,
            modify them, and then update this field.
            There is a limit of 100 tags per item, and 10,000
            unique tags per enterprise.
        :type tags: Union[None, List[str]], optional
        :param is_collaboration_restricted_to_enterprise: Specifies if new invites to this folder are restricted to users
            within the enterprise. This does not affect existing
            collaborations.
        :type is_collaboration_restricted_to_enterprise: Union[None, bool], optional
        :param collections: An array of collections to make this folder
            a member of. Currently
            we only support the `favorites` collection.
            To get the ID for a collection, use the
            [List all collections][1] endpoint.
            Passing an empty array `[]` or `null` will remove
            the folder from all collections.
            [1]: ../advanced-files-and-folders/#get-collections
        :type collections: Union[None, List[UpdateFolderByIdRequestBodyArgCollectionsField]], optional
        :param can_non_owners_view_collaborators: Restricts collaborators who are not the owner of
            this folder from viewing other collaborations on
            this folder.
            It also restricts non-owners from inviting new
            collaborators.
            When setting this field to `false`, it is required
            to also set `can_non_owners_invite_collaborators` to
            `false` if it has not already been set.
        :type can_non_owners_view_collaborators: Union[None, bool], optional
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

class DeleteFolderByIdOptionsArg(BaseObject):
    def __init__(self, if_match: Union[None, str] = None, recursive: Union[None, bool] = None, **kwargs):
        """
        :param if_match: Ensures this item hasn't recently changed before
            making changes.
            Pass in the item's last observed `etag` value
            into this header and the endpoint will fail
            with a `412 Precondition Failed` if it
            has changed since.
        :type if_match: Union[None, str], optional
        :param recursive: Delete a folder that is not empty by recursively deleting the
            folder and all of its content.
        :type recursive: Union[None, bool], optional
        """
        super().__init__(**kwargs)
        self.if_match = if_match
        self.recursive = recursive

class GetFolderTrashOptionsArg(BaseObject):
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

class TrashedFoldersManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth, JWTAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
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
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id]), FetchOptions(method='GET', params={'fields': options.fields}, headers={'if-none-match': options.if_none_match, 'boxapi': options.boxapi}, auth=self.auth))
        return FolderFull.from_dict(json.loads(response.text))
    def restore_folder_from_trash(self, folder_id: str, request_body: RestoreFolderFromTrashRequestBodyArg, options: RestoreFolderFromTrashOptionsArg = None) -> TrashFolderRestored:
        """
        Restores a folder that has been moved to the trash.
        
        An optional new parent ID can be provided to restore the folder to in case the

        
        original folder has been deleted.

        
        # Folder locking

        
        During this operation, part of the file tree will be locked, mainly

        
        the source folder and all of its descendants, as well as the destination

        
        folder.

        
        For the duration of the operation, no other move, copy, delete, or restore

        
        operation can performed on any of the locked folders.

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
            options = RestoreFolderFromTrashOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id]), FetchOptions(method='POST', params={'fields': options.fields}, body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth))
        return TrashFolderRestored.from_dict(json.loads(response.text))
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
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id]), FetchOptions(method='PUT', params={'fields': options.fields}, headers={'if-match': options.if_match}, body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth))
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
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id]), FetchOptions(method='DELETE', params={'recursive': options.recursive}, headers={'if-match': options.if_match}, auth=self.auth))
        return response.content
    def get_folder_trash(self, folder_id: str, options: GetFolderTrashOptionsArg = None) -> TrashFolder:
        """
        Retrieves a folder that has been moved to the trash.
        
        Please note that only if the folder itself has been moved to the

        
        trash can it be retrieved with this API call. If instead one of

        
        its parent folders was moved to the trash, only that folder

        
        can be inspected using the

        
        [`GET /folders/:id/trash`](e://get_folders_id_trash) API.

        
        To list all items that have been moved to the trash, please

        
        use the [`GET /folders/trash/items`](e://get-folders-trash-items/)

        
        API.

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
            options = GetFolderTrashOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/trash']), FetchOptions(method='GET', params={'fields': options.fields}, auth=self.auth))
        return TrashFolder.from_dict(json.loads(response.text))
    def delete_folder_trash(self, folder_id: str):
        """
        Permanently deletes a folder that is in the trash.
        
        This action cannot be undone.

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
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/trash']), FetchOptions(method='DELETE', auth=self.auth))
        return response.content