import base64
import io
import os
import uuid


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


