from typing import Optional

from box_sdk.base_object import BaseObject

from typing import Dict

from box_sdk.schemas import ClientError

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class DownloadFileOptionsArg(BaseObject):
    def __init__(self, range: Optional[str] = None, boxapi: Optional[str] = None, version: Optional[str] = None, access_token: Optional[str] = None, **kwargs):
        """
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
        :param version: The file version to download
        :type version: Optional[str], optional
        :param access_token: An optional access token that can be used to pre-authenticate this request, which means that a download link can be shared with a browser or a third party service without them needing to know how to handle the authentication.
            When using this parameter, please make sure that the access token is sufficiently scoped down to only allow read access to that file and no other files or folders.
        :type access_token: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.range = range
        self.boxapi = boxapi
        self.version = version
        self.access_token = access_token

class DownloadsManager(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {'network_session': 'networkSession', **BaseObject._fields_to_json_mapping}
    _json_to_fields_mapping: Dict[str, str] = {'networkSession': 'network_session', **BaseObject._json_to_fields_mapping}
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None, **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
        self.network_session = network_session
    def download_file(self, file_id: str, options: DownloadFileOptionsArg = None):
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
        """
        if options is None:
            options = DownloadFileOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/content']), FetchOptions(method='GET', params={'version': options.version, 'access_token': options.access_token}, headers={'range': options.range, 'boxapi': options.boxapi}, auth=self.auth, network_session=self.network_session))
        return response.content