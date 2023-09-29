from box_sdk_gen.base_object import BaseObject

from typing import Optional

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.serialization import serialize

from box_sdk_gen.base_object import BaseObject

from box_sdk_gen.schemas import FolderLocks

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import FolderLock

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse


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
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def get_folder_locks(
        self, folder_id: str, extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> FolderLocks:
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
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params(
            {'folder_id': to_string(folder_id)}
        )
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/folder_locks']),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, FolderLocks)

    def create_folder_lock(
        self,
        folder: CreateFolderLockFolderArg,
        locked_operations: Optional[CreateFolderLockLockedOperationsArg] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> FolderLock:
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
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body = BaseObject(locked_operations=locked_operations, folder=folder)
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/folder_locks']),
            FetchOptions(
                method='POST',
                headers=headers_map,
                body=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, FolderLock)

    def delete_folder_lock_by_id(
        self,
        folder_lock_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> None:
        """
        Deletes a folder lock on a given folder.

        You must be authenticated as the owner or co-owner of the folder to


        use this endpoint.

        :param folder_lock_id: The ID of the folder lock.
            Example: "12345"
        :type folder_lock_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                ['https://api.box.com/2.0/folder_locks/', to_string(folder_lock_id)]
            ),
            FetchOptions(
                method='DELETE',
                headers=headers_map,
                response_format=None,
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return None
