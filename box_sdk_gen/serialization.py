import json
from typing import get_origin, Union, Type

from .base_object import BaseObject
from .json import SerializedData


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


def deserialize(value: SerializedData, type: Type[BaseObject]) -> str:
    if get_origin(type) == Union:
        type = BaseObject._deserialize_union('', value, type)

    return type.from_dict(value)
