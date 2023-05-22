# Authentication

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Authentication methods](#authentication-methods)
  - [Developer Token](#developer-token)
  - [JWT Auth](#jwt-auth)
    - [Authenticate Enterprise](#authenticate-enterprise)
    - [Authenticate user](#authenticate-user)
  - [Client Credentials Grant](#client-credentials-grant)
    - [Obtaining Service Account token](#obtaining-service-account-token)
    - [Obtaining User token](#obtaining-user-token)
    - [Switching between Service Account and User](#switching-between-service-account-and-user)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Authentication methods

## Developer Token

The fastest way to get started using the API is with developer token. A
developer token is simply a short-lived access token that cannot be refreshed
and can only be used with your own account. Therefore, they're only useful for
testing an app and aren't suitable for production. You can obtain a developer
token from your application's [developer console][dev_console] page.

To create a `Client` with a developer token, construct an `DeveloperTokenAuth`
object with the `token` set to the developer token and construct the client with that.

<!-- sample x_auth init_with_dev_token -->

```python
from box_sdk.client import Client
from box_sdk.developer_token_auth import DeveloperTokenAuth

auth = DeveloperTokenAuth(token='DEVELOPER_TOKEN_GOES_HERE')
client = Client(auth=auth)

me = client.users.get_user_me()
print(f'My user ID is {me.id}')
```

[dev_console]: https://app.box.com/developers/console

## JWT Auth

Authenticating with a JWT requires some extra dependencies. To get them, use

```
pip install "boxsdk@git+https://github.com/box/box-python-sdk-generated.git#boxsdk[jwt]"
```

Before using JWT Auth make sure you set up correctly your Box App.
The guide with all required steps can be found here: [Setup with JWT][jwt_guide]

### Authenticate Enterprise

JWT auth allows your application to authenticate itself with the Box API
for a given enterprise. By default, your application has a [Service Account][service_account]
that represents it and can perform API calls. The Service Account is separate
from the Box accounts of the application developer and the enterprise admin of
any enterprise that has authorized the app — files stored in that account are
not accessible in any other account by default, and vice versa.

If you generated your public and private keys automatically through the
[Box Developer Console][dev_console], you can use the JSON file created there
to configure your SDK instance and create a client to make calls as the
Service Account. Call one of static `JWTAuth` method:
`JWTConfig.from_config_file(config_file_path='/path/to/settings.json')` and pass JSON file local path
or `JWTConfig.from_config_json_string(config_json_string)` and pass JSON config file content as string.

```python
from box_sdk.client import Client
from box_sdk.jwt_auth import JWTAuth, JWTConfig

jwt_config = JWTConfig.from_config_file(config_file_path='/path/to/settings.json')
auth = JWTAuth(config=jwt_config)
client = Client(auth=auth)

service_account = client.users.get_user_me()
print(f'Service Account user ID is {service_account.id}')
```

Otherwise, you'll need to provide the necessary configuration fields directly to the `JWTConfig` constructor:

```python
from box_sdk.client import Client
from box_sdk.jwt_auth import JWTAuth, JWTConfig

jwt_config = JWTConfig(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    jwt_key_id='YOUR_JWT_KEY_ID',
    private_key='YOUR_PRIVATE_KEY',
    private_key_passphrase='PASSPHRASE',
    enterprise_id='YOUR_ENTERPRISE_ID',
)

auth = JWTAuth(config=jwt_config)
service_account_client = Client(auth=auth)
```

### Authenticate user

App auth applications also often have associated [App Users][app_user], which are
created and managed directly by the application — they do not have normal login credentials,
and can only be accessed through the Box API by the application that created them.
You may authenticate as the Service Account to provision and manage users, or as an individual app user to
make calls as that user. See the [API documentation](https://developer.box.com/)
for detailed instructions on how to use app auth.

Clients for making calls as an App User can be created with the same JSON JWT config file generated through the
[Box Developer Console][dev_console], but it is also required to call `auth.as_user('USER_ID')`, with
a user ID you want to authenticate.

```python
from box_sdk.client import Client
from box_sdk.jwt_auth import JWTAuth, JWTConfig

jwt_config = JWTConfig.from_config_file(config_file_path='/path/to/settings.json')
auth = JWTAuth(config=jwt_config)
auth.as_user('USER_ID')
user_client = Client(auth=auth)
```

Alternatively, clients for making calls as an App User can be created with the same `JWTConfig`
constructor as in the above examples, similarly to creating a Service Account client. Simply pass the
`user_id` instead of `enterprise_id` when constructing the auth config instance:

```python
from box_sdk.client import Client
from box_sdk.jwt_auth import JWTAuth, JWTConfig

jwt_config = JWTConfig(
  client_id='YOUR_CLIENT_ID',
  client_secret='YOUR_CLIENT_SECRET',
  jwt_key_id='YOUR_JWT_KEY_ID',
  private_key='YOUR_PRIVATE_KEY',
  private_key_passphrase='PASSPHRASE',
  user_id='USER_ID',
)

auth = JWTAuth(config=jwt_config)
user_client = Client(auth=auth)
```

[jwt_guide]: https://developer.box.com/guides/authentication/jwt/jwt-setup/
[service_account]: https://developer.box.com/guides/getting-started/user-types/service-account/
[app_user]: https://developer.box.com/guides/getting-started/user-types/app-users/

## Client Credentials Grant

Before using Client Credentials Grant Auth make sure you set up correctly your Box App.
The guide with all required steps can be found here: [Setup with Client Credentials Grant][ccg_guide]

Client Credentials Grant Auth method allows you to obtain an access token by having client credentials
and secret with enterprise or user ID, which allows you to work using service or user account.

You can use `CCGAuth` to initialize a client object the same way as for other authentication types:

```python
from box_sdk.client import Client
from box_sdk.ccg_auth import CCGAuth, CCGConfig


ccg_config = CCGConfig(
  client_id="YOUR_CLIENT_ID",
  client_secret="YOUR_CLIENT_SECRET",
  user_id="YOUR_USER_ID"
)
auth = CCGAuth(config=ccg_config)
client = Client(auth=auth)

print(f'Id of the authenticated user is: {client.users.get_user_me().id}')
```

Obtained token is valid for specified amount of time, it will be refreshed automatically by default.

### Obtaining Service Account token

The [Service Account](https://developer.box.com/guides/getting-started/user-types/service-account//)
is separate from the Box accounts of the application developer and the
enterprise admin of any enterprise that has authorized the app — files stored in that account
are not accessible in any other account by default, and vice versa.
To obtain service account you will have to provide enterprise ID with client id and secret:

```python
from box_sdk.client import Client
from box_sdk.ccg_auth import CCGAuth, CCGConfig

ccg_config = CCGConfig(
  client_id="YOUR_CLIENT_ID",
  client_secret="YOUR_CLIENT_SECRET",
  enterprise_id="YOUR_ENTERPRISE_ID"
)
auth = CCGAuth(config=ccg_config)
client = Client(auth=auth)
```

### Obtaining User token

In order to enable obtaining user token you have to go to your application configuration that can be found
[here][dev_console]. In `Configuration` tab, in section `Advanced Features`
select `Generate user access tokens`. Do not forget to re-authorize application if it was already authorized.

To obtain user account you will have to provide user ID with client id and secret.

```python
from box_sdk.client import Client
from box_sdk.ccg_auth import CCGAuth, CCGConfig

ccg_config = CCGConfig(
  client_id="YOUR_CLIENT_ID",
  client_secret="YOUR_CLIENT_SECRET",
  user_id="YOUR_USER_ID"
)
auth = CCGAuth(config=ccg_config)
client = Client(auth=auth)
```

### Switching between Service Account and User

In order to switch between being authenticated as Service Account and a User you can call:

```python
auth.as_enterprise(enterprise_id='YOUR_ENTERPRISE_ID')
```

to authenticate as enterprise or

```python
auth.as_user(user_id='YOUR_USER_ID')
```

to authenticate as User with provided ID. The new token will be automatically fetched with a next API call.

[ccg_guide]: https://developer.box.com/guides/authentication/client-credentials/client-credentials-setup/
