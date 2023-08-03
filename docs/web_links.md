# WebLinksManager

## Create web link

Creates a web link object within a folder.

This operation is performed by calling function `create_web_link`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-web-links/).

<!-- sample post_web_links -->
```python
client.web_links.create_web_link(CreateWebLinkRequestBodyArg(url&#x3D;url, parent&#x3D;parent, name&#x3D;name, description&#x3D;description))
```

### Arguments

- request_body `CreateWebLinkRequestBodyArg`
  - Used as requestBody for the API call
- headers `CreateWebLinkHeadersArg`
  - Used as headers for the API call


### Returns

This function returns a value of type `WebLink`.

Returns the newly created web link object.


## Get web link

Retrieve information about a web link.

This operation is performed by calling function `get_web_link_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-web-links-id/).

<!-- sample get_web_links_id -->
```python
client.web_links.get_web_link_by_id(weblink.id)
```

### Arguments

- web_link_id `str`
  - The ID of the web link.
  - Used as `web_link_id` in path `path` of the API call
- headers `GetWebLinkByIdHeadersArg`
  - Used as headers for the API call


### Returns

This function returns a value of type `WebLink`.

Returns the web link object.


## Update web link

Updates a web link object.

This operation is performed by calling function `update_web_link_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/put-web-links-id/).

<!-- sample put_web_links_id -->
```python
client.web_links.update_web_link_by_id(weblink.id, UpdateWebLinkByIdRequestBodyArg(name&#x3D;updated_name, shared_link&#x3D;UpdateWebLinkByIdRequestBodyArgSharedLinkField(access&#x3D;shared_access, password&#x3D;password)))
```

### Arguments

- web_link_id `str`
  - The ID of the web link.
  - Used as `web_link_id` in path `path` of the API call
- request_body `UpdateWebLinkByIdRequestBodyArg`
  - Used as requestBody for the API call
- headers `UpdateWebLinkByIdHeadersArg`
  - Used as headers for the API call


### Returns

This function returns a value of type `WebLink`.

Returns the updated web link object.


## Remove web link

Deletes a web link.

This operation is performed by calling function `delete_web_link_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-web-links-id/).

<!-- sample delete_web_links_id -->
```python
client.web_links.delete_web_link_by_id(weblink.id)
```

### Arguments

- web_link_id `str`
  - The ID of the web link.
  - Used as `web_link_id` in path `path` of the API call
- headers `DeleteWebLinkByIdHeadersArg`
  - Used as headers for the API call


### Returns

This function returns a value of type `None`.

An empty response will be returned when the web link
was successfully deleted.


