from typing import List

from typing import Union

from box_sdk.base_object import BaseObject

from enum import Enum

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.fetch import fetch, FetchOptions, FetchResponse

import json

from box_sdk.schemas import SkillCardsMetadata

from box_sdk.schemas import ClientError

from box_sdk.schemas import SkillCard

from box_sdk.schemas import KeywordSkillCard

from box_sdk.schemas import TimelineSkillCard

from box_sdk.schemas import TranscriptSkillCard

from box_sdk.schemas import StatusSkillCard

class PostFilesIdMetadataGlobalBoxSkillsCardsRequestBodyArg(BaseObject):
    def __init__(self, cards: List[Union[SkillCard, KeywordSkillCard, TimelineSkillCard, TranscriptSkillCard, StatusSkillCard]], **kwargs):
        """
        :param cards: A list of Box Skill cards to apply to this file.
        :type cards: List[Union[SkillCard, KeywordSkillCard, TimelineSkillCard, TranscriptSkillCard, StatusSkillCard]]
        """
        super().__init__(**kwargs)
        self.cards = cards

class PutSkillInvocationsIdRequestBodyArgStatusField(str, Enum):
    INVOKED = 'invoked'
    PROCESSING = 'processing'
    SUCCESS = 'success'
    TRANSIENT_FAILURE = 'transient_failure'
    PERMANENT_FAILURE = 'permanent_failure'

class PutSkillInvocationsIdRequestBodyArgMetadataField(BaseObject):
    def __init__(self, cards: Union[None, List[Union[SkillCard, KeywordSkillCard, TimelineSkillCard, TranscriptSkillCard, StatusSkillCard]]] = None, **kwargs):
        """
        :param cards: A list of Box Skill cards to apply to this file.
        :type cards: Union[None, List[Union[SkillCard, KeywordSkillCard, TimelineSkillCard, TranscriptSkillCard, StatusSkillCard]]], optional
        """
        super().__init__(**kwargs)
        self.cards = cards

class PutSkillInvocationsIdRequestBodyArgFileFieldTypeField:
    pass

class PutSkillInvocationsIdRequestBodyArgFileField(BaseObject):
    def __init__(self, type: Union[None, PutSkillInvocationsIdRequestBodyArgFileFieldTypeField] = None, id: Union[None, str] = None, **kwargs):
        """
        :param type: `file`
        :type type: Union[None, PutSkillInvocationsIdRequestBodyArgFileFieldTypeField], optional
        :param id: The ID of the file
        :type id: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class PutSkillInvocationsIdRequestBodyArgFileVersionFieldTypeField:
    pass

class PutSkillInvocationsIdRequestBodyArgFileVersionField(BaseObject):
    def __init__(self, type: Union[None, PutSkillInvocationsIdRequestBodyArgFileVersionFieldTypeField] = None, id: Union[None, str] = None, **kwargs):
        """
        :param type: `file_version`
        :type type: Union[None, PutSkillInvocationsIdRequestBodyArgFileVersionFieldTypeField], optional
        :param id: The ID of the file version
        :type id: Union[None, str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id

class PutSkillInvocationsIdRequestBodyArgUsageField(BaseObject):
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

class PutSkillInvocationsIdRequestBodyArg(BaseObject):
    def __init__(self, status: PutSkillInvocationsIdRequestBodyArgStatusField, metadata: PutSkillInvocationsIdRequestBodyArgMetadataField, file: PutSkillInvocationsIdRequestBodyArgFileField, file_version: Union[None, PutSkillInvocationsIdRequestBodyArgFileVersionField] = None, usage: Union[None, PutSkillInvocationsIdRequestBodyArgUsageField] = None, **kwargs):
        """
        :param status: Defines the status of this invocation. Set this to `success` when setting Skill cards.
        :type status: PutSkillInvocationsIdRequestBodyArgStatusField
        :param metadata: The metadata to set for this skill. This is a list of
            Box Skills cards. These cards will overwrite any existing Box
            skill cards on the file.
        :type metadata: PutSkillInvocationsIdRequestBodyArgMetadataField
        :param file: The file to assign the cards to.
        :type file: PutSkillInvocationsIdRequestBodyArgFileField
        :param file_version: The optional file version to assign the cards to.
        :type file_version: Union[None, PutSkillInvocationsIdRequestBodyArgFileVersionField], optional
        :param usage: A descriptor that defines what items are affected by this call.
            Set this to the default values when setting a card to a `success`
            state, and leave it out in most other situations.
        :type usage: Union[None, PutSkillInvocationsIdRequestBodyArgUsageField], optional
        """
        super().__init__(**kwargs)
        self.status = status
        self.metadata = metadata
        self.file = file
        self.file_version = file_version
        self.usage = usage

class SkillsManager(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
    def getFilesIdMetadataGlobalBoxSkillsCards(self, fileId: str) -> SkillCardsMetadata:
        """
        List the Box Skills metadata cards that are attached to a file.
        :param fileId: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type fileId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', fileId, '/metadata/global/boxSkillsCards']), FetchOptions(method='GET', auth=self.auth))
        return SkillCardsMetadata.from_dict(json.loads(response.text))
    def postFilesIdMetadataGlobalBoxSkillsCards(self, fileId: str, requestBody: PostFilesIdMetadataGlobalBoxSkillsCardsRequestBodyArg) -> SkillCardsMetadata:
        """
        Applies one or more Box Skills metadata cards to a file.
        :param fileId: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type fileId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', fileId, '/metadata/global/boxSkillsCards']), FetchOptions(method='POST', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return SkillCardsMetadata.from_dict(json.loads(response.text))
    def deleteFilesIdMetadataGlobalBoxSkillsCards(self, fileId: str):
        """
        Removes any Box Skills cards metadata from a file.
        :param fileId: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type fileId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', fileId, '/metadata/global/boxSkillsCards']), FetchOptions(method='DELETE', auth=self.auth))
        return response.content
    def putSkillInvocationsId(self, skillId: str, requestBody: PutSkillInvocationsIdRequestBodyArg):
        """
        An alternative method that can be used to overwrite and update all Box Skill
        
        metadata cards on a file.

        :param skillId: The ID of the skill to apply this metadata for.
            Example: "33243242"
        :type skillId: str
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/skill_invocations/', skillId]), FetchOptions(method='PUT', body=json.dumps(requestBody.to_dict()), auth=self.auth))
        return response.content