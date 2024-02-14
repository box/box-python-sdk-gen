from enum import Enum

from box_sdk_gen.base_object import BaseObject

from typing import Optional

from typing import Dict

from box_sdk_gen.utils import to_string

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.serialization import serialize

from typing import List

from box_sdk_gen.schemas import Classification

from box_sdk_gen.schemas import ClientError

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


class UpdateClassificationOnFileRequestBodyOpField(str, Enum):
    REPLACE = 'replace'


class UpdateClassificationOnFileRequestBodyPathField(str, Enum):
    _BOX__SECURITY__CLASSIFICATION__KEY = '/Box__Security__Classification__Key'


class UpdateClassificationOnFileRequestBody(BaseObject):
    def __init__(
        self,
        op: UpdateClassificationOnFileRequestBodyOpField,
        path: UpdateClassificationOnFileRequestBodyPathField,
        value: str,
        **kwargs
    ):
        """
        :param op: `replace`
        :type op: UpdateClassificationOnFileRequestBodyOpField
        :param path: Defines classifications
            available in the enterprise.
        :type path: UpdateClassificationOnFileRequestBodyPathField
        :param value: The name of the classification to apply to this file.
            To list the available classifications in an enterprise,
            use the classification API to retrieve the
            [classification template](e://get_metadata_templates_enterprise_securityClassification-6VMVochwUWo_schema)
            which lists all available classification keys.
        :type value: str
        """
        super().__init__(**kwargs)
        self.op = op
        self.path = path
        self.value = value


class FileClassificationsManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: NetworkSession = None,
    ):
        if network_session is None:
            network_session = NetworkSession()
        self.auth = auth
        self.network_session = network_session

    def get_classification_on_file(
        self, file_id: str, extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> Classification:
        """
        Retrieves the classification metadata instance that

        has been applied to a file.


        This API can also be called by including the enterprise ID in the


        URL explicitly, for example


        `/files/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

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
            ''.join(
                [
                    self.network_session.base_urls.base_url,
                    '/files/',
                    to_string(file_id),
                    '/metadata/enterprise/securityClassification-6VMVochwUWo',
                ]
            ),
            FetchOptions(
                method='GET',
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, Classification)

    def add_classification_to_file(
        self,
        file_id: str,
        box_security_classification_key: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> Classification:
        """
        Adds a classification to a file by specifying the label of the

        classification to add.


        This API can also be called by including the enterprise ID in the


        URL explicitly, for example


        `/files/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        :param box_security_classification_key: The name of the classification to apply to this file.
            To list the available classifications in an enterprise,
            use the classification API to retrieve the
            [classification template](e://get_metadata_templates_enterprise_securityClassification-6VMVochwUWo_schema)
            which lists all available classification keys.
        :type box_security_classification_key: Optional[str], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body: Dict = {
            'Box__Security__Classification__Key': box_security_classification_key
        }
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    self.network_session.base_urls.base_url,
                    '/files/',
                    to_string(file_id),
                    '/metadata/enterprise/securityClassification-6VMVochwUWo',
                ]
            ),
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
        return deserialize(response.data, Classification)

    def update_classification_on_file(
        self,
        file_id: str,
        request_body: List[UpdateClassificationOnFileRequestBody],
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> Classification:
        """
        Updates a classification on a file.

        The classification can only be updated if a classification has already been


        applied to the file before. When editing classifications, only values are


        defined for the enterprise will be accepted.

        :param file_id: The unique identifier that represents a file.
            The ID for any file can be determined
            by visiting a file in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/files/123`
            the `file_id` is `123`.
            Example: "12345"
        :type file_id: str
        :param request_body: Request body of updateClassificationOnFile method
        :type request_body: List[UpdateClassificationOnFileRequestBody]
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(
                [
                    self.network_session.base_urls.base_url,
                    '/files/',
                    to_string(file_id),
                    '/metadata/enterprise/securityClassification-6VMVochwUWo',
                ]
            ),
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
        return deserialize(response.data, Classification)

    def delete_classification_from_file(
        self, file_id: str, extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> None:
        """
        Removes any classifications from a file.

        This API can also be called by including the enterprise ID in the


        URL explicitly, for example


        `/files/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

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
            ''.join(
                [
                    self.network_session.base_urls.base_url,
                    '/files/',
                    to_string(file_id),
                    '/metadata/enterprise/securityClassification-6VMVochwUWo',
                ]
            ),
            FetchOptions(
                method='DELETE',
                headers=headers_map,
                response_format=None,
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return None
