import requests
from django.utils import timezone
from copier.models import CopiedTrade, LeaderWallet

HELIUS_API_KEY = "YOUR_HELIUS_API_KEY"
BASE_URL = "https://mainnet.helius.xyz/v0/addresses"

def fetch_and_store_trades():
    leaders = LeaderWallet.objects.filter(is_active=True)
    
    for leader in leaders:
        url = f"{BASE_URL}/{leader.address}/transactions?api-key={HELIUS_API_KEY}&limit=5"
        try:
            response = requests.get(url)
            response.raise_for_status()
            transactions = response.json()

            for tx in transactions:
                signature = tx.get("signature")
                if CopiedTrade.objects.filter(signature=signature).exists():
                    continue  # Skip if already stored

                token_in = tx.get("nativeTransfers", [{}])[0].get("mint") or "SOL"
                amount = tx.get("nativeTransfers", [{}])[0].get("amount", 0)

                CopiedTrade.objects.create(
                    leader=leader,
                    signature=signature,
                    token=token_in,
                    amount=amount,
                    timestamp=timezone.now(),  # You can parse real timestamp from tx too
                    copied=False
                )
        except Exception as e:
            print(f"Error fetching transactions for {leader.address}: {e}")
