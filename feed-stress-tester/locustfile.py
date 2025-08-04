# locustfile.py

from locust import User, task
import asyncio
import websockets

WS_URL = "ws://localhost:8000/ws/token/SOL/"

class WebSocketUser(User):
    @task
    def connect_and_receive(self):
        asyncio.run(self.ws_session())

    async def ws_session(self):
        try:
            async with websockets.connect(WS_URL) as ws:
                for _ in range(3):
                    msg = await ws.recv()
                    print(f"📥 {msg}")
        except Exception as e:
            print(f"❌ WS error: {e}")
