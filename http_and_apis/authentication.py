import os

import requests

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

if not api_key:
    raise RuntimeError("API_KEY is missing")

header = {
    "X-API-KEY": api_key
}

response = requests.get("https://api.example.com/weather",
                        headers=header,
                        timeout=10
                        )

response.raise_for_status()
print(response.json())

