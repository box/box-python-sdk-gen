# MetadataCascadePoliciesManager

## List metadata cascade policies

Retrieves a list of all the metadata cascade policies
that are applied to a given folder. This can not be used on the root
folder with ID &#x60;0&#x60;.

This operation is performed by calling function `get_metadata_cascade_policies`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-metadata-cascade-policies/).

*Currently we don't have an example for calling `get_metadata_cascade_policies` in integration tests*

### Arguments

- query_params `GetMetadataCascadePoliciesQueryParamsArg`
  - Used as queryParams for the API call


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

- request_body `CreateMetadataCascadePolicyRequestBodyArg`
  - Used as requestBody for the API call


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
  - The ID of the metadata cascade policy.
  - Used as `metadata_cascade_policy_id` in path `path` of the API call


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
  - The ID of the metadata cascade policy.
  - Used as `metadata_cascade_policy_id` in path `path` of the API call


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
  - The ID of the cascade policy to force-apply.
  - Used as `metadata_cascade_policy_id` in path `path` of the API call
- request_body `CreateMetadataCascadePolicyApplyRequestBodyArg`
  - Used as requestBody for the API call


