# SharedLinksAppItemsManager

- [Find app item for shared link](#find-app-item-for-shared-link)

## Find app item for shared link

Returns the app item represented by a shared link.

The link can originate from the current enterprise or another.

This operation is performed by calling function `get_shared_item_app_items`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-shared-items--app-items/).

_Currently we don't have an example for calling `get_shared_item_app_items` in integration tests_

### Arguments

- boxapi `str`
  - A header containing the shared link and optional password for the shared link. The format for this header is `shared_link=[link]&shared_link_password=[password]`
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `AppItem`.

Returns a full app item resource if the shared link is valid and
the user has access to it.
