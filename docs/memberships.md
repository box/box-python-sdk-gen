# MembershipsManager

## List user&#x27;s groups

Retrieves all the groups for a user. Only members of this
group or users with admin-level permissions will be able to
use this API.

This operation is performed by calling function `get_user_memberships`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-users-id-memberships/).

<!-- sample get_users_id_memberships -->
```python
client.memberships.get_user_memberships(user.id)
```

### Arguments

- user_id `str`
  - The ID of the user.
  - Used as `user_id` in path `path` of the API call
- query_params `GetUserMembershipsQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `GroupMemberships`.

Returns a collection of membership objects. If there are no
memberships, an empty collection will be returned.


## List members of group

Retrieves all the members for a group. Only members of this
group or users with admin-level permissions will be able to
use this API.

This operation is performed by calling function `get_group_memberships`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-groups-id-memberships/).

<!-- sample get_groups_id_memberships -->
```python
client.memberships.get_group_memberships(group.id)
```

### Arguments

- group_id `str`
  - The ID of the group.
  - Used as `group_id` in path `path` of the API call
- query_params `GetGroupMembershipsQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `GroupMemberships`.

Returns a collection of membership objects. If there are no
memberships, an empty collection will be returned.


## Add user to group

Creates a group membership. Only users with
admin-level permissions will be able to use this API.

This operation is performed by calling function `create_group_membership`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-group-memberships/).

<!-- sample post_group_memberships -->
```python
client.memberships.create_group_membership(CreateGroupMembershipRequestBodyArg(user&#x3D;user, group&#x3D;group))
```

### Arguments

- request_body `CreateGroupMembershipRequestBodyArg`
  - Used as requestBody for the API call
- query_params `CreateGroupMembershipQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `GroupMembership`.

Returns a new group membership object.


## Get group membership

Retrieves a specific group membership. Only admins of this
group or users with admin-level permissions will be able to
use this API.

This operation is performed by calling function `get_group_membership_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-group-memberships-id/).

<!-- sample get_group_memberships_id -->
```python
client.memberships.get_group_membership_by_id(group_membership.id)
```

### Arguments

- group_membership_id `str`
  - The ID of the group membership.
  - Used as `group_membership_id` in path `path` of the API call
- query_params `GetGroupMembershipByIdQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `GroupMembership`.

Returns the group membership object.


## Update group membership

Updates a user&#x27;s group membership. Only admins of this
group or users with admin-level permissions will be able to
use this API.

This operation is performed by calling function `update_group_membership_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-group-memberships-id/).

<!-- sample put_group_memberships_id -->
```python
client.memberships.update_group_membership_by_id(group_membership.id, UpdateGroupMembershipByIdRequestBodyArg(role&#x3D;UpdateGroupMembershipByIdRequestBodyArgRoleField.ADMIN.value))
```

### Arguments

- group_membership_id `str`
  - The ID of the group membership.
  - Used as `group_membership_id` in path `path` of the API call
- request_body `UpdateGroupMembershipByIdRequestBodyArg`
  - Used as requestBody for the API call
- query_params `UpdateGroupMembershipByIdQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `GroupMembership`.

Returns a new group membership object.


## Remove user from group

Deletes a specific group membership. Only admins of this
group or users with admin-level permissions will be able to
use this API.

This operation is performed by calling function `delete_group_membership_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-group-memberships-id/).

<!-- sample delete_group_memberships_id -->
```python
client.memberships.delete_group_membership_by_id(group_membership.id)
```

### Arguments

- group_membership_id `str`
  - The ID of the group membership.
  - Used as `group_membership_id` in path `path` of the API call


