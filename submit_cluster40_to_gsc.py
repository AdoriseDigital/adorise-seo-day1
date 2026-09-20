#!/usr/bin/env python3
"""
Submit new cluster40 URLs to Google Search Console via Composio SDK
Uses the active GSC connection
"""
import os
import json
from datetime import datetime
from composio import Composio

api_key = "ak_QnRj-5zTCi_pvpSCRaZ4"
composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})

# New cluster40 URLs to submit
new_urls = [
    "https://adorisedigital.github.io/adorise-seo-day1/cluster40/lead-generation-ai-cold-outreach.html",
    "https://adorisedigital.github.io/adorise-seo-day1/cluster40/ai-automation-finance-operations.html",
    "https://adorisedigital.github.io/adorise-seo-day1/cluster40/small-business-ai-inventory-management.html",
    "https://adorisedigital.github.io/adorise-seo-day1/cluster40/productivity-ai-email-management.html",
    "https://adorisedigital.github.io/adorise-seo-day1/cluster40/lead-generation-ai-linkedin-automation.html",
    "https://adorisedigital.github.io/adorise-seo-day1/cluster40/ai-automation-hr-recruitment.html",
    "https://adorisedigital.github.io/adorise-seo-day1/cluster40/small-business-ai-financial-planning.html",
    "https://adorisedigital.github.io/adorise-seo-day1/cluster40/productivity-ai-task-automation.html",
    "https://adorisedigital.github.io/adorise-seo-day1/cluster40/lead-generation-ai-webinar-funnels.html",
    "https://adorisedigital.github.io/adorise-seo-day1/cluster40/ai-automation-customer-success.html",
]

# Get connected accounts
accounts = composio.connected_accounts.list()

# Find GSC connection - look for active/connected ones
gsc_account = None
for acc in accounts.items:
    if hasattr(acc, 'toolkit') and acc.toolkit.slug == 'google_search_console':
        if hasattr(acc, 'status') and acc.status in ['ACTIVE', 'CONNECTED']:
            gsc_account = acc
            break

# If no active, try any GSC account
if not gsc_account:
    for acc in accounts.items:
        if hasattr(acc, 'toolkit') and acc.toolkit.slug == 'google_search_console':
            gsc_account = acc
            break

print(f"Using account: {gsc_account}")

if not gsc_account:
    print("ERROR: No Google Search Console connection found!")
    print("\n=== ACTION REQUIRED ===")
    print("Visit this URL to complete OAuth:")
    print("https://connect.composio.dev/link/lk_GvhST6eMKGVK")
    print("After completing OAuth, wait a moment and re-run this script.")
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
        "cluster": "cluster40",
        "urls_submitted": len(new_urls),
        "results": results
    }, f, indent=2)

print(f"\n\nResults saved to: {log_file}")
print(f"Total submitted: {len([r for r in results if r['status'] == 'success'])}")
print(f"Errors: {len([r for r in results if r['status'] == 'error'])}")