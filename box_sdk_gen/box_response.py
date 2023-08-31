from typing import Optional
from requests import Response


class APIResponse:
    def __init__(
        self, network_response: Response, reauthentication_needed, raised_exception
    ):
        self.network_response = network_response
        self.reauthentication_needed = reauthentication_needed
        self.raised_exception = raised_exception

    @property
    def ok(self) -> bool:
        return self.network_response.ok

    @property
    def status_code(self) -> int:
        return self.network_response.status_code

    @property
    def content(self) -> bytes:
        return self.network_response.content

    @property
    def text(self) -> str:
        return self.network_response.text

    def get_header(
        self, header_name: str, default_value: Optional[str] = None
    ) -> Optional[str]:
        try:
            return self.network_response.headers[header_name]
        except (ValueError, KeyError):
            return default_value
