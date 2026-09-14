from composio import Composio
from dotenv import load_dotenv
import os

load_dotenv('/c/Users/HOME_PC/Adorise Digital/.env')
api_key = os.getenv('COMPOSIO_API_KEY')
print('Key starts with:', api_key[:10] if api_key else 'None')

composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})
# Test listing tools
tools = composio.tools.get(slugs=['google_search_console_inspect_url'])
print(tools)