from composio import Composio
import os
from dotenv import load_dotenv

load_dotenv('/c/Users/HOME_PC/Adorise Digital/.env')
api_key = 'ak_QnRj-5zTCi_pvpSCRaZ4'
composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})

# Execute GSC LIST_SITES using the active connection
from composio import ComposioToolSet
toolset = ComposioToolSet(api_key=api_key)
result = toolset.execute_action(
    action='GOOGLE_SEARCH_CONSOLE_LIST_SITES',
    params={},
    connected_account_id='ca_TurPOdzwnudS'
)
print(result)