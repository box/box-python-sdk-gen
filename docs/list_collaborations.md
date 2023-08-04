<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [ListCollaborationsManager](#listcollaborationsmanager)
  - [List file collaborations](#list-file-collaborations)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [List folder collaborations](#list-folder-collaborations)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)
  - [List pending collaborations](#list-pending-collaborations)
    - [Arguments](#arguments-2)
    - [Returns](#returns-2)
  - [List group collaborations](#list-group-collaborations)
    - [Arguments](#arguments-3)
    - [Returns](#returns-3)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ListCollaborationsManager

## List file collaborations

Retrieves a list of pending and active collaborations for a
file. This returns all the users that have access to the file
or have been invited to the file.

This operation is performed by calling function `get_file_collaborations`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-files-id-collaborations/).

*Currently we don't have an example for calling `get_file_collaborations` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/files/123&#x60; the &#x60;file_id&#x60; is &#x60;123&#x60;.
  - Used as `file_id` in path `path` of the API call
- query_params `GetFileCollaborationsQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `Collaborations`.

Returns a collection of collaboration objects. If there are no
collaborations on this file an empty collection will be returned.

This list includes pending collaborations, for which the &#x60;status&#x60;
is set to &#x60;pending&#x60;, indicating invitations that have been sent but not
yet accepted.


## List folder collaborations

Retrieves a list of pending and active collaborations for a
folder. This returns all the users that have access to the folder
or have been invited to the folder.

This operation is performed by calling function `get_folder_collaborations`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-folders-id-collaborations/).

*Currently we don't have an example for calling `get_folder_collaborations` in integration tests*

### Arguments

- folder_id `str`
  - The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/folder/123&#x60; the &#x60;folder_id&#x60; is &#x60;123&#x60;.
  - Used as `folder_id` in path `path` of the API call
- query_params `GetFolderCollaborationsQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `Collaborations`.

Returns a collection of collaboration objects. If there are no
collaborations on this folder an empty collection will be returned.

This list includes pending collaborations, for which the &#x60;status&#x60;
is set to &#x60;pending&#x60;, indicating invitations that have been sent but not
yet accepted.


## List pending collaborations

Retrieves all pending collaboration invites for this user.

This operation is performed by calling function `get_collaborations`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-collaborations/).

*Currently we don't have an example for calling `get_collaborations` in integration tests*

### Arguments

- query_params `GetCollaborationsQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `Collaborations`.

Returns a collection of pending collaboration objects.

If the user has no pending collaborations, the collection
will be empty.


## List group collaborations

Retrieves all the collaborations for a group. The user
must have admin permissions to inspect enterprise&#x27;s groups.

Each collaboration object has details on which files or
folders the group has access to and with what role.

This operation is performed by calling function `get_group_collaborations`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-groups-id-collaborations/).

*Currently we don't have an example for calling `get_group_collaborations` in integration tests*

### Arguments

- group_id `str`
  - The ID of the group.
  - Used as `group_id` in path `path` of the API call
- query_params `GetGroupCollaborationsQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `Collaborations`.

Returns a collection of collaboration objects. If there are no
collaborations, an empty collection will be returned.


