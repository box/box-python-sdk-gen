from box_sdk.base_object import BaseObject

from typing import Optional

from typing import Dict

import json

from box_sdk.base_object import BaseObject

from box_sdk.schemas import FolderLocks

from box_sdk.schemas import ClientError

from box_sdk.schemas import FolderLock

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.utils import to_map

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class CreateFolderLockLockedOperationsArg(BaseObject):
    def __init__(self, move: bool, delete: bool, **kwargs):
        """
        :param move: Whether moving the folder should be locked.
        :type move: bool
        :param delete: Whether deleting the folder should be locked.
        :type delete: bool
        """
        super().__init__(**kwargs)
        self.move = move
        self.delete = delete

class CreateFolderLockFolderArg(BaseObject):
    def __init__(self, type: str, id: str, **kwargs):
        """
        :param type: The content type the lock is being applied to. Only `folder`
            is supported.
        :type type: str
        :param id: The ID of the folder.
        :type id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class FolderLocksManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def get_folder_locks(self, folder_id: str) -> FolderLocks:
        """
        Retrieves folder lock details for a given folder.
        
        You must be authenticated as the owner or co-owner of the folder to

        
        use this endpoint.

        :param folder_id: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
        :type folder_id: str
        """
        query_params: Dict = {'folder_id': folder_id}
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folder_locks']), FetchOptions(method='GET', params=to_map(query_params), auth=self.auth, network_session=self.network_session))
        return FolderLocks.from_dict(json.loads(response.text))
    def create_folder_lock(self, folder: CreateFolderLockFolderArg, locked_operations: Optional[CreateFolderLockLockedOperationsArg] = None) -> FolderLock:
        """
        Creates a folder lock on a folder, preventing it from being moved and/or
        
        deleted.

        
        You must be authenticated as the owner or co-owner of the folder to

        
        use this endpoint.

        :param folder: The folder to apply the lock to.
        :type folder: CreateFolderLockFolderArg
        :param locked_operations: The operations to lock for the folder. If `locked_operations` is
            included in the request, both `move` and `delete` must also be
            included and both set to `true`.
        :type locked_operations: Optional[CreateFolderLockLockedOperationsArg], optional
        """
        request_body: BaseObject = BaseObject(locked_operations=locked_operations, folder=folder)
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folder_locks']), FetchOptions(method='POST', body=json.dumps(to_map(request_body)), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return FolderLock.from_dict(json.loads(response.text))
    def delete_folder_lock_by_id(self, folder_lock_id: str):
        """
        Deletes a folder lock on a given folder.
        
        You must be authenticated as the owner or co-owner of the folder to

        
        use this endpoint.

        :param folder_lock_id: The ID of the folder lock.
            Example: "12345"
        :type folder_lock_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folder_locks/', folder_lock_id]), FetchOptions(method='DELETE', auth=self.auth, network_session=self.network_session))
        return response.content