import requests
import os

OLLAMA_SERVER = os.getenv("OLLAMA_SERVER", "http://167.71.212.60:111")
OLLAMA_API_URL = f"{OLLAMA_SERVER}/api/generate"

def call_ollama(prompt: str):
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry

    session = requests.Session()
    retry_strategy = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["HEAD", "GET", "OPTIONS", "POST"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy, pool_connections=100, pool_maxsize=100)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    headers = {
        'Connection': 'keep-alive',
        'Keep-Alive': 'timeout=600, max=1000',
        'Content-Type': 'application/json'
    }

    response = session.post(
        OLLAMA_API_URL,
        json={
            "model": "gemma2:9b",
            "prompt": prompt,
            "stream": False,
            "temperature": 0.6
        },
        headers=headers,
        timeout=None
    )
    response.raise_for_status()
    return response.json()
