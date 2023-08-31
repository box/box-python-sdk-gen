from enum import Enum

from typing import Optional

from typing import Dict

import json

from box_sdk_gen.schemas import Events

from box_sdk_gen.schemas import ClientError

from box_sdk_gen.schemas import RealtimeServers

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession

from box_sdk_gen.utils import prepare_params

from box_sdk_gen.utils import to_string

from box_sdk_gen.utils import ByteStream

from box_sdk_gen.fetch import fetch

from box_sdk_gen.fetch import FetchOptions

from box_sdk_gen.fetch import FetchResponse


class GetEventsStreamTypeArg(str, Enum):
    ALL = 'all'
    CHANGES = 'changes'
    SYNC = 'sync'
    ADMIN_LOGS = 'admin_logs'
    ADMIN_LOGS_STREAMING = 'admin_logs_streaming'


class EventsManager:
    def __init__(
        self,
        auth: Optional[Authentication] = None,
        network_session: Optional[NetworkSession] = None,
    ):
        self.auth = auth
        self.network_session = network_session

    def get_events(
        self,
        stream_type: Optional[GetEventsStreamTypeArg] = None,
        stream_position: Optional[str] = None,
        limit: Optional[int] = None,
        event_type: Optional[str] = None,
        created_after: Optional[str] = None,
        created_before: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None,
    ) -> Events:
        """
        Returns up to a year of past events for a given user

        or for the entire enterprise.


        By default this returns events for the authenticated user. To retrieve events


        for the entire enterprise, set the `stream_type` to `admin_logs_streaming`


        for live monitoring of new events, or `admin_logs` for querying across


        historical events. The user making the API call will


        need to have admin privileges, and the application will need to have the


        scope `manage enterprise properties` checked.

        :param stream_type: Defines the type of events that are returned
            * `all` returns everything for a user and is the default
            * `changes` returns events that may cause file tree changes
              such as file updates or collaborations.
            * `sync` is similar to `changes` but only applies to synced folders
            * `admin_logs` returns all events for an entire enterprise and
              requires the user making the API call to have admin permissions. This
              stream type is for programmatically pulling from a 1 year history of
              events across all users within the enterprise and within a
              `created_after` and `created_before` time frame. The complete history
              of events will be returned in chronological order based on the event
              time, but latency will be much higher than `admin_logs_streaming`.
            * `admin_logs_streaming` returns all events for an entire enterprise and
              requires the user making the API call to have admin permissions. This
              stream type is for polling for recent events across all users within
              the enterprise. Latency will be much lower than `admin_logs`, but
              events will not be returned in chronological order and may
              contain duplicates.
        :type stream_type: Optional[GetEventsStreamTypeArg], optional
        :param stream_position: The location in the event stream to start receiving events from.
            * `now` will return an empty list events and
            the latest stream position for initialization.
            * `0` or `null` will return all events.
        :type stream_position: Optional[str], optional
        :param limit: Limits the number of events returned
            Note: Sometimes, the events less than the limit requested can be returned
            even when there may be more events remaining. This is primarily done in
            the case where a number of events have already been retrieved and these
            retrieved events are returned rather than delaying for an unknown amount
            of time to see if there are any more results.
        :type limit: Optional[int], optional
        :param event_type: A comma-separated list of events to filter by. This can only be used when
            requesting the events with a `stream_type` of `admin_logs` or
            `adming_logs_streaming`. For any other `stream_type` this value will be
            ignored.
        :type event_type: Optional[str], optional
        :param created_after: The lower bound date and time to return events for. This can only be used
            when requesting the events with a `stream_type` of `admin_logs`. For any
            other `stream_type` this value will be ignored.
        :type created_after: Optional[str], optional
        :param created_before: The upper bound date and time to return events for. This can only be used
            when requesting the events with a `stream_type` of `admin_logs`. For any
            other `stream_type` this value will be ignored.
        :type created_before: Optional[str], optional
        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        query_params_map: Dict[str, str] = prepare_params(
            {
                'stream_type': to_string(stream_type),
                'stream_position': to_string(stream_position),
                'limit': to_string(limit),
                'event_type': to_string(event_type),
                'created_after': to_string(created_after),
                'created_before': to_string(created_before),
            }
        )
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/events']),
            FetchOptions(
                method='GET',
                params=query_params_map,
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return Events.from_dict(json.loads(response.text))

    def get_events_with_long_polling(
        self, extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> RealtimeServers:
        """
        Returns a list of real-time servers that can be used for long-polling updates

        to the [event stream](#get-events).


        Long polling is the concept where a HTTP request is kept open until the


        server sends a response, then repeating the process over and over to receive


        updated responses.


        Long polling the event stream can only be used for user events, not for


        enterprise events.


        To use long polling, first use this endpoint to retrieve a list of long poll


        URLs. Next, make a long poll request to any of the provided URLs.


        When an event occurs in monitored account a response with the value


        `new_change` will be sent. The response contains no other details as


        it only serves as a prompt to take further action such as sending a


        request to the [events endpoint](#get-events) with the last known


        `stream_position`.


        After the server sends this response it closes the connection. You must now


        repeat the long poll process to begin listening for events again.


        If no events occur for a while and the connection times out you will


        receive a response with the value `reconnect`. When you receive this response


        you’ll make another call to this endpoint to restart the process.


        If you receive no events in `retry_timeout` seconds then you will need to


        make another request to the real-time server (one of the URLs in the response


        for this endpoint). This might be necessary due to network errors.


        Finally, if you receive a `max_retries` error when making a request to the


        real-time server, you should start over by making a call to this endpoint


        first.

        :param extra_headers: Extra headers that will be included in the HTTP request.
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        if extra_headers is None:
            extra_headers = {}
        headers_map: Dict[str, str] = prepare_params({**extra_headers})
        response: FetchResponse = fetch(
            ''.join(['https://api.box.com/2.0/events']),
            FetchOptions(
                method='OPTIONS',
                headers=headers_map,
                response_format='json',
                auth=self.auth,
                network_session=self.network_session,
            ),
        )
        return RealtimeServers.from_dict(json.loads(response.text))
