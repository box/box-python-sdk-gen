import requests


class NetworkSession:
    MAX_ATTEMPTS = 5

    def __init__(self):
        self.requests_session = requests.Session()
