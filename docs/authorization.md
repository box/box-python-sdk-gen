<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [AuthorizationManager](#authorizationmanager)
  - [Authorize user](#authorize-user)
    - [Arguments](#arguments)
    - [Returns](#returns)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# AuthorizationManager

## Authorize user

Authorize a user by sending them through the [Box](https://box.com)
website and request their permission to act on their behalf.

This is the first step when authenticating a user using
OAuth 2.0. To request a user&#x27;s authorization to use the Box APIs
on their behalf you will need to send a user to the URL with this
format.

This operation is performed by calling function `get_authorize`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-authorize/).

*Currently we don't have an example for calling `get_authorize` in integration tests*

### Arguments

- query_params `GetAuthorizeQueryParamsArg`
  - Used as queryParams for the API call


### Returns

This function returns a value of type `None`.

Does not return any data, but rather should be used in the browser.


