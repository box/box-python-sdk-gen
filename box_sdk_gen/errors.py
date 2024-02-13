import pprint
from typing import Optional

from typing import Dict


class BoxSDKError(Exception):
    def __init__(
        self,
        message: str,
        timestamp: str = None,
        error: Optional[Exception] = None,
        type: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(message)
        self.message = message
        self.timestamp = timestamp
        self.error = error
        self.type = type

    def __str__(self):
        return ''.join(
            (
                f'\nTimestamp: {self.timestamp}',
                f'\nUnderlying error: {self.error}',
                f'\nMessage: {self.message}',
            )
        )


class RequestInfo:
    def __init__(
        self,
        method: str,
        url: str,
        query_params: Dict[str, str],
        headers: Dict[str, str],
        body: Optional[str] = None,
    ):
        self.method = method
        self.url = url
        self.query_params = query_params
        self.headers = headers
        self.body = body

    def __str__(self):
        return ''.join(
            (
                f'\n\tMethod: {self.method}',
                f'\n\tURL: {self.url}',
                f'\n\tQuery params: \n{pprint.pformat(self.query_params, indent=8)}',
                f'\n\tHeaders: \n{pprint.pformat(self.headers, indent=8)}',
                ''.join(
                    [
                        '\n\tBody: ',
                        '\n' if self.body else '',
                        pprint.pformat(self.body, indent=8),
                    ]
                ),
            )
        )


class ResponseInfo:
    def __init__(
        self,
        status_code: int,
        headers: Dict[str, str],
        body: Dict = None,
        raw_body: Optional[str] = None,
    ):
        self.status_code = status_code
        self.headers = headers
        self.body = body
        self.raw_body = raw_body

    def __str__(self):
        return ''.join(
            (
                f'\n\tStatus code: {self.status_code}',
                f'\n\tHeaders: \n{pprint.pformat(self.headers, indent=8)}',
                ''.join(
                    [
                        '\n\tBody: ',
                        '\n' if self.body else '',
                        pprint.pformat(self.body, indent=8),
                    ]
                ),
                f'\n\tRaw body: {self.raw_body}',
            )
        )


class BoxAPIError(BoxSDKError):
    def __init__(
        self,
        request_info: RequestInfo,
        response_info: ResponseInfo,
        message: str,
        timestamp: str,
        error: Optional[str] = None,
        type: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            message=message, timestamp=timestamp, error=error, type=type, **kwargs
        )
        self.request_info = request_info
        self.response_info = response_info

    def __str__(self):
        return ''.join(
            [
                f'\t{super(BoxAPIError, self).__str__()}',
                f'\nRequest: {self.request_info}',
                f'\nResponse: {self.response_info}',
            ]
        )
