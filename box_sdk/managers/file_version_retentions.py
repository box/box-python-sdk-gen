from enum import Enum

from typing import Union

from box_sdk.base_object import BaseObject

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch, FetchOptions, FetchResponse

import json

from box_sdk.schemas import FileVersionRetentions

from box_sdk.schemas import ClientError

from box_sdk.schemas import FileVersionRetention

class GetFileVersionRetentionsOptionsArgDispositionActionField(str, Enum):
    PERMANENTLY_DELETE = 'permanently_delete'
    REMOVE_RETENTION = 'remove_retention'

class GetFileVersionRetentionsOptionsArg(BaseObject):
    def __init__(self, fileId: Union[None, str] = None, fileVersionId: Union[None, str] = None, policyId: Union[None, str] = None, dispositionAction: Union[None, GetFileVersionRetentionsOptionsArgDispositionActionField] = None, dispositionBefore: Union[None, str] = None, dispositionAfter: Union[None, str] = None, limit: Union[None, int] = None, marker: Union[None, str] = None, **kwargs):
        """
        :param fileId: Filters results by files with this ID.
        :type fileId: Union[None, str], optional
        :param fileVersionId: Filters results by file versions with this ID.
        :type fileVersionId: Union[None, str], optional
        :param policyId: Filters results by the retention policy with this ID.
        :type policyId: Union[None, str], optional
        :param dispositionAction: Filters results by the retention policy with this disposition
            action.
        :type dispositionAction: Union[None, GetFileVersionRetentionsOptionsArgDispositionActionField], optional
        :param dispositionBefore: Filters results by files that will have their disposition
            come into effect before this date.
        :type dispositionBefore: Union[None, str], optional
        :param dispositionAfter: Filters results by files that will have their disposition
            come into effect after this date.
        :type dispositionAfter: Union[None, str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.fileId = fileId
        self.fileVersionId = fileVersionId
        self.policyId = policyId
        self.dispositionAction = dispositionAction
        self.dispositionBefore = dispositionBefore
        self.dispositionAfter = dispositionAfter
        self.limit = limit
        self.marker = marker

class FileVersionRetentionsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getFileVersionRetentions(self, options: GetFileVersionRetentionsOptionsArg = None) -> FileVersionRetentions:
        """
        Retrieves all file version retentions for the given enterprise.
        """
        if options is None:
            options = GetFileVersionRetentionsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/file_version_retentions']), FetchOptions(method='GET', params={'file_id': options.fileId, 'file_version_id': options.fileVersionId, 'policy_id': options.policyId, 'disposition_action': options.dispositionAction, 'disposition_before': options.dispositionBefore, 'disposition_after': options.dispositionAfter, 'limit': options.limit, 'marker': options.marker}, auth=self.auth))
        return FileVersionRetentions.from_dict(json.loads(response.text))
    def getFileVersionRetentionsId(self, fileVersionRetentionId: str) -> FileVersionRetention:
        """
        Returns information about a file version retention.
        :param fileVersionRetentionId: The ID of the file version retention
            Example: "3424234"
        :type fileVersionRetentionId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/file_version_retentions/', fileVersionRetentionId]), FetchOptions(method='GET', auth=self.auth))
        return FileVersionRetention.from_dict(json.loads(response.text))