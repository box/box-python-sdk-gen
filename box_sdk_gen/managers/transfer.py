from box_sdk_gen.base_object import BaseObject

from typing import Optional

from typing import List

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import serialize

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.schemas import FolderFull

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.json import sd_to_json

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse

from box_sdk_gen.json import SerializedData


class TransferOwnedFolderOwnedByArg(BaseObject):
    def __init__(self, id: str, **kwargs):
        """
        :param id: The ID of the user who the folder will be
            transferred to
        :type id: str
        """
        super().__init__(**kwargs)
        self.id = id


class TransferManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def transfer_owned_folder(
        self,
        user_id: str,
        owned_by: TransferOwnedFolderOwnedByArg,
        fields: Optional[List[str]] = None,
        notify: Optional[bool] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> FolderFull:
        """
        Move all of the items (files, folders and workflows) owned by a user into

        another user's account


        Only the root folder (`0`) can be transferred.


        Folders can only be moved across users by users with administrative


        permissions.


        All existing shared links and folder-level collaborations are transferred


        during the operation. Please note that while collaborations at the individual


        file-level are transferred during the operation, the collaborations are


        deleted when the original user is deleted.


        This call will be performed synchronously which might lead to a slow response


        when the source user has a large number of items in all of its folders.


        If the destination path has a metadata cascade policy attached to any of


        the parent folders, a metadata cascade operation will be kicked off


        asynchronously.


        There is currently no way to check for when this operation is finished.


        The destination folder's name will be in the format `{User}'s Files and


        Folders`, where `{User}` is the display name of the user.


        To make this API call your application will need to have the "Read and write


        all files and folders stored in Box" scope enabled.


        Please make sure the destination user has access to `Relay` or `Relay Lite`,


        and has access to the files and folders involved in the workflows being


        transferred.


        Admins will receive an email when the operation is completed.

        :param user_id: The ID of the user.
            Example: "12345"
        :type user_id: str
        :param owned_by: The user who the folder will be transferred to
        :type owned_by: TransferOwnedFolderOwnedByArg
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[List[str]], optional
        :param notify: Determines if users should receive email notification
            for the action performed.
        :type notify: Optional[bool], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {'owned_by': owned_by}
        query_params_map: Dict[str, str] = prepare_params({
            'fields': to_string(fields), 'notify': to_string(notify)
        })
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/users/', to_string(user_id), '/folders/0'
            ]),
            FetchOptions(
                method='PUT',
                params=query_params_map,
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, FolderFull)
