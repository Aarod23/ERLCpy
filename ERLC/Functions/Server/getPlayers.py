import httpx
import asyncio
import logging
from ...requests import request

async def players(self, async_client):
    """Fetches the ERLC server players
                
    Parameters:
        None
                
    Returns:
        JSON Data
    """
    headers = {"Authorization": async_client.global_key,"Server-Key": async_client.server_key}
    response = await request(headers=headers, endpoint="/server/players")

    if response:
        return response.json()
    else:
        return None