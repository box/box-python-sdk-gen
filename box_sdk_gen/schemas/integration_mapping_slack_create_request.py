from typing import Optional

from box_sdk_gen.internal.base_object import BaseObject

from box_sdk_gen.schemas.integration_mapping_box_item_slack import (
    IntegrationMappingBoxItemSlack,
)

from box_sdk_gen.schemas.integration_mapping_slack_options import (
    IntegrationMappingSlackOptions,
)

from box_sdk_gen.schemas.integration_mapping_partner_item_slack import (
    IntegrationMappingPartnerItemSlack,
)


class IntegrationMappingSlackCreateRequest(BaseObject):
    def __init__(
        self,
        box_item: IntegrationMappingBoxItemSlack,
        *,
        options: Optional[IntegrationMappingSlackOptions] = None,
        partner_item: Optional[IntegrationMappingPartnerItemSlack] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.box_item = box_item
        self.options = options
        self.partner_item = partner_item
