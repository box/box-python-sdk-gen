from enum import Enum

from typing import Optional

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.schemas import FileVersionRetentions

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import FileVersionRetention

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.json_data import sd_to_json

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse

from box_sdk_gen.json_data import SerializedData


class GetFileVersionRetentionsDispositionAction(str, Enum):
    PERMANENTLY_DELETE = 'permanently_delete'
    REMOVE_RETENTION = 'remove_retention'


class FileVersionRetentionsManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: NetworkSession = None,
    ):
        if network_session is None:
            network_session = NetworkSession()
        self.auth = auth
        self.network_session = network_session

    def get_file_version_retentions(
        self,
        file_id: Optional[str] = None,
        file_version_id: Optional[str] = None,
        policy_id: Optional[str] = None,
        disposition_action: Optional[GetFileVersionRetentionsDispositionAction] = None,
        disposition_before: Optional[str] = None,
        disposition_after: Optional[str] = None,
        limit: Optional[int] = None,
        marker: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> FileVersionRetentions:
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
        :type disposition_action: Optional[GetFileVersionRetentionsDispositionAction], optional
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
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params(
            {
                'file_id': to_string(file_id),
                'file_version_id': to_string(file_version_id),
                'policy_id': to_string(policy_id),
                'disposition_action': to_string(disposition_action),
                'disposition_before': to_string(disposition_before),
                'disposition_after': to_string(disposition_after),
                'limit': to_string(limit),
                'marker': to_string(marker),
            }
        )
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [self.network_session.base_urls.base_url, '/file_version_retentions']
            ),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, FileVersionRetentions)

    def get_file_version_retention_by_id(
        self,
        file_version_retention_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> FileVersionRetention:
        """
        Returns information about a file version retention.
        :param file_version_retention_id: The ID of the file version retention
            Example: "3424234"
        :type file_version_retention_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    self.network_session.base_urls.base_url,
                    '/file_version_retentions/',
                    to_string(file_version_retention_id),
                ]
            ),
            FetchOptions(
                method='GET',
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, FileVersionRetention)
