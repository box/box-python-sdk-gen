import pytest
import json
from collections import OrderedDict
from io import BytesIO
from unittest import mock
from unittest.mock import Mock, patch
from requests import Session, Response, RequestException

from box_sdk_gen import NetworkSession, BoxAPIError, Authentication, BoxSDKError
from box_sdk_gen.networking.fetch import (
    fetch,
    FetchOptions,
    __prepare_headers,
    __prepare_body,
    __prepare_request,
    __make_request,
    __raise_on_unsuccessful_request,
    __get_retry_after_time,
    USER_AGENT_HEADER,
    X_BOX_UA_HEADER,
    APIRequest,
    APIResponse,
    MultipartItem,
)


@pytest.fixture
def mock_requests_session():
    return Mock(Session)


@pytest.fixture
def mock_byte_stream():
    return BytesIO(b'123')


@pytest.fixture
def response_500():
    response = Mock(Response)
    response.status_code = 500
    response.ok = False
    response.headers = {'Retry-After': '0'}
    return response


@pytest.fixture
def response_401():
    response = Mock(Response)
    response.status_code = 401
    response.ok = False
    response.headers = {}
    return response


@pytest.fixture
def response_429():
    response = Mock(Response)
    response.status_code = 429
    response.ok = False
    response.headers = {}
    return response


@pytest.fixture
def response_200():
    response = Mock(Response)
    response.status_code = 200
    response.ok = True
    response.headers = {}
    response.text = ''
    response.content = None
    return response


@pytest.fixture
def response_failure_no_status():
    response = Mock(Response)
    response.ok = False
    response.headers = {'Retry-After': '0'}
    return response


@pytest.fixture
def token_mock():
    return 'token123'


@pytest.fixture
def token2_mock():
    return 'new_token321'


@pytest.fixture
def network_session_mock(mock_requests_session):
    network_session = NetworkSession()
    network_session.requests_session = mock_requests_session
    return network_session


def reauthenticate_mock(auth, token):
    auth.retrieve_authorization_header.return_value = f'Bearer {token}'


@pytest.fixture
def authentication_mock(token_mock, token2_mock):
    auth = Mock(Authentication)
    auth.retrieve_authorization_header.return_value = f'Bearer {token_mock}'
    auth.refresh_token = lambda network_session: reauthenticate_mock(auth, token2_mock)
    return auth


def test_use_session_and_max_attempts_from_network_session(
    network_session_mock, mock_requests_session, response_500
):
    mock_requests_session.request.return_value = response_500

    network_session_mock.MAX_ATTEMPTS = 3

    options = FetchOptions(
        method="GET",
        network_session=network_session_mock,
    )

    with pytest.raises(BoxAPIError):
        fetch("https://example.com", options)

    assert mock_requests_session.request.call_count == 3


def test_use_default_session_and_max_attempts_when_network_session_not_provided(
    mock_requests_session, response_500
):
    mock_requests_session.request.return_value = response_500
    with patch('requests.Session', return_value=mock_requests_session):
        options = FetchOptions(method="GET")

        with pytest.raises(BoxAPIError):
            fetch("https://example.com", options)

        assert mock_requests_session.request.call_count == 5


def test_prepare_headers(authentication_mock, token_mock):
    network_session = NetworkSession(additional_headers={"additional_header": "test"})
    options = FetchOptions(
        method="GET",
        network_session=network_session,
        headers={"header": "test"},
        auth=authentication_mock,
    )

    headers = __prepare_headers(options)

    assert headers == {
        'Authorization': f'Bearer {token_mock}',
        "header": "test",
        "additional_header": "test",
        'User-Agent': USER_AGENT_HEADER,
        'X-Box-UA': X_BOX_UA_HEADER,
    }


def test_prepare_headers_reauthenticate(authentication_mock, token2_mock):
    network_session = NetworkSession(additional_headers={"additional_header": "test"})
    options = FetchOptions(
        method="GET",
        network_session=network_session,
        headers={"header": "test"},
        auth=authentication_mock,
    )

    headers = __prepare_headers(options, reauthenticate=True)

    assert headers == {
        'Authorization': f'Bearer {token2_mock}',
        "header": "test",
        "additional_header": "test",
        'User-Agent': USER_AGENT_HEADER,
        'X-Box-UA': X_BOX_UA_HEADER,
    }


@pytest.mark.parametrize(
    'content_type, data, expected_body',
    [
        ('application/json', {'key': 'value'}, '{"key": "value"}'),
        ('application/json-patch+json', {'key': 'value'}, '{"key": "value"}'),
        ('application/x-www-form-urlencoded', {'key': 'value'}, 'key=value'),
        ('multipart/form-data', mock_byte_stream, mock_byte_stream),
        ('application/octet-stream', mock_byte_stream, mock_byte_stream),
    ],
)
def test_prepare_body_valid_content_type(
    content_type, data, expected_body, mock_byte_stream
):
    body = __prepare_body(content_type, data)
    assert body == expected_body


def test_prepare_body_invalid_content_type():
    with pytest.raises(Exception):
        __prepare_body('invalid_content_type', {})


def test_prepare_json_request():
    options = FetchOptions(
        method="POST",
        data={'key': 'value'},
        headers={"header": "test"},
        params={'param': 'value'},
        content_type='application/json',
    )

    api_request = __prepare_request(url="https://example.com", options=options)

    assert api_request == APIRequest(
        method="POST",
        url="https://example.com",
        headers={
            'header': 'test',
            'User-Agent': USER_AGENT_HEADER,
            'X-Box-UA': X_BOX_UA_HEADER,
            'Content-Type': 'application/json',
        },
        params={'param': 'value'},
        data='{"key": "value"}',
    )


def test_prepare_multipart_request(mock_byte_stream):
    options = FetchOptions(
        method="POST",
        data={'key': 'value'},
        content_type='multipart/form-data',
        multipart_data=[
            MultipartItem(part_name='attributes', data={'name': 'file.pdf'}),
            MultipartItem(
                part_name='file', file_stream=mock_byte_stream, file_name='file.pdf'
            ),
        ],
    )

    api_request = __prepare_request(url="https://example.com", options=options)

    assert api_request.method == "POST"
    assert api_request.url == "https://example.com"
    assert api_request.headers['User-Agent'] == USER_AGENT_HEADER
    assert api_request.headers['X-Box-UA'] == X_BOX_UA_HEADER
    assert api_request.headers['Content-Type'].startswith(
        'multipart/form-data; boundary='
    )
    assert api_request.params == {}
    assert api_request.data.fields == OrderedDict(
        [
            ('attributes', '{"name": "file.pdf"}'),
            ('file', ('file.pdf', mock_byte_stream, None)),
        ]
    )


def test_make_request(mock_requests_session, response_200):
    request_params = {
        'method': "POST",
        'url': "https://example.com",
        'headers': {
            'header': 'test',
            'User-Agent': USER_AGENT_HEADER,
            'X-Box-UA': X_BOX_UA_HEADER,
            'Content-Type': 'application/json',
        },
        'params': {'param': 'value'},
        'data': '{"key": "value"}',
    }
    mock_requests_session.request.return_value = response_200
    api_request = APIRequest(**request_params)

    api_response = __make_request(api_request, mock_requests_session)

    assert api_response == APIResponse(
        network_response=response_200,
        reauthentication_needed=False,
        raised_exception=None,
    )
    assert mock_requests_session.request.call_count == 1
    mock_requests_session.request.assert_called_once_with(**request_params, stream=True)


def test_make_request_unauthorised(mock_requests_session, response_401):
    mock_requests_session.request.return_value = response_401
    api_request = APIRequest(
        "GET", "https://example.com", headers={}, params={}, data=""
    )
    api_response = __make_request(api_request, mock_requests_session)

    assert api_response == APIResponse(
        network_response=response_401,
        reauthentication_needed=True,
        raised_exception=None,
    )
    assert mock_requests_session.request.call_count == 1


@pytest.mark.parametrize(
    'exc_message, expected_reauthentication_needed',
    [
        ('Connection aborted', False),
        (
            "Connection broken: ConnectionResetError(54, 'Connection reset by peer')",
            False,
        ),
        (
            "SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:2396)')))",
            True,
        ),
    ],
)
def test_make_request_network_exception(
    mock_requests_session, exc_message, expected_reauthentication_needed
):
    requests_exception = RequestException(exc_message)
    mock_requests_session.request.side_effect = [requests_exception]
    api_request = APIRequest(
        "GET", "https://example.com", headers={}, params={}, data=""
    )
    api_response = __make_request(api_request, mock_requests_session)

    assert api_response == APIResponse(
        network_response=None,
        reauthentication_needed=expected_reauthentication_needed,
        raised_exception=requests_exception,
    )


def test_fetch_successfully_retry_network_exception(
    mock_requests_session, network_session_mock, response_200
):
    requests_exception = RequestException('Connection aborted')
    mock_requests_session.request.side_effect = [requests_exception, response_200]

    with patch('time.sleep'):
        response = fetch(
            "https://example.com", FetchOptions(network_session=network_session_mock)
        )
        assert response.status == 200


def test_fetch_make_only_one_retry_for_network_exception(
    mock_requests_session, network_session_mock
):
    requests_exception = RequestException('Connection aborted')
    mock_requests_session.request.side_effect = [requests_exception, requests_exception]

    with patch('time.sleep'):
        with pytest.raises(BoxSDKError, match='Connection aborted'):
            fetch(
                "https://example.com",
                FetchOptions(network_session=network_session_mock),
            )

    assert mock_requests_session.request.call_count == 2


def test_fetch_get_json_format_response_success(
    mock_requests_session, network_session_mock, response_200
):
    response_200.text = '{"id": "123456"}'
    mock_requests_session.request.return_value = response_200

    fetch_response = fetch(
        "https://example.com",
        FetchOptions(network_session=network_session_mock, response_format='json'),
    )

    assert fetch_response.status == 200
    assert fetch_response.data == {'id': '123456'}
    assert fetch_response.headers == {}


def test_fetch_get_binary_format_response_success(
    mock_requests_session, network_session_mock, response_200
):
    content = b'binary data'
    response_200.iter_content.return_value = BytesIO(content)
    mock_requests_session.request.return_value = response_200

    fetch_response = fetch(
        "https://example.com",
        FetchOptions(network_session=network_session_mock, response_format='binary'),
    )

    assert fetch_response.status == 200
    assert fetch_response.content.read() == content
    assert fetch_response.headers == {}


@pytest.mark.parametrize('retryable_status_code', [429, 500, 503])
def test_retryable_status_codes(
    mock_requests_session,
    network_session_mock,
    response_200,
    retryable_status_code,
    response_failure_no_status,
):
    response_failure_no_status.status_code = retryable_status_code
    response_200.text = '{"id": "123456"}'
    mock_requests_session.request.side_effect = [
        response_failure_no_status,
        response_failure_no_status,
        response_200,
    ]

    fetch_response = fetch(
        "https://example.com", FetchOptions(network_session=network_session_mock)
    )
    assert fetch_response.status == 200
    assert fetch_response.data == {'id': '123456'}
    assert mock_requests_session.request.call_count == 3


@pytest.mark.parametrize('not_retryable_status_code', [404, 403, 400])
def test_not_retryable_status_codes(
    mock_requests_session,
    network_session_mock,
    not_retryable_status_code,
    response_failure_no_status,
    response_200,
):
    response_failure_no_status.status_code = not_retryable_status_code
    mock_requests_session.request.side_effect = [
        response_failure_no_status,
        response_failure_no_status,
        response_200,
    ]

    with pytest.raises(BoxSDKError, match=f'Status code: {not_retryable_status_code}'):
        fetch("https://example.com", FetchOptions(network_session=network_session_mock))

    assert mock_requests_session.request.call_count == 1


def test_retrying_401_response_with_new_token_and_auth_provided(
    mock_requests_session,
    network_session_mock,
    response_401,
    response_200,
    authentication_mock,
    token_mock,
    token2_mock,
):
    response_200.text = '{"id": "123456"}'
    mock_requests_session.request.side_effect = [response_401, response_200]

    with patch('time.sleep'):
        fetch_response = fetch(
            "https://example.com",
            FetchOptions(
                method='GET',
                network_session=network_session_mock,
                auth=authentication_mock,
            ),
        )

    assert mock_requests_session.request.call_count == 2
    mock_requests_session.request.assert_has_calls(
        [
            mock.call(
                method="GET",
                url="https://example.com",
                headers={
                    'Authorization': f'Bearer {token_mock}',
                    'User-Agent': USER_AGENT_HEADER,
                    'X-Box-UA': X_BOX_UA_HEADER,
                    'Content-Type': 'application/json',
                },
                params={},
                data=None,
                stream=True,
            ),
            mock.call(
                method="GET",
                url="https://example.com",
                headers={
                    'Authorization': f'Bearer {token2_mock}',
                    'User-Agent': USER_AGENT_HEADER,
                    'X-Box-UA': X_BOX_UA_HEADER,
                    'Content-Type': 'application/json',
                },
                params={},
                data=None,
                stream=True,
            ),
        ],
    )
    assert fetch_response.status == 200
    assert fetch_response.data == {'id': '123456'}


def test_not_retrying_401_when_auth_not_provided(
    mock_requests_session,
    network_session_mock,
    response_401,
    response_200,
    authentication_mock,
):
    mock_requests_session.request.side_effect = [response_401, response_200]

    with pytest.raises(BoxSDKError, match='Status code: 401'):
        fetch(
            "https://example.com",
            FetchOptions(method='GET', network_session=network_session_mock),
        )

    assert mock_requests_session.request.call_count == 1
    mock_requests_session.request.assert_called_once_with(
        method="GET",
        url="https://example.com",
        headers={
            'User-Agent': USER_AGENT_HEADER,
            'X-Box-UA': X_BOX_UA_HEADER,
            'Content-Type': 'application/json',
        },
        params={},
        data=None,
        stream=True,
    )


def test_reaching_retry_limit(
    mock_requests_session, network_session_mock, response_500
):
    network_session_mock.MAX_ATTEMPTS = 5
    mock_requests_session.request.return_value = response_500

    with pytest.raises(BoxSDKError, match='Status code: 500'):
        fetch("https://example.com", FetchOptions(network_session=network_session_mock))
    assert mock_requests_session.request.call_count == 5


def test_get_retry_after_time_use_retry_after_header_value():
    for attempt_number in range(1, 5):
        sleep_time = __get_retry_after_time(attempt_number, "213")
        assert sleep_time == 213


def test_get_retry_after_time_use_exponential_backoff():
    for attempt_number in range(1, 5):
        sleep_time = __get_retry_after_time(attempt_number)
        assert sleep_time > 0


def test_pass_retry_after_header_to_get_retry_after_time_method(
    mock_requests_session, network_session_mock, response_429, response_200
):
    response_429.headers = {'Retry-After': '123'}
    mock_requests_session.request.side_effect = [response_429, response_200]

    with patch('time.sleep') as sleep_mock:
        fetch("https://example.com", FetchOptions(network_session=network_session_mock))
        assert mock_requests_session.request.call_count == 2
        sleep_mock.assert_called_once_with(123)


def test_raising_api_error_with_valid_json_body():
    client_error_response = Mock(Response)
    client_error_response.status_code = 400
    client_error_response.ok = False
    client_error_response.headers = {}
    client_error_response.text = '''{
      "type": "error",
      "code": "item_name_invalid",
      "context_info": {
        "message": "Something went wrong."
      },
      "help_url": "https://developer.box.com/guides/api-calls/permissions-and-errors/common-errors/",
      "message": "Method Not Allowed",
      "request_id": "abcdef123456",
      "status": 400
    }'''
    client_error_response.json.return_value = json.loads(client_error_response.text)

    request = APIRequest(
        method="POST",
        url="https://example.com",
        headers={
            'header': 'test',
            'User-Agent': USER_AGENT_HEADER,
            'X-Box-UA': X_BOX_UA_HEADER,
            'Content-Type': 'application/json',
        },
        params={'param': 'value'},
        data='{"key": "value"}',
    )

    response = APIResponse(
        network_response=client_error_response,
        reauthentication_needed=False,
        raised_exception=None,
    )
    try:
        __raise_on_unsuccessful_request(request, response)
    except BoxAPIError as e:
        assert e.request_info.method == request.method
        assert e.request_info.url == request.url
        assert e.request_info.query_params == request.params
        assert e.request_info.headers == request.headers
        assert e.request_info.body == request.data

        assert e.response_info.status_code == client_error_response.status_code
        assert e.response_info.headers == client_error_response.headers
        assert e.response_info.body == {
            "type": "error",
            "code": "item_name_invalid",
            "context_info": {"message": "Something went wrong."},
            "help_url": "https://developer.box.com/guides/api-calls/permissions-and-errors/common-errors/",
            "message": "Method Not Allowed",
            "request_id": "abcdef123456",
            "status": 400,
        }
        assert e.response_info.raw_body == client_error_response.text
        assert e.response_info.code == 'item_name_invalid'
        assert e.response_info.context_info == {"message": "Something went wrong."}
        assert e.response_info.request_id == 'abcdef123456'
        assert (
            e.response_info.help_url
            == "https://developer.box.com/guides/api-calls/permissions-and-errors/common-errors/"
        )

        assert e.message == "400 Method Not Allowed; Request ID: abcdef123456"
        assert e.error is None
        assert e.name == 'BoxAPIError'


def test_raising_api_error_without_valid_json_body():
    client_error_response = Mock(Response)
    client_error_response.status_code = 400
    client_error_response.ok = False
    client_error_response.headers = {}
    client_error_response.text = ''
    client_error_response.json.side_effect = json.JSONDecodeError(
        'Expecting value: line 1 column 1 (char 0)', '', 0
    )

    request = APIRequest(
        method="POST",
        url="https://example.com",
        headers={
            'header': 'test',
            'User-Agent': USER_AGENT_HEADER,
            'X-Box-UA': X_BOX_UA_HEADER,
            'Content-Type': 'application/json',
        },
        params={'param': 'value'},
        data='{"key": "value"}',
    )

    response = APIResponse(
        network_response=client_error_response,
        reauthentication_needed=False,
        raised_exception=None,
    )
    try:
        __raise_on_unsuccessful_request(request, response)
    except BoxAPIError as e:
        assert e.request_info.method == request.method
        assert e.request_info.url == request.url
        assert e.request_info.query_params == request.params
        assert e.request_info.headers == request.headers
        assert e.request_info.body == request.data

        assert e.response_info.status_code == client_error_response.status_code
        assert e.response_info.headers == client_error_response.headers
        assert e.response_info.body == {}
        assert e.response_info.raw_body == client_error_response.text
        assert e.response_info.code is None
        assert e.response_info.context_info == {}
        assert e.response_info.request_id is None
        assert e.response_info.help_url is None

        assert e.error is None
        assert e.name == 'BoxAPIError'


def test_raising_exception_raised_by_network_layer():
    requests_exception = RequestException('Something went wrong')
    request = APIRequest(
        method="POST",
        url="https://example.com",
        headers={
            'header': 'test',
            'User-Agent': USER_AGENT_HEADER,
            'X-Box-UA': X_BOX_UA_HEADER,
            'Content-Type': 'application/json',
        },
        params={'param': 'value'},
        data='{"key": "value"}',
    )

    response = APIResponse(
        network_response=None,
        reauthentication_needed=False,
        raised_exception=requests_exception,
    )

    try:
        __raise_on_unsuccessful_request(request, response)
    except BoxSDKError as e:
        assert e.message == "Something went wrong"
        assert e.error == requests_exception
        assert e.name == 'BoxSDKError'
