import base64
import hashlib
import os
import uuid
from time import time
from enum import Enum
from io import SEEK_END, SEEK_SET, BufferedIOBase, BytesIO
from typing import Any, Callable, Dict, Iterable, Optional, TypeVar

try:
    import jwt
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import serialization
except ImportError:
    jwt, default_backend, serialization = None, None, None

from .base_object import BaseObject
from .json_data import sd_to_json
from .serialization import serialize

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


def buffer_length(buffer: Buffer) -> int:
    return len(buffer)


def decode_base_64_byte_stream(value: str) -> ByteStream:
    return BytesIO(base64.b64decode(value))


def read_byte_stream(byte_stream: ByteStream) -> Buffer:
    return Buffer(byte_stream.read())


def prepare_params(map: Dict[str, Optional[str]]) -> Dict[str, str]:
    return {k: v for k, v in map.items() if v is not None}


def to_string(value: Any) -> Optional[str]:
    if value is None:
        return None
    if (
        isinstance(value, BaseObject)
        or isinstance(value, list)
        and isinstance(value[0], BaseObject)
    ):
        return ''.join(sd_to_json(serialize(value)).split())
    if isinstance(value, list):
        return ','.join(map(to_string, value))
    if isinstance(value, Enum):
        return value.value
    return str(value)


class HashName(str, Enum):
    SHA1 = 'sha1'


class Hash:
    def __init__(self, algorithm: HashName):
        self.algorithm = algorithm
        self.hash = hashlib.sha1()

    def update_hash(self, data: Buffer):
        self.hash.update(data)

    def digest_hash(self, encoding):
        return base64.b64encode(self.hash.digest()).decode("utf-8")


def hex_to_base_64(data: hex):
    return base64.b64encode(bytes.fromhex(data)).decode()


T = TypeVar('T')
Iterator = Iterable[T]
Accumulator = TypeVar('Accumulator')


def iterate_chunks(stream: ByteStream, chunk_size: int) -> Iterable[ByteStream]:
    stream_is_finished = False
    while not stream_is_finished:
        copied_length = 0
        chunk = b''
        while copied_length < chunk_size:
            bytes_read = stream.read(chunk_size - copied_length)
            if bytes_read is None:
                # stream returns none when no bytes are ready currently but there are
                # potentially more bytes in the stream to be read.
                continue
            if not bytes_read:
                # stream is exhausted.
                stream_is_finished = True
                break
            chunk += bytes_read
            copied_length += len(bytes_read)
        yield BytesIO(chunk)


def reduce_iterator(
    iterator: Iterator,
    reducer: Callable[[Accumulator, T], Accumulator],
    initial_value: Accumulator,
) -> Accumulator:
    result = initial_value

    for item in iterator:
        result = reducer(result, item)

    return result


def read_text_from_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()


def is_browser() -> bool:
    return False


def get_epoch_time_in_seconds() -> int:
    return int(time())


class JwtAlgorithm(str, Enum):
    HS256 = 'HS256'
    HS384 = 'HS384'
    HS512 = 'HS512'
    RS256 = 'RS256'
    RS384 = 'RS384'
    RS512 = 'RS512'
    ES256 = 'ES256'
    ES384 = 'ES384'
    ES512 = 'ES512'
    PS256 = 'PS256'
    PS384 = 'PS384'
    PS512 = 'PS512'
    none = 'none'


class JwtSignOptions(BaseObject):
    def __init__(
        self,
        algorithm: JwtAlgorithm,
        headers: Dict[str, str] = None,
        audience: Optional[str] = None,
        issuer: Optional[str] = None,
        subject: Optional[str] = None,
        jwtid: Optional[str] = None,
        keyid: Optional[str] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        if headers is None:
            headers = {}
        self.algorithm = algorithm
        self.headers = headers
        self.audience = audience
        self.issuer = issuer
        self.subject = subject
        self.jwtid = jwtid
        self.keyid = keyid


class JwtKey(BaseObject):
    def __init__(self, key: str, passphrase: str, **kwargs):
        super().__init__(**kwargs)
        self.key = key
        self.passphrase = passphrase


def encode_str_ascii_or_raise(passphrase: str) -> bytes:
    try:
        return passphrase.encode('ascii')
    except UnicodeError as unicode_error:
        raise TypeError(
            "private_key and private_key_passphrase must contain binary data (bytes/str), not a text/unicode string"
        ) from unicode_error


def get_rsa_private_key(
    private_key: str,
    passphrase: str,
) -> Any:
    encoded_private_key = encode_str_ascii_or_raise(private_key)
    encoded_passphrase = encode_str_ascii_or_raise(passphrase)

    return serialization.load_pem_private_key(
        encoded_private_key,
        password=encoded_passphrase,
        backend=default_backend(),
    )


def create_jwt_assertion(claims: dict, key: JwtKey, options: JwtSignOptions) -> str:
    return jwt.encode(
        {
            'iss': options.issuer,
            'sub': options.subject,
            'box_sub_type': claims['box_sub_type'],
            'aud': options.audience,
            'jti': options.jwtid,
            'exp': claims['exp'],
        },
        get_rsa_private_key(key.key, key.passphrase),
        algorithm=options.algorithm,
        headers={'kid': options.keyid},
    )
