# MetadataCascadePoliciesManager


- [List metadata cascade policies](#list-metadata-cascade-policies)
- [Create metadata cascade policy](#create-metadata-cascade-policy)
- [Get metadata cascade policy](#get-metadata-cascade-policy)
- [Remove metadata cascade policy](#remove-metadata-cascade-policy)
- [Force-apply metadata cascade policy to folder](#force-apply-metadata-cascade-policy-to-folder)

## List metadata cascade policies

Retrieves a list of all the metadata cascade policies
that are applied to a given folder. This can not be used on the root
folder with ID `0`.

This operation is performed by calling function `get_metadata_cascade_policies`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-metadata-cascade-policies/).

*Currently we don't have an example for calling `get_metadata_cascade_policies` in integration tests*

### Arguments

- folder_id `str`
  - Specifies which folder to return policies for. This can not be used on the root folder with ID `0`.
- owner_enterprise_id `Optional[str]`
  - The ID of the enterprise ID for which to find metadata cascade policies. If not specified, it defaults to the current enterprise.
- marker `Optional[str]`
  - Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.
- offset `Optional[int]`
  - The offset of the item at which to begin the response.  Queries with offset parameter value exceeding 10000 will be rejected with a 400 response.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


### Returns

This function returns a value of type `MetadataCascadePolicies`.

Returns a list of metadata cascade policies


## Create metadata cascade policy

Creates a new metadata cascade policy that applies a given
metadata template to a given folder and automatically
cascades it down to any files within that folder.

In order for the policy to be applied a metadata instance must first
be applied to the folder the policy is to be applied to.

This operation is performed by calling function `create_metadata_cascade_policy`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-metadata-cascade-policies/).

*Currently we don't have an example for calling `create_metadata_cascade_policy` in integration tests*

### Arguments

- folder_id `str`
  - The ID of the folder to apply the policy to. This folder will need to already have an instance of the targeted metadata template applied to it.
- scope `CreateMetadataCascadePolicyScopeArg`
  - The scope of the targeted metadata template. This template will need to already have an instance applied to the targeted folder.
- template_key `str`
  - The key of the targeted metadata template. This template will need to already have an instance applied to the targeted folder.  In many cases the template key is automatically derived of its display name, for example `Contract Template` would become `contractTemplate`. In some cases the creator of the template will have provided its own template key.  Please [list the templates for an enterprise][list], or get all instances on a [file][file] or [folder][folder] to inspect a template's key.  [list]: e://get-metadata-templates-enterprise [file]: e://get-files-id-metadata [folder]: e://get-folders-id-metadata
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


### Returns

This function returns a value of type `MetadataCascadePolicy`.

Returns a new of metadata cascade policy


## Get metadata cascade policy

Retrieve a specific metadata cascade policy assigned to a folder.

This operation is performed by calling function `get_metadata_cascade_policy_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-metadata-cascade-policies-id/).

*Currently we don't have an example for calling `get_metadata_cascade_policy_by_id` in integration tests*

### Arguments

- metadata_cascade_policy_id `str`
  - The ID of the metadata cascade policy. Example: "6fd4ff89-8fc1-42cf-8b29-1890dedd26d7"
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


### Returns

This function returns a value of type `MetadataCascadePolicy`.

Returns a metadata cascade policy


## Remove metadata cascade policy

Deletes a metadata cascade policy.

This operation is performed by calling function `delete_metadata_cascade_policy_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-metadata-cascade-policies-id/).

*Currently we don't have an example for calling `delete_metadata_cascade_policy_by_id` in integration tests*

### Arguments

- metadata_cascade_policy_id `str`
  - The ID of the metadata cascade policy. Example: "6fd4ff89-8fc1-42cf-8b29-1890dedd26d7"
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


### Returns

This function returns a value of type `None`.

Returns an empty response when the policy
is successfully deleted.


## Force-apply metadata cascade policy to folder

Force the metadata on a folder with a metadata cascade policy to be applied to
all of its children. This can be used after creating a new cascade policy to
enforce the metadata to be cascaded down to all existing files within that
folder.

This operation is performed by calling function `create_metadata_cascade_policy_apply`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-metadata-cascade-policies-id-apply/).

*Currently we don't have an example for calling `create_metadata_cascade_policy_apply` in integration tests*

### Arguments

- metadata_cascade_policy_id `str`
  - The ID of the cascade policy to force-apply. Example: "6fd4ff89-8fc1-42cf-8b29-1890dedd26d7"
- conflict_resolution `CreateMetadataCascadePolicyApplyConflictResolutionArg`
  - Describes the desired behavior when dealing with the conflict where a metadata template already has an instance applied to a child.  * `none` will preserve the existing value on the file * `overwrite` will force-apply the templates values over   any existing values.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


### Returns

This function returns a value of type `None`.

Returns an empty response when the API call was successful. The metadata
cascade operation will be performed asynchronously.

The API call will return directly, before the cascade operation
is complete. There is currently no API to check for the status of this
operation.


