# FileClassificationsManager


- [Get classification on file](#get-classification-on-file)
- [Add classification to file](#add-classification-to-file)
- [Remove classification from file](#remove-classification-from-file)

## Get classification on file

Retrieves the classification metadata instance that
has been applied to a file.

This API can also be called by including the enterprise ID in the
URL explicitly, for example
`/files/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

This operation is performed by calling function `get_file_metadata_enterprise_security_classification_6_vm_vochw_u_wo`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-files-id-metadata-enterprise-security-classification-6-vm-vochw-u-wo/).

*Currently we don't have an example for calling `get_file_metadata_enterprise_security_classification_6_vm_vochw_u_wo` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`. Example: "12345"
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


### Returns

This function returns a value of type `Classification`.

Returns an instance of the `securityClassification` metadata
template, which contains a `Box__Security__Classification__Key`
field that lists all the classifications available to this
enterprise.


## Add classification to file

Adds a classification to a file by specifying the label of the
classification to add.

This API can also be called by including the enterprise ID in the
URL explicitly, for example
`/files/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

This operation is performed by calling function `create_file_metadata_enterprise_security_classification`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-files-id-metadata-enterprise-security-classification-6-vm-vochw-u-wo/).

*Currently we don't have an example for calling `create_file_metadata_enterprise_security_classification` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`. Example: "12345"
- box_security_classification_key `Optional[str]`
  - The name of the classification to apply to this file.  To list the available classifications in an enterprise, use the classification API to retrieve the [classification template](e://get_metadata_templates_enterprise_securityClassification-6VMVochwUWo_schema) which lists all available classification keys.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


### Returns

This function returns a value of type `Classification`.

Returns the classification template instance
that was applied to the file.


## Remove classification from file

Removes any classifications from a file.

This API can also be called by including the enterprise ID in the
URL explicitly, for example
`/files/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

This operation is performed by calling function `delete_file_metadata_enterprise_security_classification`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-files-id-metadata-enterprise-security-classification-6-vm-vochw-u-wo/).

*Currently we don't have an example for calling `delete_file_metadata_enterprise_security_classification` in integration tests*

### Arguments

- file_id `str`
  - The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`. Example: "12345"
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


### Returns

This function returns a value of type `None`.

Returns an empty response when the classification is
successfully deleted.


