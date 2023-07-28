# CollaborationAllowlistEntriesManager

## List allowed collaboration domains

Returns the list domains that have been deemed safe to create collaborations
for within the current enterprise.

This operation is performed by calling function `get_collaboration_whitelist_entries`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-collaboration-whitelist-entries/).

*Currently we don't have an example for calling `get_collaboration_whitelist_entries` in integration tests*

### Arguments

- query_params `GetCollaborationWhitelistEntriesQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `CollaborationAllowlistEntries`.

Returns a collection of domains that are allowed for collaboration.


## Add domain to list of allowed collaboration domains

Creates a new entry in the list of allowed domains to allow
collaboration for.

This operation is performed by calling function `create_collaboration_whitelist_entry`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-collaboration-whitelist-entries/).

*Currently we don't have an example for calling `create_collaboration_whitelist_entry` in integration tests*

### Arguments

- request_body `CreateCollaborationWhitelistEntryRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `CollaborationAllowlistEntry`.

Returns a new entry on the list of allowed domains.


## Get allowed collaboration domain

Returns a domain that has been deemed safe to create collaborations
for within the current enterprise.

This operation is performed by calling function `get_collaboration_whitelist_entry_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-collaboration-whitelist-entries-id/).

*Currently we don't have an example for calling `get_collaboration_whitelist_entry_by_id` in integration tests*

### Arguments

- collaboration_whitelist_entry_id `str`
  - The ID of the entry in the list.
  - Used as `collaboration_whitelist_entry_id` in path `path` of the API call


### Returns

This function returns a value of type `CollaborationAllowlistEntry`.

Returns an entry on the list of allowed domains.


## Remove domain from list of allowed collaboration domains

Removes a domain from the list of domains that have been deemed safe to create
collaborations for within the current enterprise.

This operation is performed by calling function `delete_collaboration_whitelist_entry_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-collaboration-whitelist-entries-id/).

*Currently we don't have an example for calling `delete_collaboration_whitelist_entry_by_id` in integration tests*

### Arguments

- collaboration_whitelist_entry_id `str`
  - The ID of the entry in the list.
  - Used as `collaboration_whitelist_entry_id` in path `path` of the API call


