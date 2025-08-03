import asyncio
import json
import random
from django.core.management.base import BaseCommand
from channels.layers import get_channel_layer

TOKENS = ['SOL', 'BONK', 'JUP', 'WIF', 'PYTH']

class Command(BaseCommand):
    help = 'Broadcast mock token prices to WebSocket clients'

    async def broadcast_loop(self):
        channel_layer = get_channel_layer()

        while True:
            for token in TOKENS:
                price = round(random.uniform(0.0001, 200), 5)
                data = {
                    "symbol": token,
                    "price": price
                }
                await channel_layer.group_send(
                    "token_feed",
                    {
                        "type": "send_token_update",
                        "data": data
                    }
                )
            await asyncio.sleep(5)

    def handle(self, *args, **kwargs):
        self.stdout.write("🔄 Starting mock price broadcaster...")
        asyncio.run(self.broadcast_loop())
