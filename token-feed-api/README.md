# 🧠 Token Feed API – Real-Time WebSocket Simulator

A Django Channels-based real-time WebSocket API for simulating live token price and volume feeds.

---

## 🚀 Features

- WebSocket endpoint at `ws://127.0.0.1:8000/ws/feed/`
- Sends live `SOL` token price/volume every 2 seconds
- Uses Django Channels (ASGI) with optional Redis support

---

## 🛠️ Setup

```bash
git clone <repo-url>
cd token-feed-api
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
▶️ Running the Server
1. Run migrations:
bash
Copy
Edit
python manage.py migrate
2. Run via Daphne (ASGI server):
bash
Copy
Edit
daphne -b 127.0.0.1 -p 8000 tokenfeed.asgi:application
📡 WebSocket Output
json
Copy
Edit
{
  "token": "SOL",
  "price": 473.22,
  "volume": 7868
}
Data is broadcast to all clients connected to /ws/feed/.

🧪 Optional WebSocket Test (Python CLI)
python
Copy
Edit
# ws-client.py
import websocket
ws = websocket.WebSocket()
ws.connect("ws://127.0.0.1:8000/ws/feed/")
print(ws.recv())
🧑‍🔬 Dev vs Production Notes
Mode	Channel Layer	Notes
Development	InMemoryChannelLayer	Works out of the box, no Redis
Production	RedisChannelLayer	Add Redis + set in settings.py

To use Redis in production, update settings.py:

python
Copy
Edit
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}
✅ Done
This repo is part of the Realtime Trade Suite.
```
