# StoragePoliciesManager

<!-- box-python-sdk-gen deprecation banner -->
> [!CAUTION]
> **`box-python-sdk-gen` is deprecated and no longer maintained.** As of September 17, 2025, it receives no new features, bug fixes, or security patches. Do not use it for new projects.
>
> Use [`box-python-sdk`](https://github.com/box/box-python-sdk) v10+ instead: `pip install "boxsdk>=10"`.
> The equivalent of this page is [box-python-sdk/docs/storage_policies.md](https://github.com/box/box-python-sdk/blob/main/docs/storage_policies.md). To migrate existing code, see the [migration guide](https://github.com/box/box-python-sdk/blob/main/migration-guides/from-box-python-sdk-gen-v1-to-box-python-sdk.md).

- [List storage policies](#list-storage-policies)
- [Get storage policy](#get-storage-policy)

## List storage policies

Fetches all the storage policies in the enterprise.

This operation is performed by calling function `get_storage_policies`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-storage-policies/).

<!-- sample get_storage_policies -->

```python
client.storage_policies.get_storage_policies()
```

### Arguments

- fields `Optional[List[str]]`
  - A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response. Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.
- marker `Optional[str]`
  - Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination. This requires `usemarker` to be set to `true`.
- limit `Optional[int]`
  - The maximum number of items to return per page.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `StoragePolicies`.

Returns a collection of storage policies.

## Get storage policy

Fetches a specific storage policy.

This operation is performed by calling function `get_storage_policy_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-storage-policies-id/).

<!-- sample get_storage_policies_id -->

```python
client.storage_policies.get_storage_policy_by_id(storage_policy.id)
```

### Arguments

- storage_policy_id `str`
  - The ID of the storage policy. Example: "34342"
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `StoragePolicy`.

Returns a storage policy object.
