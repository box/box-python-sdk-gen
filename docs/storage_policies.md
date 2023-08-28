# StoragePoliciesManager


- [List storage policies](#list-storage-policies)
- [Get storage policy](#get-storage-policy)

## List storage policies

Fetches all the storage policies in the enterprise.
Only a Primary Admin can access this endpoint. The user
needs to generate a token for an account to authenticate this request.

This operation is performed by calling function `get_storage_policies`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-storage-policies/).

*Currently we don't have an example for calling `get_storage_policies` in integration tests*

### Arguments

- fields `Optional[str]`
  - A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.
- marker `Optional[str]`
  - Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.
- limit `Optional[int]`
  - The maximum number of items to return per page.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


### Returns

This function returns a value of type `StoragePolicies`.

Returns a collection of storage policies.


## Get storage policy

Fetches a specific storage policy. Only a Primary Admin can access this endpoint. The user needs to generate a token for an account to authenticate this request.

This operation is performed by calling function `get_storage_policy_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-storage-policies-id/).

*Currently we don't have an example for calling `get_storage_policy_by_id` in integration tests*

### Arguments

- storage_policy_id `str`
  - The ID of the storage policy. Example: "34342"
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.


### Returns

This function returns a value of type `StoragePolicy`.

Returns a storage policy object.


