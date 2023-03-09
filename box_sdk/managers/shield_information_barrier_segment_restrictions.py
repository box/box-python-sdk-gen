from typing import Union

from box_sdk.base_object import BaseObject

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch, FetchOptions, FetchResponse

import json

from box_sdk.schemas import ShieldInformationBarrierSegmentRestriction

from box_sdk.schemas import ClientError

from box_sdk.schemas import ShieldInformationBarrierBase

class GetShieldInformationBarrierSegmentRestrictionsOptionsArg(BaseObject):
    def __init__(self, marker: Union[None, str] = None, limit: Union[None, int] = None, **kwargs):
        """
        :param marker: Defines the position marker at which to begin returning results. This is
            used when paginating using marker-based pagination.
            This requires `usemarker` to be set to `true`.
        :type marker: Union[None, str], optional
        :param limit: The maximum number of items to return per page.
        :type limit: Union[None, int], optional
        """
        super().__init__(**kwargs)
        self.marker = marker
        self.limit = limit

class PostShieldInformationBarrierSegmentRestrictionsRequestBodyArgTypeField:
    pass

class PostShieldInformationBarrierSegmentRestrictionsRequestBodyArgShieldInformationBarrierSegmentFieldTypeField:
    pass

class PostShieldInformationBarrierSegmentRestrictionsRequestBodyArgShieldInformationBarrierSegmentField(BaseObject):
    def __init__(self, id: Union[None, str] = None, type: Union[None, PostShieldInformationBarrierSegmentRestrictionsRequestBodyArgShieldInformationBarrierSegmentFieldTypeField] = None, **kwargs):
        """
        :param id: The ID reference of the requesting
            shield information barrier segment.
        :type id: Union[None, str], optional
        :param type: The type of the shield barrier segment for this member.
        :type type: Union[None, PostShieldInformationBarrierSegmentRestrictionsRequestBodyArgShieldInformationBarrierSegmentFieldTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type

class PostShieldInformationBarrierSegmentRestrictionsRequestBodyArgRestrictedSegmentFieldTypeField:
    pass

class PostShieldInformationBarrierSegmentRestrictionsRequestBodyArgRestrictedSegmentField(BaseObject):
    def __init__(self, id: Union[None, str] = None, type: Union[None, PostShieldInformationBarrierSegmentRestrictionsRequestBodyArgRestrictedSegmentFieldTypeField] = None, **kwargs):
        """
        :param id: The ID reference of the restricted
            shield information barrier segment.
        :type id: Union[None, str], optional
        :param type: The type of the restricted shield
            information barrier segment.
        :type type: Union[None, PostShieldInformationBarrierSegmentRestrictionsRequestBodyArgRestrictedSegmentFieldTypeField], optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type

class PostShieldInformationBarrierSegmentRestrictionsRequestBodyArg(BaseObject):
    def __init__(self, type: PostShieldInformationBarrierSegmentRestrictionsRequestBodyArgTypeField, shield_information_barrier_segment: PostShieldInformationBarrierSegmentRestrictionsRequestBodyArgShieldInformationBarrierSegmentField, restricted_segment: PostShieldInformationBarrierSegmentRestrictionsRequestBodyArgRestrictedSegmentField, shield_information_barrier: Union[None, ShieldInformationBarrierBase] = None, **kwargs):
        """
        :param type: The type of the shield barrier segment
            restriction for this member.
        :type type: PostShieldInformationBarrierSegmentRestrictionsRequestBodyArgTypeField
        :param shield_information_barrier_segment: The `type` and `id` of the requested
            shield information barrier segment.
        :type shield_information_barrier_segment: PostShieldInformationBarrierSegmentRestrictionsRequestBodyArgShieldInformationBarrierSegmentField
        :param restricted_segment: The `type` and `id` of the restricted
            shield information barrier segment.
        :type restricted_segment: PostShieldInformationBarrierSegmentRestrictionsRequestBodyArgRestrictedSegmentField
        """
        super().__init__(**kwargs)
        self.type = type
        self.shield_information_barrier_segment = shield_information_barrier_segment
        self.restricted_segment = restricted_segment
        self.shield_information_barrier = shield_information_barrier

class ShieldInformationBarrierSegmentRestrictionsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getShieldInformationBarrierSegmentRestrictionsId(self, shieldInformationBarrierSegmentRestrictionId: str) -> ShieldInformationBarrierSegmentRestriction:
        """
        Retrieves a shield information barrier segment
        
        restriction based on provided ID.

        :param shieldInformationBarrierSegmentRestrictionId: The ID of the shield information barrier segment Restriction.
            Example: "4563"
        :type shieldInformationBarrierSegmentRestrictionId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segment_restrictions/', shieldInformationBarrierSegmentRestrictionId]), FetchOptions(method='GET', auth=self.auth))
        return ShieldInformationBarrierSegmentRestriction.from_dict(json.loads(response.text))
    def deleteShieldInformationBarrierSegmentRestrictionsId(self, shieldInformationBarrierSegmentRestrictionId: str):
        """
        Delete shield information barrier segment restriction
        
        based on provided ID.

        :param shieldInformationBarrierSegmentRestrictionId: The ID of the shield information barrier segment Restriction.
            Example: "4563"
        :type shieldInformationBarrierSegmentRestrictionId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segment_restrictions/', shieldInformationBarrierSegmentRestrictionId]), FetchOptions(method='DELETE', auth=self.auth))
        return response.content
    def getShieldInformationBarrierSegmentRestrictions(self, shieldInformationBarrierSegmentId: str, options: GetShieldInformationBarrierSegmentRestrictionsOptionsArg = None) -> None:
        """
        Lists shield information barrier segment restrictions
        
        based on provided segment ID.

        :param shieldInformationBarrierSegmentId: The ID of the shield information barrier segment.
            Example: "3423"
        :type shieldInformationBarrierSegmentId: str
        """
        if options is None:
            options = GetShieldInformationBarrierSegmentRestrictionsOptionsArg()
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segment_restrictions']), FetchOptions(method='GET', params={'shield_information_barrier_segment_id': shieldInformationBarrierSegmentId, 'marker': options.marker, 'limit': options.limit}, auth=self.auth))
        return None
    def postShieldInformationBarrierSegmentRestrictions(self, requestBody: PostShieldInformationBarrierSegmentRestrictionsRequestBodyArg) -> ShieldInformationBarrierSegmentRestriction:
        """
        Creates a shield information barrier
        
        segment restriction object.

        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/shield_information_barrier_segment_restrictions']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return ShieldInformationBarrierSegmentRestriction.from_dict(json.loads(response.text))