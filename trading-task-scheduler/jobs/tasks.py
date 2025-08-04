from celery import shared_task

@shared_task
def execute_trade(symbol: str, side: str, amount: float):
    print(f"📈 Executing trade: {side} {amount} {symbol}")
    # Simulated price fetch and trade
    import random
    price = round(random.uniform(20, 100), 2)
    print(f"✅ Trade executed at price: ${price}")
