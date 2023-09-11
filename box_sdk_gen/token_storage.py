import shelve
from abc import abstractmethod
from typing import Optional

from .schemas import AccessToken


class TokenStorage:
    @abstractmethod
    def store(self, token: AccessToken) -> None:
        pass

    @abstractmethod
    def get(self) -> Optional[AccessToken]:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass


class InMemoryTokenStorage:
    def __init__(self):
        self.token: Optional[AccessToken] = None

    def store(self, token: AccessToken) -> None:
        self.token = token

    def get(self) -> Optional[AccessToken]:
        return self.token

    def clear(self) -> None:
        self.token = None


class FileTokenStorage:
    def __init__(self, filename: str = 'token_storage'):
        self.file = shelve.open(filename)

    def store(self, token: AccessToken) -> None:
        self.file['token'] = token

    def get(self) -> Optional[AccessToken]:
        return self.file['token']

    def clear(self) -> None:
        del self.file['token']


class FileWithInMemoryCachingTokenStorage:
    def __init__(self, filename: str = 'token_storage'):
        self.file = shelve.open(filename)
        self.cached_token: Optional[AccessToken] = None

    def store(self, token: AccessToken) -> None:
        self.file['token'] = token
        self.cached_token = token

    def get(self) -> Optional[AccessToken]:
        if self.cached_token is None:
            self.cached_token = self.file['token']
        return self.cached_token

    def clear(self) -> None:
        del self.file['token']
        self.cached_token = None
