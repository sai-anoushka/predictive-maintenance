import requests
import time
import random

url = "http://127.0.0.1:8000/ingest"
for i in range(10):
    data = {
        "timestamp": f"2026-02-15T14:51:{i:02d}",
        "vibration": round(random.uniform(1.0, 10.0), 2),
        "temp": round(random.uniform(30.0, 50.0), 2)
    }
    response = requests.post(url, json=data)
    print(response.json())
    time.sleep(1)  # Delay to simulate IoT stream