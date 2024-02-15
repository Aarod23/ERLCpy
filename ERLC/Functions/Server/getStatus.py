import httpx
import asyncio
import logging
from .requests import request

async def status(self, async_client):
    """Fetches the ERLC server status
                
    Parameters:
        None
                
    Returns:
        JSON Data
    """
    headers = {"Authorization": async_client.global_key,"Server-Key": async_client.server_key}
    response = await request(headers=headers, endpoint="server")

    if response:
        return response.json()
    else:
        return None
    