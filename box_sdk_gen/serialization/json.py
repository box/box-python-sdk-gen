import json
from typing import Dict, get_origin, Union, Type
from urllib.parse import urlencode

from ..internal.base_object import BaseObject

SerializedData = Dict


def json_to_serialized_data(data: str) -> SerializedData:
    return json.loads(data)


def sd_to_json(data: SerializedData) -> str:
    return json.dumps(data)


def sd_to_url_params(data: SerializedData) -> str:
    return urlencode(data)


def get_sd_value_by_key(data: SerializedData, key: str):
    return data.get(key)


def serialize(obj: Union[BaseObject, dict, list]) -> SerializedData:
    if isinstance(obj, dict):
        obj = BaseObject(**obj).to_dict()
    if isinstance(obj, BaseObject):
        obj = obj.to_dict()
    if isinstance(obj, list):
        obj = [
            element.to_dict() if isinstance(element, BaseObject) else element
            for element in obj
        ]
    return obj


def deserialize(value: SerializedData, type: Type[BaseObject]):
    if get_origin(type) == Union:
        type = BaseObject._deserialize_union('', value, type)
    obj = type.from_dict(value)
    obj._raw_data = value
    return obj
