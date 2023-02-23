from base_object import BaseObject

from typing import Union

from enum import Enum

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

import json

from schemas import TaskAssignments

from schemas import ClientError

from schemas import TaskAssignment

class PostTaskAssignmentsRequestBodyArgTaskFieldTypeField:
    pass

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
    def getTasksIdAssignments(self, taskId: str) -> TaskAssignments:
        """
        Lists all of the assignments for a given task.
        :param taskId: The ID of the task.
            Example: "12345"
        :type taskId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/tasks/', taskId, '/assignments']), FetchOptions(method='GET', auth=self.auth))
        return TaskAssignments.from_dict(json.loads(response.text))
    def postTaskAssignments(self, requestBody: PostTaskAssignmentsRequestBodyArg) -> TaskAssignment:
        """
        Assigns a task to a user.
        
        A task can be assigned to more than one user by creating multiple

        
        assignments.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/task_assignments']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return TaskAssignment.from_dict(json.loads(response.text))
    def getTaskAssignmentsId(self, taskAssignmentId: str) -> TaskAssignment:
        """
        Retrieves information about a task assignment.
        :param taskAssignmentId: The ID of the task assignment.
            Example: "12345"
        :type taskAssignmentId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/task_assignments/', taskAssignmentId]), FetchOptions(method='GET', auth=self.auth))
        return TaskAssignment.from_dict(json.loads(response.text))
    def putTaskAssignmentsId(self, taskAssignmentId: str, requestBody: PutTaskAssignmentsIdRequestBodyArg) -> TaskAssignment:
        """
        Updates a task assignment. This endpoint can be
        
        used to update the state of a task assigned to a user.

        :param taskAssignmentId: The ID of the task assignment.
            Example: "12345"
        :type taskAssignmentId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/task_assignments/', taskAssignmentId]), FetchOptions(method='PUT', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return TaskAssignment.from_dict(json.loads(response.text))
    def deleteTaskAssignmentsId(self, taskAssignmentId: str):
        """
        Deletes a specific task assignment.
        :param taskAssignmentId: The ID of the task assignment.
            Example: "12345"
        :type taskAssignmentId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/task_assignments/', taskAssignmentId]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content