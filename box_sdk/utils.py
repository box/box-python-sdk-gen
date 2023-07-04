import base64
import io
import os
import uuid
from typing import Union


def get_env_var(name: str) -> str:
    return os.getenv(name)


def get_uuid() -> str:
    return str(uuid.uuid1())


def decode_base_64(value: str) -> str:
    return base64.b64decode(value).decode()


def generate_byte_stream() -> io.BytesIO:
    return io.BytesIO(os.urandom(1024 * 1024))


def read_byte_stream(byte_stream: io.BytesIO) -> bytes:
    return byte_stream.read()


def to_map(obj: Union[object, dict]) -> dict:
    try:
        return obj.to_dict()
    except AttributeError:
        return {k: __try_convert_to_dict(v) for k, v in obj.items()}


def __try_convert_to_dict(value):
    try:
        return value.to_dict()
    except AttributeError:
        return value
