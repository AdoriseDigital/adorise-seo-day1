#!/usr/bin/env python3
from composio import Composio
import time

api_key = "ak_QnRj-5zTCi_pvpSCRaZ4"
composio = Composio(api_key=api_key)
result = composio.connected_accounts.link(user_id="hermes_user", auth_config_id="ac_upBd_Ir-ZlQy")

print("=" * 60)
print("ACTION REQUIRED: Complete OAuth in browser")
print("=" * 60)
print(f"Visit this URL: {result.redirect_url}")
print("=" * 60)
print("Waiting for connection to complete (max 120 seconds)...")
print("Complete the OAuth flow in your browser now.")

try:
    connected = result.wait_for_connection(timeout=120)
    print("\n✓ Connection established!")
    print(f"Account ID: {connected.id}")
    print(f"Status: {connected.status}")
except Exception as e:
    print(f"\n✗ Error/Timeout: {e}")
    print("You can manually complete the OAuth and re-run the submission script.")