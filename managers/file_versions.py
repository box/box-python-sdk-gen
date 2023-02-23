from typing import Union

from base_object import BaseObject

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

import json

from schemas import FileVersions

from schemas import ClientError

from schemas import FileVersion

class GetFilesIdVersionsOptionsArg(BaseObject):
    def __init__(self, fields: Union[None, str] = None, limit: Union[None, int] = None, offset: Union[None, int] = None, **kwargs):
        """
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Union[None, str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        :param offset: The offset of the item at which to begin the response.
            Queries with offset parameter value
            exceeding 10000 will be rejected
            with a 400 response.
        :type offset: Union[None, int], optional
        """
        super().__init__(**kwargs)
        self.fields = fields
        self.limit = limit
        self.offset = offset

class GetFilesIdVersionsIdOptionsArg(BaseObject):
    def __init__(self, fields: Union[None, str] = None, **kwargs):
        """
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.fields = fields

class PutFilesIdVersionsIdRequestBodyArg(BaseObject):
    def __init__(self, trashed_at: Union[None, str] = None, **kwargs):
        """
        :param trashed_at: Set this to `null` to clear
            the date and restore the file.
        :type trashed_at: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.trashed_at = trashed_at

class DeleteFilesIdVersionsIdOptionsArg(BaseObject):
    def __init__(self, ifMatch: Union[None, str] = None, **kwargs):
        """
        :param ifMatch: Ensures this item hasn't recently changed before
            making changes.
            Pass in the item's last observed `etag` value
            into this header and the endpoint will fail
            with a `412 Precondition Failed` if it
            has changed since.
        :type ifMatch: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.ifMatch = ifMatch

class PostFilesIdVersionsCurrentRequestBodyArgTypeField:
    pass

class PostFilesIdVersionsCurrentRequestBodyArg(BaseObject):
    def __init__(self, id: Union[None, str] = None, type: Union[None, PostFilesIdVersionsCurrentRequestBodyArgTypeField] = None, **kwargs):
        """
        :param id: The file version ID
        :type id: Union[None, str], optional
        :param type: The type to promote
        :type type: Union[None, PostFilesIdVersionsCurrentRequestBodyArgTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type

class PostFilesIdVersionsCurrentOptionsArg(BaseObject):
    def __init__(self, fields: Union[None, str] = None, **kwargs):
        """
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.fields = fields

class FileVersionsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getFilesIdVersions(self, fileId: str, options: GetFilesIdVersionsOptionsArg = None) -> FileVersions:
        """
        Retrieve a list of the past versions for a file.
        
        Versions are only tracked by Box users with premium accounts. To fetch the ID

        
        of the current version of a file, use the `GET /file/:id` API.

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
            options = GetFilesIdVersionsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', fileId, '/versions']), FetchOptions(method='GET', params={'fields': options.fields, 'limit': options.limit, 'offset': options.offset}, auth=self.auth))
        return FileVersions.from_dict(json.loads(response.text))
    def getFilesIdVersionsId(self, fileId: str, fileVersionId: str, options: GetFilesIdVersionsIdOptionsArg = None) -> FileVersion:
        """
        Retrieve a specific version of a file.
        
        Versions are only tracked for Box users with premium accounts.

        :param fileId: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type fileId: str
        :param fileVersionId: The ID of the file version
            Example: "1234"
        :type fileVersionId: str
        """
        if options is None:
            options = GetFilesIdVersionsIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', fileId, '/versions/', fileVersionId]), FetchOptions(method='GET', params={'fields': options.fields}, auth=self.auth))
        return FileVersion.from_dict(json.loads(response.text))
    def putFilesIdVersionsId(self, fileId: str, fileVersionId: str, requestBody: PutFilesIdVersionsIdRequestBodyArg) -> FileVersion:
        """
        Restores a specific version of a file after it was deleted.
        
        Don't use this endpoint to restore Box Notes,

        
        as it works with file formats such as PDF, DOC,

        
        PPTX or similar.

        :param fileId: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type fileId: str
        :param fileVersionId: The ID of the file version
            Example: "1234"
        :type fileVersionId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', fileId, '/versions/', fileVersionId]), FetchOptions(method='PUT', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return FileVersion.from_dict(json.loads(response.text))
    def deleteFilesIdVersionsId(self, fileId: str, fileVersionId: str, options: DeleteFilesIdVersionsIdOptionsArg = None):
        """
        Move a file version to the trash.
        
        Versions are only tracked for Box users with premium accounts.

        :param fileId: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type fileId: str
        :param fileVersionId: The ID of the file version
            Example: "1234"
        :type fileVersionId: str
        """
        if options is None:
            options = DeleteFilesIdVersionsIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', fileId, '/versions/', fileVersionId]), FetchOptions(method='DELETE', headers={'if-match': options.ifMatch}, auth=self.auth))
        return response.content
    def postFilesIdVersionsCurrent(self, fileId: str, requestBody: PostFilesIdVersionsCurrentRequestBodyArg, options: PostFilesIdVersionsCurrentOptionsArg = None) -> FileVersion:
        """
        Promote a specific version of a file.
        
        If previous versions exist, this method can be used to

        
        promote one of the older versions to the top of the version history.

        
        This creates a new copy of the old version and puts it at the

        
        top of the versions history. The file will have the exact same contents

        
        as the older version, with the the same hash digest, `etag`, and

        
        name as the original.

        
        Other properties such as comments do not get updated to their

        
        former values.

        
        Don't use this endpoint to restore Box Notes,

        
        as it works with file formats such as PDF, DOC,

        
        PPTX or similar.

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
            options = PostFilesIdVersionsCurrentOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', fileId, '/versions/current']), FetchOptions(method='POST', params={'fields': options.fields}, body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return FileVersion.from_dict(json.loads(response.text))