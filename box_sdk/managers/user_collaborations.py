from typing import Union

from box_sdk.base_object import BaseObject

from enum import Enum

import json

from box_sdk.schemas import Collaboration

from box_sdk.schemas import ClientError

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.jwt_auth import JWTAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetCollaborationByIdOptionsArg(BaseObject):
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

class UpdateCollaborationByIdRequestBodyArgRoleField(str, Enum):
    EDITOR = 'editor'
    VIEWER = 'viewer'
    PREVIEWER = 'previewer'
    UPLOADER = 'uploader'
    PREVIEWER_UPLOADER = 'previewer uploader'
    VIEWER_UPLOADER = 'viewer uploader'
    CO_OWNER = 'co-owner'
    OWNER = 'owner'

class UpdateCollaborationByIdRequestBodyArgStatusField(str, Enum):
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'

class UpdateCollaborationByIdRequestBodyArg(BaseObject):
    def __init__(self, role: UpdateCollaborationByIdRequestBodyArgRoleField, status: Union[None, UpdateCollaborationByIdRequestBodyArgStatusField] = None, expires_at: Union[None, str] = None, can_view_path: Union[None, bool] = None, **kwargs):
        """
        :param role: The level of access granted.
        :type role: UpdateCollaborationByIdRequestBodyArgRoleField
        :param status: <!--alex ignore reject-->
            Set the status of a `pending` collaboration invitation,
            effectively accepting, or rejecting the invite.
        :type status: Union[None, UpdateCollaborationByIdRequestBodyArgStatusField], optional
        :param expires_at: Update the expiration date for the collaboration. At this date,
            the collaboration will be automatically removed from the item.
            This feature will only work if the **Automatically remove invited
            collaborators: Allow folder owners to extend the expiry date**
            setting has been enabled in the **Enterprise Settings**
            of the **Admin Console**. When the setting is not enabled,
            collaborations can not have an expiry date and a value for this
            field will be result in an error.
            Additionally, a collaboration can only be given an
            expiration if it was created after the **Automatically remove
            invited collaborator** setting was enabled.
        :type expires_at: Union[None, str], optional
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
        """
        super().__init__(**kwargs)
        self.role = role
        self.status = status
        self.expires_at = expires_at
        self.can_view_path = can_view_path

class CreateCollaborationRequestBodyArgItemFieldTypeField(str, Enum):
    FILE = 'file'
    FOLDER = 'folder'

class CreateCollaborationRequestBodyArgItemField(BaseObject):
    def __init__(self, type: CreateCollaborationRequestBodyArgItemFieldTypeField, id: str, **kwargs):
        """
        :param type: The type of the item that this collaboration will be
            granted access to
        :type type: CreateCollaborationRequestBodyArgItemFieldTypeField
        :param id: The ID of the item that will be granted access to
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class CreateCollaborationRequestBodyArgAccessibleByFieldTypeField(str, Enum):
    USER = 'user'
    GROUP = 'group'

class CreateCollaborationRequestBodyArgAccessibleByField(BaseObject):
    def __init__(self, type: CreateCollaborationRequestBodyArgAccessibleByFieldTypeField, id: Union[None, str] = None, login: Union[None, str] = None, **kwargs):
        """
        :param type: The type of collaborator to invite.
        :type type: CreateCollaborationRequestBodyArgAccessibleByFieldTypeField
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

class CreateCollaborationRequestBodyArgRoleField(str, Enum):
    EDITOR = 'editor'
    VIEWER = 'viewer'
    PREVIEWER = 'previewer'
    UPLOADER = 'uploader'
    PREVIEWER_UPLOADER = 'previewer uploader'
    VIEWER_UPLOADER = 'viewer uploader'
    CO_OWNER = 'co-owner'

class CreateCollaborationRequestBodyArg(BaseObject):
    def __init__(self, item: CreateCollaborationRequestBodyArgItemField, accessible_by: CreateCollaborationRequestBodyArgAccessibleByField, role: CreateCollaborationRequestBodyArgRoleField, can_view_path: Union[None, bool] = None, expires_at: Union[None, str] = None, **kwargs):
        """
        :param item: The item to attach the comment to.
        :type item: CreateCollaborationRequestBodyArgItemField
        :param accessible_by: The user or group to give access to the item.
        :type accessible_by: CreateCollaborationRequestBodyArgAccessibleByField
        :param role: The level of access granted.
        :type role: CreateCollaborationRequestBodyArgRoleField
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

class CreateCollaborationOptionsArg(BaseObject):
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

class UserCollaborationsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth, JWTAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_collaboration_by_id(self, collaboration_id: str, options: GetCollaborationByIdOptionsArg = None) -> Collaboration:
        """
        Retrieves a single collaboration.
        :param collaboration_id: The ID of the collaboration
            Example: "1234"
        :type collaboration_id: str
        """
        if options is None:
            options = GetCollaborationByIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaborations/', collaboration_id]), FetchOptions(method='GET', params={'fields': options.fields}, auth=self.auth))
        return Collaboration.from_dict(json.loads(response.text))
    def update_collaboration_by_id(self, collaboration_id: str, request_body: UpdateCollaborationByIdRequestBodyArg) -> Collaboration:
        """
        Updates a collaboration.
        
        Can be used to change the owner of an item, or to

        
        accept collaboration invites.

        :param collaboration_id: The ID of the collaboration
            Example: "1234"
        :type collaboration_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaborations/', collaboration_id]), FetchOptions(method='PUT', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth))
        return Collaboration.from_dict(json.loads(response.text))
    def delete_collaboration_by_id(self, collaboration_id: str):
        """
        Deletes a single collaboration.
        :param collaboration_id: The ID of the collaboration
            Example: "1234"
        :type collaboration_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaborations/', collaboration_id]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content
    def create_collaboration(self, request_body: CreateCollaborationRequestBodyArg, options: CreateCollaborationOptionsArg = None) -> Collaboration:
        """
        Adds a collaboration for a single user or a single group to a file
        
        or folder.

        
        Collaborations can be created using email address, user IDs, or a

        
        group IDs.

        
        If a collaboration is being created with a group, access to

        
        this endpoint is dependent on the group's ability to be invited.

        
        If collaboration is in `pending` status, the following fields

        
        are redacted:

        
        - `login` and `name` are hidden if a collaboration was created

        
        using `user_id`,

        
        -  `name` is hidden if a collaboration was created using `login`.

        """
        if options is None:
            options = CreateCollaborationOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaborations']), FetchOptions(method='POST', params={'fields': options.fields, 'notify': options.notify}, body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth))
        return Collaboration.from_dict(json.loads(response.text))