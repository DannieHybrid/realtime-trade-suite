import asyncio
import websockets
import json
import random

NUM_CLIENTS = 10  # You can increase to 100, 1000 later

async def connect_and_receive(client_id):
    uri = "ws://localhost:8000/ws/feed/"
    try:
        async with websockets.connect(uri) as websocket:
            print(f"[Client {client_id}] Connected")
            while True:
                msg = await websocket.recv()
                data = json.loads(msg)
                print(f"[Client {client_id}] Received: {data}")
    except Exception as e:
        print(f"[Client {client_id}] Error: {e}")

async def main():
    tasks = [connect_and_receive(i) for i in range(NUM_CLIENTS)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())