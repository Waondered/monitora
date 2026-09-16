import httpx
import os
from dotenv import load_dotenv

load_dotenv()

GECKO_API_KEY = os.getenv("GECKO_API_KEY")
url = "https://api.geckoapi.com.br/v1/extract"
payload = {
        'target': 'amazon.com.br',
        'type': 'pdp',
        'url': 'https://www.amazon.com.br/dp/B075TGQVHT',
             }

headers = { 'Authorization': f'Bearer {GECKO_API_KEY}' }
custom_timeout = httpx.Timeout(10.0, read=15.0)


request = httpx.post( url, json=payload, headers=headers, timeout=custom_timeout )



