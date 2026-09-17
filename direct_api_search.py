import requests
import os
from dotenv import load_dotenv

load_dotenv('/c/Users/HOME_PC/Adorise Digital/.env')
api_key = 'ak_QnRj-5zTCi_pvpSCRaZ4'

# Try to search for connected accounts via direct API call
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# Search for all connected accounts
response = requests.get(
    'https://backend.composio.dev/api/v3.1/connected_accounts',
    headers=headers
)
print(response.status_code)
print(response.json())