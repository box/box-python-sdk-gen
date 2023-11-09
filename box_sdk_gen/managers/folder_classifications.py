from enum import Enum

from typing import Optional

from box_sdk_gen.base_object import BaseObject

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

from box_sdk_gen.json import sd_to_json

from box_sdk_gen.json import SerializedData


class UpdateFolderMetadataEnterpriseSecurityClassificationRequestBodyArgOpField(
    str, Enum
):
    REPLACE = 'replace'


class UpdateFolderMetadataEnterpriseSecurityClassificationRequestBodyArgPathField(
    str, Enum
):
    _BOX__SECURITY__CLASSIFICATION__KEY = '/Box__Security__Classification__Key'


class UpdateFolderMetadataEnterpriseSecurityClassificationRequestBodyArg(BaseObject):
    def __init__(
        self,
        op: Optional[
            UpdateFolderMetadataEnterpriseSecurityClassificationRequestBodyArgOpField
        ] = None,
        path: Optional[
            UpdateFolderMetadataEnterpriseSecurityClassificationRequestBodyArgPathField
        ] = None,
        value: Optional[str] = None,
        **kwargs
    ):
        """
        :param op: `replace`
        :type op: Optional[UpdateFolderMetadataEnterpriseSecurityClassificationRequestBodyArgOpField], optional
        :param path: `/Box__Security__Classification__Key`
        :type path: Optional[UpdateFolderMetadataEnterpriseSecurityClassificationRequestBodyArgPathField], optional
        :param value: The name of the classification to apply to this folder.
            To list the available classifications in an enterprise,
            use the classification API to retrieve the
            [classification template](e://get_metadata_templates_enterprise_securityClassification-6VMVochwUWo_schema)
            which lists all available classification keys.
        :type value: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.op = op
        self.path = path
        self.value = value


class FolderClassificationsManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def get_folder_metadata_enterprise_security_classification_6_vm_vochw_u_wo(
        self, folder_id: str, extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> Classification:
        """
        Retrieves the classification metadata instance that

        has been applied to a folder.


        This API can also be called by including the enterprise ID in the


        URL explicitly, for example


        `/folders/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

        :param folder_id: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folder_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/folders/',
                to_string(folder_id),
                '/metadata/enterprise/securityClassification-6VMVochwUWo',
            ]),
            FetchOptions(
                method='GET',
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.data, Classification)

    def create_folder_metadata_enterprise_security_classification(
        self,
        folder_id: str,
        box_security_classification_key: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> Classification:
        """
        Adds a classification to a folder by specifying the label of the

        classification to add.


        This API can also be called by including the enterprise ID in the


        URL explicitly, for example


        `/folders/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

        :param folder_id: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folder_id: str
        :param box_security_classification_key: The name of the classification to apply to this folder.
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
            ''.join([
                'https://api.box.com/2.0/folders/',
                to_string(folder_id),
                '/metadata/enterprise/securityClassification-6VMVochwUWo',
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
        return deserialize(response.data, Classification)

    def update_folder_metadata_enterprise_security_classification(
        self,
        folder_id: str,
        request_body: List[
            UpdateFolderMetadataEnterpriseSecurityClassificationRequestBodyArg
        ],
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> Classification:
        """
        Updates a classification on a folder.

        The classification can only be updated if a classification has already been


        applied to the folder before. When editing classifications, only values are


        defined for the enterprise will be accepted.

        :param folder_id: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folder_id: str
        :param request_body: Request body of updateFolderMetadataEnterpriseSecurityClassification method
        :type request_body: List[UpdateFolderMetadataEnterpriseSecurityClassificationRequestBodyArg]
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/folders/',
                to_string(folder_id),
                '/metadata/enterprise/securityClassification-6VMVochwUWo',
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
        return deserialize(response.data, Classification)

    def delete_folder_metadata_enterprise_security_classification(
        self, folder_id: str, extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> None:
        """
        Removes any classifications from a folder.

        This API can also be called by including the enterprise ID in the


        URL explicitly, for example


        `/folders/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

        :param folder_id: The unique identifier that represent a folder.
            The ID for any folder can be determined
            by visiting this folder in the web application
            and copying the ID from the URL. For example,
            for the URL `https://*.app.box.com/folder/123`
            the `folder_id` is `123`.
            The root folder of a Box account is
            always represented by the ID `0`.
            Example: "12345"
        :type folder_id: str
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join([
                'https://api.box.com/2.0/folders/',
                to_string(folder_id),
                '/metadata/enterprise/securityClassification-6VMVochwUWo',
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
