# ERLC Client Example

## Initialize the ERLC Client

```python
import asyncio
import logging
from ERLC.erlc import client

erlc_client = client()
```

## Connect to the ERLC Client

```python
server_key = 'your_server_key'
global_key = 'your_global_key'

await erlc_client.connect(server_key, global_key)

if erlc_client.connected:
    print("Connected to ERLC!")
else:
    print("Failed to connect to ERLC.")
```

## Disconnect from the ERLC Client

```python
await erlc_client.disconnect()

if not erlc_client.connected:
    print("Disconnected from ERLC.")
else:
    print("Failed to disconnect from ERLC.")
```

## Reconnect to the ERLC Client

```python
await erlc_client.reconnect()

if erlc_client.connected:
    print("Reconnected to ERLC!")
else:
    print("Failed to reconnect to ERLC.")
```
