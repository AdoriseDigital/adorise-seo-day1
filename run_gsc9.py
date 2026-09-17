from composio import Composio
import os
from dotenv import load_dotenv

load_dotenv('/c/Users/HOME_PC/Adorise Digital/.env')
api_key = 'ak_QnRj-5zTCi_pvpSCRaZ4'
composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})

# Use session to execute with account parameter
session = composio.sessions.create(user_id='hermes_user')
result = session.execute(
    tool_slug='GOOGLE_SEARCH_CONSOLE_LIST_SITES',
    arguments={},
    account='ca_fnMQbFmot-M8'
)
print(result)