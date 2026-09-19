#!/usr/bin/env python3
"""Create new GSC connection via Composio"""
import os
import json
from datetime import datetime
from dotenv import load_dotenv
from composio import Composio

# Load environment
load_dotenv("/c/Users/HOME_PC/Adorise Digital/.env")

api_key = os.getenv('COMPOSIO_API_KEY')
if api_key and api_key.startswith('ghp_'):
    api_key = "ak_QnRj-5zTCi_pvpSCRaZ4"
print(f'Using API key: {api_key[:15]}...')

composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})

# Create new GSC connection using the auth config
print("Creating new Google Search Console connection...")
result = composio.connected_accounts.link(
    user_id="hermes_user",
    auth_config_id="ac_upBd_Ir-ZlQy",  # google_search_console-tifhzg
)

print(f"Connection result: {result}")
print(f"Redirect URL: {result.redirect_url}")

# Save the connection info
log_dir = "/c/Users/HOME_PC/adorise-seo-day1"
os.makedirs(log_dir, exist_ok=True)
log_file = f"{log_dir}/H_gsc_connection_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
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
print(f"After completing OAuth, wait a moment and re-run check_gsc_accounts.py")