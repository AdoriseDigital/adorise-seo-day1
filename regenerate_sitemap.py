#!/usr/bin/env python3
import json, os, glob
from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

BASE_URL = 'https://adorisedigital.github.io/adorise-seo-day1'
REPO_PATH = r'C:\Users\HOME_PC\adorise-seo-day1'

html_files = []
for f in glob.glob(os.path.join(REPO_PATH, '*.html')):
    html_files.append(f)
for cluster in glob.glob(os.path.join(REPO_PATH, 'cluster*')):
    if os.path.isdir(cluster):
        for f in glob.glob(os.path.join(cluster, '*.html')):
            html_files.append(f)

html_files = sorted(html_files)
print(f'Total HTML files found: {len(html_files)}')

urlset = Element('urlset', xmlns='http://www.sitemaps.org/schemas/sitemap/0.9')
for f in html_files:
    rel_path = os.path.relpath(f, REPO_PATH)
    rel_path = rel_path.replace('\\', '/')  # Normalize to forward slashes for URLs
    if rel_path == 'index.html':
        url = BASE_URL + '/'
        priority = '1.0'
    else:
        url = BASE_URL + '/' + rel_path
        priority = '0.9' if not rel_path.startswith('cluster') else '0.8'
    
    url_elem = SubElement(urlset, 'url')
    SubElement(url_elem, 'loc').text = url
    SubElement(url_elem, 'lastmod').text = datetime.now().strftime('%Y-%m-%d')
    SubElement(url_elem, 'changefreq').text = 'weekly'
    SubElement(url_elem, 'priority').text = priority

rough = tostring(urlset, 'utf-8')
reparsed = minidom.parseString(rough)
pretty = reparsed.toprettyxml(indent='  ')
lines = [line for line in pretty.split('\n') if line.strip()]
pretty = '\n'.join(lines)

sitemap_path = os.path.join(REPO_PATH, 'sitemap.xml')
with open(sitemap_path, 'w') as f:
    f.write(pretty)

print(f'Generated sitemap.xml with {len(html_files)} URLs')