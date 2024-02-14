# pip install ERLC

import asyncio
from ERLC.erlc import ErlcClient

async def main():
    erlc_client = ErlcClient()

    server_key = 'your_server_key'
    global_key = 'your_global_key'

    await erlc_client.config(server_key, global_key)

    if erlc_client.connected:
        print("Connected to ERLC!")
    else:
        print("Failed to connect to ERLC.")
        
    bans = await erlc_client.server.killlogs()
    print(bans)

asyncio.run(main())