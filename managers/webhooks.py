from typing import Union

from base_object import BaseObject

from enum import Enum

from typing import List

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

import json

from schemas import Webhooks

from schemas import ClientError

from schemas import Webhook

class GetWebhooksOptionsArg(BaseObject):
    def __init__(self, marker: Union[None, str] = None, limit: Union[None, int] = None, **kwargs):
        """
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Union[None, str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        """
        super().__init__(**kwargs)
        self.marker = marker
        self.limit = limit

class PostWebhooksRequestBodyArgTargetFieldTypeField(str, Enum):
    FILE = 'file'
    FOLDER = 'folder'

class PostWebhooksRequestBodyArgTargetField(BaseObject):
    def __init__(self, id: Union[None, str] = None, type: Union[None, PostWebhooksRequestBodyArgTargetFieldTypeField] = None, **kwargs):
        """
        :param id: The ID of the item to trigger a webhook
        :type id: Union[None, str], optional
        :param type: The type of item to trigger a webhook
        :type type: Union[None, PostWebhooksRequestBodyArgTargetFieldTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type

class PostWebhooksRequestBodyArgTriggersField(str, Enum):
    FILE_UPLOADED = 'FILE.UPLOADED'
    FILE_PREVIEWED = 'FILE.PREVIEWED'
    FILE_DOWNLOADED = 'FILE.DOWNLOADED'
    FILE_TRASHED = 'FILE.TRASHED'
    FILE_DELETED = 'FILE.DELETED'
    FILE_RESTORED = 'FILE.RESTORED'
    FILE_COPIED = 'FILE.COPIED'
    FILE_MOVED = 'FILE.MOVED'
    FILE_LOCKED = 'FILE.LOCKED'
    FILE_UNLOCKED = 'FILE.UNLOCKED'
    FILE_RENAMED = 'FILE.RENAMED'
    COMMENT_CREATED = 'COMMENT.CREATED'
    COMMENT_UPDATED = 'COMMENT.UPDATED'
    COMMENT_DELETED = 'COMMENT.DELETED'
    TASK_ASSIGNMENT_CREATED = 'TASK_ASSIGNMENT.CREATED'
    TASK_ASSIGNMENT_UPDATED = 'TASK_ASSIGNMENT.UPDATED'
    METADATA_INSTANCE_CREATED = 'METADATA_INSTANCE.CREATED'
    METADATA_INSTANCE_UPDATED = 'METADATA_INSTANCE.UPDATED'
    METADATA_INSTANCE_DELETED = 'METADATA_INSTANCE.DELETED'
    FOLDER_CREATED = 'FOLDER.CREATED'
    FOLDER_RENAMED = 'FOLDER.RENAMED'
    FOLDER_DOWNLOADED = 'FOLDER.DOWNLOADED'
    FOLDER_RESTORED = 'FOLDER.RESTORED'
    FOLDER_DELETED = 'FOLDER.DELETED'
    FOLDER_COPIED = 'FOLDER.COPIED'
    FOLDER_MOVED = 'FOLDER.MOVED'
    FOLDER_TRASHED = 'FOLDER.TRASHED'
    WEBHOOK_DELETED = 'WEBHOOK.DELETED'
    COLLABORATION_CREATED = 'COLLABORATION.CREATED'
    COLLABORATION_ACCEPTED = 'COLLABORATION.ACCEPTED'
    COLLABORATION_REJECTED = 'COLLABORATION.REJECTED'
    COLLABORATION_REMOVED = 'COLLABORATION.REMOVED'
    COLLABORATION_UPDATED = 'COLLABORATION.UPDATED'
    SHARED_LINK_DELETED = 'SHARED_LINK.DELETED'
    SHARED_LINK_CREATED = 'SHARED_LINK.CREATED'
    SHARED_LINK_UPDATED = 'SHARED_LINK.UPDATED'
    SIGN_REQUEST_COMPLETED = 'SIGN_REQUEST.COMPLETED'
    SIGN_REQUEST_DECLINED = 'SIGN_REQUEST.DECLINED'
    SIGN_REQUEST_EXPIRED = 'SIGN_REQUEST.EXPIRED'

class PostWebhooksRequestBodyArg(BaseObject):
    def __init__(self, target: PostWebhooksRequestBodyArgTargetField, address: str, triggers: List[PostWebhooksRequestBodyArgTriggersField], **kwargs):
        """
        :param target: The item that will trigger the webhook
        :type target: PostWebhooksRequestBodyArgTargetField
        :param address: The URL that is notified by this webhook
        :type address: str
        :param triggers: An array of event names that this webhook is
            to be triggered for
        :type triggers: List[PostWebhooksRequestBodyArgTriggersField]
        """
        super().__init__(**kwargs)
        self.target = target
        self.address = address
        self.triggers = triggers

class PutWebhooksIdRequestBodyArgTargetFieldTypeField(str, Enum):
    FILE = 'file'
    FOLDER = 'folder'

class PutWebhooksIdRequestBodyArgTargetField(BaseObject):
    def __init__(self, id: Union[None, str] = None, type: Union[None, PutWebhooksIdRequestBodyArgTargetFieldTypeField] = None, **kwargs):
        """
        :param id: The ID of the item to trigger a webhook
        :type id: Union[None, str], optional
        :param type: The type of item to trigger a webhook
        :type type: Union[None, PutWebhooksIdRequestBodyArgTargetFieldTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type

class PutWebhooksIdRequestBodyArgTriggersField(str, Enum):
    FILE_UPLOADED = 'FILE.UPLOADED'
    FILE_PREVIEWED = 'FILE.PREVIEWED'
    FILE_DOWNLOADED = 'FILE.DOWNLOADED'
    FILE_TRASHED = 'FILE.TRASHED'
    FILE_DELETED = 'FILE.DELETED'
    FILE_RESTORED = 'FILE.RESTORED'
    FILE_COPIED = 'FILE.COPIED'
    FILE_MOVED = 'FILE.MOVED'
    FILE_LOCKED = 'FILE.LOCKED'
    FILE_UNLOCKED = 'FILE.UNLOCKED'
    FILE_RENAMED = 'FILE.RENAMED'
    COMMENT_CREATED = 'COMMENT.CREATED'
    COMMENT_UPDATED = 'COMMENT.UPDATED'
    COMMENT_DELETED = 'COMMENT.DELETED'
    TASK_ASSIGNMENT_CREATED = 'TASK_ASSIGNMENT.CREATED'
    TASK_ASSIGNMENT_UPDATED = 'TASK_ASSIGNMENT.UPDATED'
    METADATA_INSTANCE_CREATED = 'METADATA_INSTANCE.CREATED'
    METADATA_INSTANCE_UPDATED = 'METADATA_INSTANCE.UPDATED'
    METADATA_INSTANCE_DELETED = 'METADATA_INSTANCE.DELETED'
    FOLDER_CREATED = 'FOLDER.CREATED'
    FOLDER_RENAMED = 'FOLDER.RENAMED'
    FOLDER_DOWNLOADED = 'FOLDER.DOWNLOADED'
    FOLDER_RESTORED = 'FOLDER.RESTORED'
    FOLDER_DELETED = 'FOLDER.DELETED'
    FOLDER_COPIED = 'FOLDER.COPIED'
    FOLDER_MOVED = 'FOLDER.MOVED'
    FOLDER_TRASHED = 'FOLDER.TRASHED'
    WEBHOOK_DELETED = 'WEBHOOK.DELETED'
    COLLABORATION_CREATED = 'COLLABORATION.CREATED'
    COLLABORATION_ACCEPTED = 'COLLABORATION.ACCEPTED'
    COLLABORATION_REJECTED = 'COLLABORATION.REJECTED'
    COLLABORATION_REMOVED = 'COLLABORATION.REMOVED'
    COLLABORATION_UPDATED = 'COLLABORATION.UPDATED'
    SHARED_LINK_DELETED = 'SHARED_LINK.DELETED'
    SHARED_LINK_CREATED = 'SHARED_LINK.CREATED'
    SHARED_LINK_UPDATED = 'SHARED_LINK.UPDATED'
    SIGN_REQUEST_COMPLETED = 'SIGN_REQUEST.COMPLETED'
    SIGN_REQUEST_DECLINED = 'SIGN_REQUEST.DECLINED'
    SIGN_REQUEST_EXPIRED = 'SIGN_REQUEST.EXPIRED'

class PutWebhooksIdRequestBodyArg(BaseObject):
    def __init__(self, target: Union[None, PutWebhooksIdRequestBodyArgTargetField] = None, address: Union[None, str] = None, triggers: Union[None, List[PutWebhooksIdRequestBodyArgTriggersField]] = None, **kwargs):
        """
        :param target: The item that will trigger the webhook
        :type target: Union[None, PutWebhooksIdRequestBodyArgTargetField], optional
        :param address: The URL that is notified by this webhook
        :type address: Union[None, str], optional
        :param triggers: An array of event names that this webhook is
            to be triggered for
        :type triggers: Union[None, List[PutWebhooksIdRequestBodyArgTriggersField]], optional
        """
        super().__init__(**kwargs)
        self.target = target
        self.address = address
        self.triggers = triggers

class WebhooksManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getWebhooks(self, options: GetWebhooksOptionsArg = None) -> Webhooks:
        """
        Returns all defined webhooks for the requesting application.
        
        This API only returns webhooks that are applied to files or folders that are

        
        owned by the authenticated user. This means that an admin can not see webhooks

        
        created by a service account unless the admin has access to those folders, and

        
        vice versa.

        """
        if options is None:
            options = GetWebhooksOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/webhooks']), FetchOptions(method='GET', params={'marker': options.marker, 'limit': options.limit}, auth=self.auth))
        return Webhooks.from_dict(json.loads(response.text))
    def postWebhooks(self, requestBody: PostWebhooksRequestBodyArg) -> Webhook:
        """
        Creates a webhook.
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/webhooks']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return Webhook.from_dict(json.loads(response.text))
    def getWebhooksId(self, webhookId: str) -> Webhook:
        """
        Retrieves a specific webhook
        :param webhookId: The ID of the webhook.
            Example: "3321123"
        :type webhookId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/webhooks/', webhookId]), FetchOptions(method='GET', auth=self.auth))
        return Webhook.from_dict(json.loads(response.text))
    def putWebhooksId(self, webhookId: str, requestBody: PutWebhooksIdRequestBodyArg) -> Webhook:
        """
        Updates a webhook.
        :param webhookId: The ID of the webhook.
            Example: "3321123"
        :type webhookId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/webhooks/', webhookId]), FetchOptions(method='PUT', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return Webhook.from_dict(json.loads(response.text))
    def deleteWebhooksId(self, webhookId: str):
        """
        Deletes a webhook.
        :param webhookId: The ID of the webhook.
            Example: "3321123"
        :type webhookId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/webhooks/', webhookId]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content