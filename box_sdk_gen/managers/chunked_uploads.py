from typing import Optional

from typing import Dict

import json

from typing import List

from box_sdk_gen.base_object import BaseObject

from box_sdk_gen.schemas import UploadSession

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import UploadedPart

from box_sdk_gen.schemas import UploadParts

from box_sdk_gen.schemas import Files

from box_sdk_gen.schemas import UploadPart

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse


class ChunkedUploadsManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def create_file_upload_session(
        self,
        folder_id: str,
        file_size: int,
        file_name: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> UploadSession:
        """
        Creates an upload session for a new file.
        :param folder_id: The ID of the folder to upload the new file to.
        :type folder_id: str
        :param file_size: The total number of bytes of the file to be uploaded
        :type file_size: int
        :param file_name: The name of new file
        :type file_name: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body = BaseObject(
            folder_id=folder_id, file_size=file_size, file_name=file_name
        )
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://upload.box.com/api/2.0/files/upload_sessions']),
            FetchOptions(
                method='POST',
                headers=headers_map,
                body=json.dumps(request_body.to_dict()),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return UploadSession.from_dict(json.loads(response.text))

    def create_file_upload_session_for_existing_file(
        self,
        file_id: str,
        file_size: int,
        file_name: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> UploadSession:
        """
        Creates an upload session for an existing file.
        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        :param file_size: The total number of bytes of the file to be uploaded
        :type file_size: int
        :param file_name: The optional new name of new file
        :type file_name: Optional[str], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body = BaseObject(file_size=file_size, file_name=file_name)
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                ['https://upload.box.com/api/2.0/files/', file_id, '/upload_sessions']
            ),
            FetchOptions(
                method='POST',
                headers=headers_map,
                body=json.dumps(request_body.to_dict()),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return UploadSession.from_dict(json.loads(response.text))

    def get_file_upload_session_by_id(
        self,
        upload_session_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> UploadSession:
        """
        Return information about an upload session.
        :param upload_session_id: The ID of the upload session.
            Example: "D5E3F7A"
        :type upload_session_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    'https://upload.box.com/api/2.0/files/upload_sessions/',
                    upload_session_id,
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
        return UploadSession.from_dict(json.loads(response.text))

    def upload_file_part(
        self,
        upload_session_id: str,
        request_body: ByteStream,
        digest: str,
        content_range: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> UploadedPart:
        """
        Updates a chunk of an upload session for a file.
        :param upload_session_id: The ID of the upload session.
            Example: "D5E3F7A"
        :type upload_session_id: str
        :param request_body: Request body of uploadFilePart method
        :type request_body: ByteStream
        :param digest: The [RFC3230][1] message digest of the chunk uploaded.
            Only SHA1 is supported. The SHA1 digest must be base64
            encoded. The format of this header is as
            `sha=BASE64_ENCODED_DIGEST`.
            To get the value for the `SHA` digest, use the
            openSSL command to encode the file part:
            `openssl sha1 -binary <FILE_PART_NAME> | base64`
            [1]: https://tools.ietf.org/html/rfc3230
        :type digest: str
        :param content_range: The byte range of the chunk.
            Must not overlap with the range of a part already
            uploaded this session. Each part’s size must be
            exactly equal in size to the part size specified
            in the upload session that you created.
            One exception is the last part of the file, as this can be smaller.
            When providing the value for `content-range`, remember that:
            * The lower bound of each part's byte range
              must be a multiple of the part size.
            * The higher bound must be a multiple of the part size - 1.
        :type content_range: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params(
            {
                'digest': to_string(digest),
                'content-range': to_string(content_range),
                **extra_headers,
            }
        )
        response: FetchResponse = fetch(
            ''.join(
                [
                    'https://upload.box.com/api/2.0/files/upload_sessions/',
                    upload_session_id,
                ]
            ),
            FetchOptions(
                method='PUT',
                headers=headers_map,
                body=request_body,
                content_type='application/octet-stream',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return UploadedPart.from_dict(json.loads(response.text))

    def delete_file_upload_session_by_id(
        self,
        upload_session_id: str,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> None:
        """
        Abort an upload session and discard all data uploaded.

        This cannot be reversed.

        :param upload_session_id: The ID of the upload session.
            Example: "D5E3F7A"
        :type upload_session_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    'https://upload.box.com/api/2.0/files/upload_sessions/',
                    upload_session_id,
                ]
            ),
            FetchOptions(
                method='DELETE',
                headers=headers_map,
                response_format=None,
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return None

    def get_file_upload_session_parts(
        self,
        upload_session_id: str,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> UploadParts:
        """
        Return a list of the chunks uploaded to the upload

        session so far.

        :param upload_session_id: The ID of the upload session.
            Example: "D5E3F7A"
        :type upload_session_id: str
        :param offset: The offset of the item at which to begin the response.
            Queries with offset parameter value
            exceeding 10000 will be rejected
            with a 400 response.
        :type offset: Optional[int], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params(
            {'offset': to_string(offset), 'limit': to_string(limit)}
        )
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    'https://upload.box.com/api/2.0/files/upload_sessions/',
                    upload_session_id,
                    '/parts',
                ]
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
        return UploadParts.from_dict(json.loads(response.text))

    def create_file_upload_session_commit(
        self,
        upload_session_id: str,
        parts: List[UploadPart],
        digest: str,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> Files:
        """
        Close an upload session and create a file from the

        uploaded chunks.

        :param upload_session_id: The ID of the upload session.
            Example: "D5E3F7A"
        :type upload_session_id: str
        :param parts: The list details for the uploaded parts
        :type parts: List[UploadPart]
        :param digest: The [RFC3230][1] message digest of the whole file.
            Only SHA1 is supported. The SHA1 digest must be Base64
            encoded. The format of this header is as
            `sha=BASE64_ENCODED_DIGEST`.
            [1]: https://tools.ietf.org/html/rfc3230
        :type digest: str
        :param if_match: Ensures this item hasn't recently changed before
            making changes.
            Pass in the item's last observed `etag` value
            into this header and the endpoint will fail
            with a `412 Precondition Failed` if it
            has changed since.
        :type if_match: Optional[str], optional
        :param if_none_match: Ensures an item is only returned if it has changed.
            Pass in the item's last observed `etag` value
            into this header and the endpoint will fail
            with a `304 Not Modified` if the item has not
            changed since.
        :type if_none_match: Optional[str], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body = BaseObject(parts=parts)
        headers_map: Dict[str, str] = prepare_params(
            {
                'digest': to_string(digest),
                'if-match': to_string(if_match),
                'if-none-match': to_string(if_none_match),
                **extra_headers,
            }
        )
        response: FetchResponse = fetch(
            ''.join(
                [
                    'https://upload.box.com/api/2.0/files/upload_sessions/',
                    upload_session_id,
                    '/commit',
                ]
            ),
            FetchOptions(
                method='POST',
                headers=headers_map,
                body=json.dumps(request_body.to_dict()),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return Files.from_dict(json.loads(response.text))
