#!/usr/bin/env python3
"""
Create a new Google Search Console connection via Composio using the link method
"""
from composio import Composio

api_key = "ak_QnRj-5zTCi_pvpSCRaZ4"
composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})

# Use the first GSC auth config
auth_config_id = "ac_upBd_Ir-ZlQy"

# Create new connection via link endpoint
connection = composio.connected_accounts.link(
    user_id="hermes_user",
    auth_config_id=auth_config_id
)

print(f"Connection ID: {connection.id}")
print(f"Connection Status: {connection.status}")
if hasattr(connection, 'redirect_url'):
    print(f"Redirect URL: {connection.redirect_url}")
if hasattr(connection, 'link'):
    print(f"Link: {connection.link}")

print(f"\n=== ACTION REQUIRED ===")
if hasattr(connection, 'redirect_url'):
    print(f"Visit this URL to complete OAuth authorization:")
    print(f"{connection.redirect_url}")
elif hasattr(connection, 'link'):
    print(f"Visit this URL to complete OAuth authorization:")
    print(f"{connection.link}")
print(f"\nAfter completing OAuth, wait a moment and run the check_gsc_accounts.py script to verify.")