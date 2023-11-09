from typing import Optional

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.json import sd_to_json

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse


class DownloadsManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def download_file(
        self,
        file_id: str,
        version: Optional[str] = None,
        access_token: Optional[str] = None,
        range: Optional[str] = None,
        boxapi: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> ByteStream:
        """
        Returns the contents of a file in binary format.
        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        :param version: The file version to download
        :type version: Optional[str], optional
        :param access_token: An optional access token that can be used to pre-authenticate this request, which means that a download link can be shared with a browser or a third party service without them needing to know how to handle the authentication.
            When using this parameter, please make sure that the access token is sufficiently scoped down to only allow read access to that file and no other files or folders.
        :type access_token: Optional[str], optional
        :param range: The byte range of the content to download.
            The format `bytes={start_byte}-{end_byte}` can be used to specify
            what section of the file to download.
        :type range: Optional[str], optional
        :param boxapi: The URL, and optional password, for the shared link of this item.
            This header can be used to access items that have not been
            explicitly shared with a user.
            Use the format `shared_link=[link]` or if a password is required then
            use `shared_link=[link]&shared_link_password=[password]`.
            This header can be used on the file or folder shared, as well as on any files
            or folders nested within the item.
        :type boxapi: Optional[str], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params({
            'version': to_string(version), 'access_token': to_string(access_token)
        })
        headers_map: Dict[str, str] = prepare_params({
            'range': to_string(range), 'boxapi': to_string(boxapi), **extra_headers
        })
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/files/', to_string(file_id), '/content']),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='binary',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return response.content
