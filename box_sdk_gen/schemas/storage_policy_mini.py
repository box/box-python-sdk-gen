from enum import Enum

from box_sdk_gen.internal.base_object import BaseObject


class StoragePolicyMiniTypeField(str, Enum):
    STORAGE_POLICY = 'storage_policy'


class StoragePolicyMini(BaseObject):
    _discriminator = 'type', {'storage_policy'}

    def __init__(
        self,
        id: str,
        *,
        type: StoragePolicyMiniTypeField = StoragePolicyMiniTypeField.STORAGE_POLICY.value,
        **kwargs
    ):
        """
        :param id: The unique identifier for this storage policy
        :type id: str
        :param type: `storage_policy`, defaults to StoragePolicyMiniTypeField.STORAGE_POLICY.value
        :type type: StoragePolicyMiniTypeField, optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
