import math
import random
import time
from dataclasses import dataclass
from typing import Optional, Dict, TYPE_CHECKING, Union

import requests
from requests import Response, RequestException

from .box_response import APIResponse

if TYPE_CHECKING:
    from .ccg_auth import CCGAuth
    from .developer_token_auth import DeveloperTokenAuth
    from .jwt_auth import JWTAuth

MAX_ATTEMPTS = 5
_RETRY_RANDOMIZATION_FACTOR = 0.5
_RETRY_BASE_INTERVAL = 1


@dataclass
class FetchOptions:
    auth: Union['CCGAuth', 'DeveloperTokenAuth', 'JWTAuth'] = None
    method: str = "GET"
    headers: Dict[str, str] = None
    params: dict = None
    body: str = None


@dataclass
class FetchResponse:
    status: int
    text: str
    content: bytes


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
        return '\n'.join((
            f'Message: {self.message}',
            f'Status: {self.status}',
            f'Code: {self.code}',
            f'Request ID: {self.request_id}',
            f'Headers: {self.headers}',
            f'URL: {self.url}',
            f'Method: {self.method}',
            f'Context Info: {self.context_info}',
        ))


def fetch(url: str, options: FetchOptions) -> FetchResponse:
    headers = __filter_entries_with_none_values(options.headers)
    if options.auth:
        headers['Authorization'] = f'Bearer {options.auth.retrieve_token()}'

    params = __filter_entries_with_none_values(options.params)

    attempt_nr = 1
    response: APIResponse = __make_request(
        method=options.method,
        url=url,
        headers=headers,
        body=options.body,
        params=params,
        attempt_nr=attempt_nr
    )

    while attempt_nr < MAX_ATTEMPTS:
        if response.ok:
            return FetchResponse(status=response.status_code, text=response.text, content=response.content)

        if response.reauthentication_needed:
            options.auth.refresh()
        elif response.status_code != 429 and response.status_code < 500:
            __raise_on_unsuccessful_request(network_response=response.network_response, url=url, method=options.method)

        time.sleep(__get_retry_after_time(
            attempt_number=attempt_nr,
            retry_after_header=response.get_header('Retry-After', None)
        ))

        response: APIResponse = __make_request(
            method=options.method,
            url=url,
            headers=headers,
            body=options.body,
            params=params,
            attempt_nr=attempt_nr
        )
        attempt_nr += 1

    __raise_on_unsuccessful_request(network_response=response.network_response, url=url, method=options.method)


def __filter_entries_with_none_values(dictionary: Optional[Dict[str, str]]) -> Dict[str, str]:
    if not dictionary:
        return {}
    return {k: v for k, v in dictionary.items() if v is not None}


def __make_request(method, url, headers, body, params, attempt_nr) -> APIResponse:
    raised_exception = None
    try:
        network_response = session.request(
            method=method,
            url=url,
            headers=headers,
            data=body,
            params=params
        )
        reauthentication_needed = network_response.status_code == 401
    except RequestException as request_exc:
        if attempt_nr > 1:
            raise
        raised_exception = request_exc
        network_response = None

        if 'EOF occurred in violation of protocol' in str(request_exc):
            reauthentication_needed = True
        elif any(text in str(request_exc) for text in [
            'Connection aborted', 'Connection broken', 'Connection reset'
        ]):
            reauthentication_needed = False
        else:
            raise

    return APIResponse(
        network_response=network_response,
        reauthentication_needed=reauthentication_needed,
        raised_exception=raised_exception
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
        message=response_json.get('message', None) or response_json.get('error_description', None),
        request_id=response_json.get('request_id', None),
        url=url,
        method=method,
        context_info=response_json.get('context_info', None),
        network_response=network_response
    )


def __get_retry_after_time(attempt_number: int, retry_after_header: Optional[str] = None) -> float:
    if retry_after_header is not None:
        try:
            return int(retry_after_header)
        except (ValueError, TypeError):
            pass
    min_randomization = 1 - _RETRY_RANDOMIZATION_FACTOR
    max_randomization = 1 + _RETRY_RANDOMIZATION_FACTOR
    randomization = (random.uniform(0, 1) * (max_randomization - min_randomization)) + min_randomization
    exponential = math.pow(2, attempt_number)
    return exponential * _RETRY_BASE_INTERVAL * randomization


session = requests.Session()
