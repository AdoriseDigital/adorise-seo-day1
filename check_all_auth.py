from composio import Composio
import os
from dotenv import load_dotenv
load_dotenv('/c/Users/HOME_PC/Adorise Digital/.env')
api_key = os.getenv('COMPOSIO_API_KEY')
if api_key and api_key.startswith('ghp_'):
    api_key = "ak_QnRj-5zTCi_pvpSCRaZ4"
composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})

# Get auth configs for GSC
auth_configs = composio.auth_configs.list()
print('Auth configs:', auth_configs)
print('Type:', type(auth_configs))
if hasattr(auth_configs, 'items'):
    for ac in auth_configs.items:
        print(f'  ID: {ac.id}, Name: {ac.name}, Toolkit: {ac.toolkit.slug if hasattr(ac, "toolkit") and ac.toolkit else "N/A"}')
else:
    print('No items attribute')