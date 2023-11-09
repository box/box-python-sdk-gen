import io
import math
import random
import time
from collections import OrderedDict
from dataclasses import dataclass
from typing import Optional, Dict, List
from sys import version_info as py_version

import requests
from requests import Response, RequestException
from requests_toolbelt import MultipartEncoder

from .box_response import APIResponse
from .network import NetworkSession
from .auth import Authentication
from .utils import ByteStream, ResponseByteStream
from .json import SerializedData, sd_to_json, sd_to_url_params, json_to_serialized_data

DEFAULT_MAX_ATTEMPTS = 5
_RETRY_RANDOMIZATION_FACTOR = 0.5
_RETRY_BASE_INTERVAL = 1
SDK_VERSION = '0.1.0'
USER_AGENT_HEADER = f'box-python-generated-sdk-{SDK_VERSION}'
X_BOX_UA_HEADER = (
    f'agent=box-python-generated-sdk/{SDK_VERSION}; '
    f'env=python/{py_version.major}.{py_version.minor}.{py_version.micro}'
)


@dataclass
class MultipartItem:
    part_name: str
    data: SerializedData = None
    file_stream: ByteStream = None
    file_name: str = ''
    content_type: str = None


@dataclass
class FetchOptions:
    method: str = "GET"
    params: Dict[str, str] = None
    headers: Dict[str, str] = None
    data: SerializedData = None
    file_stream: ByteStream = None
    multipart_data: List[MultipartItem] = None
    content_type: str = "application/json"
    response_format: Optional[str] = None
    auth: Authentication = None
    network_session: NetworkSession = None


@dataclass
class FetchResponse:
    status: int
    data: Optional[SerializedData] = None
    content: Optional[ByteStream] = None


@dataclass
class APIException(Exception):
    status: int
    code: Optional[str] = None
    message: Optional[str] = None
    request_id: Optional[str] = None
    headers: dict = None
    url: str = None
    method: str = None
    context_info: Optional[dict] = None
    network_response: Optional[Response] = None

    def __str__(self):
        return '\n'.join(
            (
                f'Message: {self.message}',
                f'Status: {self.status}',
                f'Code: {self.code}',
                f'Request ID: {self.request_id}',
                f'Headers: {self.headers}',
                f'URL: {self.url}',
                f'Method: {self.method}',
                f'Context Info: {self.context_info}',
            )
        )


def fetch(url: str, options: FetchOptions) -> FetchResponse:
    if options.network_session:
        max_attempts = options.network_session.MAX_ATTEMPTS
        requests_session = options.network_session.requests_session
    else:
        max_attempts = DEFAULT_MAX_ATTEMPTS
        requests_session = requests.Session()

    headers = __compose_headers_for_request(options)
    params = options.params or {}

    attempt_nr = 1
    response: APIResponse = __make_request(
        session=requests_session,
        method=options.method,
        url=url,
        headers=headers,
        data=options.file_stream or options.data,
        content_type=options.content_type,
        params=params,
        multipart_data=options.multipart_data,
        attempt_nr=attempt_nr,
    )

    while attempt_nr < max_attempts:
        if response.ok:
            if options.response_format == 'binary':
                return FetchResponse(
                    status=response.status_code,
                    content=ResponseByteStream(
                        response.network_response.iter_content(chunk_size=1024)
                    ),
                )
            else:
                return FetchResponse(
                    status=response.status_code,
                    data=(
                        json_to_serialized_data(response.text)
                        if response.text
                        else None
                    ),
                    content=io.BytesIO(response.content),
                )

        if response.reauthentication_needed:
            headers['Authorization'] = (
                'Bearer'
                f' {options.auth.refresh_token(options.network_session).access_token}'
            )
        elif response.status_code != 429 and response.status_code < 500:
            __raise_on_unsuccessful_request(
                network_response=response.network_response,
                url=url,
                method=options.method,
            )

        time.sleep(
            __get_retry_after_time(
                attempt_number=attempt_nr,
                retry_after_header=response.get_header('Retry-After', None),
            )
        )

        response: APIResponse = __make_request(
            session=requests_session,
            method=options.method,
            url=url,
            headers=headers,
            data=options.file_stream or options.data,
            content_type=options.content_type,
            params=params,
            multipart_data=options.multipart_data,
            attempt_nr=attempt_nr,
        )
        attempt_nr += 1

    __raise_on_unsuccessful_request(
        network_response=response.network_response, url=url, method=options.method
    )


def __compose_headers_for_request(options: FetchOptions) -> Dict[str, str]:
    headers = {}
    if options.network_session:
        headers.update(options.network_session.additional_headers)
    if options.headers:
        headers.update(options.headers)
    if options.auth:
        headers['Authorization'] = (
            'Bearer'
            f' {options.auth.retrieve_token(options.network_session).access_token}'
        )

    headers['User-Agent'] = USER_AGENT_HEADER
    headers['X-Box-UA'] = X_BOX_UA_HEADER
    return headers


def __make_request(
    session,
    method,
    url,
    headers,
    data,
    content_type,
    params,
    multipart_data,
    attempt_nr,
) -> APIResponse:
    if content_type:
        if content_type == 'multipart/form-data':
            fields = OrderedDict()
            for part in multipart_data:
                if part.data:
                    fields[part.part_name] = sd_to_json(part.data)
                else:
                    file_stream = part.file_stream
                    file_stream_position = file_stream.tell()
                    file_stream.seek(file_stream_position)
                    fields[part.part_name] = (
                        part.file_name or '',
                        file_stream,
                        part.content_type,
                    )

            multipart_stream = MultipartEncoder(fields)
            data = multipart_stream
            headers['Content-Type'] = multipart_stream.content_type
        else:
            headers['Content-Type'] = content_type

    def get_data():
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

    raised_exception = None
    try:
        network_response = session.request(
            method=method,
            url=url,
            headers=headers,
            data=get_data(),
            params=params,
            stream=True,
        )
        reauthentication_needed = network_response.status_code == 401
    except RequestException as request_exc:
        if attempt_nr > 1:
            raise
        raised_exception = request_exc
        network_response = None

        if 'EOF occurred in violation of protocol' in str(request_exc):
            reauthentication_needed = True
        elif any(
            text in str(request_exc)
            for text in ['Connection aborted', 'Connection broken', 'Connection reset']
        ):
            reauthentication_needed = False
        else:
            raise

    return APIResponse(
        network_response=network_response,
        reauthentication_needed=reauthentication_needed,
        raised_exception=raised_exception,
    )


def __raise_on_unsuccessful_request(network_response, url, method) -> None:
    try:
        response_json = network_response.json()
    except ValueError:
        response_json = {}

    raise APIException(
        status=network_response.status_code,
        headers=network_response.headers,
        code=response_json.get('code', None) or response_json.get('error', None),
        message=response_json.get('message', None)
        or response_json.get('error_description', None),
        request_id=response_json.get('request_id', None),
        url=url,
        method=method,
        context_info=response_json.get('context_info', None),
        network_response=network_response,
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
