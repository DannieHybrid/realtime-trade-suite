# insights/llm.py

import os
import openai  # or groq

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_trades(trades: list[str]) -> str:
    prompt = f"""
    Analyze and summarize the following user trades in simple terms:
    {chr(10).join(trades)}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "mixtral-8x7b" if using Groq
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response.choices[0].message["content"].strip()
