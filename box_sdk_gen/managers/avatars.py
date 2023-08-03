from typing import Optional

import json

from box_sdk_gen.base_object import BaseObject

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import UserAvatar

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse

from box_sdk_gen.fetch import MultipartItem

class AvatarsManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def get_user_avatar(self, user_id: str) -> ByteStream:
        """
        Retrieves an image of a the user's avatar.
        :param user_id: The ID of the user.
            Example: "12345"
        :type user_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users/', user_id, '/avatar']), FetchOptions(method='GET', response_format='binary', auth=self.auth, network_session=self.network_session))
        return response.content
    def create_user_avatar(self, user_id: str, pic: ByteStream, pic_file_name: Optional[str] = None, pic_content_type: Optional[str] = None) -> UserAvatar:
        """
        Adds or updates a user avatar.
        :param user_id: The ID of the user.
            Example: "12345"
        :type user_id: str
        :param pic: The image file to be uploaded to Box.
            Accepted file extensions are `.jpg` or `.png`.
            The maximum file size is 1MB.
        :type pic: ByteStream
        """
        request_body: BaseObject = BaseObject(pic=pic, pic_file_name=pic_file_name, pic_content_type=pic_content_type)
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users/', user_id, '/avatar']), FetchOptions(method='POST', multipart_data=[MultipartItem(part_name='pic', file_stream=request_body.pic, content_type=request_body.pic_content_type, file_name=request_body.pic_file_name)], content_type='multipart/form-data', response_format='json', auth=self.auth, network_session=self.network_session))
        return UserAvatar.from_dict(json.loads(response.text))
    def delete_user_avatar(self, user_id: str) -> None:
        """
        Removes an existing user avatar.
        
        You cannot reverse this operation.

        :param user_id: The ID of the user.
            Example: "12345"
        :type user_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users/', user_id, '/avatar']), FetchOptions(method='DELETE', response_format=None, auth=self.auth, network_session=self.network_session))
        return None