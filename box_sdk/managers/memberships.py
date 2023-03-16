from typing import Union

from box_sdk.base_object import BaseObject

from enum import Enum

import json

from box_sdk.schemas import GroupMemberships

from box_sdk.schemas import ClientError

from box_sdk.schemas import GroupMembership

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

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
    def get_users_id_memberships(self, user_id: str, options: GetUsersIdMembershipsOptionsArg = None) -> GroupMemberships:
        """
        Retrieves all the groups for a user. Only members of this
        
        group or users with admin-level permissions will be able to

        
        use this API.

        :param user_id: The ID of the user.
            Example: "12345"
        :type user_id: str
        """
        if options is None:
            options = GetUsersIdMembershipsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users/', user_id, '/memberships']), FetchOptions(method='GET', params={'limit': options.limit, 'offset': options.offset}, auth=self.auth))
        return GroupMemberships.from_dict(json.loads(response.text))
    def get_groups_id_memberships(self, group_id: str, options: GetGroupsIdMembershipsOptionsArg = None) -> GroupMemberships:
        """
        Retrieves all the members for a group. Only members of this
        
        group or users with admin-level permissions will be able to

        
        use this API.

        :param group_id: The ID of the group.
            Example: "57645"
        :type group_id: str
        """
        if options is None:
            options = GetGroupsIdMembershipsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/groups/', group_id, '/memberships']), FetchOptions(method='GET', params={'limit': options.limit, 'offset': options.offset}, auth=self.auth))
        return GroupMemberships.from_dict(json.loads(response.text))
    def post_group_memberships(self, request_body: PostGroupMembershipsRequestBodyArg, options: PostGroupMembershipsOptionsArg = None) -> GroupMembership:
        """
        Creates a group membership. Only users with
        
        admin-level permissions will be able to use this API.

        """
        if options is None:
            options = PostGroupMembershipsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/group_memberships']), FetchOptions(method='POST', params={'fields': options.fields}, body=json.dumps(request_body.to_dict()), auth=self.auth))
        return GroupMembership.from_dict(json.loads(response.text))
    def get_group_memberships_id(self, group_membership_id: str, options: GetGroupMembershipsIdOptionsArg = None) -> GroupMembership:
        """
        Retrieves a specific group membership. Only admins of this
        
        group or users with admin-level permissions will be able to

        
        use this API.

        :param group_membership_id: The ID of the group membership.
            Example: "434534"
        :type group_membership_id: str
        """
        if options is None:
            options = GetGroupMembershipsIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/group_memberships/', group_membership_id]), FetchOptions(method='GET', params={'fields': options.fields}, auth=self.auth))
        return GroupMembership.from_dict(json.loads(response.text))
    def put_group_memberships_id(self, group_membership_id: str, request_body: PutGroupMembershipsIdRequestBodyArg, options: PutGroupMembershipsIdOptionsArg = None) -> GroupMembership:
        """
        Updates a user's group membership. Only admins of this
        
        group or users with admin-level permissions will be able to

        
        use this API.

        :param group_membership_id: The ID of the group membership.
            Example: "434534"
        :type group_membership_id: str
        """
        if options is None:
            options = PutGroupMembershipsIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/group_memberships/', group_membership_id]), FetchOptions(method='PUT', params={'fields': options.fields}, body=json.dumps(request_body.to_dict()), auth=self.auth))
        return GroupMembership.from_dict(json.loads(response.text))
    def delete_group_memberships_id(self, group_membership_id: str):
        """
        Deletes a specific group membership. Only admins of this
        
        group or users with admin-level permissions will be able to

        
        use this API.

        :param group_membership_id: The ID of the group membership.
            Example: "434534"
        :type group_membership_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/group_memberships/', group_membership_id]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content