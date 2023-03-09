class DeveloperTokenAuth:
    def __init__(self, token: str):
        self.token: str = token

    def retrieve_token(self) -> str:
        return self.token

    def refresh(self) -> str:
        raise Exception("Developer token has expired. Please provide a new one.")