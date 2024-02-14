import asyncio

import ERLC  # Import the ERLC package

async def main():
    erlc_client = ERLC.ErlcClient()

    server_key = 'your_server_key'
    global_key = 'your_global_key'

    await erlc_client.config(server_key, global_key)



asyncio.run(main())
