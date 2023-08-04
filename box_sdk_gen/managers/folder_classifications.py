from typing import Optional

from typing import Dict

import json

from box_sdk_gen.base_object import BaseObject

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

class FolderClassificationsManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session
    def get_folder_metadata_enterprise_security_classification_6_vm_vochw_u_wo(self, folder_id: str, extra_headers: Optional[Dict[str, Optional[str]]] = None) -> Classification:
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
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/metadata/enterprise/securityClassification-6VMVochwUWo']), FetchOptions(method='GET', headers=headers_map, response_format='json', auth=self.auth, network_session=self.network_session))
        return Classification.from_dict(json.loads(response.text))
    def create_folder_metadata_enterprise_security_classification(self, folder_id: str, box_security_classification_key: Optional[str] = None, extra_headers: Optional[Dict[str, Optional[str]]] = None) -> Classification:
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
        request_body: BaseObject = BaseObject(box_security_classification_key=box_security_classification_key)
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/metadata/enterprise/securityClassification-6VMVochwUWo']), FetchOptions(method='POST', headers=headers_map, body=json.dumps(request_body.to_dict()), content_type='application/json', response_format='json', auth=self.auth, network_session=self.network_session))
        return Classification.from_dict(json.loads(response.text))
    def delete_folder_metadata_enterprise_security_classification(self, folder_id: str, extra_headers: Optional[Dict[str, Optional[str]]] = None) -> None:
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
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/folders/', folder_id, '/metadata/enterprise/securityClassification-6VMVochwUWo']), FetchOptions(method='DELETE', headers=headers_map, response_format=None, auth=self.auth, network_session=self.network_session))
        return None