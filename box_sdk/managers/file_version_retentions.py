from enum import Enum

from typing import Optional

from typing import Dict

import json

from box_sdk.schemas import FileVersionRetentions

from box_sdk.schemas import ClientError

from box_sdk.schemas import FileVersionRetention

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.utils import to_map

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetFileVersionRetentionsDispositionActionArg(str, Enum):
    PERMANENTLY_DELETE = 'permanently_delete'
    REMOVE_RETENTION = 'remove_retention'

class FileVersionRetentionsManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def get_file_version_retentions(self, file_id: Optional[str] = None, file_version_id: Optional[str] = None, policy_id: Optional[str] = None, disposition_action: Optional[GetFileVersionRetentionsDispositionActionArg] = None, disposition_before: Optional[str] = None, disposition_after: Optional[str] = None, limit: Optional[int] = None, marker: Optional[str] = None) -> FileVersionRetentions:
        """
        Retrieves all file version retentions for the given enterprise.
        :param file_id: Filters results by files with this ID.
        :type file_id: Optional[str], optional
        :param file_version_id: Filters results by file versions with this ID.
        :type file_version_id: Optional[str], optional
        :param policy_id: Filters results by the retention policy with this ID.
        :type policy_id: Optional[str], optional
        :param disposition_action: Filters results by the retention policy with this disposition
            action.
        :type disposition_action: Optional[GetFileVersionRetentionsDispositionActionArg], optional
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
        query_params: Dict = {'file_id': file_id, 'file_version_id': file_version_id, 'policy_id': policy_id, 'disposition_action': disposition_action, 'disposition_before': disposition_before, 'disposition_after': disposition_after, 'limit': limit, 'marker': marker}
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/file_version_retentions']), FetchOptions(method='GET', params=to_map(query_params), auth=self.auth, network_session=self.network_session))
        return FileVersionRetentions.from_dict(json.loads(response.text))
    def get_file_version_retention_by_id(self, file_version_retention_id: str) -> FileVersionRetention:
        """
        Returns information about a file version retention.
        :param file_version_retention_id: The ID of the file version retention
            Example: "3424234"
        :type file_version_retention_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/file_version_retentions/', file_version_retention_id]), FetchOptions(method='GET', auth=self.auth, network_session=self.network_session))
        return FileVersionRetention.from_dict(json.loads(response.text))