from typing import Optional

from box_sdk.base_object import BaseObject

from enum import Enum

import json

from typing import Dict

from box_sdk.schemas import ShieldInformationBarrierSegmentRestriction

from box_sdk.schemas import ClientError

from box_sdk.schemas import ShieldInformationBarrierBase

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class GetShieldInformationBarrierSegmentRestrictionsOptionsArg(BaseObject):
    def __init__(self, marker: Optional[str] = None, limit: Optional[int] = None, **kwargs):
        """
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Optional[str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.marker = marker
        self.limit = limit

class CreateShieldInformationBarrierSegmentRestrictionRequestBodyArgTypeField(str, Enum):
    SHIELD_INFORMATION_BARRIER_SEGMENT_RESTRICTION = 'shield_information_barrier_segment_restriction'

class CreateShieldInformationBarrierSegmentRestrictionRequestBodyArgShieldInformationBarrierSegmentFieldTypeField(str, Enum):
    SHIELD_INFORMATION_BARRIER_SEGMENT = 'shield_information_barrier_segment'

class CreateShieldInformationBarrierSegmentRestrictionRequestBodyArgShieldInformationBarrierSegmentField(BaseObject):
    def __init__(self, id: Optional[str] = None, type: Optional[CreateShieldInformationBarrierSegmentRestrictionRequestBodyArgShieldInformationBarrierSegmentFieldTypeField] = None, **kwargs):
        """
        :param id: The ID reference of the requesting
            shield information barrier segment.
        :type id: Optional[str], optional
        :param type: The type of the shield barrier segment for this member.
        :type type: Optional[CreateShieldInformationBarrierSegmentRestrictionRequestBodyArgShieldInformationBarrierSegmentFieldTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type

class CreateShieldInformationBarrierSegmentRestrictionRequestBodyArgRestrictedSegmentFieldTypeField(str, Enum):
    SHIELD_INFORMATION_BARRIER_SEGMENT = 'shield_information_barrier_segment'

class CreateShieldInformationBarrierSegmentRestrictionRequestBodyArgRestrictedSegmentField(BaseObject):
    def __init__(self, id: Optional[str] = None, type: Optional[CreateShieldInformationBarrierSegmentRestrictionRequestBodyArgRestrictedSegmentFieldTypeField] = None, **kwargs):
        """
        :param id: The ID reference of the restricted
            shield information barrier segment.
        :type id: Optional[str], optional
        :param type: The type of the restricted shield
            information barrier segment.
        :type type: Optional[CreateShieldInformationBarrierSegmentRestrictionRequestBodyArgRestrictedSegmentFieldTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type

class CreateShieldInformationBarrierSegmentRestrictionRequestBodyArg(BaseObject):
    def __init__(self, type: CreateShieldInformationBarrierSegmentRestrictionRequestBodyArgTypeField, shield_information_barrier_segment: CreateShieldInformationBarrierSegmentRestrictionRequestBodyArgShieldInformationBarrierSegmentField, restricted_segment: CreateShieldInformationBarrierSegmentRestrictionRequestBodyArgRestrictedSegmentField, shield_information_barrier: Optional[ShieldInformationBarrierBase] = None, **kwargs):
        """
        :param type: The type of the shield barrier segment
            restriction for this member.
        :type type: CreateShieldInformationBarrierSegmentRestrictionRequestBodyArgTypeField
        :param shield_information_barrier_segment: The `type` and `id` of the requested
            shield information barrier segment.
        :type shield_information_barrier_segment: CreateShieldInformationBarrierSegmentRestrictionRequestBodyArgShieldInformationBarrierSegmentField
        :param restricted_segment: The `type` and `id` of the restricted
            shield information barrier segment.
        :type restricted_segment: CreateShieldInformationBarrierSegmentRestrictionRequestBodyArgRestrictedSegmentField
        """
        super().__init__(**kwargs)
        self.type = type
        self.shield_information_barrier_segment = shield_information_barrier_segment
        self.restricted_segment = restricted_segment
        self.shield_information_barrier = shield_information_barrier

class ShieldInformationBarrierSegmentRestrictionsManager(BaseObject):
    _fields_to_json_mapping: Dict[str, str] = {'network_session': 'networkSession', **BaseObject._fields_to_json_mapping}
    _json_to_fields_mapping: Dict[str, str] = {'networkSession': 'network_session', **BaseObject._json_to_fields_mapping}
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None, **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
        self.network_session = network_session
    def get_shield_information_barrier_segment_restriction_by_id(self, shield_information_barrier_segment_restriction_id: str) -> ShieldInformationBarrierSegmentRestriction:
        """
        Retrieves a shield information barrier segment
        
        restriction based on provided ID.

        :param shield_information_barrier_segment_restriction_id: The ID of the shield information barrier segment Restriction.
            Example: "4563"
        :type shield_information_barrier_segment_restriction_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segment_restrictions/', shield_information_barrier_segment_restriction_id]), FetchOptions(method='GET', auth=self.auth, network_session=self.network_session))
        return ShieldInformationBarrierSegmentRestriction.from_dict(json.loads(response.text))
    def delete_shield_information_barrier_segment_restriction_by_id(self, shield_information_barrier_segment_restriction_id: str):
        """
        Delete shield information barrier segment restriction
        
        based on provided ID.

        :param shield_information_barrier_segment_restriction_id: The ID of the shield information barrier segment Restriction.
            Example: "4563"
        :type shield_information_barrier_segment_restriction_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segment_restrictions/', shield_information_barrier_segment_restriction_id]), FetchOptions(method='DELETE', auth=self.auth, network_session=self.network_session))
        return response.content
    def get_shield_information_barrier_segment_restrictions(self, shield_information_barrier_segment_id: str, options: GetShieldInformationBarrierSegmentRestrictionsOptionsArg = None) -> None:
        """
        Lists shield information barrier segment restrictions
        
        based on provided segment ID.

        :param shield_information_barrier_segment_id: The ID of the shield information barrier segment.
            Example: "3423"
        :type shield_information_barrier_segment_id: str
        """
        if options is None:
            options = GetShieldInformationBarrierSegmentRestrictionsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segment_restrictions']), FetchOptions(method='GET', params={'shield_information_barrier_segment_id': shield_information_barrier_segment_id, 'marker': options.marker, 'limit': options.limit}, auth=self.auth, network_session=self.network_session))
        return None
    def create_shield_information_barrier_segment_restriction(self, request_body: CreateShieldInformationBarrierSegmentRestrictionRequestBodyArg) -> ShieldInformationBarrierSegmentRestriction:
        """
        Creates a shield information barrier
        
        segment restriction object.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segment_restrictions']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return ShieldInformationBarrierSegmentRestriction.from_dict(json.loads(response.text))