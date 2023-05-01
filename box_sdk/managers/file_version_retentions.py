from enum import Enum

from typing import Optional

from box_sdk.base_object import BaseObject

from typing import Union

import json

from box_sdk.schemas import FileVersionRetentions

from box_sdk.schemas import ClientError

from box_sdk.schemas import FileVersionRetention

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.jwt_auth import JWTAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetFileVersionRetentionsOptionsArgDispositionActionField(str, Enum):
    PERMANENTLY_DELETE = 'permanently_delete'
    REMOVE_RETENTION = 'remove_retention'

class GetFileVersionRetentionsOptionsArg(BaseObject):
    def __init__(self, file_id: Optional[str] = None, file_version_id: Optional[str] = None, policy_id: Optional[str] = None, disposition_action: Optional[GetFileVersionRetentionsOptionsArgDispositionActionField] = None, disposition_before: Optional[str] = None, disposition_after: Optional[str] = None, limit: Optional[int] = None, marker: Optional[str] = None, **kwargs):
        """
        :param file_id: Filters results by files with this ID.
        :type file_id: Optional[str], optional
        :param file_version_id: Filters results by file versions with this ID.
        :type file_version_id: Optional[str], optional
        :param policy_id: Filters results by the retention policy with this ID.
        :type policy_id: Optional[str], optional
        :param disposition_action: Filters results by the retention policy with this disposition
            action.
        :type disposition_action: Optional[GetFileVersionRetentionsOptionsArgDispositionActionField], optional
        :param disposition_before: Filters results by files that will have their disposition
            come into effect before this date.
        :type disposition_before: Optional[str], optional
        :param disposition_after: Filters results by files that will have their disposition
            come into effect after this date.
        :type disposition_after: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.file_id = file_id
        self.file_version_id = file_version_id
        self.policy_id = policy_id
        self.disposition_action = disposition_action
        self.disposition_before = disposition_before
        self.disposition_after = disposition_after
        self.limit = limit
        self.marker = marker

class FileVersionRetentionsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth, JWTAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def get_file_version_retentions(self, options: GetFileVersionRetentionsOptionsArg = None) -> FileVersionRetentions:
        """
        Retrieves all file version retentions for the given enterprise.
        """
        if options is None:
            options = GetFileVersionRetentionsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/file_version_retentions']), FetchOptions(method='GET', params={'file_id': options.file_id, 'file_version_id': options.file_version_id, 'policy_id': options.policy_id, 'disposition_action': options.disposition_action, 'disposition_before': options.disposition_before, 'disposition_after': options.disposition_after, 'limit': options.limit, 'marker': options.marker}, auth=self.auth))
        return FileVersionRetentions.from_dict(json.loads(response.text))
    def get_file_version_retention_by_id(self, file_version_retention_id: str) -> FileVersionRetention:
        """
        Returns information about a file version retention.
        :param file_version_retention_id: The ID of the file version retention
            Example: "3424234"
        :type file_version_retention_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/file_version_retentions/', file_version_retention_id]), FetchOptions(method='GET', auth=self.auth))
        return FileVersionRetention.from_dict(json.loads(response.text))