# TaskAssignmentsManager

## List task assignments

Lists all of the assignments for a given task.

This operation is performed by calling function `get_task_assignments`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-tasks-id-assignments/).

*Currently we don't have an example for calling `get_task_assignments` in integration tests*

### Arguments

- task_id `str`
  - The ID of the task.
  - Used as `task_id` in path `path` of the API call


### Returns

This function returns a value of type `TaskAssignments`.

Returns a collection of task assignment defining what task on
a file has been assigned to which users and by who.


## Assign task

Assigns a task to a user.

A task can be assigned to more than one user by creating multiple
assignments.

This operation is performed by calling function `create_task_assignment`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-task-assignments/).

*Currently we don't have an example for calling `create_task_assignment` in integration tests*

### Arguments

- request_body `CreateTaskAssignmentRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `TaskAssignment`.

Returns a new task assignment object.


## Get task assignment

Retrieves information about a task assignment.

This operation is performed by calling function `get_task_assignment_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-task-assignments-id/).

*Currently we don't have an example for calling `get_task_assignment_by_id` in integration tests*

### Arguments

- task_assignment_id `str`
  - The ID of the task assignment.
  - Used as `task_assignment_id` in path `path` of the API call


### Returns

This function returns a value of type `TaskAssignment`.

Returns a task assignment, specifying who the task has been assigned to
and by whom.


## Update task assignment

Updates a task assignment. This endpoint can be
used to update the state of a task assigned to a user.

This operation is performed by calling function `update_task_assignment_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-task-assignments-id/).

*Currently we don't have an example for calling `update_task_assignment_by_id` in integration tests*

### Arguments

- task_assignment_id `str`
  - The ID of the task assignment.
  - Used as `task_assignment_id` in path `path` of the API call
- request_body `UpdateTaskAssignmentByIdRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `TaskAssignment`.

Returns the updated task assignment object.


## Unassign task

Deletes a specific task assignment.

This operation is performed by calling function `delete_task_assignment_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-task-assignments-id/).

*Currently we don't have an example for calling `delete_task_assignment_by_id` in integration tests*

### Arguments

- task_assignment_id `str`
  - The ID of the task assignment.
  - Used as `task_assignment_id` in path `path` of the API call


