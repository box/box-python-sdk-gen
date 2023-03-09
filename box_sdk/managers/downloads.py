from typing import Union

from box_sdk.base_object import BaseObject

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch, FetchOptions, FetchResponse

from box_sdk.schemas import ClientError

from box_sdk.schemas import Files

class GetFilesIdContentOptionsArg(BaseObject):
    def __init__(self, range: Union[None, str] = None, boxapi: Union[None, str] = None, version: Union[None, str] = None, accessToken: Union[None, str] = None, **kwargs):
        """
        :param range: The byte range of the content to download.
            The format `bytes={start_byte}-{end_byte}` can be used to specify
            what section of the file to download.
        :type range: Union[None, str], optional
        :param boxapi: The URL, and optional password, for the shared link of this item.
            This header can be used to access items that have not been
            explicitly shared with a user.
            Use the format `shared_link=[link]` or if a password is required then
            use `shared_link=[link]&shared_link_password=[password]`.
            This header can be used on the file or folder shared, as well as on any files
            or folders nested within the item.
        :type boxapi: Union[None, str], optional
        :param version: The file version to download
        :type version: Union[None, str], optional
        :param accessToken: An optional access token that can be used to pre-authenticate this request, which means that a download link can be shared with a browser or a third party service without them needing to know how to handle the authentication.
            When using this parameter, please make sure that the access token is sufficiently scoped down to only allow read access to that file and no other files or folders.
        :type accessToken: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.range = range
        self.boxapi = boxapi
        self.version = version
        self.accessToken = accessToken

class DownloadsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getFilesIdContent(self, fileId: str, options: GetFilesIdContentOptionsArg = None):
        """
        Returns the contents of a file in binary format.
        :param fileId: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type fileId: str
        """
        if options is None:
            options = GetFilesIdContentOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', fileId, '/content']), FetchOptions(method='GET', params={'version': options.version, 'access_token': options.accessToken}, headers={'range': options.range, 'boxapi': options.boxapi}, auth=self.auth))
        return response.content