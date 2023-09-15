import json
from typing import Union, Type

from .base_object import BaseObject


def serialize(obj: Union[BaseObject, dict, list]):
    if isinstance(obj, BaseObject):
        obj = obj.to_dict()
    if isinstance(obj, list):
        obj = [
            element.to_dict() if isinstance(element, BaseObject) else element
            for element in obj
        ]
    return json.dumps(obj)


def deserialize(json_str: str, type: Type[BaseObject]):
    return type.from_dict(json.loads(json_str))
