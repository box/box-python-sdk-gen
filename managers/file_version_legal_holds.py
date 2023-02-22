from typing import Union

from base_object import BaseObject

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

import json

from schemas import FileVersionLegalHold

from schemas import ClientError

from schemas import FileVersionLegalHolds

class GetFileVersionLegalHoldsOptionsArg(BaseObject):
    def __init__(self, marker: Union[None, str] = None, limit: Union[None, int] = None, **kwargs):
        """
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Union[None, str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        """
        super().__init__(**kwargs)
        self.marker = marker
        self.limit = limit

class FileVersionLegalHoldsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getFileVersionLegalHoldsId(self, fileVersionLegalHoldId: str) -> FileVersionLegalHold:
        """
        Retrieves information about the legal hold policies
        
        assigned to a file version.

        :param fileVersionLegalHoldId: The ID of the file version legal hold
            Example: "2348213"
        :type fileVersionLegalHoldId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/file_version_legal_holds/', fileVersionLegalHoldId]), FetchOptions(method='GET', auth=self.auth))
        return FileVersionLegalHold.from_dict(json.loads(response.text))
    def getFileVersionLegalHolds(self, policyId: str, options: GetFileVersionLegalHoldsOptionsArg = None) -> FileVersionLegalHolds:
        """
        Get a list of file versions on legal hold for a legal hold
        
        assignment.

        
        Due to ongoing re-architecture efforts this API might not return all file

        
        versions for this policy ID.

        
        Instead, this API will only return file versions held in the legacy

        
        architecture. Two new endpoints will available to request any file versions

        
        held in the new architecture.

        
        For file versions held in the new architecture, the `GET

        
        /legal_hold_policy_assignments/:id/file_versions_on_hold` API can be used to

        
        return all past file versions available for this policy assignment, and the

        
        `GET /legal_hold_policy_assignments/:id/files_on_hold` API can be used to

        
        return any current (latest) versions of a file under legal hold.

        
        The `GET /legal_hold_policy_assignments?policy_id={id}` API can be used to

        
        find a list of policy assignments for a given policy ID.

        
        Once the re-architecture is completed this API will be deprecated.

        :param policyId: The ID of the legal hold policy to get the file version legal
            holds for.
            Example: "133870"
        :type policyId: str
        """
        if options is None:
            options = GetFileVersionLegalHoldsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/file_version_legal_holds']), FetchOptions(method='GET', params={'policy_id': policyId, 'marker': options.marker, 'limit': options.limit}, auth=self.auth))
        return FileVersionLegalHolds.from_dict(json.loads(response.text))