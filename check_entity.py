from composio import Composio
import os
from dotenv import load_dotenv

load_dotenv('/c/Users/HOME_PC/Adorise Digital/.env')
api_key = 'ak_QnRj-5zTCi_pvpSCRaZ4'
composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})

# Get the connected account details to find the correct entity_id
accounts = composio.connected_accounts.list()
for acc in accounts.items:
    if hasattr(acc, 'toolkit') and acc.toolkit.slug == 'google_search_console':
        if acc.id == 'ca_TurPOdzwnudS':
            print(f"Found ca_TurPOdzwnudS: {acc}")
            if hasattr(acc, 'entity_id'):
                print(f"  entity_id: {acc.entity_id}")
            if hasattr(acc, 'user_id'):
                print(f"  user_id: {acc.user_id}")
            if hasattr(acc, 'connected_account_id'):
                print(f"  connected_account_id: {acc.connected_account_id}")
            break