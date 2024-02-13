from typing import Optional

from box_sdk_gen.base_object import BaseObject

from typing import List

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import serialize

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.schemas import Files

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import UploadUrl

from box_sdk_gen.schemas import ConflictError

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.json_data import sd_to_json

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse

from box_sdk_gen.fetch import MultipartItem

from box_sdk_gen.json_data import SerializedData


class UploadFileVersionAttributes(BaseObject):
    def __init__(self, name: str, content_modified_at: Optional[str] = None, **kwargs):
        """
        :param name: An optional new name for the file. If specified, the file
            will be renamed when the new version is uploaded.
        :type name: str
        :param content_modified_at: Defines the time the file was last modified at.
            If not set, the upload time will be used.
        :type content_modified_at: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.name = name
        self.content_modified_at = content_modified_at


class UploadFileAttributesParentField(BaseObject):
    def __init__(self, id: str, **kwargs):
        """
        :param id: The id of the parent folder. Use
            `0` for the user's root folder.
        :type id: str
        """
        super().__init__(**kwargs)
        self.id = id


class UploadFileAttributes(BaseObject):
    def __init__(
        self,
        name: str,
        parent: UploadFileAttributesParentField,
        content_created_at: Optional[str] = None,
        content_modified_at: Optional[str] = None,
        **kwargs
    ):
        """
        :param name: The name of the file
        :type name: str
        :param parent: The parent folder to upload the file to
        :type parent: UploadFileAttributesParentField
        :param content_created_at: Defines the time the file was originally created at.
            If not set, the upload time will be used.
        :type content_created_at: Optional[str], optional
        :param content_modified_at: Defines the time the file was last modified at.
            If not set, the upload time will be used.
        :type content_modified_at: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.name = name
        self.parent = parent
        self.content_created_at = content_created_at
        self.content_modified_at = content_modified_at


class PreflightFileUploadCheckParent(BaseObject):
    def __init__(self, id: Optional[str] = None, **kwargs):
        """
        :param id: The ID of parent item
        :type id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.id = id


class UploadsManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: NetworkSession = None,
    ):
        if network_session is None:
            network_session = NetworkSession()
        self.auth = auth
        self.network_session = network_session

    def upload_file_version(
        self,
        file_id: str,
        attributes: UploadFileVersionAttributes,
        file: ByteStream,
        file_file_name: Optional[str] = None,
        file_content_type: Optional[str] = None,
        fields: Optional[List[str]] = None,
        if_match: Optional[str] = None,
        content_md_5: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> Files:
        """
        Update a file's content. For file sizes over 50MB we recommend

        using the Chunk Upload APIs.


        # Request body order


        The `attributes` part of the body must come **before** the


        `file` part. Requests that do not follow this format when


        uploading the file will receive a HTTP `400` error with a


        `metadata_after_file_contents` error code.

        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        :param attributes: The additional attributes of the file being uploaded. Mainly the
            name and the parent folder. These attributes are part of the multi
            part request body and are in JSON format.
            <Message warning>
              The `attributes` part of the body must come **before** the
              `file` part. Requests that do not follow this format when
              uploading the file will receive a HTTP `400` error with a
              `metadata_after_file_contents` error code.
            </Message>
        :type attributes: UploadFileVersionAttributes
        :param file: The content of the file to upload to Box.
            <Message warning>
              The `attributes` part of the body must come **before** the
              `file` part. Requests that do not follow this format when
              uploading the file will receive a HTTP `400` error with a
              `metadata_after_file_contents` error code.
            </Message>
        :type file: ByteStream
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[List[str]], optional
        :param if_match: Ensures this item hasn't recently changed before
            making changes.
            Pass in the item's last observed `etag` value
            into this header and the endpoint will fail
            with a `412 Precondition Failed` if it
            has changed since.
        :type if_match: Optional[str], optional
        :param content_md_5: An optional header containing the SHA1 hash of the file to
            ensure that the file was not corrupted in transit.
        :type content_md_5: Optional[str], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {
            'attributes': attributes,
            'file': file,
            'file_file_name': file_file_name,
            'file_content_type': file_content_type,
        }
        query_params_map: Dict[str, str] = prepare_params({'fields': to_string(fields)})
        headers_map: Dict[str, str] = prepare_params(
            {
                'if-match': to_string(if_match),
                'content-md5': to_string(content_md_5),
                **extra_headers,
            }
        )
        response: FetchResponse = fetch(
            ''.join(
                [
                    self.network_session.base_urls.upload_url,
                    '/files/',
                    to_string(file_id),
                    '/content',
                ]
            ),
            FetchOptions(
                method='POST',
                params=query_params_map,
                headers=headers_map,
                multipart_data=[
                    MultipartItem(
                        part_name='attributes',
                        data=serialize(request_body['attributes']),
                    ),
                    MultipartItem(
                        part_name='file',
                        file_stream=request_body['file'],
                        file_name=request_body['file_file_name'],
                        content_type=request_body['file_content_type'],
                    ),
                ],
                content_type='multipart/form-data',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, Files)

    def upload_file(
        self,
        attributes: UploadFileAttributes,
        file: ByteStream,
        file_file_name: Optional[str] = None,
        file_content_type: Optional[str] = None,
        fields: Optional[List[str]] = None,
        content_md_5: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> Files:
        """
        Uploads a small file to Box. For file sizes over 50MB we recommend

        using the Chunk Upload APIs.


        # Request body order


        The `attributes` part of the body must come **before** the


        `file` part. Requests that do not follow this format when


        uploading the file will receive a HTTP `400` error with a


        `metadata_after_file_contents` error code.

        :param attributes: The additional attributes of the file being uploaded. Mainly the
            name and the parent folder. These attributes are part of the multi
            part request body and are in JSON format.
            <Message warning>
              The `attributes` part of the body must come **before** the
              `file` part. Requests that do not follow this format when
              uploading the file will receive a HTTP `400` error with a
              `metadata_after_file_contents` error code.
            </Message>
        :type attributes: UploadFileAttributes
        :param file: The content of the file to upload to Box.
            <Message warning>
              The `attributes` part of the body must come **before** the
              `file` part. Requests that do not follow this format when
              uploading the file will receive a HTTP `400` error with a
              `metadata_after_file_contents` error code.
            </Message>
        :type file: ByteStream
        :param fields: A comma-separated list of attributes to include in the
            response. This can be used to request fields that are
            not normally returned in a standard response.
            Be aware that specifying this parameter will have the
            effect that none of the standard fields are returned in
            the response unless explicitly specified, instead only
            fields for the mini representation are returned, additional
            to the fields requested.
        :type fields: Optional[List[str]], optional
        :param content_md_5: An optional header containing the SHA1 hash of the file to
            ensure that the file was not corrupted in transit.
        :type content_md_5: Optional[str], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {
            'attributes': attributes,
            'file': file,
            'file_file_name': file_file_name,
            'file_content_type': file_content_type,
        }
        query_params_map: Dict[str, str] = prepare_params({'fields': to_string(fields)})
        headers_map: Dict[str, str] = prepare_params(
            {'content-md5': to_string(content_md_5), **extra_headers}
        )
        response: FetchResponse = fetch(
            ''.join([self.network_session.base_urls.upload_url, '/files/content']),
            FetchOptions(
                method='POST',
                params=query_params_map,
                headers=headers_map,
                multipart_data=[
                    MultipartItem(
                        part_name='attributes',
                        data=serialize(request_body['attributes']),
                    ),
                    MultipartItem(
                        part_name='file',
                        file_stream=request_body['file'],
                        file_name=request_body['file_file_name'],
                        content_type=request_body['file_content_type'],
                    ),
                ],
                content_type='multipart/form-data',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, Files)

    def preflight_file_upload_check(
        self,
        name: Optional[str] = None,
        size: Optional[int] = None,
        parent: Optional[PreflightFileUploadCheckParent] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> UploadUrl:
        """
        Performs a check to verify that a file will be accepted by Box

        before you upload the entire file.

        :param name: The name for the file
        :type name: Optional[str], optional
        :param size: The size of the file in bytes
        :type size: Optional[int], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {'name': name, 'size': size, 'parent': parent}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([self.network_session.base_urls.base_url, '/files/content']),
            FetchOptions(
                method='OPTIONS',
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, UploadUrl)
