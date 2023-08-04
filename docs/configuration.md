# Configuration

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Max retry attempts](#max-retry-attempts)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Max retry attempts

The default maximum number of retries in case of failed API call is 5 (429 and >= 500 response codes are retried).
To change this number you can set `client.network.MAX_ATTEMPTS` field.

```python
from box_sdk_gen.client import Client
from box_sdk_gen.developer_token_auth import DeveloperTokenAuth

auth = DeveloperTokenAuth(token='DEVELOPER_TOKEN_GOES_HERE')
client = Client(auth=auth)
client.network.MAX_ATTEMPTS = 6
```
