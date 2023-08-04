<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [CollectionsManager](#collectionsmanager)
  - [List all collections](#list-all-collections)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [List collection items](#list-collection-items)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# CollectionsManager

## List all collections

Retrieves all collections for a given user.

Currently, only the &#x60;favorites&#x60; collection
is supported.

This operation is performed by calling function `get_collections`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-collections/).

*Currently we don't have an example for calling `get_collections` in integration tests*

### Arguments

- query_params `GetCollectionsQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `Collections`.

Returns all collections for the given user


## List collection items

Retrieves the files and/or folders contained within
this collection.

This operation is performed by calling function `get_collection_items`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-collections-id-items/).

*Currently we don't have an example for calling `get_collection_items` in integration tests*

### Arguments

- collection_id `str`
  - The ID of the collection.
  - Used as `collection_id` in path `path` of the API call
- query_params `GetCollectionItemsQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `Items`.

Returns an array of items in the collection.


