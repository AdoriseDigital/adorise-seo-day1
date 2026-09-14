import os
from dotenv import load_dotenv
load_dotenv('/c/Users/HOME_PC/Adorise Digital/.env')
print('COMPOSIO_API_KEY:', os.getenv('COMPOSIO_API_KEY', 'NOT SET')[:20] if os.getenv('COMPOSIO_API_KEY') else 'NOT SET')
print('GITHUB_TOKEN:', os.getenv('GITHUB_TOKEN', 'NOT SET')[:20] if os.getenv('GITHUB_TOKEN') else 'NOT SET')