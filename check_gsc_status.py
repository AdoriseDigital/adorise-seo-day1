#!/usr/bin/env python3
"""
Check the new GSC connection status and submit URLs when ready
"""
import os
import json
import time
from datetime import datetime
from dotenv import load_dotenv
from composio import Composio

load_dotenv("/c/Users/HOME_PC/Adorise Digital/.env")

api_key = os.getenv('COMPOSIO_API_KEY')
if api_key and api_key.startswith('ghp_'):
    api_key = "ak_QnRj-5zTCi_pvpSCRaZ4"

composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})

# Check status of the new connection
accounts = composio.connected_accounts.list()

gsc_account = None
if hasattr(accounts, 'items'):
    for acc in accounts.items:
        if hasattr(acc, 'toolkit') and acc.toolkit.slug == 'google_search_console':
            if hasattr(acc, 'id') and acc.id == 'ca_JxLOrjBzeUXI':
                gsc_account = acc
                break

print(f"Connection status: {gsc_account}")

if not gsc_account:
    print("Connection not found!")
    exit(1)

status = getattr(gsc_account, 'status', None)
print(f"Status: {status}")

if status == 'EXPIRED':
    print("Connection expired!")
    exit(1)
elif status == 'INITIALIZING':
    print("Connection still initializing - waiting for OAuth completion...")
    print("Please complete OAuth at: https://connect.composio.dev/link/lk_sdFHt3bCj_dy")
    exit(0)
elif status == 'ACTIVE':
    print("Connection is ACTIVE - ready to submit URLs!")
else:
    print(f"Unknown status: {status}")
    exit(1)