from dataclasses import dataclass
from typing import Optional, Dict, TYPE_CHECKING, Union

import requests
from requests import Response

if TYPE_CHECKING:
    from .ccg_auth import CCGAuth
    from .developer_token_auth import DeveloperTokenAuth

MAX_ATTEMPTS = 5


@dataclass
class FetchOptions:
    auth: Union['CCGAuth', 'DeveloperTokenAuth'] = None
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
class BoxAPIException(Exception):
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

    network_response = session.request(
        method=options.method,
        url=url,
        headers=headers,
        data=options.body,
        params=params
    )

    attempt_nr = 1
    while attempt_nr < MAX_ATTEMPTS:
        if network_response.ok:
            return FetchResponse(status=network_response.status_code, text=network_response.text, content=network_response.content)

        if network_response.status_code == 401:
            options.auth.refresh()
        elif network_response.status_code != 429 and network_response.status_code < 500:
            __raise_on_unsuccessful_request(network_response=network_response, url=url, method=options.method)

        network_response = session.request(
            method=options.method,
            url=url,
            headers=headers,
            data=options.body,
            params=params
        )
        attempt_nr += 1

    __raise_on_unsuccessful_request(network_response=network_response, url=url, method=options.method)


def __filter_entries_with_none_values(dictionary: Optional[Dict[str, str]]) -> Dict[str, str]:
    if not dictionary:
        return {}
    return {k: v for k, v in dictionary.items() if v is not None}


def __raise_on_unsuccessful_request(network_response, url, method) -> None:
    try:
        response_json = network_response.json()
    except ValueError:
        response_json = {}

    raise BoxAPIException(
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


session = requests.Session()
