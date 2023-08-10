import pytest

from box_sdk_gen.managers.folders import CreateFolderParentArg

from box_sdk_gen.managers.webhooks import CreateWebhookTargetArg

from box_sdk_gen.managers.webhooks import CreateWebhookTargetArgTypeField

from box_sdk_gen.managers.webhooks import CreateWebhookTriggersArg

from box_sdk_gen.utils import decode_base_64

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.client import Client

from box_sdk_gen.jwt_auth import JWTAuth

from box_sdk_gen.jwt_auth import JWTConfig

jwt_config = JWTConfig.from_config_json_string(decode_base_64(get_env_var('JWT_CONFIG_BASE_64')))

auth: JWTAuth = JWTAuth(config=jwt_config)

client: Client = Client(auth=auth)

def testWebhooksCRUD():
    folder: FolderFull = client.folders.create_folder(name=get_uuid(), parent=CreateFolderParentArg(id='0'))
    webhook: Webhook = client.webhooks.create_webhook(target=CreateWebhookTargetArg(id=folder.id, type=CreateWebhookTargetArgTypeField.FOLDER.value), address='https://example.com/new-webhook', triggers=[CreateWebhookTriggersArg.FILE_UPLOADED.value])
    assert webhook.target.id == folder.id
    assert webhook.target.type == 'folder'
    assert len(webhook.triggers) == len(['FILE.UPLOADED'])
    assert webhook.address == 'https://example.com/new-webhook'
    webhooks: Webhooks = client.webhooks.get_webhooks()
    assert len(webhooks.entries) > 0
    webhook_from_api: Webhook = client.webhooks.get_webhook_by_id(webhook_id=webhook.id)
    assert webhook.id == webhook_from_api.id
    assert webhook.target.id == webhook_from_api.target.id
    assert webhook.address == webhook_from_api.address
    updated_webhook: Webhook = client.webhooks.update_webhook_by_id(webhook_id=webhook.id, address='https://example.com/updated-webhook')
    assert updated_webhook.id == webhook.id
    assert updated_webhook.address == 'https://example.com/updated-webhook'
    client.webhooks.delete_webhook_by_id(webhook_id=webhook.id)
    with pytest.raises(Exception):
        client.webhooks.delete_webhook_by_id(webhook_id=webhook.id)
    client.folders.delete_folder_by_id(folder_id=folder.id)