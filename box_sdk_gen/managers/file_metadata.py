from enum import Enum

from typing import Optional

from typing import Dict

from box_sdk_gen.base_object import BaseObject

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.serialization import serialize

from typing import List

from box_sdk_gen.schemas import Metadatas

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import MetadataFull

from box_sdk_gen.schemas import Metadata

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse

from box_sdk_gen.json import sd_to_json

from box_sdk_gen.json import SerializedData


class GetFileMetadataByIdScopeArg(str, Enum):
    GLOBAL = 'global'
    ENTERPRISE = 'enterprise'


class CreateFileMetadataByIdScopeArg(str, Enum):
    GLOBAL = 'global'
    ENTERPRISE = 'enterprise'


class UpdateFileMetadataByIdScopeArg(str, Enum):
    GLOBAL = 'global'
    ENTERPRISE = 'enterprise'


class UpdateFileMetadataByIdRequestBodyArgOpField(str, Enum):
    ADD = 'add'
    REPLACE = 'replace'
    REMOVE = 'remove'
    TEST = 'test'
    MOVE = 'move'
    COPY = 'copy'


class UpdateFileMetadataByIdRequestBodyArg(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {
        'from_': 'from',
        **BaseObject._fields_to_json_mapping,
    }
    _json_to_fields_mapping: Dict[str, str] = {
        'from': 'from_',
        **BaseObject._json_to_fields_mapping,
    }

    def __init__(
        self,
        op: Optional[UpdateFileMetadataByIdRequestBodyArgOpField] = None,
        path: Optional[str] = None,
        value: Optional[str] = None,
        from_: Optional[str] = None,
        **kwargs
    ):
        """
        :param op: The type of change to perform on the template. Some
            of these are hazardous as they will change existing templates.
        :type op: Optional[UpdateFileMetadataByIdRequestBodyArgOpField], optional
        :param path: The location in the metadata JSON object
            to apply the changes to, in the format of a
            [JSON-Pointer](https://tools.ietf.org/html/rfc6901).
            The path must always be prefixed with a `/` to represent the root
            of the template. The characters `~` and `/` are reserved
            characters and must be escaped in the key.
        :type path: Optional[str], optional
        :param value: The value to be set or tested.
            Required for `add`, `replace`, and `test` operations. For `add`,
            if the value exists already the previous value will be overwritten
            by the new value. For `replace`, the value must exist before
            replacing.
            For `test`, the existing value at the `path` location must match
            the specified value.
        :type value: Optional[str], optional
        :param from_: The location in the metadata JSON object to move or copy a value
            from. Required for `move` or `copy` operations and must be in the
            format of a [JSON-Pointer](https://tools.ietf.org/html/rfc6901).
        :type from_: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.op = op
        self.path = path
        self.value = value
        self.from_ = from_


class DeleteFileMetadataByIdScopeArg(str, Enum):
    GLOBAL = 'global'
    ENTERPRISE = 'enterprise'


class FileMetadataManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def get_file_metadata(
        self, file_id: str, extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> Metadatas:
        """
        Retrieves all metadata for a given file.
        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/files/', to_string(file_id), '/metadata'
            ]),
            FetchOptions(
                method='GET',
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, Metadatas)

    def get_file_metadata_by_id(
        self,
        file_id: str,
        scope: GetFileMetadataByIdScopeArg,
        template_key: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> MetadataFull:
        """
        Retrieves the instance of a metadata template that has been applied to a

        file.

        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        :param scope: The scope of the metadata template
            Example: "global"
        :type scope: GetFileMetadataByIdScopeArg
        :param template_key: The name of the metadata template
            Example: "properties"
        :type template_key: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/files/',
                to_string(file_id),
                '/metadata/',
                to_string(scope),
                '/',
                to_string(template_key),
            ]),
            FetchOptions(
                method='GET',
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, MetadataFull)

    def create_file_metadata_by_id(
        self,
        file_id: str,
        scope: CreateFileMetadataByIdScopeArg,
        template_key: str,
        request_body: Dict[str, str],
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> Metadata:
        """
        Applies an instance of a metadata template to a file.

        In most cases only values that are present in the metadata template


        will be accepted, except for the `global.properties` template which accepts


        any key-value pair.

        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        :param scope: The scope of the metadata template
            Example: "global"
        :type scope: CreateFileMetadataByIdScopeArg
        :param template_key: The name of the metadata template
            Example: "properties"
        :type template_key: str
        :param request_body: Request body of createFileMetadataById method
        :type request_body: Dict[str, str]
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/files/',
                to_string(file_id),
                '/metadata/',
                to_string(scope),
                '/',
                to_string(template_key),
            ]),
            FetchOptions(
                method='POST',
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, Metadata)

    def update_file_metadata_by_id(
        self,
        file_id: str,
        scope: UpdateFileMetadataByIdScopeArg,
        template_key: str,
        request_body: List[UpdateFileMetadataByIdRequestBodyArg],
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> Metadata:
        """
        Updates a piece of metadata on a file.

        The metadata instance can only be updated if the template has already been


        applied to the file before. When editing metadata, only values that match


        the metadata template schema will be accepted.


        The update is applied atomically. If any errors occur during the


        application of the operations, the metadata instance will not be changed.

        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        :param scope: The scope of the metadata template
            Example: "global"
        :type scope: UpdateFileMetadataByIdScopeArg
        :param template_key: The name of the metadata template
            Example: "properties"
        :type template_key: str
        :param request_body: Request body of updateFileMetadataById method
        :type request_body: List[UpdateFileMetadataByIdRequestBodyArg]
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/files/',
                to_string(file_id),
                '/metadata/',
                to_string(scope),
                '/',
                to_string(template_key),
            ]),
            FetchOptions(
                method='PUT',
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/json-patch+json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, Metadata)

    def delete_file_metadata_by_id(
        self,
        file_id: str,
        scope: DeleteFileMetadataByIdScopeArg,
        template_key: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> None:
        """
        Deletes a piece of file metadata.
        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        :param scope: The scope of the metadata template
            Example: "global"
        :type scope: DeleteFileMetadataByIdScopeArg
        :param template_key: The name of the metadata template
            Example: "properties"
        :type template_key: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/files/',
                to_string(file_id),
                '/metadata/',
                to_string(scope),
                '/',
                to_string(template_key),
            ]),
            FetchOptions(
                method='DELETE',
                headers=headers_map,
                response_format=None,
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return None
