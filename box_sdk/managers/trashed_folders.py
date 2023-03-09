from typing import Union

from box_sdk.base_object import BaseObject

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch, FetchOptions, FetchResponse

import json

from box_sdk.schemas import TrashFolder

from box_sdk.schemas import ClientError

class GetFoldersIdTrashOptionsArg(BaseObject):
    def __init__(self, fields: Union[None, str] = None, **kwargs):
        """
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.fields = fields

class TrashedFoldersManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getFoldersIdTrash(self, folderId: str, options: GetFoldersIdTrashOptionsArg = None) -> TrashFolder:
        """
        Retrieves a folder that has been moved to the trash.
        
        Please note that only if the folder itself has been moved to the

        
        trash can it be retrieved with this API call. If instead one of

        
        its parent folders was moved to the trash, only that folder

        
        can be inspected using the

        
        [`GET /folders/:id/trash`](e://get_folders_id_trash) API.

        
        To list all items that have been moved to the trash, please

        
        use the [`GET /folders/trash/items`](e://get-folders-trash-items/)

        
        API.

        :param folderId: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folderId: str
        """
        if options is None:
            options = GetFoldersIdTrashOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folderId, '/trash']), FetchOptions(method='GET', params={'fields': options.fields}, auth=self.auth))
        return TrashFolder.from_dict(json.loads(response.text))
    def deleteFoldersIdTrash(self, folderId: str):
        """
        Permanently deletes a folder that is in the trash.
        
        This action cannot be undone.

        :param folderId: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folderId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folderId, '/trash']), FetchOptions(method='DELETE', auth=self.auth))
        return response.content