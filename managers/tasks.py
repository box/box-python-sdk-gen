from base_object import BaseObject

from enum import Enum

from typing import Union

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

import json

from schemas import Tasks

from schemas import ClientError

from schemas import Task

class PostTasksRequestBodyArgItemFieldTypeField:
    pass

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
    def getFilesIdTasks(self, fileId: str) -> Tasks:
        """
        Retrieves a list of all the tasks for a file. This
        
        endpoint does not support pagination.

        :param fileId: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type fileId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', fileId, '/tasks']), FetchOptions(method='GET', auth=self.auth))
        return Tasks.from_dict(json.loads(response.text))
    def postTasks(self, requestBody: PostTasksRequestBodyArg) -> Task:
        """
        Creates a single task on a file. This task is not assigned to any user and
        
        will need to be assigned separately.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/tasks']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return Task.from_dict(json.loads(response.text))
    def getTasksId(self, taskId: str) -> Task:
        """
        Retrieves information about a specific task.
        :param taskId: The ID of the task.
            Example: "12345"
        :type taskId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/tasks/', taskId]), FetchOptions(method='GET', auth=self.auth))
        return Task.from_dict(json.loads(response.text))
    def putTasksId(self, taskId: str, requestBody: PutTasksIdRequestBodyArg) -> Task:
        """
        Updates a task. This can be used to update a task's configuration, or to
        
        update its completion state.

        :param taskId: The ID of the task.
            Example: "12345"
        :type taskId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/tasks/', taskId]), FetchOptions(method='PUT', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return Task.from_dict(json.loads(response.text))
    def deleteTasksId(self, taskId: str):
        """
        Removes a task from a file.
        :param taskId: The ID of the task.
            Example: "12345"
        :type taskId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/tasks/', taskId]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content