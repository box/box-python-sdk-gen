from typing import Optional

from box_sdk.base_object import BaseObject

from typing import Dict

import json

from box_sdk.base_object import BaseObject

from box_sdk.schemas import TrashFolderRestored

from box_sdk.schemas import ClientError

from box_sdk.schemas import TrashFolder

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.utils import to_map

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class RestoreFolderFromTrashParentArg(BaseObject):
    def __init__(self, id: Optional[str] = None, **kwargs):
        """
        :param id: The ID of parent item
        :type id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id

class TrashedFoldersManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def restore_folder_from_trash(self, folder_id: str, name: Optional[str] = None, parent: Optional[RestoreFolderFromTrashParentArg] = None, fields: Optional[str] = None) -> TrashFolderRestored:
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
        :param name: An optional new name for the folder.
        :type name: Optional[str], optional
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
        request_body: BaseObject = BaseObject(name=name, parent=parent)
        query_params: Dict = {'fields': fields}
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id]), FetchOptions(method='POST', params=to_map(query_params), body=json.dumps(to_map(request_body)), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return TrashFolderRestored.from_dict(json.loads(response.text))
    def get_folder_trash(self, folder_id: str, fields: Optional[str] = None) -> TrashFolder:
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
        query_params: Dict = {'fields': fields}
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/trash']), FetchOptions(method='GET', params=to_map(query_params), auth=self.auth, network_session=self.network_session))
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
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/trash']), FetchOptions(method='DELETE', auth=self.auth, network_session=self.network_session))
        return response.content