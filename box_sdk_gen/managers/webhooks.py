from enum import Enum

from typing import Optional

from box_sdk_gen.base_object import BaseObject

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import deserialize

from typing import List

from box_sdk_gen.serialization import serialize

from box_sdk_gen.schemas import Webhooks

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import Webhook

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.json_data import sd_to_json

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse

from box_sdk_gen.json_data import SerializedData


class CreateWebhookTargetTypeField(str, Enum):
    FILE = 'file'
    FOLDER = 'folder'


class CreateWebhookTarget(BaseObject):
    _discriminator = 'type', {'file', 'folder'}

    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[CreateWebhookTargetTypeField] = None,
        **kwargs
    ):
        """
        :param id: The ID of the item to trigger a webhook
        :type id: Optional[str], optional
        :param type: The type of item to trigger a webhook
        :type type: Optional[CreateWebhookTargetTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class CreateWebhookTriggers(str, Enum):
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
    SIGN_REQUEST_SIGNER_EMAIL_BOUNCED = 'SIGN_REQUEST.SIGNER_EMAIL_BOUNCED'


class UpdateWebhookByIdTargetTypeField(str, Enum):
    FILE = 'file'
    FOLDER = 'folder'


class UpdateWebhookByIdTarget(BaseObject):
    _discriminator = 'type', {'file', 'folder'}

    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[UpdateWebhookByIdTargetTypeField] = None,
        **kwargs
    ):
        """
        :param id: The ID of the item to trigger a webhook
        :type id: Optional[str], optional
        :param type: The type of item to trigger a webhook
        :type type: Optional[UpdateWebhookByIdTargetTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class UpdateWebhookByIdTriggers(str, Enum):
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
    SIGN_REQUEST_SIGNER_EMAIL_BOUNCED = 'SIGN_REQUEST.SIGNER_EMAIL_BOUNCED'


class WebhooksManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: NetworkSession = None,
    ):
        if network_session is None:
            network_session = NetworkSession()
        self.auth = auth
        self.network_session = network_session

    def get_webhooks(
        self,
        marker: Optional[str] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> Webhooks:
        """
        Returns all defined webhooks for the requesting application.

        This API only returns webhooks that are applied to files or folders that are


        owned by the authenticated user. This means that an admin can not see webhooks


        created by a service account unless the admin has access to those folders, and


        vice versa.

        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params(
            {'marker': to_string(marker), 'limit': to_string(limit)}
        )
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([self.network_session.base_urls.base_url, '/webhooks']),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, Webhooks)

    def create_webhook(
        self,
        target: CreateWebhookTarget,
        address: str,
        triggers: List[CreateWebhookTriggers],
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> Webhook:
        """
        Creates a webhook.
        :param target: The item that will trigger the webhook
        :type target: CreateWebhookTarget
        :param address: The URL that is notified by this webhook
        :type address: str
        :param triggers: An array of event names that this webhook is
            to be triggered for
        :type triggers: List[CreateWebhookTriggers]
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {
            'target': target,
            'address': address,
            'triggers': triggers,
        }
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([self.network_session.base_urls.base_url, '/webhooks']),
            FetchOptions(
                method='POST',
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, Webhook)

    def get_webhook_by_id(
        self, webhook_id: str, extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> Webhook:
        """
        Retrieves a specific webhook
        :param webhook_id: The ID of the webhook.
            Example: "3321123"
        :type webhook_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    self.network_session.base_urls.base_url,
                    '/webhooks/',
                    to_string(webhook_id),
                ]
            ),
            FetchOptions(
                method='GET',
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, Webhook)

    def update_webhook_by_id(
        self,
        webhook_id: str,
        target: Optional[UpdateWebhookByIdTarget] = None,
        address: Optional[str] = None,
        triggers: Optional[List[UpdateWebhookByIdTriggers]] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> Webhook:
        """
        Updates a webhook.
        :param webhook_id: The ID of the webhook.
            Example: "3321123"
        :type webhook_id: str
        :param target: The item that will trigger the webhook
        :type target: Optional[UpdateWebhookByIdTarget], optional
        :param address: The URL that is notified by this webhook
        :type address: Optional[str], optional
        :param triggers: An array of event names that this webhook is
            to be triggered for
        :type triggers: Optional[List[UpdateWebhookByIdTriggers]], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {
            'target': target,
            'address': address,
            'triggers': triggers,
        }
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    self.network_session.base_urls.base_url,
                    '/webhooks/',
                    to_string(webhook_id),
                ]
            ),
            FetchOptions(
                method='PUT',
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, Webhook)

    def delete_webhook_by_id(
        self, webhook_id: str, extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> None:
        """
        Deletes a webhook.
        :param webhook_id: The ID of the webhook.
            Example: "3321123"
        :type webhook_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    self.network_session.base_urls.base_url,
                    '/webhooks/',
                    to_string(webhook_id),
                ]
            ),
            FetchOptions(
                method='DELETE',
                headers=headers_map,
                response_format=None,
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return None
