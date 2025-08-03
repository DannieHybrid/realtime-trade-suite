# feed/tasks.py
import asyncio
import json
import random
from channels.layers import get_channel_layer

async def broadcast_token_data():
    channel_layer = get_channel_layer()
    while True:
        data = {
            "token": "SOL",
            "price": round(random.uniform(10, 1000), 2),
            "volume": random.randint(500, 10000),
        }
        await channel_layer.group_send(
            "token_feed",
            {
                "type": "send.token.update",
                "data": data
            }
        )
        await asyncio.sleep(2)
