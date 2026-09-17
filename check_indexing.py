from composio import Composio
import os
from dotenv import load_dotenv
import json

load_dotenv('/c/Users/HOME_PC/Adorise Digital/.env')
api_key = 'ak_QnRj-5zTCi_pvpSCRaZ4'
composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})

# Get all URLs from sitemap
import requests
sitemap_url = "https://adorisedigital.github.io/adorise-seo-day1/sitemap.xml"
response = requests.get(sitemap_url)
from xml.etree import ElementTree as ET
root = ET.fromstring(response.content)
urls = []
for url_elem in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
    loc = url_elem.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
    if loc is not None:
        urls.append(loc.text)

print(f"Total URLs in sitemap: {len(urls)}")

# Inspect first 10 URLs to see indexing status
indexed_count = 0
unindexed_urls = []
for i, url in enumerate(urls[:10]):
    result = composio.tools.execute(
        slug='GOOGLE_SEARCH_CONSOLE_INSPECT_URL',
        arguments={'site_url': 'https://adorisedigital.github.io/adorise-seo-day1/', 'inspection_url': url},
        connected_account_id='ca_TurPOdzwnudS',
        user_id='pg-test-98e07661-0afd-4a0f-bd38-d7d286d8e020'
    )
    if result.get('successful'):
        verdict = result['data']['inspectionResult']['indexStatusResult']['verdict']
        coverage = result['data']['inspectionResult']['indexStatusResult'].get('coverageState', '')
        print(f"URL {i+1}: {verdict} - {coverage[:80]}")
        if verdict != 'NEUTRAL' and 'unknown' not in coverage.lower():
            indexed_count += 1
        else:
            unindexed_urls.append(url)
    else:
        print(f"URL {i+1}: ERROR - {result.get('error')}")

print(f"\nSample results: {indexed_count}/10 indexed")
print(f"Unindexed URLs found: {len(unindexed_urls)}")