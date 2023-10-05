import json
from typing import get_origin, Union, Type

from .base_object import BaseObject


def serialize(obj: Union[BaseObject, dict, list]):
    if isinstance(obj, dict):
        obj = BaseObject(**obj).to_dict()
    if isinstance(obj, BaseObject):
        obj = obj.to_dict()
    if isinstance(obj, list):
        obj = [
            element.to_dict() if isinstance(element, BaseObject) else element
            for element in obj
        ]
    return json.dumps(obj)


def deserialize(json_str: str, type: Union[Type[BaseObject], Union[Type[BaseObject]]]):
    value = json.loads(json_str)

    if get_origin(type) == Union:
        type = BaseObject._deserialize_union('', value, type)

    return type.from_dict(value)
