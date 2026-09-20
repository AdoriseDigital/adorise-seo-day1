#!/usr/bin/env python3
from composio import Composio

api_key = "ak_QnRj-5zTCi_pvpSCRaZ4"
composio = Composio(api_key=api_key)
accounts = composio.connected_accounts.list()
for acc in accounts.items:
    if hasattr(acc, 'toolkit') and acc.toolkit and acc.toolkit.slug == 'google_search_console':
        print(f'ID: {acc.id}')
        print(f'Status: {acc.status}')
        print(f'Data status: {acc.data.get("status") if hasattr(acc, "data") and acc.data else "N/A"}')
        print('---')