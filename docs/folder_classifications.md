# FolderClassificationsManager


- [Get classification on folder](#get-classification-on-folder)
- [Add classification to folder](#add-classification-to-folder)
- [Remove classification from folder](#remove-classification-from-folder)

## Get classification on folder

Retrieves the classification metadata instance that
has been applied to a folder.

This API can also be called by including the enterprise ID in the
URL explicitly, for example
`/folders/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

This operation is performed by calling function `get_folder_metadata_enterprise_security_classification_6_vm_vochw_u_wo`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-folders-id-metadata-enterprise-security-classification-6-vm-vochw-u-wo/).

*Currently we don't have an example for calling `get_folder_metadata_enterprise_security_classification_6_vm_vochw_u_wo` in integration tests*

### Arguments

- folder_id `str`
  - The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`. Example: "12345"
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


### Returns

This function returns a value of type `Classification`.

Returns an instance of the `securityClassification` metadata
template, which contains a `Box__Security__Classification__Key`
field that lists all the classifications available to this
enterprise.


## Add classification to folder

Adds a classification to a folder by specifying the label of the
classification to add.

This API can also be called by including the enterprise ID in the
URL explicitly, for example
`/folders/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

This operation is performed by calling function `create_folder_metadata_enterprise_security_classification`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-folders-id-metadata-enterprise-security-classification-6-vm-vochw-u-wo/).

*Currently we don't have an example for calling `create_folder_metadata_enterprise_security_classification` in integration tests*

### Arguments

- folder_id `str`
  - The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`. Example: "12345"
- box_security_classification_key `Optional[str]`
  - The name of the classification to apply to this folder.  To list the available classifications in an enterprise, use the classification API to retrieve the [classification template](e://get_metadata_templates_enterprise_securityClassification-6VMVochwUWo_schema) which lists all available classification keys.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


### Returns

This function returns a value of type `Classification`.

Returns the classification template instance
that was applied to the folder.


## Remove classification from folder

Removes any classifications from a folder.

This API can also be called by including the enterprise ID in the
URL explicitly, for example
`/folders/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

This operation is performed by calling function `delete_folder_metadata_enterprise_security_classification`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-folders-id-metadata-enterprise-security-classification-6-vm-vochw-u-wo/).

*Currently we don't have an example for calling `delete_folder_metadata_enterprise_security_classification` in integration tests*

### Arguments

- folder_id `str`
  - The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`. Example: "12345"
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


### Returns

This function returns a value of type `None`.

Returns an empty response when the classification is
successfully deleted.


