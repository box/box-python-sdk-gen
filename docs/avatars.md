<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [AvatarsManager](#avatarsmanager)
  - [Get user avatar](#get-user-avatar)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Add or update user avatar](#add-or-update-user-avatar)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)
  - [Delete user avatar](#delete-user-avatar)
    - [Arguments](#arguments-2)
    - [Returns](#returns-2)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# AvatarsManager

## Get user avatar

Retrieves an image of a the user&#x27;s avatar.

This operation is performed by calling function `get_user_avatar`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-users-id-avatar/).

<!-- sample get_users_id_avatar -->
```python
client.avatars.get_user_avatar(user.id)
```

### Arguments

- user_id `str`
  - The ID of the user.
  - Used as `user_id` in path `path` of the API call


### Returns

This function returns a value of type `ByteStream`.

When an avatar can be found for the user the
image data will be returned in the body of the
response.


## Add or update user avatar

Adds or updates a user avatar.

This operation is performed by calling function `create_user_avatar`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-users-id-avatar/).

<!-- sample post_users_id_avatar -->
```python
client.avatars.create_user_avatar(user.id, CreateUserAvatarRequestBodyArg(pic&#x3D;decode_base_64_byte_stream(&#x27;iVBORw0KGgoAAAANSUhEUgAAAQAAAAEAAQMAAABmvDolAAAAA1BMVEW10NBjBBbqAAAAH0lEQVRoge3BAQ0AAADCoPdPbQ43oAAAAAAAAAAAvg0hAAABmmDh1QAAAABJRU5ErkJggg&#x3D;&#x3D;&#x27;), pic_content_type&#x3D;&#x27;image/png&#x27;, pic_file_name&#x3D;&#x27;avatar.png&#x27;))
```

### Arguments

- user_id `str`
  - The ID of the user.
  - Used as `user_id` in path `path` of the API call
- request_body `CreateUserAvatarRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `UserAvatar`.

* &#x60;ok&#x60;: Returns the &#x60;pic_urls&#x60; object with URLs to existing
user avatars that were updated.* &#x60;created&#x60;: Returns the &#x60;pic_urls&#x60; object with URLS to user avatars
uploaded to Box with the request.


## Delete user avatar

Removes an existing user avatar.
You cannot reverse this operation.

This operation is performed by calling function `delete_user_avatar`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-users-id-avatar/).

<!-- sample delete_users_id_avatar -->
```python
client.avatars.delete_user_avatar(user.id)
```

### Arguments

- user_id `str`
  - The ID of the user.
  - Used as `user_id` in path `path` of the API call


### Returns

This function returns a value of type `None`.

* &#x60;no_content&#x60;: Removes the avatar and returns an empty response.


