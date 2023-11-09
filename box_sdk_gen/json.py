import json
from urllib.parse import urlencode


class SerializedData:
    pass


def json_to_serialized_data(data: str) -> SerializedData:
    return json.loads(data)


def sd_to_json(data: SerializedData) -> str:
    return json.dumps(data)


def sd_to_url_params(data: SerializedData) -> str:
    return urlencode(data)
