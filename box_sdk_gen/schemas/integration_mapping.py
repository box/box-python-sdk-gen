from enum import Enum

from typing import Union

from typing import Optional

from box_sdk_gen.schemas.integration_mapping_base import (
    IntegrationMappingBaseIntegrationTypeField,
)

from box_sdk_gen.schemas.integration_mapping_base import IntegrationMappingBase

from box_sdk_gen.schemas.integration_mapping_partner_item_slack import (
    IntegrationMappingPartnerItemSlack,
)

from box_sdk_gen.schemas.folder_mini import FolderMini

from box_sdk_gen.schemas.integration_mapping_slack_options import (
    IntegrationMappingSlackOptions,
)

from box_sdk_gen.schemas.user_integration_mappings import UserIntegrationMappings

from box_sdk_gen.internal.utils import DateTime


class IntegrationMappingTypeField(str, Enum):
    INTEGRATION_MAPPING = 'integration_mapping'


class IntegrationMapping(IntegrationMappingBase):
    def __init__(
        self,
        partner_item: Union[IntegrationMappingPartnerItemSlack],
        box_item: FolderMini,
        *,
        type: IntegrationMappingTypeField = IntegrationMappingTypeField.INTEGRATION_MAPPING.value,
        is_manually_created: Optional[bool] = None,
        options: Optional[IntegrationMappingSlackOptions] = None,
        created_by: Optional[UserIntegrationMappings] = None,
        modified_by: Optional[UserIntegrationMappings] = None,
        created_at: Optional[DateTime] = None,
        modified_at: Optional[DateTime] = None,
        id: Optional[str] = None,
        integration_type: Optional[IntegrationMappingBaseIntegrationTypeField] = None,
        **kwargs
    ):
        """
                :param partner_item: Mapped item object for Slack
                :type partner_item: Union[IntegrationMappingPartnerItemSlack]
                :param box_item: The Box folder, to which the object from the
        partner app domain (referenced in `partner_item_id`) is mapped
                :type box_item: FolderMini
                :param type: Mapping type, defaults to IntegrationMappingTypeField.INTEGRATION_MAPPING.value
                :type type: IntegrationMappingTypeField, optional
                :param is_manually_created: Identifies whether the mapping has
        been manually set
        (as opposed to being automatically created), defaults to None
                :type is_manually_created: Optional[bool], optional
                :param options: Integration mapping options for Slack, defaults to None
                :type options: Optional[IntegrationMappingSlackOptions], optional
                :param created_by: An object representing the user who
        created the integration mapping, defaults to None
                :type created_by: Optional[UserIntegrationMappings], optional
                :param modified_by: The user who
        last modified the integration mapping, defaults to None
                :type modified_by: Optional[UserIntegrationMappings], optional
                :param created_at: When the integration mapping object was created, defaults to None
                :type created_at: Optional[DateTime], optional
                :param modified_at: When the integration mapping object was last modified, defaults to None
                :type modified_at: Optional[DateTime], optional
                :param id: A unique identifier of a folder mapping
        (part of a composite key together
        with `integration_type`), defaults to None
                :type id: Optional[str], optional
                :param integration_type: Identifies the Box partner app,
        with which the mapping is associated.
        Currently only supports Slack.
        (part of the composite key together with `id`), defaults to None
                :type integration_type: Optional[IntegrationMappingBaseIntegrationTypeField], optional
        """
        super().__init__(id=id, integration_type=integration_type, **kwargs)
        self.partner_item = partner_item
        self.box_item = box_item
        self.type = type
        self.is_manually_created = is_manually_created
        self.options = options
        self.created_by = created_by
        self.modified_by = modified_by
        self.created_at = created_at
        self.modified_at = modified_at
