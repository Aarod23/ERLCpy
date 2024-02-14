# ERLC Client Example


## Setting Up
### Initialize the ERLC Client


```python
import asyncio
import logging
from ERLC.erlc import client

erlc_client = client()
```

### Connect to the ERLC Client

```python
server_key = 'your_server_key'
global_key = 'your_global_key'

await erlc_client.config(server_key, global_key)

if erlc_client.connected:
    print("Connected to ERLC!")
else:
    print("Failed to connect to ERLC.")
```

## Example Usage

```python
server_key = 'your_server_key'
global_key = 'your_global_key'

await erlc_client.config(server_key, global_key)

if erlc_client.connected:
    print("Connected to ERLC!")
else:
    print("Failed to connect to ERLC.")

bans = await erlc_client.server.bans()
print(bans)


