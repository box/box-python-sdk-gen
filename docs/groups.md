<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [GroupsManager](#groupsmanager)
  - [List groups for enterprise](#list-groups-for-enterprise)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Create group](#create-group)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)
  - [Get group](#get-group)
    - [Arguments](#arguments-2)
    - [Returns](#returns-2)
  - [Update group](#update-group)
    - [Arguments](#arguments-3)
    - [Returns](#returns-3)
  - [Remove group](#remove-group)
    - [Arguments](#arguments-4)
    - [Returns](#returns-4)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# GroupsManager

## List groups for enterprise

Retrieves all of the groups for a given enterprise. The user
must have admin permissions to inspect enterprise&#x27;s groups.

This operation is performed by calling function `get_groups`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-groups/).

<!-- sample get_groups -->
```python
client.groups.get_groups()
```

### Arguments

- query_params `GetGroupsQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `Groups`.

Returns a collection of group objects. If there are no groups, an
empty collection will be returned.


## Create group

Creates a new group of users in an enterprise. Only users with admin
permissions can create new groups.

This operation is performed by calling function `create_group`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-groups/).

<!-- sample post_groups -->
```python
client.groups.create_group(CreateGroupRequestBodyArg(name&#x3D;get_uuid()))
```

### Arguments

- request_body `CreateGroupRequestBodyArg`
  - Used as requestBody for the API call
- query_params `CreateGroupQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `Group`.

Returns the new group object.


## Get group

Retrieves information about a group. Only members of this
group or users with admin-level permissions will be able to
use this API.

This operation is performed by calling function `get_group_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-groups-id/).

<!-- sample get_groups_id -->
```python
client.groups.get_group_by_id(group.id)
```

### Arguments

- group_id `str`
  - The ID of the group.
  - Used as `group_id` in path `path` of the API call
- query_params `GetGroupByIdQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `GroupFull`.

Returns the group object


## Update group

Updates a specific group. Only admins of this
group or users with admin-level permissions will be able to
use this API.

This operation is performed by calling function `update_group_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-groups-id/).

<!-- sample put_groups_id -->
```python
client.groups.update_group_by_id(group.id, UpdateGroupByIdRequestBodyArg(name&#x3D;updated_group_name))
```

### Arguments

- group_id `str`
  - The ID of the group.
  - Used as `group_id` in path `path` of the API call
- request_body `UpdateGroupByIdRequestBodyArg`
  - Used as requestBody for the API call
- query_params `UpdateGroupByIdQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `GroupFull`.

Returns the updated group object.


## Remove group

Permanently deletes a group. Only users with
admin-level permissions will be able to use this API.

This operation is performed by calling function `delete_group_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-groups-id/).

<!-- sample delete_groups_id -->
```python
client.groups.delete_group_by_id(group.id)
```

### Arguments

- group_id `str`
  - The ID of the group.
  - Used as `group_id` in path `path` of the API call


### Returns

This function returns a value of type `None`.

A blank response is returned if the group was
successfully deleted.


