#!/usr/bin/env python3
"""
Submit new cluster18 URLs to Google Search Console via Composio SDK
"""
import os
import json
from datetime import datetime
from dotenv import load_dotenv
from composio import Composio

# Load environment
load_dotenv("/c/Users/HOME_PC/Adorise Digital/.env")

api_key = os.getenv('COMPOSIO_API_KEY')
print(f'Using API key: {api_key[:15]}...')

composio = Composio(api_key=api_key)

# New cluster18 URLs to submit
new_urls = [
    "https://adorisedigital.github.io/adorise-seo-day1/cluster18/lead-generation-ai-outbound-automation.html",
    "https://adorisedigital.github.io/adorise-seo-day1/cluster18/ai-automation-lead-enrichment-data.html",
    "https://adorisedigital.github.io/adorise-seo-day1/cluster18/small-business-tools-ai-sales-automation.html",
    "https://adorisedigital.github.io/adorise-seo-day1/cluster18/productivity-software-ai-task-automation.html",
    "https://adorisedigital.github.io/adorise-seo-day1/cluster18/lead-generation-ai-content-strategy.html",
    "https://adorisedigital.github.io/adorise-seo-day1/cluster18/ai-automation-crm-workflow-automation.html",
    "https://adorisedigital.github.io/adorise-seo-day1/cluster18/small-business-lead-gen-ai-linkedin.html",
    "https://adorisedigital.github.io/adorise-seo-day1/cluster18/productivity-automation-ai-meeting-assistant.html",
    "https://adorisedigital.github.io/adorise-seo-day1/cluster18/lead-nurture-ai-behavioral-triggers.html",
    "https://adorisedigital.github.io/adorise-seo-day1/cluster18/ai-automation-scaling-revenue-operations.html",
]

# Get connected accounts
accounts = composio.connected_accounts.list()
print(f"Connected accounts: {accounts}")

# Find GSC connection
gsc_account = None
for acc in accounts:
    if 'google_search_console' in str(acc).lower() or 'gsc' in str(acc).lower():
        gsc_account = acc
        break

if not gsc_account and accounts:
    gsc_account = accounts[0]  # Use first account if no GSC specific

print(f"Using account: {gsc_account}")

# Submit each URL to GSC for indexing
# The GSC tool for URL inspection/indexing
results = []

for url in new_urls:
    print(f"\nSubmitting to GSC: {url}")
    try:
        # Use the GSC URL inspection / indexing request tool
        result = composio.tools.execute(
            slug="google_search_console_inspect_url",
            arguments={
                "url": url,
                "site_url": "https://adorisedigital.github.io/adorise-seo-day1/"
            },
            connected_account_id=gsc_account.get('id') if isinstance(gsc_account, dict) else gsc_account.id
        )
        results.append({"url": url, "status": "success", "result": result})
        print(f"  ✓ Submitted successfully")
    except Exception as e:
        results.append({"url": url, "status": "error", "error": str(e)})
        print(f"  ✗ Error: {e}")

# Save results
log_file = f"/c/Users/HOME_PC/adorise-seo-day1/H_gsc_submission_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
with open(log_file, 'w') as f:
    json.dump({
        "timestamp": datetime.now().isoformat(),
        "cluster": "cluster18",
        "urls_submitted": len(new_urls),
        "results": results
    }, f, indent=2)

print(f"\n\nResults saved to: {log_file}")
print(f"Total submitted: {len([r for r in results if r['status'] == 'success'])}")
print(f"Errors: {len([r for r in results if r['status'] == 'error'])}")