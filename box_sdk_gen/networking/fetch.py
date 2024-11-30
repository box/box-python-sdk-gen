import io

import math
import random
import time
from collections import OrderedDict
from dataclasses import dataclass
from typing import Optional, Dict, List, Union
from sys import version_info as py_version
from http import HTTPStatus

import requests
from requests import RequestException, Session, Response
from requests_toolbelt import MultipartEncoder

from .fetch_options import FetchOptions
from .fetch_response import FetchResponse
from ..box.errors import BoxAPIError, BoxSDKError, RequestInfo, ResponseInfo
from ..internal.utils import ByteStream, ResponseByteStream
from ..serialization.json import (
    sd_to_json,
    sd_to_url_params,
    json_to_serialized_data,
)
from .version import __version__

DEFAULT_MAX_ATTEMPTS = 5
_RETRY_RANDOMIZATION_FACTOR = 0.5
_RETRY_BASE_INTERVAL = 1
SDK_VERSION = __version__
USER_AGENT_HEADER = f'box-python-generated-sdk-{SDK_VERSION}'
X_BOX_UA_HEADER = (
    f'agent=box-python-generated-sdk/{SDK_VERSION}; '
    f'env=python/{py_version.major}.{py_version.minor}.{py_version.micro}'
)


@dataclass
class APIRequest:
    method: str
    url: str
    headers: Dict[str, str]
    params: Dict[str, str]
    data: Optional[Union[str, ByteStream, MultipartEncoder]]
    allow_redirects: bool = True


@dataclass
class APIResponse:
    network_response: Optional[Response] = None
    reauthentication_needed: Optional[bool] = False
    raised_exception: Optional[Exception] = None

    def get_header(
        self, header_name: str, default_value: Optional[str] = None
    ) -> Optional[str]:
        try:
            return self.network_response.headers[header_name]
        except (ValueError, KeyError, AttributeError):
            return default_value


def fetch(options: FetchOptions) -> FetchResponse:
    if options.network_session:
        max_attempts = options.network_session.MAX_ATTEMPTS
        requests_session = options.network_session.requests_session
    else:
        max_attempts = DEFAULT_MAX_ATTEMPTS
        requests_session = requests.Session()

    attempt_nr = 1
    response = APIResponse()

    options_stream_position = __get_options_stream_position(options)
    multipart_streams_positions = __get_multipart_stream_positions(options)

    while True:
        request: APIRequest = __prepare_request(
            options=options, reauthenticate=response.reauthentication_needed
        )
        response: APIResponse = __make_request(
            request=request, session=requests_session
        )

        # Retry network exception only once
        if response.raised_exception and attempt_nr > 1:
            break

        if response.network_response is not None:
            network_response = response.network_response
            accepted_with_retry_after = (
                network_response.status_code == HTTPStatus.ACCEPTED
            ) and response.get_header('Retry-After', None)
            if network_response.ok and (
                not accepted_with_retry_after or attempt_nr >= max_attempts
            ):
                if options.response_format == 'binary':
                    return FetchResponse(
                        url=network_response.url,
                        status=network_response.status_code,
                        headers=dict(response.network_response.headers),
                        content=ResponseByteStream(
                            response.network_response.iter_content(chunk_size=1024)
                        ),
                    )
                else:
                    return FetchResponse(
                        url=network_response.url,
                        status=network_response.status_code,
                        headers=dict(response.network_response.headers),
                        data=(
                            json_to_serialized_data(network_response.text)
                            if network_response.text
                            else None
                        ),
                        content=io.BytesIO(network_response.content),
                    )

            if (
                not (response.reauthentication_needed and options.auth)
                and network_response.status_code != HTTPStatus.TOO_MANY_REQUESTS
                and not accepted_with_retry_after
                and network_response.status_code < 500
            ):
                __raise_on_unsuccessful_request(request=request, response=response)

        if attempt_nr >= max_attempts:
            break

        time.sleep(
            __get_retry_after_time(
                attempt_number=attempt_nr,
                retry_after_header=response.get_header('Retry-After', None),
            )
        )

        __reset_options_stream(
            options, options_stream_position, response.raised_exception
        )
        __reset_multipart_streams(
            options, multipart_streams_positions, response.raised_exception
        )

        attempt_nr += 1

    __raise_on_unsuccessful_request(request=request, response=response)


def __prepare_request(
    options: FetchOptions, reauthenticate: bool = False
) -> APIRequest:
    headers = __prepare_headers(options, reauthenticate)
    params = options.params or {}
    data = __prepare_body(options.content_type, options.file_stream or options.data)
    allow_redirects = options.follow_redirects

    if options.content_type:
        if options.content_type == 'multipart/form-data':
            fields = OrderedDict()
            for part in options.multipart_data:
                if part.data:
                    fields[part.part_name] = sd_to_json(part.data)
                else:
                    fields[part.part_name] = (
                        part.file_name or '',
                        part.file_stream,
                        part.content_type,
                    )

            multipart_stream = MultipartEncoder(fields)
            data = multipart_stream
            headers['Content-Type'] = multipart_stream.content_type
        else:
            headers['Content-Type'] = options.content_type

    return APIRequest(
        method=options.method,
        url=options.url,
        headers=headers,
        params=params,
        data=data,
        allow_redirects=allow_redirects,
    )


def __prepare_headers(
    options: FetchOptions, reauthenticate: bool = False
) -> Dict[str, str]:
    headers = {}
    if options.network_session:
        headers.update(options.network_session.additional_headers)
    if options.headers:
        headers.update(options.headers)
    if options.auth:
        if reauthenticate:
            options.auth.refresh_token(network_session=options.network_session)
        headers['Authorization'] = options.auth.retrieve_authorization_header(
            network_session=options.network_session
        )

    headers['User-Agent'] = USER_AGENT_HEADER
    headers['X-Box-UA'] = X_BOX_UA_HEADER
    return headers


def __prepare_body(
    content_type: str, data: Union[dict, ByteStream]
) -> Optional[Union[str, ByteStream]]:
    if (
        content_type == 'application/json'
        or content_type == 'application/json-patch+json'
    ):
        return sd_to_json(data) if data else None
    if content_type == 'application/x-www-form-urlencoded':
        return sd_to_url_params(data)
    if (
        content_type == 'multipart/form-data'
        or content_type == 'application/octet-stream'
    ):
        return data
    raise


def __make_request(request: APIRequest, session: Session) -> APIResponse:
    raised_exception = None
    reauthentication_needed = False
    try:
        network_response = session.request(
            method=request.method,
            url=request.url,
            headers=request.headers,
            data=request.data,
            params=request.params,
            allow_redirects=request.allow_redirects,
            stream=True,
        )
        reauthentication_needed = (
            network_response.status_code == HTTPStatus.UNAUTHORIZED
        )
    except RequestException as request_exc:
        raised_exception = request_exc
        network_response = None

        if 'EOF occurred in violation of protocol' in str(request_exc):
            reauthentication_needed = True

    return APIResponse(
        network_response=network_response,
        reauthentication_needed=reauthentication_needed,
        raised_exception=raised_exception,
    )


def __raise_on_unsuccessful_request(request: APIRequest, response: APIResponse) -> None:
    if response.raised_exception:
        raise BoxSDKError(
            message=str(response.raised_exception), error=response.raised_exception
        )

    network_response = response.network_response

    try:
        response_json = network_response.json()
    except ValueError:
        response_json = {}

    raise BoxAPIError(
        message=f'{network_response.status_code} {response_json.get("message", "")}; Request ID: {response_json.get("request_id", "")}',
        request_info=RequestInfo(
            method=request.method,
            url=request.url,
            query_params=request.params,
            headers=request.headers,
            body=request.data,
        ),
        response_info=ResponseInfo(
            status_code=network_response.status_code,
            headers=dict(network_response.headers),
            body=response_json,
            raw_body=network_response.text,
            code=response_json.get("code", None),
            context_info=response_json.get("context_info", {}),
            request_id=response_json.get("request_id", None),
            help_url=response_json.get("help_url", None),
        ),
    )


def __get_retry_after_time(
    attempt_number: int, retry_after_header: Optional[str] = None
) -> float:
    if retry_after_header is not None:
        try:
            return int(retry_after_header)
        except (ValueError, TypeError):
            pass
    min_randomization = 1 - _RETRY_RANDOMIZATION_FACTOR
    max_randomization = 1 + _RETRY_RANDOMIZATION_FACTOR
    randomization = (
        random.uniform(0, 1) * (max_randomization - min_randomization)
    ) + min_randomization
    exponential = math.pow(2, attempt_number)
    return exponential * _RETRY_BASE_INTERVAL * randomization


def __get_multipart_stream_positions(options: FetchOptions) -> dict:
    multipart_streams_positions = {}
    if options.multipart_data:
        for part in options.multipart_data:
            if part.file_stream and part.file_stream.seekable():
                multipart_streams_positions[part.part_name] = part.file_stream.tell()
    return multipart_streams_positions


def __get_options_stream_position(options: FetchOptions) -> int:
    filestream_position = 0
    if options.file_stream and options.file_stream.seekable():
        filestream_position = options.file_stream.tell()
    return filestream_position


def __validate_seekable(stream: ByteStream, raised_exception: Optional[Exception]):
    if not stream.seekable():
        raise BoxSDKError(
            message='Request with non-seekable stream cannot be retried',
            error=raised_exception,
        )


def __reset_stream(
    stream: ByteStream, original_position: int, raised_exception: Optional[Exception]
):
    __validate_seekable(stream, raised_exception)
    stream.seek(original_position)


def __reset_options_stream(
    options: FetchOptions,
    filestream_position: int,
    raised_exception: Optional[Exception],
):
    if options.file_stream:
        __reset_stream(options.file_stream, filestream_position, raised_exception)


def __reset_multipart_streams(
    options: FetchOptions,
    multipart_streams_positions: dict,
    raised_exception: Optional[Exception],
):
    if not options.multipart_data:
        return

    for part in options.multipart_data:
        if not part.file_stream:
            continue

        position = multipart_streams_positions.get(part.part_name)
        # we didn't get position before sending request hence the stream must be non-seekable
        if position is None:
            raise BoxSDKError(
                message='Request with non-seekable stream cannot be retried',
                error=raised_exception,
            )

        __reset_stream(
            part.file_stream,
            multipart_streams_positions[part.part_name],
            raised_exception,
        )
