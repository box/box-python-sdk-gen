# SessionTerminationManager

<!-- box-python-sdk-gen deprecation banner -->
> [!CAUTION]
> **`box-python-sdk-gen` is deprecated and no longer maintained.** As of September 17, 2025, it receives no new features, bug fixes, or security patches. Do not use it for new projects.
>
> Use [`box-python-sdk`](https://github.com/box/box-python-sdk) v10+ instead: `pip install "boxsdk>=10"`.
> The equivalent of this page is [box-python-sdk/docs/session_termination.md](https://github.com/box/box-python-sdk/blob/main/docs/session_termination.md). To migrate existing code, see the [migration guide](https://github.com/box/box-python-sdk/blob/main/migration-guides/from-box-python-sdk-gen-v1-to-box-python-sdk.md).

- [Create jobs to terminate users session](#create-jobs-to-terminate-users-session)
- [Create jobs to terminate user group session](#create-jobs-to-terminate-user-group-session)

## Create jobs to terminate users session

Validates the roles and permissions of the user,
and creates asynchronous jobs
to terminate the user's sessions.
Returns the status for the POST request.

This operation is performed by calling function `terminate_users_sessions`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-users-terminate-sessions/).

<!-- sample post_users_terminate_sessions -->

```python
client.session_termination.terminate_users_sessions(
    [get_env_var("USER_ID")], [user.login]
)
```

### Arguments

- user_ids `List[str]`
  - A list of user IDs.
- user_logins `List[str]`
  - A list of user logins.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `SessionTerminationMessage`.

Returns a message about the request status.

## Create jobs to terminate user group session

Validates the roles and permissions of the group,
and creates asynchronous jobs
to terminate the group's sessions.
Returns the status for the POST request.

This operation is performed by calling function `terminate_groups_sessions`.

See the endpoint docs at
[API Reference](https://developer.box.com/reference/post-groups-terminate-sessions/).

<!-- sample post_groups_terminate_sessions -->

```python
client.session_termination.terminate_groups_sessions([group.id])
```

### Arguments

- group_ids `List[str]`
  - A list of group IDs.
- extra_headers `Optional[Dict[str, Optional[str]]]`
  - Extra headers that will be included in the HTTP request.

### Returns

This function returns a value of type `SessionTerminationMessage`.

Returns a message about the request status.
