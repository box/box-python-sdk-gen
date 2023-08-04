<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [EmailAliasesManager](#emailaliasesmanager)
  - [List user&#x27;s email aliases](#list-userx27s-email-aliases)
    - [Arguments](#arguments)
    - [Returns](#returns)
  - [Create email alias](#create-email-alias)
    - [Arguments](#arguments-1)
    - [Returns](#returns-1)
  - [Remove email alias](#remove-email-alias)
    - [Arguments](#arguments-2)
    - [Returns](#returns-2)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# EmailAliasesManager

## List user&#x27;s email aliases

Retrieves all email aliases for a user. The collection
does not include the primary login for the user.

This operation is performed by calling function `get_user_email_aliases`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/get-users-id-email-aliases/).

*Currently we don't have an example for calling `get_user_email_aliases` in integration tests*

### Arguments

- user_id `str`
  - The ID of the user.
  - Used as `user_id` in path `path` of the API call


### Returns

This function returns a value of type `EmailAliases`.

Returns a collection of email aliases.


## Create email alias

Adds a new email alias to a user account..

This operation is performed by calling function `create_user_email_alias`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-users-id-email-aliases/).

*Currently we don't have an example for calling `create_user_email_alias` in integration tests*

### Arguments

- user_id `str`
  - The ID of the user.
  - Used as `user_id` in path `path` of the API call
- request_body `CreateUserEmailAliasRequestBodyArg`
  - Used as requestBody for the API call


### Returns

This function returns a value of type `EmailAlias`.

Returns the newly created email alias object.


## Remove email alias

Removes an email alias from a user.

This operation is performed by calling function `delete_user_email_alias_by_id`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/delete-users-id-email-aliases-id/).

*Currently we don't have an example for calling `delete_user_email_alias_by_id` in integration tests*

### Arguments

- user_id `str`
  - The ID of the user.
  - Used as `user_id` in path `path` of the API call
- email_alias_id `str`
  - The ID of the email alias.
  - Used as `email_alias_id` in path `path` of the API call


### Returns

This function returns a value of type `None`.

Removes the alias and returns an empty response.


