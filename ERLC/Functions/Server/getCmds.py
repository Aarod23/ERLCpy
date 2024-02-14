import httpx
import asyncio
import logging
from ..requests import request

async def commands(self, async_client):
    """Fetches the ERLC server Commands Logs
                
    Parameters:
        None
                
    Returns:
        Tuple (status_code, data)
    """
    headers = {"Authorization": async_client.global_key,"Server-Key": async_client.server_key}
    response = await request(headers=headers, endpoint="/server/commandlogs")

    if response:
        return response.status_code, response.json()
    else:
        return 500, None