from enum import Enum

from box_sdk.base_object import BaseObject

from typing import Union

import json

from box_sdk.schemas import Tasks

from box_sdk.schemas import ClientError

from box_sdk.schemas import Task

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class PostTasksRequestBodyArgItemFieldTypeField(str, Enum):
    FILE = 'file'

class PostTasksRequestBodyArgItemField(BaseObject):
    def __init__(self, id: str, type: PostTasksRequestBodyArgItemFieldTypeField, **kwargs):
        """
        :param id: The ID of the file
        :type id: str
        :param type: `file`
        :type type: PostTasksRequestBodyArgItemFieldTypeField
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type

class PostTasksRequestBodyArgActionField(str, Enum):
    REVIEW = 'review'
    COMPLETE = 'complete'

class PostTasksRequestBodyArgCompletionRuleField(str, Enum):
    ALL_ASSIGNEES = 'all_assignees'
    ANY_ASSIGNEE = 'any_assignee'

class PostTasksRequestBodyArg(BaseObject):
    def __init__(self, item: PostTasksRequestBodyArgItemField, action: Union[None, PostTasksRequestBodyArgActionField] = None, message: Union[None, str] = None, due_at: Union[None, str] = None, completion_rule: Union[None, PostTasksRequestBodyArgCompletionRuleField] = None, **kwargs):
        """
        :param item: The file to attach the task to.
        :type item: PostTasksRequestBodyArgItemField
        :param action: The action the task assignee will be prompted to do. Must be
            * `review` defines an approval task that can be approved or
            rejected
            * `complete` defines a general task which can be completed
        :type action: Union[None, PostTasksRequestBodyArgActionField], optional
        :param message: An optional message to include with the task.
        :type message: Union[None, str], optional
        :param due_at: Defines when the task is due. Defaults to `null` if not
            provided.
        :type due_at: Union[None, str], optional
        :param completion_rule: Defines which assignees need to complete this task before the task
            is considered completed.
            * `all_assignees` (default) requires all assignees to review or
            approve the the task in order for it to be considered completed.
            * `any_assignee` accepts any one assignee to review or
            approve the the task in order for it to be considered completed.
        :type completion_rule: Union[None, PostTasksRequestBodyArgCompletionRuleField], optional
        """
        super().__init__(**kwargs)
        self.item = item
        self.action = action
        self.message = message
        self.due_at = due_at
        self.completion_rule = completion_rule

class PutTasksIdRequestBodyArgActionField(str, Enum):
    REVIEW = 'review'
    COMPLETE = 'complete'

class PutTasksIdRequestBodyArgCompletionRuleField(str, Enum):
    ALL_ASSIGNEES = 'all_assignees'
    ANY_ASSIGNEE = 'any_assignee'

class PutTasksIdRequestBodyArg(BaseObject):
    def __init__(self, action: Union[None, PutTasksIdRequestBodyArgActionField] = None, message: Union[None, str] = None, due_at: Union[None, str] = None, completion_rule: Union[None, PutTasksIdRequestBodyArgCompletionRuleField] = None, **kwargs):
        """
        :param action: The action the task assignee will be prompted to do. Must be
            * `review` defines an approval task that can be approved or
            rejected
            * `complete` defines a general task which can be completed
        :type action: Union[None, PutTasksIdRequestBodyArgActionField], optional
        :param message: The message included with the task.
        :type message: Union[None, str], optional
        :param due_at: When the task is due at.
        :type due_at: Union[None, str], optional
        :param completion_rule: Defines which assignees need to complete this task before the task
            is considered completed.
            * `all_assignees` (default) requires all assignees to review or
            approve the the task in order for it to be considered completed.
            * `any_assignee` accepts any one assignee to review or
            approve the the task in order for it to be considered completed.
        :type completion_rule: Union[None, PutTasksIdRequestBodyArgCompletionRuleField], optional
        """
        super().__init__(**kwargs)
        self.action = action
        self.message = message
        self.due_at = due_at
        self.completion_rule = completion_rule

class TasksManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_files_id_tasks(self, file_id: str) -> Tasks:
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
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/tasks']), FetchOptions(method='GET', auth=self.auth))
        return Tasks.from_dict(json.loads(response.text))
    def post_tasks(self, request_body: PostTasksRequestBodyArg) -> Task:
        """
        Creates a single task on a file. This task is not assigned to any user and
        
        will need to be assigned separately.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/tasks']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), auth=self.auth))
        return Task.from_dict(json.loads(response.text))
    def get_tasks_id(self, task_id: str) -> Task:
        """
        Retrieves information about a specific task.
        :param task_id: The ID of the task.
            Example: "12345"
        :type task_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/tasks/', task_id]), FetchOptions(method='GET', auth=self.auth))
        return Task.from_dict(json.loads(response.text))
    def put_tasks_id(self, task_id: str, request_body: PutTasksIdRequestBodyArg) -> Task:
        """
        Updates a task. This can be used to update a task's configuration, or to
        
        update its completion state.

        :param task_id: The ID of the task.
            Example: "12345"
        :type task_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/tasks/', task_id]), FetchOptions(method='PUT', body=json.dumps(request_body.to_dict()), auth=self.auth))
        return Task.from_dict(json.loads(response.text))
    def delete_tasks_id(self, task_id: str):
        """
        Removes a task from a file.
        :param task_id: The ID of the task.
            Example: "12345"
        :type task_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/tasks/', task_id]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content