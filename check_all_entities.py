from composio import Composio
import os
from dotenv import load_dotenv

load_dotenv('/c/Users/HOME_PC/Adorise Digital/.env')
api_key = 'ak_QnRj-5zTCi_pvpSCRaZ4'
composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})

# Get all connected accounts and their details
accounts = composio.connected_accounts.list()
for acc in accounts.items:
    if hasattr(acc, 'toolkit') and acc.toolkit.slug == 'google_search_console':
        print(f"ID: {acc.id}, Status: {acc.status}")
        print(f"  Has entity_id: {hasattr(acc, 'entity_id')}")
        print(f"  Has user_id: {hasattr(acc, 'user_id')}")
        if hasattr(acc, 'entity_id'):
            print(f"  entity_id: {acc.entity_id}")
        if hasattr(acc, 'user_id'):
            print(f"  user_id: {acc.user_id}")
        if hasattr(acc, '__dict__'):
            print(f"  All attrs: {acc.__dict__.keys()}")
        print()