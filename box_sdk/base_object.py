from enum import EnumMeta, Enum
from typing import get_args, get_origin, Union, Optional


class BaseObject:
    def __init__(self, **kwargs):
        pass

    @classmethod
    def from_dict(cls, data: dict):
        unpacked_attributes = {}
        for key, value in data.items():
            possible_types = cls._extract_types_from_annotation(key)
            if isinstance(value, dict):
                value = cls.__deserialize_nested_type(possible_types, value)
            elif any(isinstance(possible_type, EnumMeta) for possible_type in possible_types):
                value = cls.__deserialize_enum(possible_types, value)
            elif any(get_origin(possible_type) == list for possible_type in possible_types):
                value = cls.__deserialize_list(possible_types, value)

            unpacked_attributes[key] = value

        return cls(**unpacked_attributes)

    def to_dict(self) -> dict:
        result_dict = {}
        for k, v in vars(self).items():
            if v is None:
                continue
            if type(v) is list:
                value = [item.to_dict() if isinstance(item, BaseObject) else item for item in v]
            elif isinstance(v, BaseObject):
                value = v.to_dict()
            elif isinstance(v, Enum):
                value = v.value
            else:
                value = v
            result_dict[k] = value

        return result_dict

    @classmethod
    def _extract_types_from_annotation(cls, key: str):
        try:
            annotation = cls.__init__.__annotations__[key]
            if get_origin(annotation) in (Union, Optional):
                return get_args(annotation)
            else:
                return annotation,
        except KeyError:
            return tuple()

    @classmethod
    def __deserialize_nested_type(cls, possible_types: tuple, value_to_deserialize: dict):

        for possible_type in possible_types:
            try:
                return possible_type.from_dict(value_to_deserialize)
            except Exception:
                pass
        return value_to_deserialize

    @classmethod
    def __deserialize_enum(cls, possible_types: tuple, value_to_deserialize: str):

        for possible_type in possible_types:
            if not isinstance(possible_type, EnumMeta):
                continue
            try:
                return getattr(possible_type, value_to_deserialize.upper().replace(' ', '_'))
            except Exception:
                pass
        return value_to_deserialize

    @classmethod
    def __deserialize_list(cls, possible_types: tuple, value_to_deserialize: list):
        for possible_type in possible_types:
            if not get_origin(possible_type) == list or not get_args(possible_type):
                continue
            try:
                return [cls.__deserialize_nested_type(
                    possible_types=get_args(possible_type),
                    value_to_deserialize=list_entry
                ) for list_entry in value_to_deserialize]
            except Exception:
                pass
        return value_to_deserialize
