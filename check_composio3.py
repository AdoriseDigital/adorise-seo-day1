from composio import Composio
import os
from dotenv import load_dotenv

load_dotenv('/c/Users/HOME_PC/Adorise Digital/.env')
api_key = 'ak_QnRj-5zTCi_pvpSCRaZ4'
composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})

# Check the tools attribute
print("composio.tools:", composio.tools)
print("Type:", type(composio.tools))
if hasattr(composio.tools, '__dir__'):
    print("tools dir:", dir(composio.tools))