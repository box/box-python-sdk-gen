from typing import Union

from base_object import BaseObject

from enum import Enum

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

import json

from schemas import Groups

from schemas import ClientError

from schemas import Group

class GetGroupsOptionsArg(BaseObject):
    def __init__(self, filterTerm: Union[None, str] = None, fields: Union[None, str] = None, limit: Union[None, int] = None, offset: Union[None, int] = None, **kwargs):
        """
        :param filterTerm: Limits the results to only groups whose `name` starts
            with the search term.
        :type filterTerm: Union[None, str], optional
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
        :param offset: The offset of the item at which to begin the response.
            Queries with offset parameter value
            exceeding 10000 will be rejected
            with a 400 response.
        :type offset: Union[None, int], optional
        """
        super().__init__(**kwargs)
        self.filterTerm = filterTerm
        self.fields = fields
        self.limit = limit
        self.offset = offset

class PostGroupsRequestBodyArgInvitabilityLevelField(str, Enum):
    ADMINS_ONLY = 'admins_only'
    ADMINS_AND_MEMBERS = 'admins_and_members'
    ALL_MANAGED_USERS = 'all_managed_users'

class PostGroupsRequestBodyArgMemberViewabilityLevelField(str, Enum):
    ADMINS_ONLY = 'admins_only'
    ADMINS_AND_MEMBERS = 'admins_and_members'
    ALL_MANAGED_USERS = 'all_managed_users'

class PostGroupsRequestBodyArg(BaseObject):
    def __init__(self, name: str, provenance: Union[None, str] = None, external_sync_identifier: Union[None, str] = None, description: Union[None, str] = None, invitability_level: Union[None, PostGroupsRequestBodyArgInvitabilityLevelField] = None, member_viewability_level: Union[None, PostGroupsRequestBodyArgMemberViewabilityLevelField] = None, **kwargs):
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
        :type provenance: Union[None, str], optional
        :param external_sync_identifier: An arbitrary identifier that can be used by
            external group sync tools to link this Box Group to
            an external group.
            Example values of this field
            could be an **Active Directory Object ID** or a **Google
            Group ID**.
            We recommend you use of this field in
            order to avoid issues when group names are updated in
            either Box or external systems.
        :type external_sync_identifier: Union[None, str], optional
        :param description: A human readable description of the group.
        :type description: Union[None, str], optional
        :param invitability_level: Specifies who can invite the group to collaborate
            on folders.
            When set to `admins_only` the enterprise admin, co-admins,
            and the group's admin can invite the group.
            When set to `admins_and_members` all the admins listed
            above and group members can invite the group.
            When set to `all_managed_users` all managed users in the
            enterprise can invite the group.
        :type invitability_level: Union[None, PostGroupsRequestBodyArgInvitabilityLevelField], optional
        :param member_viewability_level: Specifies who can see the members of the group.
            * `admins_only` - the enterprise admin, co-admins, group's
              group admin
            * `admins_and_members` - all admins and group members
            * `all_managed_users` - all managed users in the
              enterprise
        :type member_viewability_level: Union[None, PostGroupsRequestBodyArgMemberViewabilityLevelField], optional
        """
        super().__init__(**kwargs)
        self.name = name
        self.provenance = provenance
        self.external_sync_identifier = external_sync_identifier
        self.description = description
        self.invitability_level = invitability_level
        self.member_viewability_level = member_viewability_level

class PostGroupsOptionsArg(BaseObject):
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

class GetGroupsIdOptionsArg(BaseObject):
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

class PutGroupsIdRequestBodyArgInvitabilityLevelField(str, Enum):
    ADMINS_ONLY = 'admins_only'
    ADMINS_AND_MEMBERS = 'admins_and_members'
    ALL_MANAGED_USERS = 'all_managed_users'

class PutGroupsIdRequestBodyArgMemberViewabilityLevelField(str, Enum):
    ADMINS_ONLY = 'admins_only'
    ADMINS_AND_MEMBERS = 'admins_and_members'
    ALL_MANAGED_USERS = 'all_managed_users'

class PutGroupsIdRequestBodyArg(BaseObject):
    def __init__(self, name: Union[None, str] = None, provenance: Union[None, str] = None, external_sync_identifier: Union[None, str] = None, description: Union[None, str] = None, invitability_level: Union[None, PutGroupsIdRequestBodyArgInvitabilityLevelField] = None, member_viewability_level: Union[None, PutGroupsIdRequestBodyArgMemberViewabilityLevelField] = None, **kwargs):
        """
        :param name: The name of the new group to be created. Must be unique within the
            enterprise.
        :type name: Union[None, str], optional
        :param provenance: Keeps track of which external source this group is
            coming, for example `Active Directory`, or `Okta`.
            Setting this will also prevent Box admins from editing
            the group name and its members directly via the Box
            web application.
            This is desirable for one-way syncing of groups.
        :type provenance: Union[None, str], optional
        :param external_sync_identifier: An arbitrary identifier that can be used by
            external group sync tools to link this Box Group to
            an external group.
            Example values of this field
            could be an **Active Directory Object ID** or a **Google
            Group ID**.
            We recommend you use of this field in
            order to avoid issues when group names are updated in
            either Box or external systems.
        :type external_sync_identifier: Union[None, str], optional
        :param description: A human readable description of the group.
        :type description: Union[None, str], optional
        :param invitability_level: Specifies who can invite the group to collaborate
            on folders.
            When set to `admins_only` the enterprise admin, co-admins,
            and the group's admin can invite the group.
            When set to `admins_and_members` all the admins listed
            above and group members can invite the group.
            When set to `all_managed_users` all managed users in the
            enterprise can invite the group.
        :type invitability_level: Union[None, PutGroupsIdRequestBodyArgInvitabilityLevelField], optional
        :param member_viewability_level: Specifies who can see the members of the group.
            * `admins_only` - the enterprise admin, co-admins, group's
              group admin
            * `admins_and_members` - all admins and group members
            * `all_managed_users` - all managed users in the
              enterprise
        :type member_viewability_level: Union[None, PutGroupsIdRequestBodyArgMemberViewabilityLevelField], optional
        """
        super().__init__(**kwargs)
        self.name = name
        self.provenance = provenance
        self.external_sync_identifier = external_sync_identifier
        self.description = description
        self.invitability_level = invitability_level
        self.member_viewability_level = member_viewability_level

class PutGroupsIdOptionsArg(BaseObject):
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

class GroupsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getGroups(self, options: GetGroupsOptionsArg = None) -> Groups:
        """
        Retrieves all of the groups for a given enterprise. The user
        
        must have admin permissions to inspect enterprise's groups.

        """
        if options is None:
            options = GetGroupsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/groups']), FetchOptions(method='GET', params={'filter_term': options.filterTerm, 'fields': options.fields, 'limit': options.limit, 'offset': options.offset}, auth=self.auth))
        return Groups.from_dict(json.loads(response.text))
    def postGroups(self, requestBody: PostGroupsRequestBodyArg, options: PostGroupsOptionsArg = None) -> Group:
        """
        Creates a new group of users in an enterprise. Only users with admin
        
        permissions can create new groups.

        """
        if options is None:
            options = PostGroupsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/groups']), FetchOptions(method='POST', params={'fields': options.fields}, body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return Group.from_dict(json.loads(response.text))
    def getGroupsId(self, groupId: str, options: GetGroupsIdOptionsArg = None) -> Group:
        """
        Retrieves information about a group. Only members of this
        
        group or users with admin-level permissions will be able to

        
        use this API.

        :param groupId: The ID of the group.
            Example: "57645"
        :type groupId: str
        """
        if options is None:
            options = GetGroupsIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/groups/', groupId]), FetchOptions(method='GET', params={'fields': options.fields}, auth=self.auth))
        return Group.from_dict(json.loads(response.text))
    def putGroupsId(self, groupId: str, requestBody: PutGroupsIdRequestBodyArg, options: PutGroupsIdOptionsArg = None) -> Group:
        """
        Updates a specific group. Only admins of this
        
        group or users with admin-level permissions will be able to

        
        use this API.

        :param groupId: The ID of the group.
            Example: "57645"
        :type groupId: str
        """
        if options is None:
            options = PutGroupsIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/groups/', groupId]), FetchOptions(method='PUT', params={'fields': options.fields}, body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return Group.from_dict(json.loads(response.text))
    def deleteGroupsId(self, groupId: str):
        """
        Permanently deletes a group. Only users with
        
        admin-level permissions will be able to use this API.

        :param groupId: The ID of the group.
            Example: "57645"
        :type groupId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/groups/', groupId]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content