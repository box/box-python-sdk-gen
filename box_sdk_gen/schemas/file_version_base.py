from enum import Enum

from box_sdk_gen.internal.base_object import BaseObject


class FileVersionBaseTypeField(str, Enum):
    FILE_VERSION = 'file_version'


class FileVersionBase(BaseObject):
    _discriminator = 'type', {'file_version'}

    def __init__(
        self,
        id: str,
        *,
        type: FileVersionBaseTypeField = FileVersionBaseTypeField.FILE_VERSION.value,
        **kwargs
    ):
        """
        :param id: The unique identifier that represent a file version.
        :type id: str
        :param type: `file_version`, defaults to FileVersionBaseTypeField.FILE_VERSION.value
        :type type: FileVersionBaseTypeField, optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
