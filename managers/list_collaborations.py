from typing import Union

from base_object import BaseObject

from enum import Enum

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

import json

from schemas import Collaborations

from schemas import ClientError

from schemas import Collaboration

class GetFilesIdCollaborationsOptionsArg(BaseObject):
    def __init__(self, fields: Union[None, str] = None, limit: Union[None, int] = None, marker: Union[None, str] = None, **kwargs):
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
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.fields = fields
        self.limit = limit
        self.marker = marker

class GetFoldersIdCollaborationsOptionsArg(BaseObject):
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

class GetCollaborationsStatusArg:
    pass

class GetCollaborationsOptionsArg(BaseObject):
    def __init__(self, fields: Union[None, str] = None, offset: Union[None, int] = None, limit: Union[None, int] = None, **kwargs):
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
        :param offset: The offset of the item at which to begin the response.
            Queries with offset parameter value
            exceeding 10000 will be rejected
            with a 400 response.
        :type offset: Union[None, int], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        """
        super().__init__(**kwargs)
        self.fields = fields
        self.offset = offset
        self.limit = limit

class PostCollaborationsRequestBodyArgItemFieldTypeField(str, Enum):
    FILE = 'file'
    FOLDER = 'folder'

class PostCollaborationsRequestBodyArgItemField(BaseObject):
    def __init__(self, type: PostCollaborationsRequestBodyArgItemFieldTypeField, id: str, **kwargs):
        """
        :param type: The type of the item that this collaboration will be
            granted access to
        :type type: PostCollaborationsRequestBodyArgItemFieldTypeField
        :param id: The ID of the item that will be granted access to
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class PostCollaborationsRequestBodyArgAccessibleByFieldTypeField(str, Enum):
    USER = 'user'
    GROUP = 'group'

class PostCollaborationsRequestBodyArgAccessibleByField(BaseObject):
    def __init__(self, type: PostCollaborationsRequestBodyArgAccessibleByFieldTypeField, id: Union[None, str] = None, login: Union[None, str] = None, **kwargs):
        """
        :param type: The type of collaborator to invite.
        :type type: PostCollaborationsRequestBodyArgAccessibleByFieldTypeField
        :param id: The ID of the user or group.
            Alternatively, use `login` to specify a user by email
            address.
        :type id: Union[None, str], optional
        :param login: The email address of the user to grant access to the item.
            Alternatively, use `id` to specify a user by user ID.
        :type login: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id
        self.login = login

class PostCollaborationsRequestBodyArgRoleField(str, Enum):
    EDITOR = 'editor'
    VIEWER = 'viewer'
    PREVIEWER = 'previewer'
    UPLOADER = 'uploader'
    PREVIEWER_UPLOADER = 'previewer uploader'
    VIEWER_UPLOADER = 'viewer uploader'
    CO_OWNER = 'co-owner'

class PostCollaborationsRequestBodyArg(BaseObject):
    def __init__(self, item: PostCollaborationsRequestBodyArgItemField, accessible_by: PostCollaborationsRequestBodyArgAccessibleByField, role: PostCollaborationsRequestBodyArgRoleField, can_view_path: Union[None, bool] = None, expires_at: Union[None, str] = None, **kwargs):
        """
        :param item: The item to attach the comment to.
        :type item: PostCollaborationsRequestBodyArgItemField
        :param accessible_by: The user or group to give access to the item.
        :type accessible_by: PostCollaborationsRequestBodyArgAccessibleByField
        :param role: The level of access granted.
        :type role: PostCollaborationsRequestBodyArgRoleField
        :param can_view_path: Determines if the invited users can see the entire parent path to
            the associated folder. The user will not gain privileges in any
            parent folder and therefore can not see content the user is not
            collaborated on.
            Be aware that this meaningfully increases the time required to load the
            invitee's **All Files** page. We recommend you limit the number of
            collaborations with `can_view_path` enabled to 1,000 per user.
            Only owner or co-owners can invite collaborators with a `can_view_path` of
            `true`.
            `can_view_path` can only be used for folder collaborations.
        :type can_view_path: Union[None, bool], optional
        :param expires_at: Set the expiration date for the collaboration. At this date, the
            collaboration will be automatically removed from the item.
            This feature will only work if the **Automatically remove invited
            collaborators: Allow folder owners to extend the expiry date**
            setting has been enabled in the **Enterprise Settings**
            of the **Admin Console**. When the setting is not enabled,
            collaborations can not have an expiry date and a value for this
            field will be result in an error.
        :type expires_at: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.item = item
        self.accessible_by = accessible_by
        self.role = role
        self.can_view_path = can_view_path
        self.expires_at = expires_at

class PostCollaborationsOptionsArg(BaseObject):
    def __init__(self, fields: Union[None, str] = None, notify: Union[None, bool] = None, **kwargs):
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
        :param notify: Determines if users should receive email notification
            for the action performed.
        :type notify: Union[None, bool], optional
        """
        super().__init__(**kwargs)
        self.fields = fields
        self.notify = notify

class GetGroupsIdCollaborationsOptionsArg(BaseObject):
    def __init__(self, limit: Union[None, int] = None, offset: Union[None, int] = None, **kwargs):
        """
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        :param offset: The offset of the item at which to begin the response.
            Queries with offset parameter value
            exceeding 10000 will be rejected
            with a 400 response.
        :type offset: Union[None, int], optional
        """
        super().__init__(**kwargs)
        self.limit = limit
        self.offset = offset

class ListCollaborationsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getFilesIdCollaborations(self, fileId: str, options: GetFilesIdCollaborationsOptionsArg = None) -> Collaborations:
        """
        Retrieves a list of pending and active collaborations for a
        
        file. This returns all the users that have access to the file

        
        or have been invited to the file.

        :param fileId: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type fileId: str
        """
        if options is None:
            options = GetFilesIdCollaborationsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', fileId, '/collaborations']), FetchOptions(method='GET', params={'fields': options.fields, 'limit': options.limit, 'marker': options.marker}, auth=self.auth))
        return Collaborations.from_dict(json.loads(response.text))
    def getFoldersIdCollaborations(self, folderId: str, options: GetFoldersIdCollaborationsOptionsArg = None) -> Collaborations:
        """
        Retrieves a list of pending and active collaborations for a
        
        folder. This returns all the users that have access to the folder

        
        or have been invited to the folder.

        :param folderId: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            Example: "12345"
        :type folderId: str
        """
        if options is None:
            options = GetFoldersIdCollaborationsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folderId, '/collaborations']), FetchOptions(method='GET', params={'fields': options.fields}, auth=self.auth))
        return Collaborations.from_dict(json.loads(response.text))
    def getCollaborations(self, status: GetCollaborationsStatusArg, options: GetCollaborationsOptionsArg = None) -> Collaborations:
        """
        Retrieves all pending collaboration invites for this user.
        :param status: The status of the collaborations to retrieve
            Example: "pending"
        :type status: GetCollaborationsStatusArg
        """
        if options is None:
            options = GetCollaborationsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaborations']), FetchOptions(method='GET', params={'status': status, 'fields': options.fields, 'offset': options.offset, 'limit': options.limit}, auth=self.auth))
        return Collaborations.from_dict(json.loads(response.text))
    def postCollaborations(self, requestBody: PostCollaborationsRequestBodyArg, options: PostCollaborationsOptionsArg = None) -> Collaboration:
        """
        Adds a collaboration for a single user or a single group to a file
        
        or folder.

        
        Collaborations can be created using email address, user IDs, or a

        
        group IDs.

        
        If a collaboration is being created with a group, access to

        
        this endpoint is dependent on the group's ability to be invited.

        """
        if options is None:
            options = PostCollaborationsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaborations']), FetchOptions(method='POST', params={'fields': options.fields, 'notify': options.notify}, body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return Collaboration.from_dict(json.loads(response.text))
    def getGroupsIdCollaborations(self, groupId: str, options: GetGroupsIdCollaborationsOptionsArg = None) -> Collaborations:
        """
        Retrieves all the collaborations for a group. The user
        
        must have admin permissions to inspect enterprise's groups.

        
        Each collaboration object has details on which files or

        
        folders the group has access to and with what role.

        :param groupId: The ID of the group.
            Example: "57645"
        :type groupId: str
        """
        if options is None:
            options = GetGroupsIdCollaborationsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/groups/', groupId, '/collaborations']), FetchOptions(method='GET', params={'limit': options.limit, 'offset': options.offset}, auth=self.auth))
        return Collaborations.from_dict(json.loads(response.text))