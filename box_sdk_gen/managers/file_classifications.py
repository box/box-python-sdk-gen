from typing import Optional

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


class FileClassificationsManager:
    def __init__(self, auth: Optional[Authentication] = None, network_session: Optional[NetworkSession] = None):
        self.auth = auth
        self.network_session = network_session

    def get_file_metadata_enterprise_security_classification_6_vm_vochw_u_wo(self, file_id: str) -> Classification:
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
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/metadata/enterprise/securityClassification-6VMVochwUWo']), FetchOptions(method='GET', response_format='json', auth=self.auth, network_session=self.network_session))
        return Classification.from_dict(json.loads(response.text))

    def create_file_metadata_enterprise_security_classification(self, file_id: str, box_security_classification_key: Optional[str] = None) -> Classification:
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
        """
        request_body: BaseObject = BaseObject(box_security_classification_key=box_security_classification_key)
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/metadata/enterprise/securityClassification-6VMVochwUWo']), FetchOptions(method='POST', body=json.dumps(request_body.to_dict()), content_type='application/json', response_format='json', auth=self.auth, network_session=self.network_session))
        return Classification.from_dict(json.loads(response.text))

    def delete_file_metadata_enterprise_security_classification(self, file_id: str) -> None:
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
        """
        response: FetchResponse = fetch(''.join(['https://api.box.com/2.0/files/', file_id, '/metadata/enterprise/securityClassification-6VMVochwUWo']), FetchOptions(method='DELETE', response_format=None, auth=self.auth, network_session=self.network_session))
        return None