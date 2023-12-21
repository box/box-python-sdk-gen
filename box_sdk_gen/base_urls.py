from typing import Dict

from box_sdk_gen.base_object import BaseObject


class BaseUrls(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {
        'oauth_2_url': 'oauth2_url',
        **BaseObject._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        'oauth2_url': 'oauth_2_url',
        **BaseObject._json_to_fields_mapping,
    }

    def __init__(
        self,
        base_url: str = 'https://api.box.com/2.0',
        upload_url: str = 'https://upload.box.com/api/2.0',
        oauth_2_url: str = 'https://account.box.com/api/oauth2',
        **kwargs
    ):
        super().__init__(**kwargs)
        self.base_url = base_url
        self.upload_url = upload_url
        self.oauth_2_url = oauth_2_url
