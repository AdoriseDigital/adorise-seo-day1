from dotenv import load_dotenv
import os
from composio import Composio

load_dotenv('/c/Users/HOME_PC/Adorise Digital/.env')
api_key = os.getenv('COMPOSIO_API_KEY')
if api_key and api_key.startswith('ghp_'):
    api_key = 'ak_QnRj-5zTCi_pvpSCRaZ4'

composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})
accounts = composio.connected_accounts.list()

for acc in accounts.items:
    print(f'ID: {acc.id}')
    print(f'  Toolkit: {getattr(acc, "toolkit", None)}')
    if hasattr(acc, 'toolkit') and acc.toolkit:
        print(f'  Toolkit slug: {acc.toolkit.slug}')
    print(f'  Status: {getattr(acc, "status", "N/A")}')
    print(f'  Name: {getattr(acc, "name", "N/A")}')
    print(f'  Created: {getattr(acc, "created_at", "N/A")}')
    print()