from enum import Enum

from box_sdk_gen.internal.base_object import BaseObject


class GroupBaseTypeField(str, Enum):
    GROUP = 'group'


class GroupBase(BaseObject):
    _discriminator = 'type', {'group'}

    def __init__(
        self,
        id: str,
        *,
        type: GroupBaseTypeField = GroupBaseTypeField.GROUP.value,
        **kwargs
    ):
        """
        :param id: The unique identifier for this object
        :type id: str
        :param type: `group`, defaults to GroupBaseTypeField.GROUP.value
        :type type: GroupBaseTypeField, optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
