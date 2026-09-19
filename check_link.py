#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from composio import Composio

load_dotenv('/c/Users/HOME_PC/Adorise Digital/.env')
api_key = os.getenv('COMPOSIO_API_KEY')
if api_key and api_key.startswith('ghp_'):
    api_key = 'ak_QnRj-5zTCi_pvpSCRaZ4'

composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})

# Check link method
import inspect
print(inspect.signature(composio.connected_accounts.link))
print()
print(inspect.getdoc(composio.connected_accounts.link))