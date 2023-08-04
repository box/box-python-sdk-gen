<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [CommentsManager](#commentsmanager)
  - [List file comments](#list-file-comments)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Get comment](#get-comment)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)
  - [Update comment](#update-comment)
    - [Arguments](#arguments-2)
    - [Returns](#returns-2)
  - [Remove comment](#remove-comment)
    - [Arguments](#arguments-3)
    - [Returns](#returns-3)
  - [Create comment](#create-comment)
    - [Arguments](#arguments-4)
    - [Returns](#returns-4)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# CommentsManager

## List file comments

Retrieves a list of comments for a file.

This operation is performed by calling function `get_file_comments`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-files-id-comments/).

<!-- sample get_files_id_comments -->
```python
client.comments.get_file_comments(file_id)
```

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/files/123&#x60; the &#x60;file_id&#x60; is &#x60;123&#x60;.
  - Used as `file_id` in path `path` of the API call
- query_params `GetFileCommentsQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `Comments`.

Returns a collection of comment objects. If there are no
comments on this file an empty collection will be returned.


## Get comment

Retrieves the message and metadata for a specific comment, as well
as information on the user who created the comment.

This operation is performed by calling function `get_comment_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-comments-id/).

<!-- sample get_comments_id -->
```python
client.comments.get_comment_by_id(new_comment.id)
```

### Arguments

- comment_id `str`
  - The ID of the comment.
  - Used as `comment_id` in path `path` of the API call
- query_params `GetCommentByIdQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `CommentFull`.

Returns a full comment object.


## Update comment

Update the message of a comment.

This operation is performed by calling function `update_comment_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-comments-id/).

<!-- sample put_comments_id -->
```python
client.comments.update_comment_by_id(new_reply_comment.id, UpdateCommentByIdRequestBodyArg(message&#x3D;new_message))
```

### Arguments

- comment_id `str`
  - The ID of the comment.
  - Used as `comment_id` in path `path` of the API call
- request_body `UpdateCommentByIdRequestBodyArg`
  - Used as requestBody for the API call
- query_params `UpdateCommentByIdQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `CommentFull`.

Returns the updated comment object.


## Remove comment

Permanently deletes a comment.

This operation is performed by calling function `delete_comment_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-comments-id/).

<!-- sample delete_comments_id -->
```python
client.comments.delete_comment_by_id(new_comment.id)
```

### Arguments

- comment_id `str`
  - The ID of the comment.
  - Used as `comment_id` in path `path` of the API call


### Returns

This function returns a value of type `None`.

Returns an empty response when the comment has been deleted.


## Create comment

Adds a comment by the user to a specific file, or
as a reply to an other comment.

This operation is performed by calling function `create_comment`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-comments/).

<!-- sample post_comments -->
```python
client.comments.create_comment(CreateCommentRequestBodyArg(message&#x3D;message, item&#x3D;CreateCommentRequestBodyArgItemField(id&#x3D;new_comment.id, type&#x3D;CreateCommentRequestBodyArgItemFieldTypeField.COMMENT.value)))
```

### Arguments

- request_body `CreateCommentRequestBodyArg`
  - Used as requestBody for the API call
- query_params `CreateCommentQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `Comment`.

Returns the newly created comment object.

Not all available fields are returned by default. Use the
[fields](#param-fields) query parameter to explicitly request
any specific fields.


