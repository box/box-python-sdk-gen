from box_sdk.base_object import BaseObject

from typing import Optional

import json

from typing import Dict

from box_sdk.schemas import Invite

from box_sdk.schemas import ClientError

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class CreateInviteRequestBodyArgEnterpriseField(BaseObject):
    def __init__(self, id: str, **kwargs):
        """
        :param id: The ID of the enterprise
        :type id: str
        """
        super().__init__(**kwargs)
        self.id = id

class CreateInviteRequestBodyArgActionableByField(BaseObject):
    def __init__(self, login: Optional[str] = None, **kwargs):
        """
        :param login: The login of the invited user
        :type login: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.login = login

class CreateInviteRequestBodyArg(BaseObject):
    def __init__(self, enterprise: CreateInviteRequestBodyArgEnterpriseField, actionable_by: CreateInviteRequestBodyArgActionableByField, **kwargs):
        """
        :param enterprise: The enterprise to invite the user to
        :type enterprise: CreateInviteRequestBodyArgEnterpriseField
        :param actionable_by: The user to invite
        :type actionable_by: CreateInviteRequestBodyArgActionableByField
        """
        super().__init__(**kwargs)
        self.enterprise = enterprise
        self.actionable_by = actionable_by

class CreateInviteOptionsArg(BaseObject):
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

class GetInviteByIdOptionsArg(BaseObject):
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

class InvitesManager(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {'network_session': 'networkSession', **BaseObject._fields_to_json_mapping}
    _json_to_fields_mapping: Dict[str, str] = {'networkSession': 'network_session', **BaseObject._json_to_fields_mapping}
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None, **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
        self.network_session = network_session
    def create_invite(self, request_body: CreateInviteRequestBodyArg, options: CreateInviteOptionsArg = None) -> Invite:
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
            options = CreateInviteOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/invites']), FetchOptions(method='POST', params={'fields': options.fields}, body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return Invite.from_dict(json.loads(response.text))
    def get_invite_by_id(self, invite_id: str, options: GetInviteByIdOptionsArg = None) -> Invite:
        """
        Returns the status of a user invite.
        :param invite_id: The ID of an invite.
            Example: "213723"
        :type invite_id: str
        """
        if options is None:
            options = GetInviteByIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/invites/', invite_id]), FetchOptions(method='GET', params={'fields': options.fields}, auth=self.auth, network_session=self.network_session))
        return Invite.from_dict(json.loads(response.text))