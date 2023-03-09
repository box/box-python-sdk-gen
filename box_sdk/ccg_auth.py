import json
from enum import Enum
from urllib.parse import urlencode
from typing import Union, List

from .base_object import BaseObject
from .fetch import fetch, FetchResponse, FetchOptions


class CCGConfig:
    def __init__(
            self,
            client_id: str,
            client_secret: str,
            enterprise_id: Union[None, str] = None,
            user_id: Union[None, str] = None
    ):
        if not enterprise_id and not user_id:
            raise Exception("Enterprise ID or User ID is needed")

        self.client_id = client_id
        self.client_secret = client_secret
        self.enterprise_id = enterprise_id
        self.user_id = user_id


class CCGAuth:
    def __init__(self,  ccg_config: CCGConfig):
        self.ccg_config = ccg_config
        self.token: Union[None, str] = None

    def retrieve_token(self) -> str:
        if self.token is None:
            return self.refresh()
        return self.token

    def refresh(self) -> str:
        if self.ccg_config.user_id is None:
            subject_id = self.ccg_config.enterprise_id
            subject_type = TokenRequestBoxSubjectType.ENTERPRISE
        else:
            subject_id = self.ccg_config.user_id
            subject_type = TokenRequestBoxSubjectType.USER

        request_body = TokenRequest(
            grant_type=TokenRequestGrantType.CLIENT_CREDENTIALS,
            client_id=self.ccg_config.client_id,
            client_secret=self.ccg_config.client_secret,
            box_subject_id=subject_id,
            box_subject_type=subject_type
        )

        response: FetchResponse = fetch(
            'https://api.box.com/oauth2/token',
            FetchOptions(
                method='POST',
                body=urlencode(request_body.to_dict()),
                headers={'content-type': 'application/x-www-form-urlencoded'})
        )

        token_response = AccessToken.from_dict(json.loads(response.text))
        self.token = token_response.access_token
        return self.token


class TokenRequestGrantType(str, Enum):
    AUTHORIZATION_CODE = 'authorization_code'
    REFRESH_TOKEN = 'refresh_token'
    CLIENT_CREDENTIALS = 'client_credentials'
    URN_IETF_PARAMS_OAUTH_GRANT_TYPE_JWT_BEARER = 'urn:ietf:params:oauth:grant-type:jwt-bearer'
    URN_IETF_PARAMS_OAUTH_GRANT_TYPE_TOKEN_EXCHANGE = 'urn:ietf:params:oauth:grant-type:token-exchange'


class TokenRequestBoxSubjectType(str, Enum):
    ENTERPRISE = 'enterprise'
    USER = 'user'


class TokenRequest(BaseObject):
    def __init__(self, grant_type: TokenRequestGrantType, client_id: Union[None, str] = None, client_secret: Union[None, str] = None, code: Union[None, str] = None, refresh_token: Union[None, str] = None, assertion: Union[None, str] = None, subject_token: Union[None, str] = None, subject_token_type: Union[None, str] = None, actor_token: Union[None, str] = None, actor_token_type: Union[None, str] = None, scope: Union[None, str] = None, resource: Union[None, str] = None, box_subject_type: Union[None, TokenRequestBoxSubjectType] = None, box_subject_id: Union[None, str] = None, box_shared_link: Union[None, str] = None, **kwargs):
        super().__init__(**kwargs)
        self.grant_type = grant_type
        self.client_id = client_id
        self.client_secret = client_secret
        self.code = code
        self.refresh_token = refresh_token
        self.assertion = assertion
        self.subject_token = subject_token
        self.subject_token_type = subject_token_type
        self.actor_token = actor_token
        self.actor_token_type = actor_token_type
        self.scope = scope
        self.resource = resource
        self.box_subject_type = box_subject_type
        self.box_subject_id = box_subject_id
        self.box_shared_link = box_shared_link


class FileScope(str, Enum):
    ANNOTATION_EDIT = 'annotation_edit'
    ANNOTATION_VIEW_ALL = 'annotation_view_all'
    ANNOTATION_VIEW_SELF = 'annotation_view_self'
    BASE_EXPLORER = 'base_explorer'
    BASE_PICKER = 'base_picker'
    BASE_PREVIEW = 'base_preview'
    BASE_UPLOAD = 'base_upload'
    ITEM_DELETE = 'item_delete'
    ITEM_DOWNLOAD = 'item_download'
    ITEM_PREVIEW = 'item_preview'
    ITEM_RENAME = 'item_rename'
    ITEM_SHARE = 'item_share'


class AccessToken(BaseObject):
    def __init__(self, access_token: Union[None, str] = None, expires_in: Union[None, int] = None, token_type: Union[None, str] = None, restricted_to: Union[None, List[FileScope]] = None, refresh_token: Union[None, str] = None, issued_token_type: Union[None, str] = None, **kwargs):
        super().__init__(**kwargs)
        self.access_token = access_token
        self.expires_in = expires_in
        self.token_type = token_type
        self.restricted_to = restricted_to
        self.refresh_token = refresh_token
        self.issued_token_type = issued_token_type
