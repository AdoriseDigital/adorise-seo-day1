from composio import Composio
import os
from dotenv import load_dotenv
load_dotenv('/c/Users/HOME_PC/Adorise Digital/.env')
api_key = os.getenv('COMPOSIO_API_KEY')
if api_key and api_key.startswith('ghp_'):
    api_key = "ak_QnRj-5zTCi_pvpSCRaZ4"
composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})

# Get all auth configs
auth_configs = composio.auth_configs.list()
print('All Auth configs:')
for ac in auth_configs:
    print(f'  ID: {ac.id}, Name: {ac.name}, Toolkit: {getattr(ac, "toolkit", None)}')