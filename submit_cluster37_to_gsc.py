#!/usr/bin/env python3
"""
Submit new cluster37 URLs to Google Search Console via Composio SDK using new active connection
"""
import os
import json
from datetime import datetime
from dotenv import load_dotenv
from composio import Composio

# Load environment
load_dotenv("/c/Users/HOME_PC/Adorise Digital/.env")

api_key = os.getenv('COMPOSIO_API_KEY')
# Use the correct developer key from .env (ak_ prefix, not ghp_)
if api_key and api_key.startswith('ghp_'):
    api_key = "ak_QnRj-5zTCi_pvpSCRaZ4"
print(f'Using API key: {api_key[:15]}...')

composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})

# New cluster37 URLs to submit
new_urls = [
    "https://adorisedigital.github.io/adorise-seo-day1/cluster37/lead-generation-ai-predictive-scoring.html",
    "https://adorisedigital.github.io/adorise-seo-day1/cluster37/ai-automation-supply-chain-optimization.html",
    "https://adorisedigital.github.io/adorise-seo-day1/cluster37/small-business-ai-marketing-attribution.html",
    "https://adorisedigital.github.io/adorise-seo-day1/cluster37/productivity-ai-document-processing.html",
    "https://adorisedigital.github.io/adorise-seo-day1/cluster37/lead-generation-ai-outbound-personalization.html",
    "https://adorisedigital.github.io/adorise-seo-day1/cluster37/ai-automation-quality-assurance.html",
    "https://adorisedigital.github.io/adorise-seo-day1/cluster37/small-business-ai-pricing-optimization.html",
    "https://adorisedigital.github.io/adorise-seo-day1/cluster37/productivity-ai-meeting-intelligence.html",
    "https://adorisedigital.github.io/adorise-seo-day1/cluster37/lead-generation-ai-referral-automation.html",
    "https://adorisedigital.github.io/adorise-seo-day1/cluster37/ai-automation-compliance-monitoring.html",
]

# Get connected accounts
accounts = composio.connected_accounts.list()
print(f"Connected accounts count: {len(accounts.items) if hasattr(accounts, 'items') else 'N/A'}")

# Find GSC connection - first non-EXPIRED one
gsc_account = None
if hasattr(accounts, 'items'):
    for acc in accounts.items:
        if hasattr(acc, 'toolkit') and acc.toolkit.slug == 'google_search_console':
            if hasattr(acc, 'status') and acc.status != 'EXPIRED':
                gsc_account = acc
                break

print(f"Using account: {gsc_account}")

if not gsc_account:
    print("ERROR: No active Google Search Console connection found!")
    print("\n=== ACTION REQUIRED ===")
    print("Visit this URL to connect GSC:")
    print("https://connect.composio.dev/link/lk_m1aMXZLJlgkd")
    print("After completing OAuth, re-run this script.")
    exit(1)

# Submit each URL to GSC for indexing
results = []

for url in new_urls:
    print(f"\nSubmitting to GSC: {url}")
    try:
        result = composio.tools.execute(
            slug="google_search_console_inspect_url",
            arguments={
                "url": url,
                "site_url": "https://adorisedigital.github.io/adorise-seo-day1/"
            },
            connected_account_id=gsc_account.id,
            user_id="hermes_user"
        )
        results.append({"url": url, "status": "success", "result": str(result)})
        print(f"  ✓ Submitted successfully")
    except Exception as e:
        results.append({"url": url, "status": "error", "error": str(e)})
        print(f"  ✗ Error: {e}")

# Save results
log_dir = "/c/Users/HOME_PC/adorise-seo-day1"
os.makedirs(log_dir, exist_ok=True)
log_file = f"{log_dir}/H_gsc_submission_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
with open(log_file, 'w') as f:
    json.dump({
        "timestamp": datetime.now().isoformat(),
        "cluster": "cluster37",
        "urls_submitted": len(new_urls),
        "results": results
    }, f, indent=2)

print(f"\n\nResults saved to: {log_file}")
print(f"Total submitted: {len([r for r in results if r['status'] == 'success'])}")
print(f"Errors: {len([r for r in results if r['status'] == 'error'])}")