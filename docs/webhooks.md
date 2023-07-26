# WebhooksManager

## List all webhooks

Returns all defined webhooks for the requesting application.

This API only returns webhooks that are applied to files or folders that are
owned by the authenticated user. This means that an admin can not see webhooks
created by a service account unless the admin has access to those folders, and
vice versa.

This operation is performed by calling function `get_webhooks`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-webhooks/).

<!-- sample get_webhooks -->
```python
client.webhooks.get_webhooks()
```

### Arguments

- query_params `Optional[GetWebhooksQueryParamsArg]`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `Webhooks`.

Returns a list of webhooks.


## Create webhook

Creates a webhook.

This operation is performed by calling function `create_webhook`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-webhooks/).

<!-- sample post_webhooks -->
```python
client.webhooks.create_webhook(CreateWebhookRequestBodyArg(target&#x3D;CreateWebhookRequestBodyArgTargetField(id&#x3D;folder.id, type&#x3D;CreateWebhookRequestBodyArgTargetFieldTypeField.FOLDER.value), address&#x3D;&#x27;https://example.com/new-webhook&#x27;, triggers&#x3D;[&#x27;FILE.UPLOADED&#x27;]))
```

### Arguments

- request_body `CreateWebhookRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `Webhook`.

Returns the new webhook object.


## Get webhook

Retrieves a specific webhook

This operation is performed by calling function `get_webhook_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-webhooks-id/).

<!-- sample get_webhooks_id -->
```python
client.webhooks.get_webhook_by_id(webhook.id)
```

### Arguments

- webhook_id `str`
  - The ID of the webhook.
  - Used as `webhook_id` in path `path` of the API call


### Returns

This function returns a value of type `Webhook`.

Returns a webhook object


## Update webhook

Updates a webhook.

This operation is performed by calling function `update_webhook_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-webhooks-id/).

<!-- sample put_webhooks_id -->
```python
client.webhooks.update_webhook_by_id(webhook.id, UpdateWebhookByIdRequestBodyArg(address&#x3D;&#x27;https://example.com/updated-webhook&#x27;))
```

### Arguments

- webhook_id `str`
  - The ID of the webhook.
  - Used as `webhook_id` in path `path` of the API call
- request_body `UpdateWebhookByIdRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `Webhook`.

Returns the new webhook object.


## Remove webhook

Deletes a webhook.

This operation is performed by calling function `delete_webhook_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-webhooks-id/).

<!-- sample delete_webhooks_id -->
```python
client.webhooks.delete_webhook_by_id(webhook.id)
```

### Arguments

- webhook_id `str`
  - The ID of the webhook.
  - Used as `webhook_id` in path `path` of the API call


