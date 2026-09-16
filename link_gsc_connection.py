import os
from dotenv import load_dotenv
from composio import Composio

load_dotenv('/c/Users/HOME_PC/Adorise Digital/.env')
api_key = os.getenv('COMPOSIO_API_KEY')
if api_key and api_key.startswith('ghp_'):
    api_key = 'ak_QnRj-5zTCi_pvpSCRaZ4'

composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})

# Get auth configs for GSC
auth_configs = composio.auth_configs.list()
for ac in auth_configs.items:
    if ac.toolkit and ac.toolkit.slug == 'google_search_console':
        print(f'Auth Config ID: {ac.id}')
        print(f'  Auth Scheme: {ac.auth_scheme}')
        print(f'  Is Composio Managed: {ac.is_composio_managed}')

# Use the link endpoint for Composio-managed OAuth
gsc_auth_config = None
for ac in auth_configs.items:
    if ac.toolkit and ac.toolkit.slug == 'google_search_console':
        gsc_auth_config = ac
        break

if gsc_auth_config:
    print(f"\nLinking connection with auth_config_id: {gsc_auth_config.id}")
    connection = composio.connected_accounts.link(
        auth_config_id=gsc_auth_config.id,
        user_id="hermes_user"
    )
    print(f"Connection link created: {connection}")
    if hasattr(connection, 'redirect_url'):
        print(f"Redirect URL: {connection.redirect_url}")
    elif hasattr(connection, 'url'):
        print(f"URL: {connection.url}")