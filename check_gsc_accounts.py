from dotenv import load_dotenv
from composio import Composio
import os
load_dotenv('/c/Users/HOME_PC/Adorise Digital/.env')
api_key = os.getenv('COMPOSIO_API_KEY')
if api_key and api_key.startswith('ghp_'):
    api_key = 'ak_QnRj-5zTCi_pvpSCRaZ4'
composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})
accounts = composio.connected_accounts.list()
print(f'Total: {len(accounts.items)}')
for acc in accounts.items:
    print(f'  ID: {acc.id}, Toolkit: {acc.toolkit.slug if hasattr(acc, "toolkit") else "N/A"}, Status: {getattr(acc, "status", "N/A")}')