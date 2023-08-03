import base64
from io import BytesIO, SEEK_SET, SEEK_END, BufferedIOBase
import os
import uuid
from typing import Dict, Optional

ByteStream = BufferedIOBase
Buffer = bytes


class ResponseByteStream(ByteStream):
    def __init__(self, request_iterator):
        self._bytes = BytesIO()
        self._iterator = request_iterator

    def _load_all(self):
        self._bytes.seek(0, SEEK_END)
        for chunk in self._iterator:
            self._bytes.write(chunk)

    def _load_until(self, goal_position):
        current_position = self._bytes.seek(0, SEEK_END)
        while current_position < goal_position:
            try:
                current_position += self._bytes.write(next(self._iterator))
            except StopIteration:
                break

    def tell(self):
        return self._bytes.tell()

    def read(self, size=None):
        left_off_at = self._bytes.tell()
        if size is None:
            self._load_all()
        else:
            goal_position = left_off_at + size
            self._load_until(goal_position)

        self._bytes.seek(left_off_at)
        return self._bytes.read(size)

    def seek(self, position, whence=SEEK_SET):
        if whence == SEEK_END:
            self._load_all()
        else:
            self._bytes.seek(position, whence)


def get_env_var(name: str) -> str:
    return os.getenv(name)


def get_uuid() -> str:
    return str(uuid.uuid1())


def decode_base_64(value: str) -> str:
    return base64.b64decode(value).decode()


def generate_byte_buffer(size: int) -> Buffer:
    return Buffer(os.urandom(size))


def generate_byte_stream_from_buffer(buffer: Buffer) -> ByteStream:
    return BytesIO(buffer)


def generate_byte_stream(size: int) -> ByteStream:
    return BytesIO(os.urandom(size))


def buffer_equals(buffer1: Buffer, buffer2: Buffer) -> bool:
    return buffer1 == buffer2


def decode_base_64_byte_stream(value: str) -> ByteStream:
    return BytesIO(base64.b64decode(value))


def read_byte_stream(byte_stream: ByteStream) -> Buffer:
    return Buffer(byte_stream.read())


def prepare_params(map: Dict[str, Optional[str]]) -> Dict[str, str]:
    return {k: v for k, v in map.items() if v is not None}


def to_string(value: any) -> Optional[str]:
    if value is None:
        return value
    return str(value)
