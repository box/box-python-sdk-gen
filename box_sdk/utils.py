import base64
import io
import os
import uuid
from typing import Dict, Union

from .base_object import BaseObject


def get_env_var(name: str) -> str:
    return os.getenv(name)


def get_uuid() -> str:
    return str(uuid.uuid1())


def decode_base_64(value: str) -> str:
    return base64.b64decode(value).decode()


def generate_byte_stream(size: int) -> io.BytesIO:
    return io.BytesIO(os.urandom(size))


def decode_base_64_byte_stream(value: str) -> str:
    return base64.b64decode(value)


def read_byte_stream(byte_stream: io.BytesIO) -> bytes:
    return byte_stream.read()


def prepare_params(obj: Union[Dict[str, any], BaseObject]) -> Dict[str, str]:
    if isinstance(obj, BaseObject):
        obj = obj.to_dict()
    return {k: str(v) for k, v in obj.items() if v is not None}
