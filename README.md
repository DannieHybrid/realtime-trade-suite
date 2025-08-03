# 🧠 Realtime Trade Suite

A monorepo of 6 backend-focused projects purpose-built for real-time Solana-based social and copy trading.

## 📦 Projects

| Project | Folder | Description |
|--------|--------|-------------|
| ✅ Real-time Token Feed | `token-feed-api` | Django WebSocket API emitting simulated SOL token prices |
| ✅ Copy Trading Engine | `copy-trading-engine` | REST API to mirror trades from selected Solana wallets |
| ✅ LLM Trade Insights | `llm-trade-insights` | Uses LLMs to summarize and generate trade strategies |
| ✅ Solana Trading Bot CLI | `solana-trading-cli` | CLI bot for executing real-time trading strategies |
| ✅ Trading Task Scheduler | `trading-task-scheduler` | Celery-based scheduler for background trading tasks |
| ✅ Feed Stress Tester | `feed-stress-tester` | Load tester simulating thousands of feed requests |

---

## 🚀 Getting Started

Each project folder includes its own README with setup and usage.

To run a project:

```bash
cd token-feed-api
python manage.py runserver
# or use daphne:
daphne -b 127.0.0.1 -p 8000 tokenfeed.asgi:application
To simulate trading:

bash
Copy
Edit
cd solana-trading-cli
python trade.py --strategy "momentum"
To load test:

bash
Copy
Edit
cd feed-stress-tester
locust -f locustfile.py
🧪 WebSocket Example (Token Feed)
Quick Python WebSocket test client:

python
Copy
Edit
# ws-client.py
import websocket
ws = websocket.WebSocket()
ws.connect("ws://127.0.0.1:8000/ws/feed/")
print(ws.recv())
🔧 Stack Summary
Backend: Django, FastAPI

Real-Time: Django Channels, ASGI, WebSockets

Infra: Redis, Celery, Docker, MongoDB

Solana APIs: Jupiter Aggregator, Helius, Phantom

LLMs: OpenAI/Groq for trade insights

📁 Folder Structure
bash
Copy
Edit
realtime-trade-suite/
├── token-feed-api/
├── copy-trading-engine/
├── llm-trade-insights/
├── solana-trading-cli/
├── trading-task-scheduler/
├── feed-stress-tester/
├── docker-compose.yml
├── .env
└── README.md  ← You're here
✅ Project Status
Project	Status
Token Feed API	✅ Complete
Copy Trading Engine	✅ Complete
LLM Trade Insights	✅ Complete
Solana CLI Bot	✅ Complete
Task Scheduler	✅ Complete
Feed Stress Tester	✅ Complete

🔐 Environment
Set environment variables via .env in root. Redis, API keys, Mongo, etc. are shared across services via Docker Compose.

🧭 License
MIT License. Built for professional interviews, Web3 backend demos, and fast prototyping.
