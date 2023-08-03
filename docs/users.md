# UsersManager

## List enterprise users

Returns a list of all users for the Enterprise along with their &#x60;user_id&#x60;,
&#x60;public_name&#x60;, and &#x60;login&#x60;.

The application and the authenticated user need to
have the permission to look up users in the entire
enterprise.

This operation is performed by calling function `get_users`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-users/).

<!-- sample get_users -->
```python
client.users.get_users()
```

### Arguments

- query_params `GetUsersQueryParamsArg`
  - Used as queryParams for the API call
- headers `GetUsersHeadersArg`
  - Used as headers for the API call


### Returns

This function returns a value of type `Users`.

Returns all of the users in the enterprise.


## Create user

Creates a new managed user in an enterprise. This endpoint
is only available to users and applications with the right
admin permissions.

This operation is performed by calling function `create_user`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-users/).

<!-- sample post_users -->
```python
client.users.create_user(CreateUserRequestBodyArg(name&#x3D;user_name, login&#x3D;user_login, is_platform_access_only&#x3D;True))
```

### Arguments

- request_body `CreateUserRequestBodyArg`
  - Used as requestBody for the API call
- query_params `CreateUserQueryParamsArg`
  - Used as queryParams for the API call
- headers `CreateUserHeadersArg`
  - Used as headers for the API call


### Returns

This function returns a value of type `User`.

Returns a user object for the newly created user.


## Get current user

Retrieves information about the user who is currently authenticated.

In the case of a client-side authenticated OAuth 2.0 application
this will be the user who authorized the app.

In the case of a JWT, server-side authenticated application
this will be the service account that belongs to the application
by default.

Use the &#x60;As-User&#x60; header to change who this API call is made on behalf of.

This operation is performed by calling function `get_user_me`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-users-me/).

<!-- sample get_users_me -->
```python
client.users.get_user_me()
```

### Arguments

- query_params `GetUserMeQueryParamsArg`
  - Used as queryParams for the API call
- headers `GetUserMeHeadersArg`
  - Used as headers for the API call


### Returns

This function returns a value of type `UserFull`.

Returns a single user object.


## Get user

Retrieves information about a user in the enterprise.

The application and the authenticated user need to
have the permission to look up users in the entire
enterprise.

This endpoint also returns a limited set of information
for external users who are collaborated on content
owned by the enterprise for authenticated users with the
right scopes. In this case, disallowed fields will return
null instead.

This operation is performed by calling function `get_user_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-users-id/).

<!-- sample get_users_id -->
```python
client.users.get_user_by_id(user.id)
```

### Arguments

- user_id `str`
  - The ID of the user.
  - Used as `user_id` in path `path` of the API call
- query_params `GetUserByIdQueryParamsArg`
  - Used as queryParams for the API call
- headers `GetUserByIdHeadersArg`
  - Used as headers for the API call


### Returns

This function returns a value of type `UserFull`.

Returns a single user object.

Not all available fields are returned by default. Use the
[fields](#param-fields) query parameter to explicitly request
any specific fields using the [fields](#get-users-id--request--fields)
parameter.


## Update user

Updates a managed or app user in an enterprise. This endpoint
is only available to users and applications with the right
admin permissions.

This operation is performed by calling function `update_user_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-users-id/).

<!-- sample put_users_id -->
```python
client.users.update_user_by_id(user.id, UpdateUserByIdRequestBodyArg(name&#x3D;updated_user_name))
```

### Arguments

- user_id `str`
  - The ID of the user.
  - Used as `user_id` in path `path` of the API call
- request_body `UpdateUserByIdRequestBodyArg`
  - Used as requestBody for the API call
- query_params `UpdateUserByIdQueryParamsArg`
  - Used as queryParams for the API call
- headers `UpdateUserByIdHeadersArg`
  - Used as headers for the API call


### Returns

This function returns a value of type `UserFull`.

Returns the updated user object.


## Delete user

Deletes a user. By default this will fail if the user
still owns any content. Move their owned content first
before proceeding, or use the &#x60;force&#x60; field to delete
the user and their files.

This operation is performed by calling function `delete_user_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-users-id/).

<!-- sample delete_users_id -->
```python
client.users.delete_user_by_id(user.id)
```

### Arguments

- user_id `str`
  - The ID of the user.
  - Used as `user_id` in path `path` of the API call
- query_params `DeleteUserByIdQueryParamsArg`
  - Used as queryParams for the API call
- headers `DeleteUserByIdHeadersArg`
  - Used as headers for the API call


### Returns

This function returns a value of type `None`.

Removes the user and returns an empty response.


