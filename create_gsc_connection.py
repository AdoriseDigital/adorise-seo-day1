#!/usr/bin/env python3
"""
Create new GSC connection via Composio
"""
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

# Create new GSC connection
print("Creating new Google Search Console connection...")
result = composio.connected_accounts.link(
    toolkit_slug="google_search_console",
    user_id="hermes_user",
    force_new_integration=True
)

print(f"Connection result: {result}")

# Save the connection info
log_dir = "/c/Users/HOME_PC/adorise-seo-day1"
os.makedirs(log_dir, exist_ok=True)
log_file = f"{log_dir}/H_gsc_connection_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
with open(log_file, 'w') as f:
    json.dump({
        "timestamp": datetime.now().isoformat(),
        "connection": str(result)
    }, f, indent=2)

print(f"Connection info saved to: {log_file}")