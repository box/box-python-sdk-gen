from typing import Union

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from base_object import BaseObject

from managers.files import FilesManager

class Client(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
        self.files = FilesManager(auth=self.auth)