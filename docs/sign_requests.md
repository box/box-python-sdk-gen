# Sign Requests

Sign Requests are used to request e-signatures on documents from signers.  
A Sign Request can refer to one or more Box Files and can be sent to one or more Box Sign Request Signers.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Create Sign Request](#create-sign-request)
- [Get All Sign Requests](#get-all-sign-requests)
- [Get Sign Request by ID](#get-sign-request-by-id)
- [Cancel Sign Request](#cancel-sign-request)
- [Resend Sign Request](#resend-sign-request)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Create Sign Request

The `create_sign_request`method will create a Sign Request. You need to provide at least one file
(from which the signing document will be created) and at least one signer to receive the Sign Request.

```python
from box_sdk.schemas import SignRequestCreateSigner, FileBaseTypeField, FolderBaseTypeField, FileBase, FolderMini

destination_folder_id = '12345'
file_to_sign_id = '11111'
signer_email = 'signer@box.com'

created_sign_request = client.sign_requests.create_sign_request(
    signers=[SignRequestCreateSigner(email=signer_email)],
    parent_folder=FolderMini(id=destination_folder_id, type=FolderBaseTypeField.FOLDER.value),
    source_files=[FileBase(id=file_to_sign_id, type=FileBaseTypeField.FILE.value)]
)

print(f'(Sign Request ID: {created_sign_request.id})')
```

If you set `isDocumentPreparationNeeded` flag to true, you need to visit `prepareUrl` before the Sign Request will be sent.
For more information on `isDocumentPreparationNeeded` and the other parameters available, please refer to the [developer documentation](https://developer.box.com/guides/sign-request/).

# Get All Sign Requests

Calling the `get_sign_requests` will return `SignRequests` object that will allow getting access to all the Sign Requests.

```python
sign_requests = client.sign_requests.get_sign_requests()
for sign_request in sign_requests.entries:
    print(f'(Sign Request ID: {sign_request.id})')
```

# Get Sign Request by ID

Calling `get_sign_request_by_id` will return `SignRequest` object containing information about the Sign Request.

```python
sign_request = new_sign_request = client.sign_requests.get_sign_request_by_id('123456')
print(f'Sign Request ID is {sign_request.id}')
```

# Cancel Sign Request

Calling `cancel_sign_request` will cancel a created Sign Request.

```python
cancelled_sign_request = client.sign_requests.cancel_sign_request('123456')
print(f'Cancelled Sign Request status is {cancelled_sign_request.status}')
```

# Resend Sign Request

Calling `resend_sign_request` will resend a Sign Request to all signers that have not signed it yet.
There is an 10-minute cooling-off period between re-sending reminder emails.

```python
sign_request_to_resend_id = '123456'
client.sign_requests.resend_sign_request(sign_request_to_resend_id)
print(f'Sign Request with ID {sign_request_to_resend_id} was resent')
```
