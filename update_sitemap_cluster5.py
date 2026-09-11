#!/usr/bin/env python3
import os
from datetime import datetime

# Read current sitemap
sitemap_path = r"C:\Users\HOME_PC\adorise-seo-day1\sitemap.xml"
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

# New pages to add (cluster5 pages)
new_pages = [
    "ai-lead-generation-tools-small-business.html",
    "small-business-marketing-automation-guide.html",
    "ai-powered-crm-small-business.html",
    "productivity-software-comparison-2024.html",
    "ai-sales-automation-strategies.html",
    "lead-magnet-creation-automation.html",
    "small-business-workflow-automation-examples.html",
    "ai-content-marketing-strategy.html",
    "conversion-rate-optimization-automation.html",
    "business-intelligence-tools-small-business.html"
]

today = datetime.now().strftime("%Y-%m-%d")

# Generate new URL entries
new_urls = []
for page in new_pages:
    new_urls.append(f'''    <url>
        <loc>https://adorisedigital.github.io/adorise-seo-day1/cluster5/{page}</loc>
        <lastmod>{today}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>''')

# Insert before closing </urlset>
new_urls_block = "\n".join(new_urls)
insert_marker = "</urlset>"
new_sitemap = sitemap_content.replace(insert_marker, f"    <!-- Cluster 5: New SEO Pages ({today}) -->\n{new_urls_block}\n</urlset>")

# Write updated sitemap
with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(new_sitemap)

print(f"Added {len(new_pages)} new URLs to sitemap.xml")
print(f"Date: {today}")