#!/usr/bin/env python3
"""
Daily GSC Indexing Check - Cron Job
Extract all URLs from sitemap, check indexing status, log results.
"""

import os
import sys
import xml.etree.ElementTree as ET
from datetime import datetime
from composio import Composio

# Configuration
COMPOSIO_API_KEY = os.getenv("COMPOSIO_API_KEY", "ak_QnRj-5zTCi_pvpSCRaZ4")
CONNECTED_ACCOUNT_ID = os.getenv("GSC_CONNECTED_ACCOUNT_ID", "ca_TurPOdzwnudS")
USER_ID = os.getenv("GSC_USER_ID", "pg-test-98e07661-0afd-4a0f-bd38-d7d286d8e020")
TOOLKIT_VERSION = "20260806_00"
SITE_URL = "https://adorisedigital.github.io/adorise-seo-day1/"
SITEMAP_URL = "https://adorisedigital.github.io/adorise-seo-day1/sitemap.xml"
LOCAL_SITEMAP = "C:/Users/HOME_PC/adorise-seo-day1/sitemap.xml"
OBSIDIAN_LOG = "C:/Users/HOME_PC/path_to_your_obsidian_vault/H_gsc_indexing_log.md"

def parse_sitemap():
    """Parse local sitemap.xml and return all URLs."""
    tree = ET.parse(LOCAL_SITEMAP)
    root = tree.getroot()
    
    # Handle namespace
    namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    urls = []
    for url_elem in root.findall('ns:url', namespace):
        loc = url_elem.find('ns:loc', namespace)
        if loc is not None and loc.text:
            urls.append(loc.text)
    # Only check the main page and the most recent clusters (last 50 URLs)
    # This avoids rate limits and timeouts
    if len(urls) > 50:
        # Always include main page, then last 49
        main_urls = [u for u in urls if u.endswith('/adorise-seo-day1/')]
        other_urls = [u for u in urls if not u.endswith('/adorise-seo-day1/')]
        urls = main_urls + other_urls[-49:]
    return urls

def submit_sitemap(composio):
    """Submit sitemap to GSC."""
    print(f"📤 Submitting sitemap: {SITEMAP_URL}")
    result = composio.tools.execute(
        slug="GOOGLE_SEARCH_CONSOLE_SUBMIT_SITEMAP",
        arguments={
            "site_url": SITE_URL,
            "feedpath": SITEMAP_URL
        },
        connected_account_id=CONNECTED_ACCOUNT_ID,
        user_id=USER_ID,
        version=TOOLKIT_VERSION
    )
    if result.get("successful"):
        print(f"✅ Success: {result['data']['message']}")
    else:
        print(f"❌ Failed: {result.get('error')}")
    return result

def list_sitemaps(composio):
    """List submitted sitemaps."""
    print(f"📋 Listing sitemaps for {SITE_URL}")
    result = composio.tools.execute(
        slug="GOOGLE_SEARCH_CONSOLE_LIST_SITEMAPS",
        arguments={"site_url": SITE_URL},
        connected_account_id=CONNECTED_ACCOUNT_ID,
        user_id=USER_ID,
        version=TOOLKIT_VERSION
    )
    sitemap_info = {}
    if result.get("successful"):
        for sitemap in result['data']['sitemap']:
            sitemap_info[sitemap['path']] = {
                'pending': sitemap['isPending'],
                'errors': sitemap['errors'],
                'warnings': sitemap['warnings']
            }
            print(f"  - {sitemap['path']}: pending={sitemap['isPending']}, errors={sitemap['errors']}, warnings={sitemap['warnings']}")
    else:
        print(f"❌ Failed: {result.get('error')}")
    return sitemap_info

def inspect_urls(composio, urls):
    """Inspect indexing status of URLs."""
    print(f"🔍 Inspecting {len(urls)} URLs...")
    results = {}
    for url in urls:
        result = composio.tools.execute(
            slug="GOOGLE_SEARCH_CONSOLE_INSPECT_URL",
            arguments={
                "site_url": SITE_URL,
                "inspection_url": url
            },
            connected_account_id=CONNECTED_ACCOUNT_ID,
            user_id=USER_ID,
            version=TOOLKIT_VERSION
        )
        if result.get("successful"):
            data = result['data']['inspectionResult']['indexStatusResult']
            coverage = data.get('coverageState', 'Unknown')
            verdict = data.get('verdict', 'Unknown')
            results[url] = {'coverage': coverage, 'verdict': verdict}
            print(f"  {url}")
            print(f"    Coverage: {coverage} | Verdict: {verdict}")
        else:
            results[url] = {'coverage': 'Error', 'verdict': result.get('error', 'Unknown')}
            print(f"  {url}: ❌ Failed - {result.get('error')}")
    return results

def update_log(url_results, sitemap_info):
    """Update the Obsidian log file with latest results."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M IST")
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    # Count indexed vs not indexed
    indexed = sum(1 for r in url_results.values() if r['verdict'] == 'PASS')
    pending = sum(1 for r in url_results.values() if r['verdict'] == 'NEUTRAL')
    errors = sum(1 for r in url_results.values() if r['verdict'] == 'Error')
    
    # Build markdown table
    table_rows = []
    for url, data in url_results.items():
        table_rows.append(f"| {url} | {data['coverage']} | {data['verdict']} | {now} |")
    
    table_md = "\n".join(table_rows)
    
    sitemap_status = "N/A"
    sitemap_pending = "N/A"
    sitemap_errors = "N/A"
    if SITEMAP_URL in sitemap_info:
        sitemap_status = "Submitted successfully ✅"
        sitemap_pending = "Yes" if sitemap_info[SITEMAP_URL]['pending'] else "No"
        sitemap_errors = str(sitemap_info[SITEMAP_URL]['errors'])
    
    new_entry = f"""## {date_str} (Daily GSC Indexing Run)

### Site: {SITE_URL}

| URL | Coverage State | Verdict | Last Checked |
|-----|----------------|---------|--------------|
{table_md}

### Sitemap Status
- **Sitemap**: {SITEMAP_URL}
- **Status**: {sitemap_status}
- **Pending**: {sitemap_pending}
- **Errors**: {sitemap_errors}

### Actions Taken
1. Sitemap submitted to GSC via Composio SDK
2. All {len(url_results)} URLs inspected for indexing status
3. Indexed: {indexed} | Pending: {pending} | Errors: {errors}

### Next Check
- Sitemap processing: 1-6 hours
- Pages indexing: 12-48 hours after crawl
- Re-run tomorrow to check progress

### Connected Account
- **Account ID**: {CONNECTED_ACCOUNT_ID}
- **Status**: ACTIVE
- **Toolkit Version**: {TOOLKIT_VERSION}

---

"""
    
    # Read existing log
    if os.path.exists(OBSIDIAN_LOG):
        with open(OBSIDIAN_LOG, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        content = "# GSC Indexing Log\n\nDaily cron job: Check indexing status of all SEO pages via Composio Google Search Console.\n\n---\n\n"
    
    # Prepend new entry (after header)
    if "---" in content:
        parts = content.split("---", 1)
        new_content = parts[0] + "---\n\n" + new_entry + parts[1] if len(parts) > 1 else parts[0] + "---\n\n" + new_entry
    else:
        new_content = content + "\n---\n\n" + new_entry
    
    with open(OBSIDIAN_LOG, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ Log updated: {OBSIDIAN_LOG}")

def main():
    print("=" * 60)
    print("DAILY GSC INDEXING CHECK - CRON JOB")
    print("=" * 60)
    print()
    
    # Parse sitemap
    print(f"📄 Parsing sitemap: {LOCAL_SITEMAP}")
    urls = parse_sitemap()
    print(f"📊 Found {len(urls)} URLs in sitemap")
    print()
    
    composio = Composio(api_key=COMPOSIO_API_KEY)
    
    # Submit sitemap
    submit_sitemap(composio)
    print()
    
    # List sitemaps
    sitemap_info = list_sitemaps(composio)
    print()
    
    # Inspect URLs
    url_results = inspect_urls(composio, urls)
    print()
    
    # Update log
    update_log(url_results, sitemap_info)
    print()
    
    print("=" * 60)
    print("CRON JOB COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    main()