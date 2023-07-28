from enum import Enum

from typing import Optional

from box_sdk.base_object import BaseObject

from typing import Dict

import json

from typing import List

from typing import Union

from box_sdk.base_object import BaseObject

from box_sdk.schemas import Webhooks

from box_sdk.schemas import ClientError

from box_sdk.schemas import Webhook

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.utils import prepare_params

from box_sdk.utils import to_string

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class CreateWebhookTargetArgTypeField(str, Enum):
    FILE = 'file'
    FOLDER = 'folder'

class CreateWebhookTargetArg(BaseObject):
    def __init__(self, id: Optional[str] = None, type: Optional[CreateWebhookTargetArgTypeField] = None, **kwargs):
        """
        :param id: The ID of the item to trigger a webhook
        :type id: Optional[str], optional
        :param type: The type of item to trigger a webhook
        :type type: Optional[CreateWebhookTargetArgTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type

class UpdateWebhookByIdTargetArgTypeField(str, Enum):
    FILE = 'file'
    FOLDER = 'folder'

class UpdateWebhookByIdTargetArg(BaseObject):
    def __init__(self, id: Optional[str] = None, type: Optional[UpdateWebhookByIdTargetArgTypeField] = None, **kwargs):
        """
        :param id: The ID of the item to trigger a webhook
        :type id: Optional[str], optional
        :param type: The type of item to trigger a webhook
        :type type: Optional[UpdateWebhookByIdTargetArgTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type

class WebhooksManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def get_webhooks(self, marker: Optional[str] = None, limit: Optional[int] = None) -> Webhooks:
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
        """
        query_params_map: Dict[str, str] = prepare_params({'marker': to_string(marker), 'limit': to_string(limit)})
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/webhooks']), FetchOptions(method='GET', params=query_params_map, auth=self.auth, network_session=self.network_session))
        return Webhooks.from_dict(json.loads(response.text))
    def create_webhook(self, target: CreateWebhookTargetArg, address: str, triggers: List[Union[str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str]]) -> Webhook:
        """
        Creates a webhook.
        :param target: The item that will trigger the webhook
        :type target: CreateWebhookTargetArg
        :param address: The URL that is notified by this webhook
        :type address: str
        :param triggers: An array of event names that this webhook is
            to be triggered for
        :type triggers: List[Union[str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str]]
        """
        request_body: BaseObject = BaseObject(target=target, address=address, triggers=triggers)
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/webhooks']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return Webhook.from_dict(json.loads(response.text))
    def get_webhook_by_id(self, webhook_id: str) -> Webhook:
        """
        Retrieves a specific webhook
        :param webhook_id: The ID of the webhook.
            Example: "3321123"
        :type webhook_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/webhooks/', webhook_id]), FetchOptions(method='GET', auth=self.auth, network_session=self.network_session))
        return Webhook.from_dict(json.loads(response.text))
    def update_webhook_by_id(self, webhook_id: str, target: Optional[UpdateWebhookByIdTargetArg] = None, address: Optional[str] = None, triggers: Optional[List[Union[str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str]]] = None) -> Webhook:
        """
        Updates a webhook.
        :param webhook_id: The ID of the webhook.
            Example: "3321123"
        :type webhook_id: str
        :param target: The item that will trigger the webhook
        :type target: Optional[UpdateWebhookByIdTargetArg], optional
        :param address: The URL that is notified by this webhook
        :type address: Optional[str], optional
        :param triggers: An array of event names that this webhook is
            to be triggered for
        :type triggers: Optional[List[Union[str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str]]], optional
        """
        request_body: BaseObject = BaseObject(target=target, address=address, triggers=triggers)
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/webhooks/', webhook_id]), FetchOptions(method='PUT', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return Webhook.from_dict(json.loads(response.text))
    def delete_webhook_by_id(self, webhook_id: str):
        """
        Deletes a webhook.
        :param webhook_id: The ID of the webhook.
            Example: "3321123"
        :type webhook_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/webhooks/', webhook_id]), FetchOptions(method='DELETE', auth=self.auth, network_session=self.network_session))
        return response.content