# feed_stress/stress_tester.py

import asyncio
import websockets

FEED_URL = "ws://localhost:8000/ws/token/SOL/"  # Replace with real endpoint if needed

async def simulate_client(id):
    try:
        async with websockets.connect(FEED_URL) as ws:
            for _ in range(3):
                msg = await ws.recv()
                print(f"[Client {id}] Received: {msg}")
    except Exception as e:
        print(f"[Client {id}] Error: {e}")

async def run_stress_test(count=1000):
    print(f"🚀 Launching {count} simulated clients...")
    tasks = [simulate_client(i) for i in range(count)]
    await asyncio.gather(*tasks)
