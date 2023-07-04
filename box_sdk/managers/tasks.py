from enum import Enum

from box_sdk.base_object import BaseObject

from typing import Optional

import json

from box_sdk.base_object import BaseObject

from box_sdk.schemas import Tasks

from box_sdk.schemas import ClientError

from box_sdk.schemas import Task

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.utils import to_map

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class CreateTaskItemArgTypeField(str, Enum):
    FILE = 'file'

class CreateTaskItemArg(BaseObject):
    def __init__(self, id: str, type: CreateTaskItemArgTypeField, **kwargs):
        """
        :param id: The ID of the file
        :type id: str
        :param type: `file`
        :type type: CreateTaskItemArgTypeField
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type

class CreateTaskActionArg(str, Enum):
    REVIEW = 'review'
    COMPLETE = 'complete'

class CreateTaskCompletionRuleArg(str, Enum):
    ALL_ASSIGNEES = 'all_assignees'
    ANY_ASSIGNEE = 'any_assignee'

class UpdateTaskByIdActionArg(str, Enum):
    REVIEW = 'review'
    COMPLETE = 'complete'

class UpdateTaskByIdCompletionRuleArg(str, Enum):
    ALL_ASSIGNEES = 'all_assignees'
    ANY_ASSIGNEE = 'any_assignee'

class TasksManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def get_file_tasks(self, file_id: str) -> Tasks:
        """
        Retrieves a list of all the tasks for a file. This
        
        endpoint does not support pagination.

        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/tasks']), FetchOptions(method='GET', auth=self.auth, network_session=self.network_session))
        return Tasks.from_dict(json.loads(response.text))
    def create_task(self, item: CreateTaskItemArg, action: Optional[CreateTaskActionArg] = None, message: Optional[str] = None, due_at: Optional[str] = None, completion_rule: Optional[CreateTaskCompletionRuleArg] = None) -> Task:
        """
        Creates a single task on a file. This task is not assigned to any user and
        
        will need to be assigned separately.

        :param item: The file to attach the task to.
        :type item: CreateTaskItemArg
        :param action: The action the task assignee will be prompted to do. Must be
            * `review` defines an approval task that can be approved or
            rejected
            * `complete` defines a general task which can be completed
        :type action: Optional[CreateTaskActionArg], optional
        :param message: An optional message to include with the task.
        :type message: Optional[str], optional
        :param due_at: Defines when the task is due. Defaults to `null` if not
            provided.
        :type due_at: Optional[str], optional
        :param completion_rule: Defines which assignees need to complete this task before the task
            is considered completed.
            * `all_assignees` (default) requires all assignees to review or
            approve the the task in order for it to be considered completed.
            * `any_assignee` accepts any one assignee to review or
            approve the the task in order for it to be considered completed.
        :type completion_rule: Optional[CreateTaskCompletionRuleArg], optional
        """
        request_body: BaseObject = BaseObject(item=item, action=action, message=message, due_at=due_at, completion_rule=completion_rule)
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/tasks']), FetchOptions(method='POST', body=json.dumps(to_map(request_body)), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return Task.from_dict(json.loads(response.text))
    def get_task_by_id(self, task_id: str) -> Task:
        """
        Retrieves information about a specific task.
        :param task_id: The ID of the task.
            Example: "12345"
        :type task_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/tasks/', task_id]), FetchOptions(method='GET', auth=self.auth, network_session=self.network_session))
        return Task.from_dict(json.loads(response.text))
    def update_task_by_id(self, task_id: str, action: Optional[UpdateTaskByIdActionArg] = None, message: Optional[str] = None, due_at: Optional[str] = None, completion_rule: Optional[UpdateTaskByIdCompletionRuleArg] = None) -> Task:
        """
        Updates a task. This can be used to update a task's configuration, or to
        
        update its completion state.

        :param task_id: The ID of the task.
            Example: "12345"
        :type task_id: str
        :param action: The action the task assignee will be prompted to do. Must be
            * `review` defines an approval task that can be approved or
            rejected
            * `complete` defines a general task which can be completed
        :type action: Optional[UpdateTaskByIdActionArg], optional
        :param message: The message included with the task.
        :type message: Optional[str], optional
        :param due_at: When the task is due at.
        :type due_at: Optional[str], optional
        :param completion_rule: Defines which assignees need to complete this task before the task
            is considered completed.
            * `all_assignees` (default) requires all assignees to review or
            approve the the task in order for it to be considered completed.
            * `any_assignee` accepts any one assignee to review or
            approve the the task in order for it to be considered completed.
        :type completion_rule: Optional[UpdateTaskByIdCompletionRuleArg], optional
        """
        request_body: BaseObject = BaseObject(action=action, message=message, due_at=due_at, completion_rule=completion_rule)
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/tasks/', task_id]), FetchOptions(method='PUT', body=json.dumps(to_map(request_body)), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return Task.from_dict(json.loads(response.text))
    def delete_task_by_id(self, task_id: str):
        """
        Removes a task from a file.
        :param task_id: The ID of the task.
            Example: "12345"
        :type task_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/tasks/', task_id]), FetchOptions(method='DELETE', auth=self.auth, network_session=self.network_session))
        return response.content