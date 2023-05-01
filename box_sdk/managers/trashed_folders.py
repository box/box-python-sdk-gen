from typing import Optional

from box_sdk.base_object import BaseObject

from typing import Union

import json

from box_sdk.schemas import TrashFolderRestored

from box_sdk.schemas import ClientError

from box_sdk.schemas import TrashFolder

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.jwt_auth import JWTAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class RestoreFolderFromTrashRequestBodyArgParentField(BaseObject):
    def __init__(self, id: Optional[str] = None, **kwargs):
        """
        :param id: The ID of parent item
        :type id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id

class RestoreFolderFromTrashRequestBodyArg(BaseObject):
    def __init__(self, name: Optional[str] = None, parent: Optional[RestoreFolderFromTrashRequestBodyArgParentField] = None, **kwargs):
        """
        :param name: An optional new name for the folder.
        :type name: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.name = name
        self.parent = parent

class RestoreFolderFromTrashOptionsArg(BaseObject):
    def __init__(self, fields: Optional[str] = None, **kwargs):
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
        """
        super().__init__(**kwargs)
        self.fields = fields

class GetFolderTrashOptionsArg(BaseObject):
    def __init__(self, fields: Optional[str] = None, **kwargs):
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
        """
        super().__init__(**kwargs)
        self.fields = fields

class TrashedFoldersManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth, JWTAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def restore_folder_from_trash(self, folder_id: str, request_body: RestoreFolderFromTrashRequestBodyArg, options: RestoreFolderFromTrashOptionsArg = None) -> TrashFolderRestored:
        """
        Restores a folder that has been moved to the trash.
        
        An optional new parent ID can be provided to restore the folder to in case the

        
        original folder has been deleted.

        
        # Folder locking

        
        During this operation, part of the file tree will be locked, mainly

        
        the source folder and all of its descendants, as well as the destination

        
        folder.

        
        For the duration of the operation, no other move, copy, delete, or restore

        
        operation can performed on any of the locked folders.

        :param folder_id: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folder_id: str
        """
        if options is None:
            options = RestoreFolderFromTrashOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id]), FetchOptions(method='POST', params={'fields': options.fields}, body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth))
        return TrashFolderRestored.from_dict(json.loads(response.text))
    def get_folder_trash(self, folder_id: str, options: GetFolderTrashOptionsArg = None) -> TrashFolder:
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

        :param folder_id: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folder_id: str
        """
        if options is None:
            options = GetFolderTrashOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/trash']), FetchOptions(method='GET', params={'fields': options.fields}, auth=self.auth))
        return TrashFolder.from_dict(json.loads(response.text))
    def delete_folder_trash(self, folder_id: str):
        """
        Permanently deletes a folder that is in the trash.
        
        This action cannot be undone.

        :param folder_id: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folder_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/trash']), FetchOptions(method='DELETE', auth=self.auth))
        return response.content