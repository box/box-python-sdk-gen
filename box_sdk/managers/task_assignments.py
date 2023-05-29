from enum import Enum

from box_sdk.base_object import BaseObject

from typing import Optional

import json

from typing import Dict

from box_sdk.schemas import TaskAssignments

from box_sdk.schemas import ClientError

from box_sdk.schemas import TaskAssignment

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class CreateTaskAssignmentRequestBodyArgTaskFieldTypeField(str, Enum):
    TASK = 'task'

class CreateTaskAssignmentRequestBodyArgTaskField(BaseObject):
    def __init__(self, id: str, type: CreateTaskAssignmentRequestBodyArgTaskFieldTypeField, **kwargs):
        """
        :param id: The ID of the task
        :type id: str
        :param type: The type of the item to assign.
        :type type: CreateTaskAssignmentRequestBodyArgTaskFieldTypeField
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type

class CreateTaskAssignmentRequestBodyArgAssignToField(BaseObject):
    def __init__(self, id: Optional[str] = None, login: Optional[str] = None, **kwargs):
        """
        :param id: The ID of the user to assign to the
            task.
            To specify a user by their email
            address use the `login` parameter.
        :type id: Optional[str], optional
        :param login: The email address of the user to assign to the task.
            To specify a user by their user ID please use the `id` parameter.
        :type login: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.login = login

class CreateTaskAssignmentRequestBodyArg(BaseObject):
    def __init__(self, task: CreateTaskAssignmentRequestBodyArgTaskField, assign_to: CreateTaskAssignmentRequestBodyArgAssignToField, **kwargs):
        """
        :param task: The task to assign to a user.
        :type task: CreateTaskAssignmentRequestBodyArgTaskField
        :param assign_to: The user to assign the task to.
        :type assign_to: CreateTaskAssignmentRequestBodyArgAssignToField
        """
        super().__init__(**kwargs)
        self.task = task
        self.assign_to = assign_to

class UpdateTaskAssignmentByIdRequestBodyArgResolutionStateField(str, Enum):
    COMPLETED = 'completed'
    INCOMPLETE = 'incomplete'
    APPROVED = 'approved'
    REJECTED = 'rejected'

class UpdateTaskAssignmentByIdRequestBodyArg(BaseObject):
    def __init__(self, message: Optional[str] = None, resolution_state: Optional[UpdateTaskAssignmentByIdRequestBodyArgResolutionStateField] = None, **kwargs):
        """
        :param message: An optional message by the assignee that can be added to the task.
        :type message: Optional[str], optional
        :param resolution_state: The state of the task assigned to the user.
            * For a task with an `action` value of `complete` this can be
            `incomplete` or `completed`.
            * For a task with an `action` of `review` this can be
            `incomplete`, `approved`, or `rejected`.
        :type resolution_state: Optional[UpdateTaskAssignmentByIdRequestBodyArgResolutionStateField], optional
        """
        super().__init__(**kwargs)
        self.message = message
        self.resolution_state = resolution_state

class TaskAssignmentsManager(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {'network_session': 'networkSession', **BaseObject._fields_to_json_mapping}
    _json_to_fields_mapping: Dict[str, str] = {'networkSession': 'network_session', **BaseObject._json_to_fields_mapping}
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None, **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
        self.network_session = network_session
    def get_task_assignments(self, task_id: str) -> TaskAssignments:
        """
        Lists all of the assignments for a given task.
        :param task_id: The ID of the task.
            Example: "12345"
        :type task_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/tasks/', task_id, '/assignments']), FetchOptions(method='GET', auth=self.auth, network_session=self.network_session))
        return TaskAssignments.from_dict(json.loads(response.text))
    def create_task_assignment(self, request_body: CreateTaskAssignmentRequestBodyArg) -> TaskAssignment:
        """
        Assigns a task to a user.
        
        A task can be assigned to more than one user by creating multiple

        
        assignments.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/task_assignments']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return TaskAssignment.from_dict(json.loads(response.text))
    def get_task_assignment_by_id(self, task_assignment_id: str) -> TaskAssignment:
        """
        Retrieves information about a task assignment.
        :param task_assignment_id: The ID of the task assignment.
            Example: "12345"
        :type task_assignment_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/task_assignments/', task_assignment_id]), FetchOptions(method='GET', auth=self.auth, network_session=self.network_session))
        return TaskAssignment.from_dict(json.loads(response.text))
    def update_task_assignment_by_id(self, task_assignment_id: str, request_body: UpdateTaskAssignmentByIdRequestBodyArg) -> TaskAssignment:
        """
        Updates a task assignment. This endpoint can be
        
        used to update the state of a task assigned to a user.

        :param task_assignment_id: The ID of the task assignment.
            Example: "12345"
        :type task_assignment_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/task_assignments/', task_assignment_id]), FetchOptions(method='PUT', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return TaskAssignment.from_dict(json.loads(response.text))
    def delete_task_assignment_by_id(self, task_assignment_id: str):
        """
        Deletes a specific task assignment.
        :param task_assignment_id: The ID of the task assignment.
            Example: "12345"
        :type task_assignment_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/task_assignments/', task_assignment_id]), FetchOptions(method='DELETE', auth=self.auth, network_session=self.network_session))
        return response.content