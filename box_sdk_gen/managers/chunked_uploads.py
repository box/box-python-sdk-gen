from typing import List

from typing import Optional

from typing import Dict

from box_sdk_gen.serialization import serialize

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import Buffer

from box_sdk_gen.utils import HashName

from box_sdk_gen.utils import Iterator

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

from box_sdk_gen.json import SerializedData

from box_sdk_gen.json import sd_to_json

from box_sdk_gen.utils import generate_byte_stream_from_buffer

from box_sdk_gen.utils import hex_to_base_64

from box_sdk_gen.utils import iterate_chunks

from box_sdk_gen.utils import read_byte_stream

from box_sdk_gen.utils import reduce_iterator

from box_sdk_gen.utils import Hash

from box_sdk_gen.utils import list_concat

from box_sdk_gen.utils import buffer_length


class PartAccumulator:
    def __init__(
        self,
        last_index: int,
        parts: List[UploadPart],
        file_size: int,
        upload_session_id: str,
        file_hash: Hash,
    ):
        self.last_index = last_index
        self.parts = parts
        self.file_size = file_size
        self.upload_session_id = upload_session_id
        self.file_hash = file_hash


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
        request_body: Dict = {
            'folder_id': folder_id,
            'file_size': file_size,
            'file_name': file_name,
        }
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://upload.box.com/api/2.0/files/upload_sessions']),
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
        return deserialize(response.data, UploadSession)

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
        request_body: Dict = {'file_size': file_size, 'file_name': file_name}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://upload.box.com/api/2.0/files/',
                to_string(file_id),
                '/upload_sessions',
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
        return deserialize(response.data, UploadSession)

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
            ''.join([
                'https://upload.box.com/api/2.0/files/upload_sessions/',
                to_string(upload_session_id),
            ]),
            FetchOptions(
                method='GET',
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, UploadSession)

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
        headers_map: Dict[str, str] = prepare_params({
            'digest': to_string(digest),
            'content-range': to_string(content_range),
            **extra_headers,
        })
        response: FetchResponse = fetch(
            ''.join([
                'https://upload.box.com/api/2.0/files/upload_sessions/',
                to_string(upload_session_id),
            ]),
            FetchOptions(
                method='PUT',
                headers=headers_map,
                file_stream=request_body,
                content_type='application/octet-stream',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, UploadedPart)

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
            ''.join([
                'https://upload.box.com/api/2.0/files/upload_sessions/',
                to_string(upload_session_id),
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
        query_params_map: Dict[str, str] = prepare_params({
            'offset': to_string(offset), 'limit': to_string(limit)
        })
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://upload.box.com/api/2.0/files/upload_sessions/',
                to_string(upload_session_id),
                '/parts',
            ]),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, UploadParts)

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
        request_body: Dict = {'parts': parts}
        headers_map: Dict[str, str] = prepare_params({
            'digest': to_string(digest),
            'if-match': to_string(if_match),
            'if-none-match': to_string(if_none_match),
            **extra_headers,
        })
        response: FetchResponse = fetch(
            ''.join([
                'https://upload.box.com/api/2.0/files/upload_sessions/',
                to_string(upload_session_id),
                '/commit',
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
        return deserialize(response.data, Files)

    def reducer(self, acc: PartAccumulator, chunk: ByteStream):
        last_index: int = acc.last_index
        parts: List[UploadPart] = acc.parts
        chunk_buffer: Buffer = read_byte_stream(chunk)
        hash: Hash = Hash(algorithm=HashName.SHA1.value)
        hash.update_hash(chunk_buffer)
        sha_1: str = hash.digest_hash('base64')
        digest: str = ''.join(['sha=', sha_1])
        chunk_size: int = buffer_length(chunk_buffer)
        bytes_start: int = last_index + 1
        bytes_end: int = last_index + chunk_size
        content_range: str = ''.join([
            'bytes ',
            to_string(bytes_start),
            '-',
            to_string(bytes_end),
            '/',
            to_string(acc.file_size),
        ])
        uploaded_part: UploadedPart = self.upload_file_part(
            upload_session_id=acc.upload_session_id,
            request_body=generate_byte_stream_from_buffer(chunk_buffer),
            digest=digest,
            content_range=content_range,
        )
        part: UploadPart = uploaded_part.part
        part_sha_1: str = hex_to_base_64(part.sha_1)
        assert part_sha_1 == sha_1
        assert part.size == chunk_size
        assert part.offset == bytes_start
        acc.file_hash.update_hash(chunk_buffer)
        return PartAccumulator(
            last_index=bytes_end,
            parts=list_concat(parts, [part]),
            file_size=acc.file_size,
            upload_session_id=acc.upload_session_id,
            file_hash=acc.file_hash,
        )

    def upload_big_file(
        self, file: ByteStream, file_name: str, file_size: int, parent_folder_id: str
    ):
        """
        Starts the process of chunk uploading a big file. Should return a File object representing uploaded file.
        :param file: The stream of the file to upload.
        :type file: ByteStream
        :param file_name: The name of the file, which will be used for storage in Box.
        :type file_name: str
        :param file_size: The total size of the file for the chunked upload in bytes.
        :type file_size: int
        :param parent_folder_id: The ID of the folder where the file should be uploaded.
        :type parent_folder_id: str
        """
        upload_session: UploadSession = self.create_file_upload_session(
            folder_id=parent_folder_id, file_size=file_size, file_name=file_name
        )
        upload_session_id: str = upload_session.id
        part_size: int = upload_session.part_size
        total_parts: int = upload_session.total_parts
        assert part_size * total_parts >= file_size
        assert upload_session.num_parts_processed == 0
        file_hash: Hash = Hash(algorithm=HashName.SHA1.value)
        chunks_iterator: Iterator = iterate_chunks(file, part_size)
        results: PartAccumulator = reduce_iterator(
            chunks_iterator,
            self.reducer,
            PartAccumulator(
                last_index=-1,
                parts=[],
                file_size=file_size,
                upload_session_id=upload_session_id,
                file_hash=file_hash,
            ),
        )
        parts: List[UploadPart] = results.parts
        processed_session_parts: UploadParts = self.get_file_upload_session_parts(
            upload_session_id=upload_session_id
        )
        assert processed_session_parts.total_count == total_parts
        processed_session: UploadSession = self.get_file_upload_session_by_id(
            upload_session_id=upload_session_id
        )
        assert processed_session.num_parts_processed == total_parts
        sha_1: str = file_hash.digest_hash('base64')
        digest: str = ''.join(['sha=', sha_1])
        committed_session: Files = self.create_file_upload_session_commit(
            upload_session_id=upload_session_id, parts=parts, digest=digest
        )
        return committed_session.entries[0]
