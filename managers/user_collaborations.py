from typing import Union

from base_object import BaseObject

from enum import Enum

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

import json

from schemas import Collaboration

from schemas import ClientError

class GetCollaborationsIdOptionsArg(BaseObject):
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

class PutCollaborationsIdRequestBodyArgRoleField(str, Enum):
    EDITOR = 'editor'
    VIEWER = 'viewer'
    PREVIEWER = 'previewer'
    UPLOADER = 'uploader'
    PREVIEWER_UPLOADER = 'previewer uploader'
    VIEWER_UPLOADER = 'viewer uploader'
    CO_OWNER = 'co-owner'
    OWNER = 'owner'

class PutCollaborationsIdRequestBodyArgStatusField(str, Enum):
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'

class PutCollaborationsIdRequestBodyArg(BaseObject):
    def __init__(self, role: PutCollaborationsIdRequestBodyArgRoleField, status: Union[None, PutCollaborationsIdRequestBodyArgStatusField] = None, expires_at: Union[None, str] = None, can_view_path: Union[None, bool] = None, **kwargs):
        """
        :param role: The level of access granted.
        :type role: PutCollaborationsIdRequestBodyArgRoleField
        :param status: <!--alex ignore reject-->
            Set the status of a `pending` collaboration invitation,
            effectively accepting, or rejecting the invite.
        :type status: Union[None, PutCollaborationsIdRequestBodyArgStatusField], optional
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

class UserCollaborationsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getCollaborationsId(self, collaborationId: str, options: GetCollaborationsIdOptionsArg = None) -> Collaboration:
        """
        Retrieves a single collaboration.
        :param collaborationId: The ID of the collaboration
            Example: "1234"
        :type collaborationId: str
        """
        if options is None:
            options = GetCollaborationsIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaborations/', collaborationId]), FetchOptions(method='GET', params={'fields': options.fields}, auth=self.auth))
        return Collaboration.from_dict(json.loads(response.text))
    def putCollaborationsId(self, collaborationId: str, requestBody: PutCollaborationsIdRequestBodyArg) -> Collaboration:
        """
        Updates a collaboration.
        
        Can be used to change the owner of an item, or to

        
        accept collaboration invites.

        :param collaborationId: The ID of the collaboration
            Example: "1234"
        :type collaborationId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaborations/', collaborationId]), FetchOptions(method='PUT', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return Collaboration.from_dict(json.loads(response.text))
    def deleteCollaborationsId(self, collaborationId: str):
        """
        Deletes a single collaboration.
        :param collaborationId: The ID of the collaboration
            Example: "1234"
        :type collaborationId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaborations/', collaborationId]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content