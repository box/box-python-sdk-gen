# Migration guide from `boxsdk` to `box-sdk-gen`

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Introduction](#introduction)
- [Installation](#installation)
- [Key differences](#key-differences)
  - [Manager approach](#manager-approach)
  - [Explicitly defined schemas](#explicitly-defined-schemas)
- [Authentication](#authentication)
  - [Developer Token](#developer-token)
  - [JWT Auth](#jwt-auth)
    - [Using JWT configuration file](#using-jwt-configuration-file)
    - [Providing JWT configuration manually](#providing-jwt-configuration-manually)
    - [Authenticate user](#authenticate-user)
  - [Client Credentials Grant](#client-credentials-grant)
    - [Obtaining Service Account token](#obtaining-service-account-token)
    - [Obtaining User token](#obtaining-user-token)
  - [Switching between Service Account and User](#switching-between-service-account-and-user)
  - [OAuth 2.0 Auth](#oauth-20-auth)
    - [Get Authorization URL](#get-authorization-url)
    - [Authenticate](#authenticate)
  - [Store token and retrieve token callbacks](#store-token-and-retrieve-token-callbacks)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Introduction

The new `box-sdk-gen` SDK library, which helps Python developers to conveniently integrate with Box API.
In the contrary to the previous library (`boxsdk`), it is not manually maintained, but auto-generated
based on Open API Specification. This means you can leverage the most up-to-date Box API features in your
applications without delay. More information and benefits of using the new can be found in the
[README](https://github.com/box/box-python-sdk-gen/blob/main/README.md) file.

## Installation

To install a new Box Python SDK GENERATED use command:

```console
pip install box-sdk-gen
```

The new Box Python SDK GENERATED library could be used in the same project along with the legacy one.
If you want to use a feature available only in the new SDK, you don't need to necessarily migrate all your code
to use Box Python SDK GENERATED at once. You can use a new feature from the new library,
while keeping the rest of your code unchanged. Note that it may be required to alias some imported names
from the new SDK to avoid conflicts with the old one. However, we recommend to fully migrate to the new SDK eventually.

## Key differences

### Manager approach

The main difference between the old SDK and the new one is the way how API methods are aggregated into objects.

**Old (`boxsdk`)**

Firstly, in the old SDK to be able to perform any action on an API object, e.g. `User`, you first had to create its class.
To do it is required to call:

```python
user = client.user(user_id='123456')
```

to create a class representing an already existing User with id '12345', or create a new one with a call:

```python
user = client.create_user(name='Some User')
```

Then, you could perform any action on created class, which will affect the user, e.g.

```python
updated_user = user.update_info(data={'name': 'New User Name'})
```

**New (`box-sdk-gen`)**

In the new SDK the API methods are grouped into dedicated manager classes, e.g. `User` object
has dedicated `UserManager` class. Each manager class instance is available in `BoxClient` object.
So if you want to perform any operation connected with a `User` you need to call a respective method of `UserManager`.
E.g. to get info about existing user you need to call:

```python
user = client.users.get_user_by_id(user_id='123456')
```

or to create a new user:

```python
user = client.users.create_user(name='Some User')
```

The `User` object returned by both of these methods is a data class - it does not contain any methods to call.
To perform any action on `User` object, you need to still use a `UserManager` method for that.
Usually these methods have a first argument, which accepts an id of the object you want to access,
e.g. to update a user name, call method:

```python
updated_user = client.users.update_user_by_id(user_id=user.id, name='New User Name')
```

### Explicitly defined schemas

**Old (`boxsdk`)**

In the old SDK there were no data types explicitly defined -
the responses were dynamically mapped into classes in the runtime. For example, if you get information about a file:

```python
file = client.file(file_id='12345678').get()
```

you couldn't be sure which fields to expect in the response object until the runtime,
because `File` class doesn't have any predefined fields.

**New (`box-sdk-gen`)**

In the new SDK the data classe are defined in `schemas` module, so you know, which fields to expect before
actually making a call. For example `FileBase` class is defined this way:

```python
class FileBase(BaseObject):
    def __init__(self, id: str, type: FileBaseTypeField, etag: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.etag = etag
```

## Authentication

The Box Python SDK GENERATED library offers the same authentication methods as the legacy one.
Let's see the differences of their usage:

### Developer Token

The new SDK provides a convenient `BoxDeveloperTokenAuth`, which allows authenticating
using developer token without necessity to provide a Client ID and Client Secret

**Old (`boxsdk`)**

```python
from boxsdk import Client, OAuth2

auth = OAuth2(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    access_token='DEVELOPER_TOKEN_GOES_HERE',
)
client = Client(auth)
```

**New (`box-sdk-gen`)**

```python
from box_sdk_gen import Client, BoxDeveloperTokenAuth

auth = BoxDeveloperTokenAuth(token='DEVELOPER_TOKEN_GOES_HERE')
client = BoxClient(auth=auth)
```

### JWT Auth

#### Using JWT configuration file

**Old (`boxsdk`)**

The static method, which reads the JWT configuration file has been changed:

```python
from boxsdk import JWTAuth, Client

auth = JWTAuth.from_settings_file('/path/to/config.json')
client = Client(auth)
```

**New (`box-sdk-gen`)**

```python
from box_sdk_gen import BoxClient, BoxJWTAuth, JWTConfig

jwt_config = JWTConfig.from_config_file(config_file_path='/path/to/config.json')
auth = BoxJWTAuth(config=jwt_config)
client = BoxClient(auth=auth)
```

#### Providing JWT configuration manually

Some params in `JWTConfig` constructor have slightly different names than one in old `JWTAuth` class.

**Old (`boxsdk`)**

```python
from boxsdk import JWTAuth

auth = JWTAuth(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    enterprise_id='YOUR_ENTERPRISE_ID',
    user_id='USER_ID',
    jwt_key_id='YOUR_JWT_KEY_ID',
    rsa_private_key_file_sys_path='CERT.PEM',
    rsa_private_key_passphrase='PASSPHRASE',
    jwt_algorithm='RS256',
)
```

**New (`box-sdk-gen`)**

```python
from box_sdk_gen import BoxJWTAuth, JWTConfig

jwt_config = JWTConfig(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    enterprise_id='YOUR_ENTERPRISE_ID',
    user_id='USER_ID',
    jwt_key_id='YOUR_JWT_KEY_ID',
    private_key='YOUR_PRIVATE_KEY',
    private_key_passphrase='PASSPHRASE',
    jwt_algorithm='RS256',
)
auth = BoxJWTAuth(config=jwt_config)
```

#### Authenticate user

To authenticate as user you need to call `as_user(user_id: str)` method with id of the user to authenticate.
In old SDK this method was named `authenticate_user(self, user: Union[str, 'User'] = None) -> str` and
was accepting both user object and User ID or was using User ID provided in `JWTAuth` class if none provided in
this method call. The new method `as_user(user_id: str)` accepts only User ID, which is required.

**Old (`boxsdk`)**

```python
auth.authenticate_user(user)
```

or

```python
auth.authenticate_user('USER_ID')
```

**New (`box-sdk-gen`)**

```python
auth.as_user('USER_ID')
```

### Client Credentials Grant

#### Obtaining Service Account token

To authenticate as enterprise, the only difference between the old and the new SDK,
is using the `CCGConfig` as a middle step.

**Old (`boxsdk`)**

```python
from boxsdk import CCGAuth, Client

auth = CCGAuth(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    enterprise_id="YOUR_ENTERPRISE_ID",
)

client = Client(auth)
```

**New (`box-sdk-gen`)**

```python
from box_sdk_gen import BoxClient, BoxCCGAuth, CCGConfig

ccg_config = CCGConfig(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    enterprise_id="YOUR_ENTERPRISE_ID",
)
auth = BoxCCGAuth(config=ccg_config)
client = BoxClient(auth=auth)
```

#### Obtaining User token

In old SDK `CCGAuth` was accepting both user object and User ID. The new constructor accepts only User ID instead.

**Old (`boxsdk`)**

```python
from boxsdk import CCGAuth

auth = CCGAuth(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user="YOUR_USER_ID"
)
```

**New (`box-sdk-gen`)**

```python
from box_sdk_gen import BoxCCGAuth, CCGConfig

ccg_config = CCGConfig(
  client_id="YOUR_CLIENT_ID",
  client_secret="YOUR_CLIENT_SECRET",
  user_id="YOUR_USER_ID"
)
auth = BoxCCGAuth(config=ccg_config)
```

### Switching between Service Account and User

The method responsible for switching to Service Account got changed:

**Old (`boxsdk`)**

```python
auth.authenticate_enterprise('ENTERPRISE_ID')
```

**New (`box-sdk-gen`)**

```python
auth.as_enterprise(enterprise_id='YOUR_ENTERPRISE_ID')
```

And the one to switch to a User:

**Old (`boxsdk`)**

```python
auth.authenticate_user('USER_ID')
```

**New (`box-sdk-gen`)**

```python
auth.as_user(user_id='USER_ID')
```

Note that the new method accepts only User ID, while the old one was accepting both User object and User ID.

### OAuth 2.0 Auth

#### Get Authorization URL

To get authorization url in the new SDK, you need to first create the `OAuth` class (previously `OAuth2`) using
`OAuthConfig` class. Then to get authorization url, call
`get_authorize_url(self, options: Optional[GetAuthorizeUrlOptions] = None) -> str` instead of
`get_authorization_url(self, redirect_url: Optional[str]) -> Tuple[str, str]`. Note that this method
now accepts the instance of `GetAuthorizeUrlOptions` class, which allows specifying extra options to API call.
The new function returns only the authentication url string,
while the old one returns tuple of authentication url and csrf_token.

**Old (`boxsdk`)**

```python
from boxsdk import OAuth2

auth = OAuth2(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
)

auth_url, csrf_token = auth.get_authorization_url('http://YOUR_REDIRECT_URL')
```

**New (`box-sdk-gen`)**

```python
from box_sdk_gen import BoxOAuth, OAuthConfig, GetAuthorizeUrlOptions

auth = BoxOAuth(
  OAuthConfig(
      client_id='YOUR_CLIENT_ID',
      client_secret='YOUR_CLIENT_SECRET',
  )
)
auth_url = auth.get_authorize_url(options=GetAuthorizeUrlOptions(redirect_uri='http://YOUR_REDIRECT_URL'))
```

#### Authenticate

The signature of method for authenticating with obtained auth code got changed from:
`authenticate(self, auth_code: Optional[str]) -> Tuple[str, str]` to
`def get_tokens_authorization_code_grant(self, authorization_code: str, network_session: Optional[NetworkSession] = None) -> str`.
The method now returns only access token, while the old one was returning a tuple of access token and refresh token.

**Old (`boxsdk`)**

```python
from boxsdk import Client
access_token, refresh_token = auth.authenticate('YOUR_AUTH_CODE')
client = Client(auth)
```

**New (`box-sdk-gen`)**

```python
from box_sdk_gen import BoxClient

access_token = auth.get_tokens_authorization_code_grant('YOUR_AUTH_CODE')
client = BoxClient(auth)
```

### Store token and retrieve token callbacks

In old SDK you could provide a `store_tokens` callback method to an authentication class, which was called each time
an access token was refreshed. It could be used to save your access token to a custom token storage
and allow to reuse this token later.
What is more, old SDK allowed also to provide `retrieve_tokens` callback, which is called each time the SDK needs to use
token to perform an API call. To provide that, it was required to use `CooperativelyManagedOAuth2` and provide
`retrieve_tokens` callback method to its constructor.

**Old (`boxsdk`)**

```python
from typing import Tuple
from boxsdk.auth import CooperativelyManagedOAuth2

def retrieve_tokens() -> Tuple[str, str]:
    # retrieve access_token and refresh_token
    return access_token, refresh_token

def store_tokens(access_token: str, refresh_token: str):
    # store access_token and refresh_token
    pass


auth = CooperativelyManagedOAuth2(
  client_id='YOUR_CLIENT_ID',
  client_secret='YOUR_CLIENT_SECRET',
  retrieve_tokens=retrieve_tokens,
  store_tokens=store_tokens
)
access_token, refresh_token = auth.authenticate('YOUR_AUTH_CODE')
client = Client(auth)
```

In the new SDK you can define your own class delegated for storing and retrieving a token. It has to inherit from
`TokenStorage` and implement all of its abstract methods. Then, pass an instance of this class to the
AuthConfig constructor.

**New (`box-sdk-gen`)**

```python
from typing import Optional
from box_sdk_gen import BoxOAuth, OAuthConfig, FileWithInMemoryCacheTokenStorage, TokenStorage, AccessToken

class MyCustomTokenStorage(TokenStorage):
  def store(self, token: AccessToken) -> None:
    # store token
    pass

  def get(self) -> Optional[AccessToken]:
    # get token
    pass

  def clear(self) -> None:
    # clear token
    pass


auth = BoxOAuth(
  OAuthConfig(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    token_storage=MyCustomTokenStorage()
  )
)
```

or reuse one of the provided implementations: `FileTokenStorage` or `FileWithInMemoryCacheTokenStorage`:

```python
from box_sdk_gen import BoxOAuth, OAuthConfig, FileWithInMemoryCacheTokenStorage

auth = BoxOAuth(
  OAuthConfig(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    token_storage=FileWithInMemoryCacheTokenStorage()
  )
)
```
