import requests
import os
from dotenv import load_dotenv

load_dotenv('/c/Users/HOME_PC/Adorise Digital/.env')
api_key = 'ak_QnRj-5zTCi_pvpSCRaZ4'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# Search through all pages for ca_TurPOdzwnudS
cursor = None
found = False
page = 1
while True:
    params = {}
    if cursor:
        params['cursor'] = cursor
    
    response = requests.get(
        'https://backend.composio.dev/api/v3.1/connected_accounts',
        headers=headers,
        params=params
    )
    data = response.json()
    
    for item in data['items']:
        if 'TurPO' in item['id']:
            print(f'Found: {item}')
            found = True
            break
    
    if found:
        break
        
    if not data.get('next_cursor'):
        break
    cursor = data['next_cursor']
    page += 1

if not found:
    print('ca_TurPOdzwnudS not found in any page')