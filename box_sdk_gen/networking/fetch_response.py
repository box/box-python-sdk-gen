from typing import Optional

from typing import Dict

from box_sdk_gen.serialization.json.json_data import SerializedData

from box_sdk_gen.internal.utils import ByteStream


class FetchResponse:
    def __init__(
        self,
        status: int,
        headers: Dict[str, str],
        *,
        data: Optional[SerializedData] = None,
        content: Optional[ByteStream] = None
    ):
        """
        :param status: HTTP status code of the response
        :type status: int
        :param headers: HTTP headers of the response
        :type headers: Dict[str, str]
        :param data: Response body of the response, defaults to None
        :type data: Optional[SerializedData], optional
        :param content: Streamed content of the response, defaults to None
        :type content: Optional[ByteStream], optional
        """
        self.status = status
        self.headers = headers
        self.data = data
        self.content = content
