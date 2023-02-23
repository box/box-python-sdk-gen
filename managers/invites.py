from base_object import BaseObject

from typing import Union

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

import json

from fetch import fetch, FetchOptions, FetchResponse

from schemas import Invite

from schemas import ClientError

class PostInvitesRequestBodyArgEnterpriseField(BaseObject):
    def __init__(self, id: str, **kwargs):
        """
        :param id: The ID of the enterprise
        :type id: str
        """
        super().__init__(**kwargs)
        self.id = id

class PostInvitesRequestBodyArgActionableByField(BaseObject):
    def __init__(self, login: Union[None, str] = None, **kwargs):
        """
        :param login: The login of the invited user
        :type login: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.login = login

class PostInvitesRequestBodyArg(BaseObject):
    def __init__(self, enterprise: PostInvitesRequestBodyArgEnterpriseField, actionable_by: PostInvitesRequestBodyArgActionableByField, **kwargs):
        """
        :param enterprise: The enterprise to invite the user to
        :type enterprise: PostInvitesRequestBodyArgEnterpriseField
        :param actionable_by: The user to invite
        :type actionable_by: PostInvitesRequestBodyArgActionableByField
        """
        super().__init__(**kwargs)
        self.enterprise = enterprise
        self.actionable_by = actionable_by

class PostInvitesOptionsArg(BaseObject):
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

class GetInvitesIdOptionsArg(BaseObject):
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

class InvitesManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def postInvites(self, requestBody: PostInvitesRequestBodyArg, options: PostInvitesOptionsArg = None) -> Invite:
        """
        Invites an existing external user to join an enterprise.
        
        The existing user can not be part of another enterprise and

        
        must already have a Box account. Once invited, the user will receive an

        
        email and are prompted to accept the invitation within the

        
        Box web application.

        
        This method requires the "Manage An Enterprise" scope enabled for

        
        the application, which can be enabled within the developer console.

        """
        if options is None:
            options = PostInvitesOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/invites']), FetchOptions(method='POST', params={'fields': options.fields}, body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return Invite.from_dict(json.loads(response.text))
    def getInvitesId(self, inviteId: str, options: GetInvitesIdOptionsArg = None) -> Invite:
        """
        Returns the status of a user invite.
        :param inviteId: The ID of an invite.
            Example: "213723"
        :type inviteId: str
        """
        if options is None:
            options = GetInvitesIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/invites/', inviteId]), FetchOptions(method='GET', params={'fields': options.fields}, auth=self.auth))
        return Invite.from_dict(json.loads(response.text))