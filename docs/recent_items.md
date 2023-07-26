# RecentItemsManager

## List recently accessed items

Returns information about the recent items accessed
by a user, either in the last 90 days or up to the last
1000 items accessed.

This operation is performed by calling function `get_recent_items`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-recent-items/).

*Currently we don't have an example for calling `get_recent_items` in integration tests*

### Arguments

- query_params `Optional[GetRecentItemsQueryParamsArg]`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `RecentItems`.

Returns a list recent items access by a user.


