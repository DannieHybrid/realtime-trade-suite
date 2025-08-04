# main.py

import asyncio
from feed_stress.stress_tester import run_stress_test

if __name__ == "__main__":
    asyncio.run(run_stress_test(count=100))  # Adjust client count as needed
