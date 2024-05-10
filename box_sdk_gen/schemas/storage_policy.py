from typing import Optional

from box_sdk_gen.schemas.storage_policy_mini import StoragePolicyMiniTypeField

from box_sdk_gen.schemas.storage_policy_mini import StoragePolicyMini


class StoragePolicy(StoragePolicyMini):
    def __init__(
        self,
        id: str,
        *,
        name: Optional[str] = None,
        type: StoragePolicyMiniTypeField = StoragePolicyMiniTypeField.STORAGE_POLICY.value,
        **kwargs
    ):
        """
        :param id: The unique identifier for this storage policy
        :type id: str
        :param name: A descriptive name of the region, defaults to None
        :type name: Optional[str], optional
        :param type: `storage_policy`, defaults to StoragePolicyMiniTypeField.STORAGE_POLICY.value
        :type type: StoragePolicyMiniTypeField, optional
        """
        super().__init__(id=id, type=type, **kwargs)
        self.name = name
