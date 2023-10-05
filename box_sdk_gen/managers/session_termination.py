from typing import Optional

from typing import List

from typing import Dict

from box_sdk_gen.serialization import serialize

from box_sdk_gen.serialization import deserialize

from box_sdk_gen.schemas import SessionTerminationMessage

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse


class SessionTerminationManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def create_user_terminate_session(
        self,
        user_ids: List[str],
        user_logins: List[str],
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> SessionTerminationMessage:
        """
        Validates the roles and permissions of the user,

        and creates asynchronous jobs


        to terminate the user's sessions.


        Returns the status for the POST request.

        :param user_ids: A list of user IDs
        :type user_ids: List[str]
        :param user_logins: A list of user logins
        :type user_logins: List[str]
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body = {'user_ids': user_ids, 'user_logins': user_logins}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/users/terminate_sessions']),
            FetchOptions(
                method='POST',
                headers=headers_map,
                body=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, SessionTerminationMessage)

    def create_group_terminate_session(
        self,
        group_ids: List[str],
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> SessionTerminationMessage:
        """
        Validates the roles and permissions of the group,

        and creates asynchronous jobs


        to terminate the group's sessions.


        Returns the status for the POST request.

        :param group_ids: A list of group IDs
        :type group_ids: List[str]
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        request_body = {'group_ids': group_ids}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/groups/terminate_sessions']),
            FetchOptions(
                method='POST',
                headers=headers_map,
                body=serialize(request_body),
                content_type='application/json',
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return deserialize(response.text, SessionTerminationMessage)
