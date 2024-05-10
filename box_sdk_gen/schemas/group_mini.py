from enum import Enum

from typing import Optional

from box_sdk_gen.schemas.group_base import GroupBaseTypeField

from box_sdk_gen.schemas.group_base import GroupBase


class GroupMiniGroupTypeField(str, Enum):
    MANAGED_GROUP = 'managed_group'
    ALL_USERS_GROUP = 'all_users_group'


class GroupMini(GroupBase):
    def __init__(
        self,
        id: str,
        *,
        name: Optional[str] = None,
        group_type: Optional[GroupMiniGroupTypeField] = None,
        type: GroupBaseTypeField = GroupBaseTypeField.GROUP.value,
        **kwargs
    ):
        """
        :param id: The unique identifier for this object
        :type id: str
        :param name: The name of the group, defaults to None
        :type name: Optional[str], optional
        :param group_type: The type of the group., defaults to None
        :type group_type: Optional[GroupMiniGroupTypeField], optional
        :param type: `group`, defaults to GroupBaseTypeField.GROUP.value
        :type type: GroupBaseTypeField, optional
        """
        super().__init__(id=id, type=type, **kwargs)
        self.name = name
        self.group_type = group_type
