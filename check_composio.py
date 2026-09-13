import os
from dotenv import load_dotenv
from composio import Composio

# Load the correct .env file
load_dotenv("/c/Users/HOME_PC/Adorise Digital/.env")

api_key = os.getenv('COMPOSIO_API_KEY')
print(f'Using API key: {api_key[:15]}...')

composio = Composio(api_key=api_key)

# Check connected accounts
accounts = composio.connected_accounts.list()
print(f'Connected accounts: {accounts}')