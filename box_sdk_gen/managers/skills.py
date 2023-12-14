from enum import Enum

from typing import Optional

from typing import Union

from box_sdk_gen.base_object import BaseObject

from typing import List

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.serialization import serialize

from box_sdk_gen.schemas import SkillCardsMetadata

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import KeywordSkillCard

from box_sdk_gen.schemas import TimelineSkillCard

from box_sdk_gen.schemas import TranscriptSkillCard

from box_sdk_gen.schemas import StatusSkillCard

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse

from box_sdk_gen.json_data import sd_to_json

from box_sdk_gen.json_data import SerializedData


class UpdateFileMetadataGlobalBoxSkillsCardRequestBodyOpField(str, Enum):
    REPLACE = 'replace'


class UpdateFileMetadataGlobalBoxSkillsCardRequestBody(BaseObject):
    def __init__(
        self,
        op: Optional[UpdateFileMetadataGlobalBoxSkillsCardRequestBodyOpField] = None,
        path: Optional[str] = None,
        value: Optional[
            Union[
                KeywordSkillCard,
                TimelineSkillCard,
                TranscriptSkillCard,
                StatusSkillCard,
            ]
        ] = None,
        **kwargs
    ):
        """
        :param op: `replace`
        :type op: Optional[UpdateFileMetadataGlobalBoxSkillsCardRequestBodyOpField], optional
        :param path: The JSON Path that represents the card to replace. In most cases
            this will be in the format `/cards/{index}` where `index` is the
            zero-indexed position of the card in the list of cards.
        :type path: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.op = op
        self.path = path
        self.value = value


class UpdateSkillInvocationByIdStatus(str, Enum):
    INVOKED = 'invoked'
    PROCESSING = 'processing'
    SUCCESS = 'success'
    TRANSIENT_FAILURE = 'transient_failure'
    PERMANENT_FAILURE = 'permanent_failure'


class UpdateSkillInvocationByIdMetadata(BaseObject):
    def __init__(
        self,
        cards: Optional[
            List[
                Union[
                    KeywordSkillCard,
                    TimelineSkillCard,
                    TranscriptSkillCard,
                    StatusSkillCard,
                ]
            ]
        ] = None,
        **kwargs
    ):
        """
        :param cards: A list of Box Skill cards to apply to this file.
        :type cards: Optional[List[Union[KeywordSkillCard, TimelineSkillCard, TranscriptSkillCard, StatusSkillCard]]], optional
        """
        super().__init__(**kwargs)
        self.cards = cards


class UpdateSkillInvocationByIdFileTypeField(str, Enum):
    FILE = 'file'


class UpdateSkillInvocationByIdFile(BaseObject):
    def __init__(
        self,
        type: Optional[UpdateSkillInvocationByIdFileTypeField] = None,
        id: Optional[str] = None,
        **kwargs
    ):
        """
        :param type: `file`
        :type type: Optional[UpdateSkillInvocationByIdFileTypeField], optional
        :param id: The ID of the file
        :type id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id


class UpdateSkillInvocationByIdFileVersionTypeField(str, Enum):
    FILE_VERSION = 'file_version'


class UpdateSkillInvocationByIdFileVersion(BaseObject):
    def __init__(
        self,
        type: Optional[UpdateSkillInvocationByIdFileVersionTypeField] = None,
        id: Optional[str] = None,
        **kwargs
    ):
        """
        :param type: `file_version`
        :type type: Optional[UpdateSkillInvocationByIdFileVersionTypeField], optional
        :param id: The ID of the file version
        :type id: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id


class UpdateSkillInvocationByIdUsage(BaseObject):
    def __init__(
        self, unit: Optional[str] = None, value: Optional[float] = None, **kwargs
    ):
        """
        :param unit: `file`
        :type unit: Optional[str], optional
        :param value: `1`
        :type value: Optional[float], optional
        """
        super().__init__(**kwargs)
        self.unit = unit
        self.value = value


class SkillsManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: NetworkSession = None,
    ):
        if network_session is None:
            network_session = NetworkSession()
        self.auth = auth
        self.network_session = network_session

    def get_file_metadata_global_box_skills_cards(
        self, file_id: str, extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> SkillCardsMetadata:
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
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                self.network_session.base_urls.base_url,
                '/files/',
                to_string(file_id),
                '/metadata/global/boxSkillsCards',
            ]),
            FetchOptions(
                method='GET',
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, SkillCardsMetadata)

    def create_file_metadata_global_box_skills_card(
        self,
        file_id: str,
        cards: List[
            Union[
                KeywordSkillCard,
                TimelineSkillCard,
                TranscriptSkillCard,
                StatusSkillCard,
            ]
        ],
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> SkillCardsMetadata:
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
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {'cards': cards}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                self.network_session.base_urls.base_url,
                '/files/',
                to_string(file_id),
                '/metadata/global/boxSkillsCards',
            ]),
            FetchOptions(
                method='POST',
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, SkillCardsMetadata)

    def update_file_metadata_global_box_skills_card(
        self,
        file_id: str,
        request_body: List[UpdateFileMetadataGlobalBoxSkillsCardRequestBody],
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> SkillCardsMetadata:
        """
        Updates one or more Box Skills metadata cards to a file.
        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        :param request_body: Request body of updateFileMetadataGlobalBoxSkillsCard method
        :type request_body: List[UpdateFileMetadataGlobalBoxSkillsCardRequestBody]
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                self.network_session.base_urls.base_url,
                '/files/',
                to_string(file_id),
                '/metadata/global/boxSkillsCards',
            ]),
            FetchOptions(
                method='PUT',
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/json-patch+json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, SkillCardsMetadata)

    def delete_file_metadata_global_box_skills_card(
        self, file_id: str, extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> None:
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
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                self.network_session.base_urls.base_url,
                '/files/',
                to_string(file_id),
                '/metadata/global/boxSkillsCards',
            ]),
            FetchOptions(
                method='DELETE',
                headers=headers_map,
                response_format=None,
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return None

    def update_skill_invocation_by_id(
        self,
        skill_id: str,
        status: UpdateSkillInvocationByIdStatus,
        metadata: UpdateSkillInvocationByIdMetadata,
        file: UpdateSkillInvocationByIdFile,
        file_version: Optional[UpdateSkillInvocationByIdFileVersion] = None,
        usage: Optional[UpdateSkillInvocationByIdUsage] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> None:
        """
        An alternative method that can be used to overwrite and update all Box Skill

        metadata cards on a file.

        :param skill_id: The ID of the skill to apply this metadata for.
            Example: "33243242"
        :type skill_id: str
        :param status: Defines the status of this invocation. Set this to `success` when setting Skill cards.
        :type status: UpdateSkillInvocationByIdStatus
        :param metadata: The metadata to set for this skill. This is a list of
            Box Skills cards. These cards will overwrite any existing Box
            skill cards on the file.
        :type metadata: UpdateSkillInvocationByIdMetadata
        :param file: The file to assign the cards to.
        :type file: UpdateSkillInvocationByIdFile
        :param file_version: The optional file version to assign the cards to.
        :type file_version: Optional[UpdateSkillInvocationByIdFileVersion], optional
        :param usage: A descriptor that defines what items are affected by this call.
            Set this to the default values when setting a card to a `success`
            state, and leave it out in most other situations.
        :type usage: Optional[UpdateSkillInvocationByIdUsage], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {
            'status': status,
            'metadata': metadata,
            'file': file,
            'file_version': file_version,
            'usage': usage,
        }
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                self.network_session.base_urls.base_url,
                '/skill_invocations/',
                to_string(skill_id),
            ]),
            FetchOptions(
                method='PUT',
                headers=headers_map,
                data=serialize(request_body),
                content_type='application/json',
                response_format=None,
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return None
