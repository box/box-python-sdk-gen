from enum import Enum

from typing import Optional

from typing import Dict

import json

from box_sdk.schemas import Collaborations

from box_sdk.schemas import ClientError

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.utils import prepare_params

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetCollaborationsStatusArg(str, Enum):
    PENDING = 'pending'

class ListCollaborationsManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def get_file_collaborations(self, file_id: str, fields: Optional[str] = None, limit: Optional[int] = None, marker: Optional[str] = None) -> Collaborations:
        """
        Retrieves a list of pending and active collaborations for a
        
        file. This returns all the users that have access to the file

        
        or have been invited to the file.

        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        """
        query_params: Dict = {'fields': fields, 'limit': limit, 'marker': marker}
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/collaborations']), FetchOptions(method='GET', params=prepare_params(query_params), auth=self.auth, network_session=self.network_session))
        return Collaborations.from_dict(json.loads(response.text))
    def get_folder_collaborations(self, folder_id: str, fields: Optional[str] = None) -> Collaborations:
        """
        Retrieves a list of pending and active collaborations for a
        
        folder. This returns all the users that have access to the folder

        
        or have been invited to the folder.

        :param folder_id: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
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
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/collaborations']), FetchOptions(method='GET', params=prepare_params(query_params), auth=self.auth, network_session=self.network_session))
        return Collaborations.from_dict(json.loads(response.text))
    def get_collaborations(self, status: GetCollaborationsStatusArg, fields: Optional[str] = None, offset: Optional[int] = None, limit: Optional[int] = None) -> Collaborations:
        """
        Retrieves all pending collaboration invites for this user.
        :param status: The status of the collaborations to retrieve
        :type status: GetCollaborationsStatusArg
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[str], optional
        :param offset: The offset of the item at which to begin the response.
            Queries with offset parameter value
            exceeding 10000 will be rejected
            with a 400 response.
        :type offset: Optional[int], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        """
        query_params: Dict = {'status': status, 'fields': fields, 'offset': offset, 'limit': limit}
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/collaborations']), FetchOptions(method='GET', params=prepare_params(query_params), auth=self.auth, network_session=self.network_session))
        return Collaborations.from_dict(json.loads(response.text))
    def get_group_collaborations(self, group_id: str, limit: Optional[int] = None, offset: Optional[int] = None) -> Collaborations:
        """
        Retrieves all the collaborations for a group. The user
        
        must have admin permissions to inspect enterprise's groups.

        
        Each collaboration object has details on which files or

        
        folders the group has access to and with what role.

        :param group_id: The ID of the group.
            Example: "57645"
        :type group_id: str
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        :param offset: The offset of the item at which to begin the response.
            Queries with offset parameter value
            exceeding 10000 will be rejected
            with a 400 response.
        :type offset: Optional[int], optional
        """
        query_params: Dict = {'limit': limit, 'offset': offset}
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/groups/', group_id, '/collaborations']), FetchOptions(method='GET', params=prepare_params(query_params), auth=self.auth, network_session=self.network_session))
        return Collaborations.from_dict(json.loads(response.text))