#!/usr/bin/env python3
import os
from datetime import datetime

# Read current sitemap
sitemap_path = r"C:\Users\HOME_PC\adorise-seo-day1\sitemap.xml"
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

# New pages to add (cluster8 pages)
new_pages = [
    "lead-generation-ai-automation-strategies-small-business.html",
    "ai-automation-tools-comparison-2024-productivity-software.html",
    "small-business-tools-stack-ai-integrated-workflow.html",
    "productivity-software-ai-automation-guide-non-technical.html",
    "lead-generation-funnel-optimization-ai-powered.html",
    "ai-workflow-automation-implementation-checklist.html",
    "small-business-process-automation-ai-tools.html",
    "automated-lead-scoring-qualification-ai-system.html",
    "business-process-automation-ai-roadmap-2024.html",
    "ai-productivity-tools-comparison-small-business-2024.html"
]

today = datetime.now().strftime("%Y-%m-%d")

# Generate new URL entries
new_urls = []
for page in new_pages:
    new_urls.append(f'''    <url>
        <loc>https://adorisedigital.github.io/adorise-seo-day1/cluster8/{page}</loc>
        <lastmod>{today}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>''')

# Insert before closing </urlset>
new_urls_block = "\n".join(new_urls)
insert_marker = "</urlset>"
new_sitemap = sitemap_content.replace(insert_marker, f"    <!-- Cluster 8: New SEO Pages ({today}) -->\n{new_urls_block}\n</urlset>")

# Write updated sitemap
with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(new_sitemap)

print(f"Added {len(new_pages)} new URLs to sitemap.xml")
print(f"Date: {today}")