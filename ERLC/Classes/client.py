import asyncio
import logging
from ERLC.Classes.server import Server
import httpx

class ErlcClient:
    def __init__(self):
        self.connected = False
        self.global_key = None
        self.server_key = None

    async def connect(self, server_key: str, global_key: str):
        if self.connected:
            return logging.error("You are already connected to ERLC.")

        if global_key is None:
            logging.info("You have not submitted a global API key.")

        self.server_key = server_key
        self.global_key = global_key
        self.connected = True

        logging.info("Your API keys are now ready to be used.")

    async def disconnect(self):
        if not self.connected:
            return logging.error("You are not connected to ERLC.")

        await asyncio.sleep(1)
        logging.info("Your API keys have been removed.")

        self.connected = False
        self.server_key = None
        self.global_key = None

    async def reconnect(self):
        logging.info("Reconnecting to ERLC...")
        await self.disconnect()
        await self.connect(self.server_key, self.global_key)
        
    server = Server()
    
