from enum import Enum

from typing import Union

from base_object import BaseObject

from json import isJSON, JSON

from typing import List

class ClientErrorCodeField(str, Enum):
    CREATED = 'created'
    ACCEPTED = 'accepted'
    NO_CONTENT = 'no_content'
    REDIRECT = 'redirect'
    NOT_MODIFIED = 'not_modified'
    BAD_REQUEST = 'bad_request'
    UNAUTHORIZED = 'unauthorized'
    FORBIDDEN = 'forbidden'
    NOT_FOUND = 'not_found'
    METHOD_NOT_ALLOWED = 'method_not_allowed'
    CONFLICT = 'conflict'
    PRECONDITION_FAILED = 'precondition_failed'
    TOO_MANY_REQUESTS = 'too_many_requests'
    INTERNAL_SERVER_ERROR = 'internal_server_error'
    UNAVAILABLE = 'unavailable'
    ITEM_NAME_INVALID = 'item_name_invalid'
    INSUFFICIENT_SCOPE = 'insufficient_scope'

def deserializeClientErrorCodeField(value: Union[None, JSON] = None) -> Union[None, ClientErrorCodeField]:
    if value == None:
        return None
    return value

def serializeClientErrorCodeField(value: Union[None, ClientErrorCodeField] = None) -> Union[None, JSON]:
    if value == None:
        return None
    return value

class ClientErrorContextInfoField(BaseObject):
    def __init__(self, message: Union[None, str] = None, **kwargs):
        """
        :param message: More details on the error.
        :type message: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.message = message

def deserializeClientErrorContextInfoField(value: Union[None, JSON] = None) -> Union[None, ClientErrorContextInfoField]:
    if value == None:
        return None
    if not isJSON(value, 'object'):
        raise Exception('Expecting an object for "ClientErrorContextInfoField"')
    return ClientErrorContextInfoField(message=value['message'])

def serializeClientErrorContextInfoField(value: Union[None, ClientErrorContextInfoField] = None) -> Union[None, JSON]:
    if value == None:
        return None
    return {'message': value.message}

class ClientError(BaseObject):
    def __init__(self, type: Union[None, str] = None, status: Union[None, int] = None, code: Union[None, ClientErrorCodeField] = None, message: Union[None, str] = None, context_info: Union[None, ClientErrorContextInfoField] = None, help_url: Union[None, str] = None, request_id: Union[None, str] = None, **kwargs):
        """
        :param type: `error`
        :type type: Union[None, str], optional
        :param status: The HTTP status of the response.
        :type status: Union[None, int], optional
        :param code: A Box-specific error code
        :type code: Union[None, ClientErrorCodeField], optional
        :param message: A short message describing the error.
        :type message: Union[None, str], optional
        :param context_info: A free-form object that contains additional context
            about the error. The possible fields are defined on
            a per-endpoint basis. `message` is only one example.
        :type context_info: Union[None, ClientErrorContextInfoField], optional
        :param help_url: A URL that links to more information about why this error occurred.
        :type help_url: Union[None, str], optional
        :param request_id: A unique identifier for this response, which can be used
            when contacting Box support.
        :type request_id: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.status = status
        self.code = code
        self.message = message
        self.context_info = context_info
        self.help_url = help_url
        self.request_id = request_id

def deserializeClientError(value: Union[None, JSON] = None) -> Union[None, ClientError]:
    if value == None:
        return None
    if not isJSON(value, 'object'):
        raise Exception('Expecting an object for "ClientError"')
    return ClientError(type=value['type'], status=value['status'], code=deserializeClientErrorCodeField(value['code']), message=value['message'], contextInfo=deserializeClientErrorContextInfoField(value['context_info']), helpUrl=value['help_url'], requestId=value['request_id'])

def serializeClientError(value: Union[None, ClientError] = None) -> Union[None, JSON]:
    if value == None:
        return None
    return {'type': value.type, 'status': value.status, 'code': serializeClientErrorCodeField(value.code), 'message': value.message, 'context_info': serializeClientErrorContextInfoField(value.contextInfo), 'help_url': value.helpUrl, 'request_id': value.requestId}

class FileSharedLinkFieldAccessField(str, Enum):
    OPEN = 'open'
    COMPANY = 'company'
    COLLABORATORS = 'collaborators'

class FileSharedLinkFieldEffectiveAccessField(str, Enum):
    OPEN = 'open'
    COMPANY = 'company'
    COLLABORATORS = 'collaborators'

class FileSharedLinkFieldEffectivePermissionField(str, Enum):
    CAN_EDIT = 'can_edit'
    CAN_DOWNLOAD = 'can_download'
    CAN_PREVIEW = 'can_preview'
    NO_ACCESS = 'no_access'

class FileSharedLinkFieldPermissionsField(BaseObject):
    def __init__(self, can_download: bool, can_preview: bool, can_edit: bool, **kwargs):
        """
        :param can_download: Defines if the shared link allows for the item to be downloaded. For
            shared links on folders, this also applies to any items in the folder.
            This value can be set to `true` when the effective access level is
            set to `open` or `company`, not `collaborators`.
        :type can_download: bool
        :param can_preview: Defines if the shared link allows for the item to be previewed.
            This value is always `true`. For shared links on folders this also
            applies to any items in the folder.
        :type can_preview: bool
        :param can_edit: Defines if the shared link allows for the item to be edited.
            This value can only be `true` if `can_download` is also `true` and if
            the item has a type of `file`.
        :type can_edit: bool
        """
        super().__init__(**kwargs)
        self.can_download = can_download
        self.can_preview = can_preview
        self.can_edit = can_edit

class FileSharedLinkField(BaseObject):
    def __init__(self, url: str, effective_access: FileSharedLinkFieldEffectiveAccessField, effective_permission: FileSharedLinkFieldEffectivePermissionField, is_password_enabled: bool, download_count: int, preview_count: int, download_url: Union[None, str] = None, vanity_url: Union[None, str] = None, vanity_name: Union[None, str] = None, access: Union[None, FileSharedLinkFieldAccessField] = None, unshared_at: Union[None, str] = None, permissions: Union[None, FileSharedLinkFieldPermissionsField] = None, **kwargs):
        """
        :param url: The URL that can be used to access the item on Box.
            This URL will display the item in Box's preview UI where the file
            can be downloaded if allowed.
            This URL will continue to work even when a custom `vanity_url`
            has been set for this shared link.
        :type url: str
        :param effective_access: The effective access level for the shared link. This can be a more
            restrictive access level than the value in the `access` field when the
            enterprise settings restrict the allowed access levels.
        :type effective_access: FileSharedLinkFieldEffectiveAccessField
        :param effective_permission: The effective permissions for this shared link.
            These result in the more restrictive combination of
            the share link permissions and the item permissions set
            by the administrator, the owner, and any ancestor item
            such as a folder.
        :type effective_permission: FileSharedLinkFieldEffectivePermissionField
        :param is_password_enabled: Defines if the shared link requires a password to access the item.
        :type is_password_enabled: bool
        :param download_count: The number of times this item has been downloaded.
        :type download_count: int
        :param preview_count: The number of times this item has been previewed.
        :type preview_count: int
        :param download_url: A URL that can be used to download the file. This URL can be used in
            a browser to download the file. This URL includes the file
            extension so that the file will be saved with the right file type.
            This property will be `null` for folders.
        :type download_url: Union[None, str], optional
        :param vanity_url: The "Custom URL" that can also be used to preview the item on Box.  Custom
            URLs can only be created or modified in the Box Web application.
        :type vanity_url: Union[None, str], optional
        :param vanity_name: The custom name of a shared link, as used in the `vanity_url` field.
        :type vanity_name: Union[None, str], optional
        :param access: The access level for this shared link.
            * `open` - provides access to this item to anyone with this link
            * `company` - only provides access to this item to people the same company
            * `collaborators` - only provides access to this item to people who are
               collaborators on this item
            If this field is omitted when creating the shared link, the access level
            will be set to the default access level specified by the enterprise admin.
        :type access: Union[None, FileSharedLinkFieldAccessField], optional
        :param unshared_at: The date and time when this link will be unshared. This field can only be
            set by users with paid accounts.
        :type unshared_at: Union[None, str], optional
        :param permissions: Defines if this link allows a user to preview, edit, and download an item.
            These permissions refer to the shared link only and
            do not supersede permissions applied to the item itself.
        :type permissions: Union[None, FileSharedLinkFieldPermissionsField], optional
        """
        super().__init__(**kwargs)
        self.url = url
        self.effective_access = effective_access
        self.effective_permission = effective_permission
        self.is_password_enabled = is_password_enabled
        self.download_count = download_count
        self.preview_count = preview_count
        self.download_url = download_url
        self.vanity_url = vanity_url
        self.vanity_name = vanity_name
        self.access = access
        self.unshared_at = unshared_at
        self.permissions = permissions

class FileItemStatusField(str, Enum):
    ACTIVE = 'active'
    TRASHED = 'trashed'
    DELETED = 'deleted'

class FileBase(BaseObject):
    def __init__(self, id: str, type: str, etag: Union[None, str] = None, **kwargs):
        """
        :param id: The unique identifier that represent a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
        :type id: str
        :param type: `file`
        :type type: str
        :param etag: The HTTP `etag` of this file. This can be used within some API
            endpoints in the `If-Match` and `If-None-Match` headers to only
            perform changes on the file if (no) changes have happened.
        :type etag: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.etag = etag

def deserializeFileBase(value: Union[None, JSON] = None) -> Union[None, FileBase]:
    if value == None:
        return None
    if not isJSON(value, 'object'):
        raise Exception('Expecting an object for "FileBase"')
    return FileBase(id=value['id'], etag=value['etag'], type=value['type'])

def serializeFileBase(value: Union[None, FileBase] = None) -> Union[None, JSON]:
    if value == None:
        return None
    return {'id': value.id, 'etag': value.etag, 'type': value.type}

class FileVersionBase(BaseObject):
    def __init__(self, id: str, type: str, **kwargs):
        """
        :param id: The unique identifier that represent a file version.
        :type id: str
        :param type: `file_version`
        :type type: str
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type

def deserializeFileVersionBase(value: Union[None, JSON] = None) -> Union[None, FileVersionBase]:
    if value == None:
        return None
    if not isJSON(value, 'object'):
        raise Exception('Expecting an object for "FileVersionBase"')
    return FileVersionBase(id=value['id'], type=value['type'])

def serializeFileVersionBase(value: Union[None, FileVersionBase] = None) -> Union[None, JSON]:
    if value == None:
        return None
    return {'id': value.id, 'type': value.type}

class FileVersionMini(FileVersionBase):
    def __init__(self, id: str, type: str, sha1: Union[None, str] = None, **kwargs):
        """
        :param id: The unique identifier that represent a file version.
        :type id: str
        :param type: `file_version`
        :type type: str
        :param sha1: The SHA1 hash of this version of the file.
        :type sha1: Union[None, str], optional
        """
        super().__init__(id=id, type=type, **kwargs)
        self.sha1 = sha1

def deserializeFileVersionMini(value: Union[None, JSON] = None) -> Union[None, FileVersionMini]:
    if value == None:
        return None
    return value

def serializeFileVersionMini(value: Union[None, FileVersionMini] = None) -> Union[None, JSON]:
    if value == None:
        return None
    return {**serializeFileVersionBase(value), **{'sha1': value.sha1}}

class FileMini(FileBase):
    def __init__(self, sequence_id: str, sha1: str, id: str, type: str, name: Union[None, str] = None, file_version: Union[None, FileVersionMini] = None, etag: Union[None, str] = None, **kwargs):
        """
        :param sha1: The SHA1 hash of the file. This can be used to compare the contents
            of a file on Box with a local file.
        :type sha1: str
        :param id: The unique identifier that represent a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
        :type id: str
        :param type: `file`
        :type type: str
        :param name: The name of the file
        :type name: Union[None, str], optional
        :param etag: The HTTP `etag` of this file. This can be used within some API
            endpoints in the `If-Match` and `If-None-Match` headers to only
            perform changes on the file if (no) changes have happened.
        :type etag: Union[None, str], optional
        """
        super().__init__(id=id, type=type, etag=etag, **kwargs)
        self.sequence_id = sequence_id
        self.sha1 = sha1
        self.name = name
        self.file_version = file_version

def deserializeFileMini(value: Union[None, JSON] = None) -> Union[None, FileMini]:
    if value == None:
        return None
    return value

def serializeFileMini(value: Union[None, FileMini] = None) -> Union[None, JSON]:
    if value == None:
        return None
    return {**serializeFileBase(value), **{'sequence_id': value.sequenceId, 'name': value.name, 'sha1': value.sha1, 'file_version': serializeFileVersionMini(value.fileVersion)}}

class FolderBase(BaseObject):
    def __init__(self, id: str, type: str, etag: Union[None, str] = None, **kwargs):
        """
        :param id: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting a folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folders/123`
            the `folder_id` is `123`.
        :type id: str
        :param type: `folder`
        :type type: str
        :param etag: The HTTP `etag` of this folder. This can be used within some API
            endpoints in the `If-Match` and `If-None-Match` headers to only
            perform changes on the folder if (no) changes have happened.
        :type etag: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.etag = etag

def deserializeFolderBase(value: Union[None, JSON] = None) -> Union[None, FolderBase]:
    if value == None:
        return None
    if not isJSON(value, 'object'):
        raise Exception('Expecting an object for "FolderBase"')
    return FolderBase(id=value['id'], etag=value['etag'], type=value['type'])

def serializeFolderBase(value: Union[None, FolderBase] = None) -> Union[None, JSON]:
    if value == None:
        return None
    return {'id': value.id, 'etag': value.etag, 'type': value.type}

class FolderMini(FolderBase):
    def __init__(self, id: str, type: str, sequence_id: Union[None, str] = None, name: Union[None, str] = None, etag: Union[None, str] = None, **kwargs):
        """
        :param id: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting a folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folders/123`
            the `folder_id` is `123`.
        :type id: str
        :param type: `folder`
        :type type: str
        :param name: The name of the folder.
        :type name: Union[None, str], optional
        :param etag: The HTTP `etag` of this folder. This can be used within some API
            endpoints in the `If-Match` and `If-None-Match` headers to only
            perform changes on the folder if (no) changes have happened.
        :type etag: Union[None, str], optional
        """
        super().__init__(id=id, type=type, etag=etag, **kwargs)
        self.sequence_id = sequence_id
        self.name = name

class TrashFileRestoredPathCollectionField(BaseObject):
    def __init__(self, total_count: int, entries: List[FolderMini], **kwargs):
        """
        :param total_count: The number of folders in this list.
        :type total_count: int
        :param entries: The parent folders for this item
        :type entries: List[FolderMini]
        """
        super().__init__(**kwargs)
        self.total_count = total_count
        self.entries = entries

def deserializeTrashFileRestoredPathCollectionField(value: Union[None, JSON] = None) -> Union[None, TrashFileRestoredPathCollectionField]:
    if value == None:
        return None
    if not isJSON(value, 'object'):
        raise Exception('Expecting an object for "TrashFileRestoredPathCollectionField"')
    return TrashFileRestoredPathCollectionField(totalCount=value['total_count'], entries=value['entries'])

def serializeTrashFileRestoredPathCollectionField(value: Union[None, TrashFileRestoredPathCollectionField] = None) -> Union[None, JSON]:
    if value == None:
        return None
    return {'total_count': value.totalCount, 'entries': value.entries}

def deserializeFolderMini(value: Union[None, JSON] = None) -> Union[None, FolderMini]:
    if value == None:
        return None
    return value

def serializeFolderMini(value: Union[None, FolderMini] = None) -> Union[None, JSON]:
    if value == None:
        return None
    return {**serializeFolderBase(value), **{'sequence_id': value.sequenceId, 'name': value.name}}

class FilePathCollectionField(BaseObject):
    def __init__(self, total_count: int, entries: List[FolderMini], **kwargs):
        """
        :param total_count: The number of folders in this list.
        :type total_count: int
        :param entries: The parent folders for this item
        :type entries: List[FolderMini]
        """
        super().__init__(**kwargs)
        self.total_count = total_count
        self.entries = entries

class UserBase(BaseObject):
    def __init__(self, type: str, id: Union[None, str] = None, **kwargs):
        """
        :param type: `user`
        :type type: str
        :param id: The unique identifier for this user
        :type id: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

def deserializeUserBase(value: Union[None, JSON] = None) -> Union[None, UserBase]:
    if value == None:
        return None
    if not isJSON(value, 'object'):
        raise Exception('Expecting an object for "UserBase"')
    return UserBase(id=value['id'], type=value['type'])

def serializeUserBase(value: Union[None, UserBase] = None) -> Union[None, JSON]:
    if value == None:
        return None
    return {'id': value.id, 'type': value.type}

class UserMini(UserBase):
    def __init__(self, name: str, login: str, type: str, id: Union[None, str] = None, **kwargs):
        """
        :param name: The display name of this user
        :type name: str
        :param login: The primary email address of this user
        :type login: str
        :param type: `user`
        :type type: str
        :param id: The unique identifier for this user
        :type id: Union[None, str], optional
        """
        super().__init__(type=type, id=id, **kwargs)
        self.name = name
        self.login = login

def deserializeUserMini(value: Union[None, JSON] = None) -> Union[None, UserMini]:
    if value == None:
        return None
    return value

def serializeUserMini(value: Union[None, UserMini] = None) -> Union[None, JSON]:
    if value == None:
        return None
    return {**serializeUserBase(value), **{'name': value.name, 'login': value.login}}

class File(FileMini):
    def __init__(self, description: str, size: int, path_collection: FilePathCollectionField, created_at: str, modified_at: str, modified_by: UserMini, owned_by: UserMini, item_status: FileItemStatusField, sequence_id: str, sha1: str, id: str, type: str, trashed_at: Union[None, str] = None, purged_at: Union[None, str] = None, content_created_at: Union[None, str] = None, content_modified_at: Union[None, str] = None, created_by: Union[None, UserMini] = None, shared_link: Union[None, FileSharedLinkField] = None, parent: Union[None, FolderMini] = None, name: Union[None, str] = None, file_version: Union[None, FileVersionMini] = None, etag: Union[None, str] = None, **kwargs):
        """
        :param description: The optional description of this file
        :type description: str
        :param size: The file size in bytes. Be careful parsing this integer as it can
            get very large and cause an integer overflow.
        :type size: int
        :param created_at: The date and time when the file was created on Box.
        :type created_at: str
        :param modified_at: The date and time when the file was last updated on Box.
        :type modified_at: str
        :param item_status: Defines if this item has been deleted or not.
            * `active` when the item has is not in the trash
            * `trashed` when the item has been moved to the trash but not deleted
            * `deleted` when the item has been permanently deleted.
        :type item_status: FileItemStatusField
        :param sha1: The SHA1 hash of the file. This can be used to compare the contents
            of a file on Box with a local file.
        :type sha1: str
        :param id: The unique identifier that represent a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
        :type id: str
        :param type: `file`
        :type type: str
        :param trashed_at: The time at which this file was put in the trash.
        :type trashed_at: Union[None, str], optional
        :param purged_at: The time at which this file is expected to be purged
            from the trash.
        :type purged_at: Union[None, str], optional
        :param content_created_at: The date and time at which this file was originally
            created, which might be before it was uploaded to Box.
        :type content_created_at: Union[None, str], optional
        :param content_modified_at: The date and time at which this file was last updated,
            which might be before it was uploaded to Box.
        :type content_modified_at: Union[None, str], optional
        :param name: The name of the file
        :type name: Union[None, str], optional
        :param etag: The HTTP `etag` of this file. This can be used within some API
            endpoints in the `If-Match` and `If-None-Match` headers to only
            perform changes on the file if (no) changes have happened.
        :type etag: Union[None, str], optional
        """
        super().__init__(sequence_id=sequence_id, sha1=sha1, id=id, type=type, name=name, file_version=file_version, etag=etag, **kwargs)
        self.description = description
        self.size = size
        self.path_collection = path_collection
        self.created_at = created_at
        self.modified_at = modified_at
        self.modified_by = modified_by
        self.owned_by = owned_by
        self.item_status = item_status
        self.trashed_at = trashed_at
        self.purged_at = purged_at
        self.content_created_at = content_created_at
        self.content_modified_at = content_modified_at
        self.created_by = created_by
        self.shared_link = shared_link
        self.parent = parent

def deserializeFile(value: Union[None, JSON] = None) -> Union[None, File]:
    if value == None:
        return None
    return value

def serializeFile(value: Union[None, File] = None) -> Union[None, JSON]:
    if value == None:
        return None
    return {**serializeFileMini(value), **{'description': value.description, 'size': value.size, 'path_collection': value.pathCollection, 'created_at': value.createdAt, 'modified_at': value.modifiedAt, 'trashed_at': value.trashedAt, 'purged_at': value.purgedAt, 'content_created_at': value.contentCreatedAt, 'content_modified_at': value.contentModifiedAt, 'created_by': serializeUserMini(value.createdBy), 'modified_by': serializeUserMini(value.modifiedBy), 'owned_by': serializeUserMini(value.ownedBy), 'shared_link': value.sharedLink, 'parent': serializeFolderMini(value.parent), 'item_status': value.itemStatus}}

class TrashFileRestoredItemStatusField(str, Enum):
    ACTIVE = 'active'
    TRASHED = 'trashed'
    DELETED = 'deleted'

def deserializeTrashFileRestoredItemStatusField(value: Union[None, JSON] = None) -> Union[None, TrashFileRestoredItemStatusField]:
    if value == None:
        return None
    return value

def serializeTrashFileRestoredItemStatusField(value: Union[None, TrashFileRestoredItemStatusField] = None) -> Union[None, JSON]:
    if value == None:
        return None
    return value

class TrashFileRestored(BaseObject):
    def __init__(self, id: str, type: str, sequence_id: str, sha1: str, description: str, size: int, path_collection: TrashFileRestoredPathCollectionField, created_at: str, modified_at: str, modified_by: UserMini, owned_by: UserMini, item_status: TrashFileRestoredItemStatusField, etag: Union[None, str] = None, name: Union[None, str] = None, file_version: Union[None, FileVersionMini] = None, trashed_at: Union[None, str] = None, purged_at: Union[None, str] = None, content_created_at: Union[None, str] = None, content_modified_at: Union[None, str] = None, created_by: Union[None, UserMini] = None, shared_link: Union[None, str] = None, parent: Union[None, FolderMini] = None, **kwargs):
        """
        :param id: The unique identifier that represent a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
        :type id: str
        :param type: `file`
        :type type: str
        :param sha1: The SHA1 hash of the file. This can be used to compare the contents
            of a file on Box with a local file.
        :type sha1: str
        :param description: The optional description of this file
        :type description: str
        :param size: The file size in bytes. Be careful parsing this integer as it can
            get very large and cause an integer overflow.
        :type size: int
        :param created_at: The date and time when the file was created on Box.
        :type created_at: str
        :param modified_at: The date and time when the file was last updated on Box.
        :type modified_at: str
        :param item_status: Defines if this item has been deleted or not.
            * `active` when the item has is not in the trash
            * `trashed` when the item has been moved to the trash but not deleted
            * `deleted` when the item has been permanently deleted.
        :type item_status: TrashFileRestoredItemStatusField
        :param etag: The HTTP `etag` of this file. This can be used within some API
            endpoints in the `If-Match` and `If-None-Match` headers to only
            perform changes on the file if (no) changes have happened.
        :type etag: Union[None, str], optional
        :param name: The name of the file
        :type name: Union[None, str], optional
        :param trashed_at: The time at which this file was put in the
            trash - becomes `null` after restore.
        :type trashed_at: Union[None, str], optional
        :param purged_at: The time at which this file is expected to be purged
            from the trash  - becomes `null` after restore.
        :type purged_at: Union[None, str], optional
        :param content_created_at: The date and time at which this file was originally
            created, which might be before it was uploaded to Box.
        :type content_created_at: Union[None, str], optional
        :param content_modified_at: The date and time at which this file was last updated,
            which might be before it was uploaded to Box.
        :type content_modified_at: Union[None, str], optional
        :param shared_link: The shared link for this file. This will
            be `null` if a file had been trashed, even though the original shared
            link does become active again.
        :type shared_link: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.sequence_id = sequence_id
        self.sha1 = sha1
        self.description = description
        self.size = size
        self.path_collection = path_collection
        self.created_at = created_at
        self.modified_at = modified_at
        self.modified_by = modified_by
        self.owned_by = owned_by
        self.item_status = item_status
        self.etag = etag
        self.name = name
        self.file_version = file_version
        self.trashed_at = trashed_at
        self.purged_at = purged_at
        self.content_created_at = content_created_at
        self.content_modified_at = content_modified_at
        self.created_by = created_by
        self.shared_link = shared_link
        self.parent = parent

def deserializeTrashFileRestored(value: Union[None, JSON] = None) -> Union[None, TrashFileRestored]:
    if value == None:
        return None
    if not isJSON(value, 'object'):
        raise Exception('Expecting an object for "TrashFileRestored"')
    return TrashFileRestored(id=value['id'], etag=value['etag'], type=value['type'], sequenceId=value['sequence_id'], name=value['name'], sha1=value['sha1'], fileVersion=deserializeFileVersionMini(value['file_version']), description=value['description'], size=value['size'], pathCollection=deserializeTrashFileRestoredPathCollectionField(value['path_collection']), createdAt=value['created_at'], modifiedAt=value['modified_at'], trashedAt=value['trashed_at'], purgedAt=value['purged_at'], contentCreatedAt=value['content_created_at'], contentModifiedAt=value['content_modified_at'], createdBy=deserializeUserMini(value['created_by']), modifiedBy=deserializeUserMini(value['modified_by']), ownedBy=deserializeUserMini(value['owned_by']), sharedLink=value['shared_link'], parent=deserializeFolderMini(value['parent']), itemStatus=deserializeTrashFileRestoredItemStatusField(value['item_status']))

def serializeTrashFileRestored(value: Union[None, TrashFileRestored] = None) -> Union[None, JSON]:
    if value == None:
        return None
    return {'id': value.id, 'etag': value.etag, 'type': value.type, 'sequence_id': value.sequenceId, 'name': value.name, 'sha1': value.sha1, 'file_version': serializeFileVersionMini(value.fileVersion), 'description': value.description, 'size': value.size, 'path_collection': serializeTrashFileRestoredPathCollectionField(value.pathCollection), 'created_at': value.createdAt, 'modified_at': value.modifiedAt, 'trashed_at': value.trashedAt, 'purged_at': value.purgedAt, 'content_created_at': value.contentCreatedAt, 'content_modified_at': value.contentModifiedAt, 'created_by': serializeUserMini(value.createdBy), 'modified_by': serializeUserMini(value.modifiedBy), 'owned_by': serializeUserMini(value.ownedBy), 'shared_link': value.sharedLink, 'parent': serializeFolderMini(value.parent), 'item_status': serializeTrashFileRestoredItemStatusField(value.itemStatus)}