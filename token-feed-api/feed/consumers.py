import json
import random
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer

class TokenFeedConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("token_feed", self.channel_name)
        await self.accept()
        self.send_task = asyncio.create_task(self.send_fake_prices())  # 🔥 start sending fake prices

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("token_feed", self.channel_name)
        self.send_task.cancel()

    async def send_fake_prices(self):
        while True:
            await asyncio.sleep(2)  # 🔁 every 2 seconds
            price = round(random.uniform(10, 1000), 2)
            token_data = {
                "token": "SOL",
                "price": price,
                "volume": random.randint(100, 10000)
            }
            await self.channel_layer.group_send("token_feed", {
                "type": "send_token_update",
                "data": token_data
            })

    async def send_token_update(self, event):
        await self.send(text_data=json.dumps(event["data"]))
