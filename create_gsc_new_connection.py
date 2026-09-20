#!/usr/bin/env python3
"""Create new GSC connection via Composio"""
import os
import json
from datetime import datetime
from composio import Composio

api_key = "ak_QnRj-5zTCi_pvpSCRaZ4"
composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})

# Create new GSC connection using the auth config
print("Creating new Google Search Console connection...")
result = composio.connected_accounts.link(
    user_id="hermes_user",
    auth_config_id="ac_LcZ9t93Gu8oT",  # google_search_console-n22xrg
)

print(f"Connection result: {result}")
print(f"Redirect URL: {result.redirect_url}")

# Save the connection info
log_dir = "/c/Users/HOME_PC/adorise-seo-day1"
os.makedirs(log_dir, exist_ok=True)
log_file = f"{log_dir}/H_gsc_connection_new_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
with open(log_file, 'w') as f:
    json.dump({
        "timestamp": datetime.now().isoformat(),
        "connection": str(result),
        "redirect_url": result.redirect_url,
        "connection_id": result.id
    }, f, indent=2)

print(f"Connection info saved to: {log_file}")
print(f"\n=== ACTION REQUIRED ===")
print(f"Visit this URL to complete OAuth:")
print(f"{result.redirect_url}")
print(f"After completing OAuth, wait a moment and re-run check_accounts_detail.py")