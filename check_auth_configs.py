#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from composio import Composio

load_dotenv('/c/Users/HOME_PC/Adorise Digital/.env')
api_key = os.getenv('COMPOSIO_API_KEY')
if api_key and api_key.startswith('ghp_'):
    api_key = 'ak_QnRj-5zTCi_pvpSCRaZ4'

composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})

# Check auth_configs
auth_configs = composio.auth_configs.list()
print(f"Auth configs count: {len(auth_configs.items) if hasattr(auth_configs, 'items') else 'N/A'}")
if hasattr(auth_configs, 'items'):
    for ac in auth_configs.items:
        print(f'  ID: {ac.id}, Slug: {ac.toolkit.slug if hasattr(ac, "toolkit") else "N/A"}, Name: {ac.name if hasattr(ac, "name") else "N/A"}')