from enum import Enum

from typing import Optional

from typing import List

from typing import Union

from box_sdk.base_object import BaseObject

import json

from box_sdk.base_object import BaseObject

from box_sdk.schemas import SkillCardsMetadata

from box_sdk.schemas import ClientError

from box_sdk.schemas import KeywordSkillCard

from box_sdk.schemas import TimelineSkillCard

from box_sdk.schemas import TranscriptSkillCard

from box_sdk.schemas import StatusSkillCard

from box_sdk.auth import Authentication

from box_sdk.network import NetworkSession

from box_sdk.utils import prepare_params

from box_sdk.utils import to_string

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class UpdateSkillInvocationByIdStatusArg(str, Enum):
    INVOKED = 'invoked'
    PROCESSING = 'processing'
    SUCCESS = 'success'
    TRANSIENT_FAILURE = 'transient_failure'
    PERMANENT_FAILURE = 'permanent_failure'

class UpdateSkillInvocationByIdMetadataArg(BaseObject):
    def __init__(self, cards: Optional[List[Union[KeywordSkillCard, TimelineSkillCard, TranscriptSkillCard, StatusSkillCard]]] = None, **kwargs):
        """
        :param cards: A list of Box Skill cards to apply to this file.
        :type cards: Optional[List[Union[KeywordSkillCard, TimelineSkillCard, TranscriptSkillCard, StatusSkillCard]]], optional
        """
        super().__init__(**kwargs)
        self.cards = cards

class UpdateSkillInvocationByIdFileArgTypeField(str, Enum):
    FILE = 'file'

class UpdateSkillInvocationByIdFileArg(BaseObject):
    def __init__(self, type: Optional[UpdateSkillInvocationByIdFileArgTypeField] = None, id: Optional[str] = None, **kwargs):
        """
        :param type: `file`
        :type type: Optional[UpdateSkillInvocationByIdFileArgTypeField], optional
        :param id: The ID of the file
        :type id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class UpdateSkillInvocationByIdFileVersionArgTypeField(str, Enum):
    FILE_VERSION = 'file_version'

class UpdateSkillInvocationByIdFileVersionArg(BaseObject):
    def __init__(self, type: Optional[UpdateSkillInvocationByIdFileVersionArgTypeField] = None, id: Optional[str] = None, **kwargs):
        """
        :param type: `file_version`
        :type type: Optional[UpdateSkillInvocationByIdFileVersionArgTypeField], optional
        :param id: The ID of the file version
        :type id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class UpdateSkillInvocationByIdUsageArg(BaseObject):
    def __init__(self, unit: Optional[str] = None, value: Optional[int] = None, **kwargs):
        """
        :param unit: `file`
        :type unit: Optional[str], optional
        :param value: `1`
        :type value: Optional[int], optional
        """
        super().__init__(**kwargs)
        self.unit = unit
        self.value = value

class SkillsManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def get_file_metadata_global_box_skills_cards(self, file_id: str) -> SkillCardsMetadata:
        """
        List the Box Skills metadata cards that are attached to a file.
        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/metadata/global/boxSkillsCards']), FetchOptions(method='GET', auth=self.auth, network_session=self.network_session))
        return SkillCardsMetadata.from_dict(json.loads(response.text))
    def create_file_metadata_global_box_skills_card(self, file_id: str, cards: List[Union[KeywordSkillCard, TimelineSkillCard, TranscriptSkillCard, StatusSkillCard]]) -> SkillCardsMetadata:
        """
        Applies one or more Box Skills metadata cards to a file.
        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        :param cards: A list of Box Skill cards to apply to this file.
        :type cards: List[Union[KeywordSkillCard, TimelineSkillCard, TranscriptSkillCard, StatusSkillCard]]
        """
        request_body: BaseObject = BaseObject(cards=cards)
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/metadata/global/boxSkillsCards']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return SkillCardsMetadata.from_dict(json.loads(response.text))
    def delete_file_metadata_global_box_skills_card(self, file_id: str):
        """
        Removes any Box Skills cards metadata from a file.
        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/metadata/global/boxSkillsCards']), FetchOptions(method='DELETE', auth=self.auth, network_session=self.network_session))
        return response.content
    def update_skill_invocation_by_id(self, skill_id: str, status: UpdateSkillInvocationByIdStatusArg, metadata: UpdateSkillInvocationByIdMetadataArg, file: UpdateSkillInvocationByIdFileArg, file_version: Optional[UpdateSkillInvocationByIdFileVersionArg] = None, usage: Optional[UpdateSkillInvocationByIdUsageArg] = None):
        """
        An alternative method that can be used to overwrite and update all Box Skill
        
        metadata cards on a file.

        :param skill_id: The ID of the skill to apply this metadata for.
            Example: "33243242"
        :type skill_id: str
        :param status: Defines the status of this invocation. Set this to `success` when setting Skill cards.
        :type status: UpdateSkillInvocationByIdStatusArg
        :param metadata: The metadata to set for this skill. This is a list of
            Box Skills cards. These cards will overwrite any existing Box
            skill cards on the file.
        :type metadata: UpdateSkillInvocationByIdMetadataArg
        :param file: The file to assign the cards to.
        :type file: UpdateSkillInvocationByIdFileArg
        :param file_version: The optional file version to assign the cards to.
        :type file_version: Optional[UpdateSkillInvocationByIdFileVersionArg], optional
        :param usage: A descriptor that defines what items are affected by this call.
            Set this to the default values when setting a card to a `success`
            state, and leave it out in most other situations.
        :type usage: Optional[UpdateSkillInvocationByIdUsageArg], optional
        """
        request_body: BaseObject = BaseObject(status=status, metadata=metadata, file=file, file_version=file_version, usage=usage)
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/skill_invocations/', skill_id]), FetchOptions(method='PUT', body=json.dumps(request_body.to_dict()), content_type='application/json', auth=self.auth, network_session=self.network_session))
        return response.content