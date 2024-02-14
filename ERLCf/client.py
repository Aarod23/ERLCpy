import asyncio
import logging
from .server import ServerClient as Server
import httpx
from .requests import request

class ErlcClient:
    def __init__(self):
        self.connected = False
        self.global_key = None
        self.server_key = None
        self.server = None 
        self.client = None

    async def config(self, server_key: str, global_key: str = None):
        if self.connected:
            return print("You are already connected to ERLC.")

        if global_key is None:
            print("You have not submitted a global API key.")

        self.server_key = server_key
        self.global_key = global_key

        self.client = await self.fetch_async_client()

        self.server = Server(async_client=self.client)
        headers = {"Authorization": global_key,"Server-Key": server_key}
        response = await request(headers=headers, endpoint="/server")
        
        if response is not None and response.status_code == 200:
            print("Succesfully connected to ERLC.")
            self.connected = True
        if response is not None and response.status_code == 404 or not 200:
            print("Failed to connect to ERLC.")
            self.connected = False


    async def disconnect(self):
        if not self.connected:
            return logging.error("You are not connected to ERLC.")

        await asyncio.sleep(1)
        logging.info("Your API keys have been removed.")

        self.connected = False
        self.server_key = None
        self.global_key = None
        self.server = None
        self.client = None

    async def reconnect(self):
        logging.info("Reconnecting to ERLC...")
        await self.disconnect()
        await self.connect(self.server_key, self.global_key)
    
    
    async def fetch_async_client(self):
        return AsyncClient(server_key=self.server_key, global_key=self.global_key)

class AsyncClient:
    def __init__(self, server_key, global_key):
        self.server_key = server_key
        self.global_key = global_key


client = ErlcClient()
