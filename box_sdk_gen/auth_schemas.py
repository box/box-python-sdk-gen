from enum import Enum
from typing import Union, List

from .base_object import BaseObject


class TokenRequestGrantType(str, Enum):
    AUTHORIZATION_CODE = 'authorization_code'
    REFRESH_TOKEN = 'refresh_token'
    CLIENT_CREDENTIALS = 'client_credentials'
    URN_IETF_PARAMS_OAUTH_GRANT_TYPE_JWT_BEARER = (
        'urn:ietf:params:oauth:grant-type:jwt-bearer'
    )
    URN_IETF_PARAMS_OAUTH_GRANT_TYPE_TOKEN_EXCHANGE = (
        'urn:ietf:params:oauth:grant-type:token-exchange'
    )


class TokenRequestBoxSubjectType(str, Enum):
    ENTERPRISE = 'enterprise'
    USER = 'user'


class TokenRequest(BaseObject):
    def __init__(
        self,
        grant_type: TokenRequestGrantType,
        client_id: Union[None, str] = None,
        client_secret: Union[None, str] = None,
        code: Union[None, str] = None,
        refresh_token: Union[None, str] = None,
        assertion: Union[None, str] = None,
        subject_token: Union[None, str] = None,
        subject_token_type: Union[None, str] = None,
        actor_token: Union[None, str] = None,
        actor_token_type: Union[None, str] = None,
        scope: Union[None, str] = None,
        resource: Union[None, str] = None,
        box_subject_type: Union[None, TokenRequestBoxSubjectType] = None,
        box_subject_id: Union[None, str] = None,
        box_shared_link: Union[None, str] = None,
        **kwargs
    ):
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
