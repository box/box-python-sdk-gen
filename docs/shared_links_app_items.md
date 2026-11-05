# SharedLinksAppItemsManager

<!-- box-python-sdk-gen deprecation banner -->
> [!CAUTION]
> **`box-python-sdk-gen` is deprecated and no longer maintained.** As of September 17, 2025, it receives no new features, bug fixes, or security patches. Do not use it for new projects.
>
> Use [`box-python-sdk`](https://github.com/box/box-python-sdk) v10+ instead: `pip install "boxsdk>=10"`.
> The equivalent of this page is [box-python-sdk/docs/shared_links_app_items.md](https://github.com/box/box-python-sdk/blob/main/docs/shared_links_app_items.md). To migrate existing code, see the [migration guide](https://github.com/box/box-python-sdk/blob/main/migration-guides/from-box-python-sdk-gen-v1-to-box-python-sdk.md).

- [Find app item for shared link](#find-app-item-for-shared-link)

## Find app item for shared link

Returns the app item represented by a shared link.

The link can originate from the current enterprise or another.

This operation is performed by calling function `find_app_item_for_shared_link`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-shared-items--app-items/).

<!-- sample get_shared_items#app_items -->

```python
client.shared_links_app_items.find_app_item_for_shared_link(
    "".join(["shared_link=", app_item_shared_link])
)
```

### Arguments

- boxapi `str`
  - A header containing the shared link and optional password for the shared link. The format for this header is `shared_link=[link]&shared_link_password=[password]`.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `AppItem`.

Returns a full app item resource if the shared link is valid and
the user has access to it.
