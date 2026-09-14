from composio import Composio
import os
import requests
from dotenv import load_dotenv
load_dotenv('/c/Users/HOME_PC/Adorise Digital/.env')
api_key = os.getenv('COMPOSIO_API_KEY')
if api_key and api_key.startswith('ghp_'):
    api_key = "ak_QnRj-5zTCi_pvpSCRaZ4"

# Use the link endpoint as suggested
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

data = {
    'auth_config_id': 'ac_upBd_Ir-ZlQy',
    'user_id': 'hermes_user'
}

response = requests.post(
    'https://backend.composio.dev/api/v3/connected_accounts/link',
    headers=headers,
    json=data
)

print('Status:', response.status_code)
print('Response:', response.json())