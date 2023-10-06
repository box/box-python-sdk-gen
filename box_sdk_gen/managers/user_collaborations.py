from enum import Enum

from typing import Optional

from box_sdk_gen.base_object import BaseObject

from typing import List

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.serialization import serialize

from box_sdk_gen.schemas import Collaboration

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse


class UpdateCollaborationByIdRoleArg(str, Enum):
    EDITOR = 'editor'
    VIEWER = 'viewer'
    PREVIEWER = 'previewer'
    UPLOADER = 'uploader'
    PREVIEWER_UPLOADER = 'previewer uploader'
    VIEWER_UPLOADER = 'viewer uploader'
    CO_OWNER = 'co-owner'
    OWNER = 'owner'


class UpdateCollaborationByIdStatusArg(str, Enum):
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'


class CreateCollaborationItemArgTypeField(str, Enum):
    FILE = 'file'
    FOLDER = 'folder'


class CreateCollaborationItemArg(BaseObject):
    def __init__(
        self,
        type: Optional[CreateCollaborationItemArgTypeField] = None,
        id: Optional[str] = None,
        **kwargs
    ):
        """
        :param type: The type of the item that this collaboration will be
            granted access to
        :type type: Optional[CreateCollaborationItemArgTypeField], optional
        :param id: The ID of the item that will be granted access to
        :type id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id


class CreateCollaborationAccessibleByArgTypeField(str, Enum):
    USER = 'user'
    GROUP = 'group'


class CreateCollaborationAccessibleByArg(BaseObject):
    def __init__(
        self,
        type: CreateCollaborationAccessibleByArgTypeField,
        id: Optional[str] = None,
        login: Optional[str] = None,
        **kwargs
    ):
        """
        :param type: The type of collaborator to invite.
        :type type: CreateCollaborationAccessibleByArgTypeField
        :param id: The ID of the user or group.
            Alternatively, use `login` to specify a user by email
            address.
        :type id: Optional[str], optional
        :param login: The email address of the user to grant access to the item.
            Alternatively, use `id` to specify a user by user ID.
        :type login: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id
        self.login = login


class CreateCollaborationRoleArg(str, Enum):
    EDITOR = 'editor'
    VIEWER = 'viewer'
    PREVIEWER = 'previewer'
    UPLOADER = 'uploader'
    PREVIEWER_UPLOADER = 'previewer uploader'
    VIEWER_UPLOADER = 'viewer uploader'
    CO_OWNER = 'co-owner'


class UserCollaborationsManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def get_collaboration_by_id(
        self,
        collaboration_id: str,
        fields: Optional[List[str]] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> Collaboration:
        """
        Retrieves a single collaboration.
        :param collaboration_id: The ID of the collaboration
            Example: "1234"
        :type collaboration_id: str
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
        query_params_map: Dict[str, str] = prepare_params({'fields': to_string(fields)})
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                ['https://api.box.com/2.0/collaborations/', to_string(collaboration_id)]
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
        return deserialize(response.text, Collaboration)

    def update_collaboration_by_id(
        self,
        collaboration_id: str,
        role: UpdateCollaborationByIdRoleArg,
        status: Optional[UpdateCollaborationByIdStatusArg] = None,
        expires_at: Optional[str] = None,
        can_view_path: Optional[bool] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> Collaboration:
        """
        Updates a collaboration.

        Can be used to change the owner of an item, or to


        accept collaboration invites.

        :param collaboration_id: The ID of the collaboration
            Example: "1234"
        :type collaboration_id: str
        :param role: The level of access granted.
        :type role: UpdateCollaborationByIdRoleArg
        :param status: <!--alex ignore reject-->
            Set the status of a `pending` collaboration invitation,
            effectively accepting, or rejecting the invite.
        :type status: Optional[UpdateCollaborationByIdStatusArg], optional
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
        :type expires_at: Optional[str], optional
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
        :type can_view_path: Optional[bool], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body = {
            'role': role,
            'status': status,
            'expires_at': expires_at,
            'can_view_path': can_view_path,
        }
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                ['https://api.box.com/2.0/collaborations/', to_string(collaboration_id)]
            ),
            FetchOptions(
                method='PUT',
                headers=headers_map,
                body=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, Collaboration)

    def delete_collaboration_by_id(
        self,
        collaboration_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> None:
        """
        Deletes a single collaboration.
        :param collaboration_id: The ID of the collaboration
            Example: "1234"
        :type collaboration_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                ['https://api.box.com/2.0/collaborations/', to_string(collaboration_id)]
            ),
            FetchOptions(
                method='DELETE',
                headers=headers_map,
                response_format=None,
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return None

    def create_collaboration(
        self,
        item: CreateCollaborationItemArg,
        accessible_by: CreateCollaborationAccessibleByArg,
        role: CreateCollaborationRoleArg,
        is_access_only: Optional[bool] = None,
        can_view_path: Optional[bool] = None,
        expires_at: Optional[str] = None,
        fields: Optional[List[str]] = None,
        notify: Optional[bool] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> Collaboration:
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

        :param item: The item to attach the comment to.
        :type item: CreateCollaborationItemArg
        :param accessible_by: The user or group to give access to the item.
        :type accessible_by: CreateCollaborationAccessibleByArg
        :param role: The level of access granted.
        :type role: CreateCollaborationRoleArg
        :param is_access_only: If set to `true`, collaborators have access to
            shared items, but such items won't be visible in the
            All Files list. Additionally, collaborators won't
            see the the path to the root folder for the
            shared item.
        :type is_access_only: Optional[bool], optional
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
        :type can_view_path: Optional[bool], optional
        :param expires_at: Set the expiration date for the collaboration. At this date, the
            collaboration will be automatically removed from the item.
            This feature will only work if the **Automatically remove invited
            collaborators: Allow folder owners to extend the expiry date**
            setting has been enabled in the **Enterprise Settings**
            of the **Admin Console**. When the setting is not enabled,
            collaborations can not have an expiry date and a value for this
            field will be result in an error.
        :type expires_at: Optional[str], optional
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[List[str]], optional
        :param notify: Determines if users should receive email notification
            for the action performed.
        :type notify: Optional[bool], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body = {
            'item': item,
            'accessible_by': accessible_by,
            'role': role,
            'is_access_only': is_access_only,
            'can_view_path': can_view_path,
            'expires_at': expires_at,
        }
        query_params_map: Dict[str, str] = prepare_params(
            {'fields': to_string(fields), 'notify': to_string(notify)}
        )
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/collaborations']),
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
        return deserialize(response.text, Collaboration)
