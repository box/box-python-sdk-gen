from typing import Union

from box_sdk.base_object import BaseObject

from enum import Enum

from typing import List

import json

from box_sdk.schemas import Webhooks

from box_sdk.schemas import ClientError

from box_sdk.schemas import Webhook

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.jwt_auth import JWTAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

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

class CreateWebhookRequestBodyArgTargetFieldTypeField(str, Enum):
    FILE = 'file'
    FOLDER = 'folder'

class CreateWebhookRequestBodyArgTargetField(BaseObject):
    def __init__(self, id: Union[None, str] = None, type: Union[None, CreateWebhookRequestBodyArgTargetFieldTypeField] = None, **kwargs):
        """
        :param id: The ID of the item to trigger a webhook
        :type id: Union[None, str], optional
        :param type: The type of item to trigger a webhook
        :type type: Union[None, CreateWebhookRequestBodyArgTargetFieldTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type

class CreateWebhookRequestBodyArgTriggersField(str, Enum):
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

class CreateWebhookRequestBodyArg(BaseObject):
    def __init__(self, target: CreateWebhookRequestBodyArgTargetField, address: str, triggers: List[CreateWebhookRequestBodyArgTriggersField], **kwargs):
        """
        :param target: The item that will trigger the webhook
        :type target: CreateWebhookRequestBodyArgTargetField
        :param address: The URL that is notified by this webhook
        :type address: str
        :param triggers: An array of event names that this webhook is
            to be triggered for
        :type triggers: List[CreateWebhookRequestBodyArgTriggersField]
        """
        super().__init__(**kwargs)
        self.target = target
        self.address = address
        self.triggers = triggers

class UpdateWebhookByIdRequestBodyArgTargetFieldTypeField(str, Enum):
    FILE = 'file'
    FOLDER = 'folder'

class UpdateWebhookByIdRequestBodyArgTargetField(BaseObject):
    def __init__(self, id: Union[None, str] = None, type: Union[None, UpdateWebhookByIdRequestBodyArgTargetFieldTypeField] = None, **kwargs):
        """
        :param id: The ID of the item to trigger a webhook
        :type id: Union[None, str], optional
        :param type: The type of item to trigger a webhook
        :type type: Union[None, UpdateWebhookByIdRequestBodyArgTargetFieldTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type

class UpdateWebhookByIdRequestBodyArgTriggersField(str, Enum):
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

class UpdateWebhookByIdRequestBodyArg(BaseObject):
    def __init__(self, target: Union[None, UpdateWebhookByIdRequestBodyArgTargetField] = None, address: Union[None, str] = None, triggers: Union[None, List[UpdateWebhookByIdRequestBodyArgTriggersField]] = None, **kwargs):
        """
        :param target: The item that will trigger the webhook
        :type target: Union[None, UpdateWebhookByIdRequestBodyArgTargetField], optional
        :param address: The URL that is notified by this webhook
        :type address: Union[None, str], optional
        :param triggers: An array of event names that this webhook is
            to be triggered for
        :type triggers: Union[None, List[UpdateWebhookByIdRequestBodyArgTriggersField]], optional
        """
        super().__init__(**kwargs)
        self.target = target
        self.address = address
        self.triggers = triggers

class WebhooksManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth, JWTAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_webhooks(self, options: GetWebhooksOptionsArg = None) -> Webhooks:
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
    def create_webhook(self, request_body: CreateWebhookRequestBodyArg) -> Webhook:
        """
        Creates a webhook.
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/webhooks']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth))
        return Webhook.from_dict(json.loads(response.text))
    def get_webhook_by_id(self, webhook_id: str) -> Webhook:
        """
        Retrieves a specific webhook
        :param webhook_id: The ID of the webhook.
            Example: "3321123"
        :type webhook_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/webhooks/', webhook_id]), FetchOptions(method='GET', auth=self.auth))
        return Webhook.from_dict(json.loads(response.text))
    def update_webhook_by_id(self, webhook_id: str, request_body: UpdateWebhookByIdRequestBodyArg) -> Webhook:
        """
        Updates a webhook.
        :param webhook_id: The ID of the webhook.
            Example: "3321123"
        :type webhook_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/webhooks/', webhook_id]), FetchOptions(method='PUT', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth))
        return Webhook.from_dict(json.loads(response.text))
    def delete_webhook_by_id(self, webhook_id: str):
        """
        Deletes a webhook.
        :param webhook_id: The ID of the webhook.
            Example: "3321123"
        :type webhook_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/webhooks/', webhook_id]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content