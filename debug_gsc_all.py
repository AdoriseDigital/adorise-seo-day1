from dotenv import load_dotenv
import os
from composio import Composio

load_dotenv('/c/Users/HOME_PC/Adorise Digital/.env')
api_key = os.getenv('COMPOSIO_API_KEY')
if api_key and api_key.startswith('ghp_'):
    api_key = 'ak_QnRj-5zTCi_pvpSCRaZ4'

composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})
accounts = composio.connected_accounts.list()

print(f"Total accounts: {len(accounts.items)}")
for acc in accounts.items:
    if hasattr(acc, 'toolkit'):
        print(f'ID: {acc.id}, Status: {acc.status}, Toolkit: {acc.toolkit.slug}')
    else:
        print(f'ID: {acc.id}, Status: {acc.status}, Toolkit: N/A')