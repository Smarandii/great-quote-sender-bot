import aiohttp


class Quoter:
    def __init__(self):
        self.url_api = "https://api.quotable.io"

    async def get_random_quote(self):
        client = aiohttp.ClientSession()
        async with client.get(f'{self.url_api}/random') as resp:
            await client.close()
            return await resp.json()
