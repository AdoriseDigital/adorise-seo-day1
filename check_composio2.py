from composio import Composio
import os
from dotenv import load_dotenv

load_dotenv('/c/Users/HOME_PC/Adorise Digital/.env')
api_key = 'ak_QnRj-5zTCi_pvpSCRaZ4'
composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})

# Check what's available for executing actions
print("Composio client:", dir(composio))
print("Composio.core:", dir(composio.core) if hasattr(composio, 'core') else 'No core')
print("Composio.sdk:", dir(composio.sdk) if hasattr(composio, 'sdk') else 'No sdk')