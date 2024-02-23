# SignRequestsManager

- [Cancel sign request](#cancel-sign-request)
- [Resend sign request](#resend-sign-request)
- [Get sign request by ID](#get-sign-request-by-id)
- [List sign requests](#list-sign-requests)
- [Create sign request](#create-sign-request)

## Cancel sign request

Cancels a sign request.

This operation is performed by calling function `cancel_sign_request`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-sign-requests-id-cancel/).

<!-- sample post_sign_requests_id_cancel -->

```python
client.sign_requests.cancel_sign_request(sign_request_id=created_sign_request.id)
```

### Arguments

- sign_request_id `str`
  - The ID of the sign request Example: "33243242"
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `SignRequest`.

Returns a Sign Request object.

## Resend sign request

Resends a sign request email to all outstanding signers.

This operation is performed by calling function `resend_sign_request`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-sign-requests-id-resend/).

_Currently we don't have an example for calling `resend_sign_request` in integration tests_

### Arguments

- sign_request_id `str`
  - The ID of the sign request Example: "33243242"
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `None`.

Returns an empty response when the API call was successful.
The email notifications will be sent asynchronously.

## Get sign request by ID

Gets a sign request by ID.

This operation is performed by calling function `get_sign_request_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-sign-requests-id/).

<!-- sample get_sign_requests_id -->

```python
client.sign_requests.get_sign_request_by_id(sign_request_id=created_sign_request.id)
```

### Arguments

- sign_request_id `str`
  - The ID of the sign request Example: "33243242"
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `SignRequest`.

Returns a sign request

## List sign requests

Gets sign requests created by a user. If the `sign_files` and/or
`parent_folder` are deleted, the sign request will not return in the list.

This operation is performed by calling function `get_sign_requests`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-sign-requests/).

<!-- sample get_sign_requests -->

```python
client.sign_requests.get_sign_requests()
```

### Arguments

- marker `Optional[str]`
  - Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination. This requires `usemarker` to be set to `true`.
- limit `Optional[int]`
  - The maximum number of items to return per page.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `SignRequests`.

Returns a collection of sign requests

## Create sign request

Creates a sign request. This involves preparing a document for signing and
sending the sign request to signers.

This operation is performed by calling function `create_sign_request`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-sign-requests/).

<!-- sample post_sign_requests -->

```python
client.sign_requests.create_sign_request(source_files=[FileBase(id=file_to_sign.id, type=FileBaseTypeField.FILE.value)], signers=[SignRequestCreateSigner(email=signer_1_email, signer_group_id='user'), SignRequestCreateSigner(email=signer_2_email, signer_group_id='user')], parent_folder=FolderMini(id=destination_folder.id, type=FolderBaseTypeField.FOLDER.value))
```

### Arguments

- source_files `Optional[List[FileBase]]`
  - List of files to create a signing document from. This is currently limited to ten files. Only the ID and type fields are required for each file.
- signature_color `Optional[CreateSignRequestSignatureColor]`
  - Force a specific color for the signature (blue, black, or red)
- signers `List[SignRequestCreateSigner]`
  - Array of signers for the sign request. 35 is the max number of signers permitted.
- parent_folder `Optional[FolderMini]`
  -
- is_document_preparation_needed `Optional[bool]`
  - Indicates if the sender should receive a `prepare_url` in the response to complete document preparation via UI.
- redirect_url `Optional[str]`
  - When specified, signature request will be redirected to this url when a document is signed.
- declined_redirect_url `Optional[str]`
  - The uri that a signer will be redirected to after declining to sign a document.
- are_text_signatures_enabled `Optional[bool]`
  - Disables the usage of signatures generated by typing (text).
- email_subject `Optional[str]`
  - Subject of sign request email. This is cleaned by sign request. If this field is not passed, a default subject will be used.
- email_message `Optional[str]`
  - Message to include in sign request email. The field is cleaned through sanitization of specific characters. However, some html tags are allowed. Links included in the message are also converted to hyperlinks in the email. The message may contain the following html tags including `a`, `abbr`, `acronym`, `b`, `blockquote`, `code`, `em`, `i`, `ul`, `li`, `ol`, and `strong`. Be aware that when the text to html ratio is too high, the email may end up in spam filters. Custom styles on these tags are not allowed. If this field is not passed, a default message will be used.
- are_reminders_enabled `Optional[bool]`
  - Reminds signers to sign a document on day 3, 8, 13 and 18. Reminders are only sent to outstanding signers.
- name `Optional[str]`
  - Name of the sign request.
- prefill_tags `Optional[List[SignRequestPrefillTag]]`
  - When a document contains sign related tags in the content, you can prefill them using this `prefill_tags` by referencing the 'id' of the tag as the `external_id` field of the prefill tag.
- days_valid `Optional[int]`
  - Set the number of days after which the created signature request will automatically expire if not completed. By default, we do not apply any expiration date on signature requests, and the signature request does not expire.
- external_id `Optional[str]`
  - This can be used to reference an ID in an external system that the sign request is related to.
- is_phone_verification_required_to_view `Optional[bool]`
  - Forces signers to verify a text message prior to viewing the document. You must specify the phone number of signers to have this setting apply to them.
- template_id `Optional[str]`
  - When a signature request is created from a template this field will indicate the id of that template.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `SignRequest`.

Returns a Sign Request object.
