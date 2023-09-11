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
  - [OAuth 2.0 Auth](#oauth-20-auth)

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
from box_sdk_gen.client import Client
from box_sdk_gen.developer_token_auth import DeveloperTokenAuth

auth = DeveloperTokenAuth(token='DEVELOPER_TOKEN_GOES_HERE')
client = Client(auth=auth)

me = client.users.get_user_me()
print(f'My user ID is {me.id}')
```

[dev_console]: https://app.box.com/developers/console

## JWT Auth

Authenticating with a JWT requires some extra dependencies. To get them, use

```
pip install box-sdk-gen[jwt]
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
from box_sdk_gen.client import Client
from box_sdk_gen.jwt_auth import JWTAuth, JWTConfig

jwt_config = JWTConfig.from_config_file(config_file_path='/path/to/settings.json')
auth = JWTAuth(config=jwt_config)
client = Client(auth=auth)

service_account = client.users.get_user_me()
print(f'Service Account user ID is {service_account.id}')
```

Otherwise, you'll need to provide the necessary configuration fields directly to the `JWTConfig` constructor:

```python
from box_sdk_gen.client import Client
from box_sdk_gen.jwt_auth import JWTAuth, JWTConfig

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
from box_sdk_gen.client import Client
from box_sdk_gen.jwt_auth import JWTAuth, JWTConfig

jwt_config = JWTConfig.from_config_file(config_file_path='/path/to/settings.json')
auth = JWTAuth(config=jwt_config)
auth.as_user('USER_ID')
user_client = Client(auth=auth)
```

Alternatively, clients for making calls as an App User can be created with the same `JWTConfig`
constructor as in the above examples, similarly to creating a Service Account client. Simply pass the
`user_id` instead of `enterprise_id` when constructing the auth config instance:

```python
from box_sdk_gen.client import Client
from box_sdk_gen.jwt_auth import JWTAuth, JWTConfig

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
from box_sdk_gen.client import Client
from box_sdk_gen.ccg_auth import CCGAuth, CCGConfig


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
from box_sdk_gen.client import Client
from box_sdk_gen.ccg_auth import CCGAuth, CCGConfig

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
from box_sdk_gen.client import Client
from box_sdk_gen.ccg_auth import CCGAuth, CCGConfig

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

## OAuth 2.0 Auth

If your application needs to integrate with existing Box users who will provide
their login credentials to grant your application access to their account, you
will need to go through the standard OAuth2 login flow. A detailed guide for
this process is available in the
[Authentication with OAuth API documentation](https://developer.box.com/en/guides/authentication/oauth2/).

Using an auth code is the most common way of authenticating with the Box API for
existing Box users, to integrate with their accounts.
Your application must provide a way for the user to login to Box (usually with a
browser or web view) in order to obtain an auth code.

<!-- sample get_authorize -->

```python
from box_sdk_gen.oauth import OAuth, OAuthConfig

auth = OAuth(
  OAuthConfig(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET')
)
auth_url = auth.get_authorize_url()
```

After a user logs in and grants your application access to their Box account,
they will be redirected to your application's `redirect_uri` which will contain
an auth code. This auth code can then be used along with your client ID and
client secret to establish an API connection.
You need to provide the auth code to the SDK to obtain an access token, then you can use the SDK as usual.

<!-- sample post_oauth2_token --->

```python
from box_sdk_gen.client import Client

auth.get_tokens_authorization_code_grant('YOUR_ACCESS_CODE')
client = Client(auth)
```

Here you can find a Flask app example, which handles complete OAuth workflow to authenticate and
list names of all items in a root folder.

```python
from flask import Flask, request, redirect

from box_sdk_gen.client import Client
from box_sdk_gen.oauth import OAuth, OAuthConfig

app = Flask(__name__)

AUTH = OAuth(
    OAuthConfig(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET')
)


@app.route("/")
def get_auth():
    auth_url = AUTH.get_authorize_url()
    return redirect(auth_url, code=302)


@app.route("/oauth2callback")
def callback():
    AUTH.get_tokens_authorization_code_grant(request.args.get("code"))
    client = Client(AUTH)

    items_in_root_folder = [item.name for item in client.folders.get_folder_items(folder_id='0').entries]
    return ', '.join(items_in_root_folder)


if __name__ == '__main__':
    app.run(port=4999)
```

# Token storage

## In-memory token storage

By default, the SDK stores the access token in volatile memory. When rerunning your application,
the access token won't be reused from the previous run; a new token has to be obtained again.
To use in-memory token storage, you don't need to do anything more than
create an Auth class using AuthConfig, for example, for OAuth:

```python
from box_sdk_gen.oauth import OAuth, OAuthConfig

auth = OAuth(
    OAuthConfig(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET')
)
```

## File token storage

If you want to keep an up-to-date access token in a file, allowing it to be reused after rerunning your application,
you can use the `FileTokenStorage` class. To enable storing the token in a file, you need to pass an object of type
`FileTokenStorage` to the AuthConfig class. For example, for OAuth:

```python
from box_sdk_gen.oauth import OAuth, OAuthConfig
from box_sdk_gen.token_storage import FileTokenStorage

auth = OAuth(
    OAuthConfig(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET', token_storage=FileTokenStorage())
)
```

## File with in-memory token storage

If you want to keep an up-to-date access token in a file and also maintain a valid access token in in-memory cache,
allowing you to reuse the token after rerunning your application while maintaining fast access times to the token,
you can use the `FileWithInMemoryCachingTokenStorage` class. To enable storing the token in a file,
you need to pass an object of type `FileWithInMemoryCachingTokenStorage` to the AuthConfig class. For example, for OAuth:

```python
from box_sdk_gen.oauth import OAuth, OAuthConfig
from box_sdk_gen.token_storage import FileWithInMemoryCachingTokenStorage

auth = OAuth(
    OAuthConfig(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET', token_storage=FileWithInMemoryCachingTokenStorage())
)
```

## Custom storage

You can also provide a custom token storage class. All you need to do is create a class that inherits from `TokenStorage`
and implements all of its abstract methods. Then, pass an instance of your class to the AuthConfig constructor.

```python
from box_sdk_gen.oauth import OAuth, OAuthConfig

auth = OAuth(
    OAuthConfig(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET', token_storage=MyCustomTokenStorage())
)
```
