from composio import Composio
import os
from dotenv import load_dotenv

load_dotenv('/c/Users/HOME_PC/Adorise Digital/.env')
api_key = 'ak_QnRj-5zTCi_pvpSCRaZ4'
composio = Composio(api_key=api_key)

# Try to link connection - this is the new way
print('\nLinking GSC connection...')
conn = composio.connected_accounts.link(
    auth_config_id='ac_upBd_Ir-ZlQy',
    user_id='hermes_user'
)
print(f'Connection linked: {conn}')
print(f'Redirect URL: {conn.redirect_url}')