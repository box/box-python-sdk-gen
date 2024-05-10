from box_sdk_gen.internal.utils import to_string

from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas.events import Events

from box_sdk_gen.schemas.event import Event

from box_sdk_gen.managers.events import GetEventsStreamType

from box_sdk_gen.managers.events import GetEventsEventType

from box_sdk_gen.schemas.realtime_servers import RealtimeServers

from box_sdk_gen.schemas.realtime_server import RealtimeServer

from test.commons import get_default_client

from box_sdk_gen.schemas.event_source import EventSource

from box_sdk_gen.schemas.file import File

from box_sdk_gen.schemas.folder import Folder

from box_sdk_gen.schemas.user import User

client: BoxClient = get_default_client()


def testEvents():
    events: Events = client.events.get_events()
    assert len(events.entries) > 0
    event: Event = events.entries[0]
    assert to_string(event.created_by.type) == 'user'
    assert not to_string(event.event_type) == ''


def testEventUpload():
    events: Events = client.events.get_events(
        stream_type=GetEventsStreamType.ADMIN_LOGS.value,
        event_type=[GetEventsEventType.UPLOAD.value],
    )
    assert len(events.entries) > 0
    event: Event = events.entries[0]
    assert to_string(event.event_type) == 'UPLOAD'
    source: EventSource = event.source
    assert (
        to_string(source.item_type) == 'file' or to_string(source.item_type) == 'folder'
    )
    assert not source.item_id == ''
    assert not source.item_name == ''


def testEventDeleteUser():
    events: Events = client.events.get_events(
        stream_type=GetEventsStreamType.ADMIN_LOGS.value,
        event_type=[GetEventsEventType.DELETE_USER.value],
    )
    assert len(events.entries) > 0
    event: Event = events.entries[0]
    assert to_string(event.event_type) == 'DELETE_USER'
    source: User = event.source
    assert to_string(source.type) == 'user'
    assert not source.id == ''


def testEventSourceFileOrFolder():
    events: Events = client.events.get_events(
        stream_type=GetEventsStreamType.CHANGES.value
    )
    assert len(events.entries) > 0
    event: Event = events.entries[0]
    source: File = event.source
    assert to_string(source.type) == 'file' or to_string(source.type) == 'folder'
    assert not source.id == ''


def testGetEventsWithLongPolling():
    servers: RealtimeServers = client.events.get_events_with_long_polling()
    assert len(servers.entries) > 0
    server: RealtimeServer = servers.entries[0]
    assert to_string(server.type) == 'realtime_server'
    assert not server.url == ''
