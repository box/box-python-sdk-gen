# Configuration

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Max retry attempts](#max-retry-attempts)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Max retry attempts

The default maximum number of retries in case of failed API call is 5 (429 and >= 500 response codes are retried).
To change this number you can set `client.network.MAX_ATTEMPTS` field.

```python
from box_sdk_gen import BoxClient, BoxDeveloperTokenAuth

auth = BoxDeveloperTokenAuth(token='DEVELOPER_TOKEN_GOES_HERE')
client = BoxClient(auth=auth)
client.network_session.MAX_ATTEMPTS = 6
```
