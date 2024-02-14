import httpx
import asyncio
import logging

async def request(endpoint, method="GET", headers=None, params=None, data=None):
    base_api_url = "api.policeroleplay.community/v1"
    full_url = f"{base_api_url}/{endpoint}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.request(method, full_url, headers=headers, params=params, data=data)

            if 200 <= response.status_code < 300:
                logging.info(f"Request to {full_url} successful. Status code: {response.status_code}")
            else:
                logging.error(f"Request to {full_url} failed. Status code: {response.status_code}")

        except httpx.RequestError as e:
            logging.error(f"Request to {full_url} failed. Error: {e}")
            return None

        return response