from box_sdk.base_object import BaseObject

from typing import Optional

from typing import Union

import json

from box_sdk.schemas import FolderFull

from box_sdk.schemas import ClientError

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.jwt_auth import JWTAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class TransferOwnedFolderRequestBodyArgOwnedByField(BaseObject):
    def __init__(self, id: str, **kwargs):
        """
        :param id: The ID of the user who the folder will be
            transferred to
        :type id: str
        """
        super().__init__(**kwargs)
        self.id = id

class TransferOwnedFolderRequestBodyArg(BaseObject):
    def __init__(self, owned_by: TransferOwnedFolderRequestBodyArgOwnedByField, **kwargs):
        """
        :param owned_by: The user who the folder will be transferred to
        :type owned_by: TransferOwnedFolderRequestBodyArgOwnedByField
        """
        super().__init__(**kwargs)
        self.owned_by = owned_by

class TransferOwnedFolderOptionsArg(BaseObject):
    def __init__(self, fields: Optional[str] = None, notify: Optional[bool] = None, **kwargs):
        """
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[str], optional
        :param notify: Determines if users should receive email notification
            for the action performed.
        :type notify: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.fields = fields
        self.notify = notify

class TransferManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth, JWTAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def transfer_owned_folder(self, user_id: str, request_body: TransferOwnedFolderRequestBodyArg, options: TransferOwnedFolderOptionsArg = None) -> FolderFull:
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
        """
        if options is None:
            options = TransferOwnedFolderOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/users/', user_id, '/folders/0']), FetchOptions(method='PUT', params={'fields': options.fields, 'notify': options.notify}, body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth))
        return FolderFull.from_dict(json.loads(response.text))