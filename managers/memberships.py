from typing import Union

from base_object import BaseObject

from enum import Enum

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

import json

from schemas import GroupMemberships

from schemas import ClientError

from schemas import GroupMembership

class GetUsersIdMembershipsOptionsArg(BaseObject):
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

class GetGroupsIdMembershipsOptionsArg(BaseObject):
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

class PostGroupMembershipsRequestBodyArgUserField(BaseObject):
    def __init__(self, id: str, **kwargs):
        """
        :param id: The ID of the user to add to the group
        :type id: str
        """
        super().__init__(**kwargs)
        self.id = id

class PostGroupMembershipsRequestBodyArgGroupField(BaseObject):
    def __init__(self, id: str, **kwargs):
        """
        :param id: The ID of the group to add the user to
        :type id: str
        """
        super().__init__(**kwargs)
        self.id = id

class PostGroupMembershipsRequestBodyArgRoleField(str, Enum):
    MEMBER = 'member'
    ADMIN = 'admin'

class PostGroupMembershipsRequestBodyArgConfigurablePermissionsField(BaseObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class PostGroupMembershipsRequestBodyArg(BaseObject):
    def __init__(self, user: PostGroupMembershipsRequestBodyArgUserField, group: PostGroupMembershipsRequestBodyArgGroupField, role: Union[None, PostGroupMembershipsRequestBodyArgRoleField] = None, configurable_permissions: Union[None, PostGroupMembershipsRequestBodyArgConfigurablePermissionsField] = None, **kwargs):
        """
        :param user: The user to add to the group.
        :type user: PostGroupMembershipsRequestBodyArgUserField
        :param group: The group to add the user to.
        :type group: PostGroupMembershipsRequestBodyArgGroupField
        :param role: The role of the user in the group.
        :type role: Union[None, PostGroupMembershipsRequestBodyArgRoleField], optional
        :param configurable_permissions: Custom configuration for the permissions an admin
            if a group will receive. This option has no effect
            on members with a role of `member`.
            Setting these permissions overwrites the default
            access levels of an admin.
            Specifying a value of "null" for this object will disable
            all configurable permissions. Specifying permissions will set
            them accordingly, omitted permissions will be enabled by default.
        :type configurable_permissions: Union[None, PostGroupMembershipsRequestBodyArgConfigurablePermissionsField], optional
        """
        super().__init__(**kwargs)
        self.user = user
        self.group = group
        self.role = role
        self.configurable_permissions = configurable_permissions

class PostGroupMembershipsOptionsArg(BaseObject):
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

class GetGroupMembershipsIdOptionsArg(BaseObject):
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

class PutGroupMembershipsIdRequestBodyArgRoleField(str, Enum):
    MEMBER = 'member'
    ADMIN = 'admin'

class PutGroupMembershipsIdRequestBodyArgConfigurablePermissionsField(BaseObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class PutGroupMembershipsIdRequestBodyArg(BaseObject):
    def __init__(self, role: Union[None, PutGroupMembershipsIdRequestBodyArgRoleField] = None, configurable_permissions: Union[None, PutGroupMembershipsIdRequestBodyArgConfigurablePermissionsField] = None, **kwargs):
        """
        :param role: The role of the user in the group.
        :type role: Union[None, PutGroupMembershipsIdRequestBodyArgRoleField], optional
        :param configurable_permissions: Custom configuration for the permissions an admin
            if a group will receive. This option has no effect
            on members with a role of `member`.
            Setting these permissions overwrites the default
            access levels of an admin.
            Specifying a value of "null" for this object will disable
            all configurable permissions. Specifying permissions will set
            them accordingly, omitted permissions will be enabled by default.
        :type configurable_permissions: Union[None, PutGroupMembershipsIdRequestBodyArgConfigurablePermissionsField], optional
        """
        super().__init__(**kwargs)
        self.role = role
        self.configurable_permissions = configurable_permissions

class PutGroupMembershipsIdOptionsArg(BaseObject):
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

class MembershipsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getUsersIdMemberships(self, userId: str, options: GetUsersIdMembershipsOptionsArg = None) -> GroupMemberships:
        """
        Retrieves all the groups for a user. Only members of this
        
        group or users with admin-level permissions will be able to

        
        use this API.

        :param userId: The ID of the user.
            Example: "12345"
        :type userId: str
        """
        if options is None:
            options = GetUsersIdMembershipsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users/', userId, '/memberships']), FetchOptions(method='GET', params={'limit': options.limit, 'offset': options.offset}, auth=self.auth))
        return GroupMemberships.from_dict(json.loads(response.text))
    def getGroupsIdMemberships(self, groupId: str, options: GetGroupsIdMembershipsOptionsArg = None) -> GroupMemberships:
        """
        Retrieves all the members for a group. Only members of this
        
        group or users with admin-level permissions will be able to

        
        use this API.

        :param groupId: The ID of the group.
            Example: "57645"
        :type groupId: str
        """
        if options is None:
            options = GetGroupsIdMembershipsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/groups/', groupId, '/memberships']), FetchOptions(method='GET', params={'limit': options.limit, 'offset': options.offset}, auth=self.auth))
        return GroupMemberships.from_dict(json.loads(response.text))
    def postGroupMemberships(self, requestBody: PostGroupMembershipsRequestBodyArg, options: PostGroupMembershipsOptionsArg = None) -> GroupMembership:
        """
        Creates a group membership. Only users with
        
        admin-level permissions will be able to use this API.

        """
        if options is None:
            options = PostGroupMembershipsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/group_memberships']), FetchOptions(method='POST', params={'fields': options.fields}, body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return GroupMembership.from_dict(json.loads(response.text))
    def getGroupMembershipsId(self, groupMembershipId: str, options: GetGroupMembershipsIdOptionsArg = None) -> GroupMembership:
        """
        Retrieves a specific group membership. Only admins of this
        
        group or users with admin-level permissions will be able to

        
        use this API.

        :param groupMembershipId: The ID of the group membership.
            Example: "434534"
        :type groupMembershipId: str
        """
        if options is None:
            options = GetGroupMembershipsIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/group_memberships/', groupMembershipId]), FetchOptions(method='GET', params={'fields': options.fields}, auth=self.auth))
        return GroupMembership.from_dict(json.loads(response.text))
    def putGroupMembershipsId(self, groupMembershipId: str, requestBody: PutGroupMembershipsIdRequestBodyArg, options: PutGroupMembershipsIdOptionsArg = None) -> GroupMembership:
        """
        Updates a user's group membership. Only admins of this
        
        group or users with admin-level permissions will be able to

        
        use this API.

        :param groupMembershipId: The ID of the group membership.
            Example: "434534"
        :type groupMembershipId: str
        """
        if options is None:
            options = PutGroupMembershipsIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/group_memberships/', groupMembershipId]), FetchOptions(method='PUT', params={'fields': options.fields}, body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return GroupMembership.from_dict(json.loads(response.text))
    def deleteGroupMembershipsId(self, groupMembershipId: str):
        """
        Deletes a specific group membership. Only admins of this
        
        group or users with admin-level permissions will be able to

        
        use this API.

        :param groupMembershipId: The ID of the group membership.
            Example: "434534"
        :type groupMembershipId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/group_memberships/', groupMembershipId]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content