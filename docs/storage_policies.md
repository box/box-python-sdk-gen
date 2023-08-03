# StoragePoliciesManager

## List storage policies

Fetches all the storage policies in the enterprise.

This operation is performed by calling function `get_storage_policies`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-storage-policies/).

*Currently we don't have an example for calling `get_storage_policies` in integration tests*

### Arguments

- query_params `GetStoragePoliciesQueryParamsArg`
  - Used as queryParams for the API call
- headers `GetStoragePoliciesHeadersArg`
  - Used as headers for the API call


### Returns

This function returns a value of type `StoragePolicies`.

Returns a collection of storage policies.


## Get storage policy

Fetches a specific storage policy.

This operation is performed by calling function `get_storage_policy_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-storage-policies-id/).

*Currently we don't have an example for calling `get_storage_policy_by_id` in integration tests*

### Arguments

- storage_policy_id `str`
  - The ID of the storage policy.
  - Used as `storage_policy_id` in path `path` of the API call
- headers `GetStoragePolicyByIdHeadersArg`
  - Used as headers for the API call


### Returns

This function returns a value of type `StoragePolicy`.

Returns a storage policy object.


