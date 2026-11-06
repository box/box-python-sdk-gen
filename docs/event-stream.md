# Event Stream

<!-- box-python-sdk-gen deprecation banner -->
> [!CAUTION]
> **`box-python-sdk-gen` is deprecated and no longer maintained.** As of September 17, 2025, it receives no new features, bug fixes, or security patches. Do not use it for new projects.
>
> Use [`box-python-sdk`](https://github.com/box/box-python-sdk) v10+ instead: `pip install "boxsdk>=10"`.
> The equivalent of this page is [box-python-sdk/docs/event-stream.md](https://github.com/box/box-python-sdk/blob/main/docs/event-stream.md). To migrate existing code, see the [migration guide](https://github.com/box/box-python-sdk/blob/main/migration-guides/from-box-python-sdk-gen-v1-to-box-python-sdk.md).

The Event Stream class utilizes long-polling to receive real-time events from Box. The SDK provides an easy way to set up and manage the event stream which returns an iterable object and yields events as they are received.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Event Stream](#event-stream)
  - [Listening to the Event Stream](#listening-to-the-event-stream)
  - [Deduplication](#deduplication)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Listening to the Event Stream

When the `EventStream` is started, it will begin long-polling asynchronously. Events received from the API are then yielded to the caller.

```python
event_stream = client.events.get_event_stream()
for event in event_stream:
    print("Received event:", event)
```

## Deduplication

The `EventStream` class automatically deduplicates events based on their `event_id`. This means that if the same event is received multiple times, it will only be emitted once to the listeners.
