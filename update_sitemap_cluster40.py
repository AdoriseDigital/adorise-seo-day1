#!/usr/bin/env python3
import os
from datetime import datetime

# Read current sitemap
sitemap_path = r"C:\Users\HOME_PC\adorise-seo-day1\sitemap.xml"
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

# New pages to add (cluster40 pages)
new_pages = [
    "lead-generation-ai-cold-outreach.html",
    "ai-automation-finance-operations.html",
    "small-business-ai-inventory-management.html",
    "productivity-ai-email-management.html",
    "lead-generation-ai-linkedin-automation.html",
    "ai-automation-hr-recruitment.html",
    "small-business-ai-financial-planning.html",
    "productivity-ai-task-automation.html",
    "lead-generation-ai-webinar-funnels.html",
    "ai-automation-customer-success.html"
]

today = datetime.now().strftime("%Y-%m-%d")

# Generate new URL entries
new_urls = []
for page in new_pages:
    new_urls.append(f'''    <url>
        <loc>https://adorisedigital.github.io/adorise-seo-day1/cluster40/{page}</loc>
        <lastmod>{today}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>''')

# Insert before closing </urlset>
new_urls_block = "\n".join(new_urls)
insert_marker = "</urlset>"
new_sitemap = sitemap_content.replace(insert_marker, f"    <!-- Cluster 40: New SEO Pages ({today}) -->\n{new_urls_block}\n</urlset>")

# Write updated sitemap
with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(new_sitemap)

print(f"Added {len(new_pages)} new URLs to sitemap.xml")
print(f"Date: {today}")