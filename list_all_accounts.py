from composio import Composio
import os
from dotenv import load_dotenv

load_dotenv('/c/Users/HOME_PC/Adorise Digital/.env')
api_key = 'ak_QnRj-5zTCi_pvpSCRaZ4'
composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})

# Get ALL connected accounts for ALL toolkits
accounts = composio.connected_accounts.list()
for acc in accounts.items:
    if hasattr(acc, 'toolkit'):
        print(f"ID: {acc.id}, Toolkit: {acc.toolkit.slug}, Status: {acc.status}, user_id: {acc.user_id}")
    else:
        print(f"ID: {acc.id}, Toolkit: None, Status: {acc.status}, user_id: {getattr(acc, 'user_id', 'N/A')}")