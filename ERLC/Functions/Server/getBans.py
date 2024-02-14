import httpx
import asyncio
import logging
from ..requests import request

async def bans(self, async_client):
    """Fetches the ERLC server Ban Logs
                
    Parameters:
        None
                
    Returns:
        Tuple (status_code, data)
    """
    headers = {"Authorization": async_client.global_key,"Server-Key": async_client.server_key}
    response = await request(headers=headers, endpoint="/server/bans")

    if response:
        return response.status_code, response.json()
    else:
        return 500, None