import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "copyengine.settings")
django.setup()

from copier.poll_helius import fetch_and_store_trades

if __name__ == "__main__":
    fetch_and_store_trades()
