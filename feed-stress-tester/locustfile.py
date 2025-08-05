# locustfile.py
import time, asyncio, aiohttp
from locust import User, task, between, events

# Solana feed URL (you can plug in Birdeye, Jupiter, or Helius here)
FEED_URL = "https://public-api.birdeye.so/public/price?address=So11111111111111111111111111111111111111112"

class SolanaFeedUser(User):
    wait_time = between(0.1, 0.3)  # simulate frequent polling
    host = FEED_URL

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loop = asyncio.get_event_loop()

    @task
    def fetch_price(self):
        self.loop.run_until_complete(self.async_fetch())

    async def async_fetch(self):
        start_time = time.time()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.host) as resp:
                    if resp.status != 200:
                        raise Exception(f"Non-200: {resp.status}")
                    data = await resp.json()
            total_time = int((time.time() - start_time) * 1000)
            events.request_success.fire(request_type="GET", name="price_feed", response_time=total_time, response_length=len(str(data)))
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type="GET", name="price_feed", response_time=total_time, exception=e)
