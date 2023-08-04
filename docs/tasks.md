<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [TasksManager](#tasksmanager)
  - [List tasks on file](#list-tasks-on-file)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Create task](#create-task)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)
  - [Get task](#get-task)
    - [Arguments](#arguments-2)
    - [Returns](#returns-2)
  - [Update task](#update-task)
    - [Arguments](#arguments-3)
    - [Returns](#returns-3)
  - [Remove task](#remove-task)
    - [Arguments](#arguments-4)
    - [Returns](#returns-4)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# TasksManager

## List tasks on file

Retrieves a list of all the tasks for a file. This
endpoint does not support pagination.

This operation is performed by calling function `get_file_tasks`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-files-id-tasks/).

*Currently we don't have an example for calling `get_file_tasks` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL &#x60;https://*.app.box.com/files/123&#x60; the &#x60;file_id&#x60; is &#x60;123&#x60;.
  - Used as `file_id` in path `path` of the API call


### Returns

This function returns a value of type `Tasks`.

Returns a list of tasks on a file.

If there are no tasks on this file an empty collection is returned
instead.


## Create task

Creates a single task on a file. This task is not assigned to any user and
will need to be assigned separately.

This operation is performed by calling function `create_task`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-tasks/).

*Currently we don't have an example for calling `create_task` in integration tests*

### Arguments

- request_body `CreateTaskRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `Task`.

Returns the newly created task.


## Get task

Retrieves information about a specific task.

This operation is performed by calling function `get_task_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-tasks-id/).

*Currently we don't have an example for calling `get_task_by_id` in integration tests*

### Arguments

- task_id `str`
  - The ID of the task.
  - Used as `task_id` in path `path` of the API call


### Returns

This function returns a value of type `Task`.

Returns a task object.


## Update task

Updates a task. This can be used to update a task&#x27;s configuration, or to
update its completion state.

This operation is performed by calling function `update_task_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-tasks-id/).

*Currently we don't have an example for calling `update_task_by_id` in integration tests*

### Arguments

- task_id `str`
  - The ID of the task.
  - Used as `task_id` in path `path` of the API call
- request_body `UpdateTaskByIdRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `Task`.

Returns the updated task object


## Remove task

Removes a task from a file.

This operation is performed by calling function `delete_task_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-tasks-id/).

*Currently we don't have an example for calling `delete_task_by_id` in integration tests*

### Arguments

- task_id `str`
  - The ID of the task.
  - Used as `task_id` in path `path` of the API call


### Returns

This function returns a value of type `None`.

Returns an empty response when the task was successfully deleted.


