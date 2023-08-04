<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [CollaborationAllowlistEntriesManager](#collaborationallowlistentriesmanager)
  - [List allowed collaboration domains](#list-allowed-collaboration-domains)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Add domain to list of allowed collaboration domains](#add-domain-to-list-of-allowed-collaboration-domains)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)
  - [Get allowed collaboration domain](#get-allowed-collaboration-domain)
    - [Arguments](#arguments-2)
    - [Returns](#returns-2)
  - [Remove domain from list of allowed collaboration domains](#remove-domain-from-list-of-allowed-collaboration-domains)
    - [Arguments](#arguments-3)
    - [Returns](#returns-3)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

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


### Returns

This function returns a value of type `None`.

A blank response is returned if the entry was
successfully deleted.


