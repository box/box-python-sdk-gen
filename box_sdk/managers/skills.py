from typing import List

from typing import Union

from box_sdk.base_object import BaseObject

from enum import Enum

import json

from box_sdk.schemas import SkillCardsMetadata

from box_sdk.schemas import ClientError

from box_sdk.schemas import KeywordSkillCard

from box_sdk.schemas import TimelineSkillCard

from box_sdk.schemas import TranscriptSkillCard

from box_sdk.schemas import StatusSkillCard

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.jwt_auth import JWTAuth

from box_sdk.fetch import fetch

from box_sdk.fetch import FetchOptions

from box_sdk.fetch import FetchResponse

class CreateFileMetadataGlobalBoxSkillsCardRequestBodyArg(BaseObject):
    def __init__(self, cards: List[Union[KeywordSkillCard, TimelineSkillCard, TranscriptSkillCard, StatusSkillCard]], **kwargs):
        """
        :param cards: A list of Box Skill cards to apply to this file.
        :type cards: List[Union[KeywordSkillCard, TimelineSkillCard, TranscriptSkillCard, StatusSkillCard]]
        """
        super().__init__(**kwargs)
        self.cards = cards

class UpdateSkillInvocationByIdRequestBodyArgStatusField(str, Enum):
    INVOKED = 'invoked'
    PROCESSING = 'processing'
    SUCCESS = 'success'
    TRANSIENT_FAILURE = 'transient_failure'
    PERMANENT_FAILURE = 'permanent_failure'

class UpdateSkillInvocationByIdRequestBodyArgMetadataField(BaseObject):
    def __init__(self, cards: Union[None, List[Union[KeywordSkillCard, TimelineSkillCard, TranscriptSkillCard, StatusSkillCard]]] = None, **kwargs):
        """
        :param cards: A list of Box Skill cards to apply to this file.
        :type cards: Union[None, List[Union[KeywordSkillCard, TimelineSkillCard, TranscriptSkillCard, StatusSkillCard]]], optional
        """
        super().__init__(**kwargs)
        self.cards = cards

class UpdateSkillInvocationByIdRequestBodyArgFileFieldTypeField(str, Enum):
    FILE = 'file'

class UpdateSkillInvocationByIdRequestBodyArgFileField(BaseObject):
    def __init__(self, type: Union[None, UpdateSkillInvocationByIdRequestBodyArgFileFieldTypeField] = None, id: Union[None, str] = None, **kwargs):
        """
        :param type: `file`
        :type type: Union[None, UpdateSkillInvocationByIdRequestBodyArgFileFieldTypeField], optional
        :param id: The ID of the file
        :type id: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class UpdateSkillInvocationByIdRequestBodyArgFileVersionFieldTypeField(str, Enum):
    FILE_VERSION = 'file_version'

class UpdateSkillInvocationByIdRequestBodyArgFileVersionField(BaseObject):
    def __init__(self, type: Union[None, UpdateSkillInvocationByIdRequestBodyArgFileVersionFieldTypeField] = None, id: Union[None, str] = None, **kwargs):
        """
        :param type: `file_version`
        :type type: Union[None, UpdateSkillInvocationByIdRequestBodyArgFileVersionFieldTypeField], optional
        :param id: The ID of the file version
        :type id: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class UpdateSkillInvocationByIdRequestBodyArgUsageField(BaseObject):
    def __init__(self, unit: Union[None, str] = None, value: Union[None, int] = None, **kwargs):
        """
        :param unit: `file`
        :type unit: Union[None, str], optional
        :param value: `1`
        :type value: Union[None, int], optional
        """
        super().__init__(**kwargs)
        self.unit = unit
        self.value = value

class UpdateSkillInvocationByIdRequestBodyArg(BaseObject):
    def __init__(self, status: UpdateSkillInvocationByIdRequestBodyArgStatusField, metadata: UpdateSkillInvocationByIdRequestBodyArgMetadataField, file: UpdateSkillInvocationByIdRequestBodyArgFileField, file_version: Union[None, UpdateSkillInvocationByIdRequestBodyArgFileVersionField] = None, usage: Union[None, UpdateSkillInvocationByIdRequestBodyArgUsageField] = None, **kwargs):
        """
        :param status: Defines the status of this invocation. Set this to `success` when setting Skill cards.
        :type status: UpdateSkillInvocationByIdRequestBodyArgStatusField
        :param metadata: The metadata to set for this skill. This is a list of
            Box Skills cards. These cards will overwrite any existing Box
            skill cards on the file.
        :type metadata: UpdateSkillInvocationByIdRequestBodyArgMetadataField
        :param file: The file to assign the cards to.
        :type file: UpdateSkillInvocationByIdRequestBodyArgFileField
        :param file_version: The optional file version to assign the cards to.
        :type file_version: Union[None, UpdateSkillInvocationByIdRequestBodyArgFileVersionField], optional
        :param usage: A descriptor that defines what items are affected by this call.
            Set this to the default values when setting a card to a `success`
            state, and leave it out in most other situations.
        :type usage: Union[None, UpdateSkillInvocationByIdRequestBodyArgUsageField], optional
        """
        super().__init__(**kwargs)
        self.status = status
        self.metadata = metadata
        self.file = file
        self.file_version = file_version
        self.usage = usage

class SkillsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth, JWTAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
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
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/metadata/global/boxSkillsCards']), FetchOptions(method='GET', auth=self.auth))
        return SkillCardsMetadata.from_dict(json.loads(response.text))
    def create_file_metadata_global_box_skills_card(self, file_id: str, request_body: CreateFileMetadataGlobalBoxSkillsCardRequestBodyArg) -> SkillCardsMetadata:
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
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/metadata/global/boxSkillsCards']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), auth=self.auth))
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
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/metadata/global/boxSkillsCards']), FetchOptions(method='DELETE', auth=self.auth))
        return response.content
    def update_skill_invocation_by_id(self, skill_id: str, request_body: UpdateSkillInvocationByIdRequestBodyArg):
        """
        An alternative method that can be used to overwrite and update all Box Skill
        
        metadata cards on a file.

        :param skill_id: The ID of the skill to apply this metadata for.
            Example: "33243242"
        :type skill_id: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/skill_invocations/', skill_id]), FetchOptions(method='PUT', body=json.dumps(request_body.to_dict()), auth=self.auth))
        return response.content