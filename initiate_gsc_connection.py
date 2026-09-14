from composio import Composio
import os
from dotenv import load_dotenv
load_dotenv('/c/Users/HOME_PC/Adorise Digital/.env')
api_key = os.getenv('COMPOSIO_API_KEY')
if api_key and api_key.startswith('ghp_'):
    api_key = "ak_QnRj-5zTCi_pvpSCRaZ4"
composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})

# Try to initiate a new connection for GSC using the auth config with most connections
# ac_upBd_Ir-ZlQy has 19 connections, let's try that one
try:
    connection = composio.connected_accounts.initiate(
        auth_config_id='ac_upBd_Ir-ZlQy',
        user_id='hermes_user'
    )
    print('Connection initiated:', connection)
except Exception as e:
    print('Error:', e)