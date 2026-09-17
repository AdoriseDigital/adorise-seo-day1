from composio import Composio
import os
from dotenv import load_dotenv

load_dotenv('/c/Users/HOME_PC/Adorise Digital/.env')
api_key = 'ak_QnRj-5zTCi_pvpSCRaZ4'
composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})

# Get the sitemap content to see all pages - use feedpath parameter
result = composio.tools.execute(
    slug='GOOGLE_SEARCH_CONSOLE_GET_SITEMAP',
    arguments={'site_url': 'https://adorisedigital.github.io/adorise-seo-day1/', 'feedpath': 'https://adorisedigital.github.io/adorise-seo-day1/sitemap.xml'},
    connected_account_id='ca_TurPOdzwnudS',
    user_id='pg-test-98e07661-0afd-4a0f-bd38-d7d286d8e020'
)
print(result)