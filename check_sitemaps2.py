from composio import Composio
import os
from dotenv import load_dotenv

load_dotenv('/c/Users/HOME_PC/Adorise Digital/.env')
api_key = 'ak_QnRj-5zTCi_pvpSCRaZ4'
composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})

# Check sitemaps for the github pages site
result = composio.tools.execute(
    slug='GOOGLE_SEARCH_CONSOLE_LIST_SITEMAPS',
    arguments={'site_url': 'https://adorisedigital.github.io/adorise-seo-day1/'},
    connected_account_id='ca_TurPOdzwnudS',
    user_id='pg-test-98e07661-0afd-4a0f-bd38-d7d286d8e020'
)
print(result)