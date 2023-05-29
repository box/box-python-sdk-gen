from typing import Optional

from box_sdk.base_object import BaseObject

from enum import Enum

import json

from typing import Dict

from box_sdk.schemas import Groups

from box_sdk.schemas import ClientError

from box_sdk.schemas import Group

from box_sdk.schemas import GroupFull

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetGroupsOptionsArg(BaseObject):
    def __init__(self, filter_term: Optional[str] = None, fields: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, **kwargs):
        """
        :param filter_term: Limits the results to only groups whose `name` starts
            with the search term.
        :type filter_term: Optional[str], optional
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        :param offset: The offset of the item at which to begin the response.
            Queries with offset parameter value
            exceeding 10000 will be rejected
            with a 400 response.
        :type offset: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.filter_term = filter_term
        self.fields = fields
        self.limit = limit
        self.offset = offset

class CreateGroupRequestBodyArgInvitabilityLevelField(str, Enum):
    ADMINS_ONLY = 'admins_only'
    ADMINS_AND_MEMBERS = 'admins_and_members'
    ALL_MANAGED_USERS = 'all_managed_users'

class CreateGroupRequestBodyArgMemberViewabilityLevelField(str, Enum):
    ADMINS_ONLY = 'admins_only'
    ADMINS_AND_MEMBERS = 'admins_and_members'
    ALL_MANAGED_USERS = 'all_managed_users'

class CreateGroupRequestBodyArg(BaseObject):
    def __init__(self, name: str, provenance: Optional[str] = None, external_sync_identifier: Optional[str] = None, description: Optional[str] = None, invitability_level: Optional[CreateGroupRequestBodyArgInvitabilityLevelField] = None, member_viewability_level: Optional[CreateGroupRequestBodyArgMemberViewabilityLevelField] = None, **kwargs):
        """
        :param name: The name of the new group to be created. This name must be unique
            within the enterprise.
        :type name: str
        :param provenance: Keeps track of which external source this group is
            coming, for example `Active Directory`, or `Okta`.
            Setting this will also prevent Box admins from editing
            the group name and its members directly via the Box
            web application.
            This is desirable for one-way syncing of groups.
        :type provenance: Optional[str], optional
        :param external_sync_identifier: An arbitrary identifier that can be used by
            external group sync tools to link this Box Group to
            an external group.
            Example values of this field
            could be an **Active Directory Object ID** or a **Google
            Group ID**.
            We recommend you use of this field in
            order to avoid issues when group names are updated in
            either Box or external systems.
        :type external_sync_identifier: Optional[str], optional
        :param description: A human readable description of the group.
        :type description: Optional[str], optional
        :param invitability_level: Specifies who can invite the group to collaborate
            on folders.
            When set to `admins_only` the enterprise admin, co-admins,
            and the group's admin can invite the group.
            When set to `admins_and_members` all the admins listed
            above and group members can invite the group.
            When set to `all_managed_users` all managed users in the
            enterprise can invite the group.
        :type invitability_level: Optional[CreateGroupRequestBodyArgInvitabilityLevelField], optional
        :param member_viewability_level: Specifies who can see the members of the group.
            * `admins_only` - the enterprise admin, co-admins, group's
              group admin
            * `admins_and_members` - all admins and group members
            * `all_managed_users` - all managed users in the
              enterprise
        :type member_viewability_level: Optional[CreateGroupRequestBodyArgMemberViewabilityLevelField], optional
        """
        super().__init__(**kwargs)
        self.name = name
        self.provenance = provenance
        self.external_sync_identifier = external_sync_identifier
        self.description = description
        self.invitability_level = invitability_level
        self.member_viewability_level = member_viewability_level

class CreateGroupOptionsArg(BaseObject):
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

class GetGroupByIdOptionsArg(BaseObject):
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

class UpdateGroupByIdRequestBodyArgInvitabilityLevelField(str, Enum):
    ADMINS_ONLY = 'admins_only'
    ADMINS_AND_MEMBERS = 'admins_and_members'
    ALL_MANAGED_USERS = 'all_managed_users'

class UpdateGroupByIdRequestBodyArgMemberViewabilityLevelField(str, Enum):
    ADMINS_ONLY = 'admins_only'
    ADMINS_AND_MEMBERS = 'admins_and_members'
    ALL_MANAGED_USERS = 'all_managed_users'

class UpdateGroupByIdRequestBodyArg(BaseObject):
    def __init__(self, name: Optional[str] = None, provenance: Optional[str] = None, external_sync_identifier: Optional[str] = None, description: Optional[str] = None, invitability_level: Optional[UpdateGroupByIdRequestBodyArgInvitabilityLevelField] = None, member_viewability_level: Optional[UpdateGroupByIdRequestBodyArgMemberViewabilityLevelField] = None, **kwargs):
        """
        :param name: The name of the new group to be created. Must be unique within the
            enterprise.
        :type name: Optional[str], optional
        :param provenance: Keeps track of which external source this group is
            coming, for example `Active Directory`, or `Okta`.
            Setting this will also prevent Box admins from editing
            the group name and its members directly via the Box
            web application.
            This is desirable for one-way syncing of groups.
        :type provenance: Optional[str], optional
        :param external_sync_identifier: An arbitrary identifier that can be used by
            external group sync tools to link this Box Group to
            an external group.
            Example values of this field
            could be an **Active Directory Object ID** or a **Google
            Group ID**.
            We recommend you use of this field in
            order to avoid issues when group names are updated in
            either Box or external systems.
        :type external_sync_identifier: Optional[str], optional
        :param description: A human readable description of the group.
        :type description: Optional[str], optional
        :param invitability_level: Specifies who can invite the group to collaborate
            on folders.
            When set to `admins_only` the enterprise admin, co-admins,
            and the group's admin can invite the group.
            When set to `admins_and_members` all the admins listed
            above and group members can invite the group.
            When set to `all_managed_users` all managed users in the
            enterprise can invite the group.
        :type invitability_level: Optional[UpdateGroupByIdRequestBodyArgInvitabilityLevelField], optional
        :param member_viewability_level: Specifies who can see the members of the group.
            * `admins_only` - the enterprise admin, co-admins, group's
              group admin
            * `admins_and_members` - all admins and group members
            * `all_managed_users` - all managed users in the
              enterprise
        :type member_viewability_level: Optional[UpdateGroupByIdRequestBodyArgMemberViewabilityLevelField], optional
        """
        super().__init__(**kwargs)
        self.name = name
        self.provenance = provenance
        self.external_sync_identifier = external_sync_identifier
        self.description = description
        self.invitability_level = invitability_level
        self.member_viewability_level = member_viewability_level

class UpdateGroupByIdOptionsArg(BaseObject):
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

class GroupsManager(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {'network_session': 'networkSession', **BaseObject._fields_to_json_mapping}
    _json_to_fields_mapping: Dict[str, str] = {'networkSession': 'network_session', **BaseObject._json_to_fields_mapping}
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None, **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
        self.network_session = network_session
    def get_groups(self, options: GetGroupsOptionsArg = None) -> Groups:
        """
        Retrieves all of the groups for a given enterprise. The user
        
        must have admin permissions to inspect enterprise's groups.

        """
        if options is None:
            options = GetGroupsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/groups']), FetchOptions(method='GET', params={'filter_term': options.filter_term, 'fields': options.fields, 'limit': options.limit, 'offset': options.offset}, auth=self.auth, network_session=self.network_session))
        return Groups.from_dict(json.loads(response.text))
    def create_group(self, request_body: CreateGroupRequestBodyArg, options: CreateGroupOptionsArg = None) -> Group:
        """
        Creates a new group of users in an enterprise. Only users with admin
        
        permissions can create new groups.

        """
        if options is None:
            options = CreateGroupOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/groups']), FetchOptions(method='POST', params={'fields': options.fields}, body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return Group.from_dict(json.loads(response.text))
    def get_group_by_id(self, group_id: str, options: GetGroupByIdOptionsArg = None) -> GroupFull:
        """
        Retrieves information about a group. Only members of this
        
        group or users with admin-level permissions will be able to

        
        use this API.

        :param group_id: The ID of the group.
            Example: "57645"
        :type group_id: str
        """
        if options is None:
            options = GetGroupByIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/groups/', group_id]), FetchOptions(method='GET', params={'fields': options.fields}, auth=self.auth, network_session=self.network_session))
        return GroupFull.from_dict(json.loads(response.text))
    def update_group_by_id(self, group_id: str, request_body: UpdateGroupByIdRequestBodyArg, options: UpdateGroupByIdOptionsArg = None) -> GroupFull:
        """
        Updates a specific group. Only admins of this
        
        group or users with admin-level permissions will be able to

        
        use this API.

        :param group_id: The ID of the group.
            Example: "57645"
        :type group_id: str
        """
        if options is None:
            options = UpdateGroupByIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/groups/', group_id]), FetchOptions(method='PUT', params={'fields': options.fields}, body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return GroupFull.from_dict(json.loads(response.text))
    def delete_group_by_id(self, group_id: str):
        """
        Permanently deletes a group. Only users with
        
        admin-level permissions will be able to use this API.

        :param group_id: The ID of the group.
            Example: "57645"
        :type group_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/groups/', group_id]), FetchOptions(method='DELETE', auth=self.auth, network_session=self.network_session))
        return response.content