from enum import Enum

from box_sdk.base_object import BaseObject

from typing import Union

import json

from box_sdk.schemas import TaskAssignments

from box_sdk.schemas import ClientError

from box_sdk.schemas import TaskAssignment

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class PostTaskAssignmentsRequestBodyArgTaskFieldTypeField(str, Enum):
    TASK = 'task'

class PostTaskAssignmentsRequestBodyArgTaskField(BaseObject):
    def __init__(self, id: str, type: PostTaskAssignmentsRequestBodyArgTaskFieldTypeField, **kwargs):
        """
        :param id: The ID of the task
        :type id: str
        :param type: The type of the item to assign.
        :type type: PostTaskAssignmentsRequestBodyArgTaskFieldTypeField
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type

class PostTaskAssignmentsRequestBodyArgAssignToField(BaseObject):
    def __init__(self, id: Union[None, str] = None, login: Union[None, str] = None, **kwargs):
        """
        :param id: The ID of the user to assign to the
            task.
            To specify a user by their email
            address use the `login` parameter.
        :type id: Union[None, str], optional
        :param login: The email address of the user to assign to the task.
            To specify a user by their user ID please use the `id` parameter.
        :type login: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.login = login

class PostTaskAssignmentsRequestBodyArg(BaseObject):
    def __init__(self, task: PostTaskAssignmentsRequestBodyArgTaskField, assign_to: PostTaskAssignmentsRequestBodyArgAssignToField, **kwargs):
        """
        :param task: The task to assign to a user.
        :type task: PostTaskAssignmentsRequestBodyArgTaskField
        :param assign_to: The user to assign the task to.
        :type assign_to: PostTaskAssignmentsRequestBodyArgAssignToField
        """
        super().__init__(**kwargs)
        self.task = task
        self.assign_to = assign_to

class PutTaskAssignmentsIdRequestBodyArgResolutionStateField(str, Enum):
    COMPLETED = 'completed'
    INCOMPLETE = 'incomplete'
    APPROVED = 'approved'
    REJECTED = 'rejected'

class PutTaskAssignmentsIdRequestBodyArg(BaseObject):
    def __init__(self, message: Union[None, str] = None, resolution_state: Union[None, PutTaskAssignmentsIdRequestBodyArgResolutionStateField] = None, **kwargs):
        """
        :param message: An optional message by the assignee that can be added to the task.
        :type message: Union[None, str], optional
        :param resolution_state: The state of the task assigned to the user.
            * For a task with an `action` value of `complete` this can be
            `incomplete` or `completed`.
            * For a task with an `action` of `review` this can be
            `incomplete`, `approved`, or `rejected`.
        :type resolution_state: Union[None, PutTaskAssignmentsIdRequestBodyArgResolutionStateField], optional
        """
        super().__init__(**kwargs)
        self.message = message
        self.resolution_state = resolution_state

class TaskAssignmentsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_tasks_id_assignments(self, task_id: str) -> TaskAssignments:
        """
        Lists all of the assignments for a given task.
        :param task_id: The ID of the task.
            Example: "12345"
        :type task_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/tasks/', task_id, '/assignments']), FetchOptions(method='GET', auth=self.auth))
        return TaskAssignments.from_dict(json.loads(response.text))
    def post_task_assignments(self, request_body: PostTaskAssignmentsRequestBodyArg) -> TaskAssignment:
        """
        Assigns a task to a user.
        
        A task can be assigned to more than one user by creating multiple

        
        assignments.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/task_assignments']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), auth=self.auth))
        return TaskAssignment.from_dict(json.loads(response.text))
    def get_task_assignments_id(self, task_assignment_id: str) -> TaskAssignment:
        """
        Retrieves information about a task assignment.
        :param task_assignment_id: The ID of the task assignment.
            Example: "12345"
        :type task_assignment_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/task_assignments/', task_assignment_id]), FetchOptions(method='GET', auth=self.auth))
        return TaskAssignment.from_dict(json.loads(response.text))
    def put_task_assignments_id(self, task_assignment_id: str, request_body: PutTaskAssignmentsIdRequestBodyArg) -> TaskAssignment:
        """
        Updates a task assignment. This endpoint can be
        
        used to update the state of a task assigned to a user.

        :param task_assignment_id: The ID of the task assignment.
            Example: "12345"
        :type task_assignment_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/task_assignments/', task_assignment_id]), FetchOptions(method='PUT', body=json.dumps(request_body.to_dict()), auth=self.auth))
        return TaskAssignment.from_dict(json.loads(response.text))
    def delete_task_assignments_id(self, task_assignment_id: str):
        """
        Deletes a specific task assignment.
        :param task_assignment_id: The ID of the task assignment.
            Example: "12345"
        :type task_assignment_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/task_assignments/', task_assignment_id]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content