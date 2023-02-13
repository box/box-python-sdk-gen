from typing import Union

from typing import List

from base_object import BaseObject

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from fetch import fetch, FetchOptions, FetchResponse

import json

from schemas import File

from schemas import ClientError

from schemas import TrashFileRestored

class GetByIdOptionsArg(BaseObject):
    def __init__(self, fields: Union[None, List[str]] = None, ifNoneMatch: Union[None, str] = None, boxapi: Union[None, str] = None, **kwargs):
        """
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
            Additionally this field can be used to query any metadata
            applied to the file by specifying the `metadata` field as well
            as the scope and key of the template to retrieve, for example
            `?field=metadata.enterprise_12345.contractTemplate`.
        :type fields: Union[None, List[str]], optional
        :param ifNoneMatch: Ensures an item is only returned if it has changed.
            Pass in the item's last observed `etag` value
            into this header and the endpoint will fail
            with a `304 Not Modified` if the item has not
            changed since.
        :type ifNoneMatch: Union[None, str], optional
        :param boxapi: The URL, and optional password, for the shared link of this item.
            This header can be used to access items that have not been
            explicitly shared with a user.
            Use the format `shared_link=[link]` or if a password is required then
            use `shared_link=[link]&shared_link_password=[password]`.
            This header can be used on the file or folder shared, as well as on any files
            or folders nested within the item.
        :type boxapi: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.fields = fields
        self.ifNoneMatch = ifNoneMatch
        self.boxapi = boxapi

class CreateRequestBodyArgParentField(BaseObject):
    def __init__(self, id: Union[None, str] = None, **kwargs):
        """
        :param id: The ID of parent item
        :type id: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.id = id

class CreateRequestBodyArg(BaseObject):
    def __init__(self, name: Union[None, str] = None, parent: Union[None, CreateRequestBodyArgParentField] = None, **kwargs):
        """
        :param name: An optional new name for the file.
        :type name: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.name = name
        self.parent = parent

class CreateOptionsArg(BaseObject):
    def __init__(self, fields: Union[None, List[str]] = None, **kwargs):
        """
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Union[None, List[str]], optional
        """
        super().__init__(**kwargs)
        self.fields = fields

class FilesManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getById(self, fileId: str, xRepHints: str, options: GetByIdOptionsArg = None) -> File:
        """
        Retrieves the details about a file.
        :param fileId: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type fileId: str
        :param xRepHints: A header required to request specific `representations`
            of a file. Use this in combination with the `fields` query
            parameter to request a specific file representation.
            The general format for these representations is
            `X-Rep-Hints: [...]` where `[...]` is one or many
            hints in the format `[fileType?query]`.
            For example, to request a `png` representation in `32x32`
            as well as `64x64` pixel dimensions provide the following
            hints.
            `x-rep-hints: [jpg?dimensions=32x32][jpg?dimensions=64x64]`
            Additionally, a `text` representation is available for all
            document file types in Box using the `[extracted_text]`
            representation.
            `x-rep-hints: [extracted_text]`
            Example: "[pdf]"
        :type xRepHints: str
        """
        if options is None:
            options = GetByIdOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', fileId]), FetchOptions(method='GET', params={'fields': options.fields}, headers={'if-none-match': options.ifNoneMatch, 'boxapi': options.boxapi, 'x-rep-hints': xRepHints}, auth=self.auth))
        return File.from_dict(json.loads(response.text))
    def create(self, fileId: str, requestBody: CreateRequestBodyArg, options: CreateOptionsArg = None) -> TrashFileRestored:
        """
        Restores a file that has been moved to the trash.
        
        An optional new parent ID can be provided to restore the file to in case the

        
        original folder has been deleted.

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
            options = CreateOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', fileId]), FetchOptions(method='POST', params={'fields': options.fields}, body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return TrashFileRestored.from_dict(json.loads(response.text))