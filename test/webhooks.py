from box_sdk_gen.utils import to_string

import pytest

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import FolderFull

from box_sdk_gen.managers.folders import CreateFolderParentArg

from box_sdk_gen.schemas import Webhook

from box_sdk_gen.managers.webhooks import CreateWebhookTargetArg

from box_sdk_gen.managers.webhooks import CreateWebhookTargetArgTypeField

from box_sdk_gen.managers.webhooks import CreateWebhookTriggersArg

from box_sdk_gen.schemas import Webhooks

from box_sdk_gen.utils import get_uuid

from test.commons import get_default_client

client: BoxClient = get_default_client()


def testWebhooksCRUD():
    folder: FolderFull = client.folders.create_folder(
        name=get_uuid(), parent=CreateFolderParentArg(id='0')
    )
    webhook: Webhook = client.webhooks.create_webhook(
        target=CreateWebhookTargetArg(
            id=folder.id, type=CreateWebhookTargetArgTypeField.FOLDER.value
        ),
        address='https://example.com/new-webhook',
        triggers=[CreateWebhookTriggersArg.FILE_UPLOADED.value],
    )
    assert webhook.target.id == folder.id
    assert to_string(webhook.target.type) == 'folder'
    assert len(webhook.triggers) == len(['FILE.UPLOADED'])
    assert webhook.address == 'https://example.com/new-webhook'
    webhooks: Webhooks = client.webhooks.get_webhooks()
    assert len(webhooks.entries) > 0
    webhook_from_api: Webhook = client.webhooks.get_webhook_by_id(webhook_id=webhook.id)
    assert webhook.id == webhook_from_api.id
    assert webhook.target.id == webhook_from_api.target.id
    assert webhook.address == webhook_from_api.address
    updated_webhook: Webhook = client.webhooks.update_webhook_by_id(
        webhook_id=webhook.id, address='https://example.com/updated-webhook'
    )
    assert updated_webhook.id == webhook.id
    assert updated_webhook.address == 'https://example.com/updated-webhook'
    client.webhooks.delete_webhook_by_id(webhook_id=webhook.id)
    with pytest.raises(Exception):
        client.webhooks.delete_webhook_by_id(webhook_id=webhook.id)
    client.folders.delete_folder_by_id(folder_id=folder.id)
