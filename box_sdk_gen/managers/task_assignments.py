from enum import Enum

from box_sdk_gen.base_object import BaseObject

from typing import Optional

from typing import Dict

import json

from box_sdk_gen.base_object import BaseObject

from box_sdk_gen.schemas import TaskAssignments

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import TaskAssignment

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse


class CreateTaskAssignmentTaskArgTypeField(str, Enum):
    TASK = 'task'


class CreateTaskAssignmentTaskArg(BaseObject):
    def __init__(self, id: str, type: CreateTaskAssignmentTaskArgTypeField, **kwargs):
        """
        :param id: The ID of the task
        :type id: str
        :param type: The type of the item to assign.
        :type type: CreateTaskAssignmentTaskArgTypeField
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class CreateTaskAssignmentAssignToArg(BaseObject):
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


class UpdateTaskAssignmentByIdResolutionStateArg(str, Enum):
    COMPLETED = 'completed'
    INCOMPLETE = 'incomplete'
    APPROVED = 'approved'
    REJECTED = 'rejected'


class TaskAssignmentsManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def get_task_assignments(
        self, task_id: str, extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> TaskAssignments:
        """
        Lists all of the assignments for a given task.
        :param task_id: The ID of the task.
            Example: "12345"
        :type task_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/tasks/', task_id, '/assignments']),
            FetchOptions(
                method='GET',
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return TaskAssignments.from_dict(json.loads(response.text))

    def create_task_assignment(
        self,
        task: CreateTaskAssignmentTaskArg,
        assign_to: CreateTaskAssignmentAssignToArg,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> TaskAssignment:
        """
        Assigns a task to a user.

        A task can be assigned to more than one user by creating multiple


        assignments.

        :param task: The task to assign to a user.
        :type task: CreateTaskAssignmentTaskArg
        :param assign_to: The user to assign the task to.
        :type assign_to: CreateTaskAssignmentAssignToArg
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body = BaseObject(task=task, assign_to=assign_to)
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/task_assignments']),
            FetchOptions(
                method='POST',
                headers=headers_map,
                body=json.dumps(request_body.to_dict()),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return TaskAssignment.from_dict(json.loads(response.text))

    def get_task_assignment_by_id(
        self,
        task_assignment_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> TaskAssignment:
        """
        Retrieves information about a task assignment.
        :param task_assignment_id: The ID of the task assignment.
            Example: "12345"
        :type task_assignment_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/task_assignments/', task_assignment_id]),
            FetchOptions(
                method='GET',
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return TaskAssignment.from_dict(json.loads(response.text))

    def update_task_assignment_by_id(
        self,
        task_assignment_id: str,
        message: Optional[str] = None,
        resolution_state: Optional[UpdateTaskAssignmentByIdResolutionStateArg] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> TaskAssignment:
        """
        Updates a task assignment. This endpoint can be

        used to update the state of a task assigned to a user.

        :param task_assignment_id: The ID of the task assignment.
            Example: "12345"
        :type task_assignment_id: str
        :param message: An optional message by the assignee that can be added to the task.
        :type message: Optional[str], optional
        :param resolution_state: The state of the task assigned to the user.
            * For a task with an `action` value of `complete` this can be
            `incomplete` or `completed`.
            * For a task with an `action` of `review` this can be
            `incomplete`, `approved`, or `rejected`.
        :type resolution_state: Optional[UpdateTaskAssignmentByIdResolutionStateArg], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body = BaseObject(message=message, resolution_state=resolution_state)
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/task_assignments/', task_assignment_id]),
            FetchOptions(
                method='PUT',
                headers=headers_map,
                body=json.dumps(request_body.to_dict()),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return TaskAssignment.from_dict(json.loads(response.text))

    def delete_task_assignment_by_id(
        self,
        task_assignment_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> None:
        """
        Deletes a specific task assignment.
        :param task_assignment_id: The ID of the task assignment.
            Example: "12345"
        :type task_assignment_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/task_assignments/', task_assignment_id]),
            FetchOptions(
                method='DELETE',
                headers=headers_map,
                response_format=None,
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return None