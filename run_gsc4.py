from composio import Composio
import os
from dotenv import load_dotenv

load_dotenv('/c/Users/HOME_PC/Adorise Digital/.env')
api_key = 'ak_QnRj-5zTCi_pvpSCRaZ4'
composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})

# Execute GSC LIST_SITES using the tools.execute method with user_id
result = composio.tools.execute(
    slug='GOOGLE_SEARCH_CONSOLE_LIST_SITES',
    arguments={},
    connected_account_id='ca_TurPOdzwnudS',
    user_id='hermes_user'
)
print(result)