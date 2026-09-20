from composio import Composio

api_key = "ak_QnRj-5zTCi_pvpSCRaZ4"
composio = Composio(api_key=api_key)

print("Connected accounts methods:")
print([m for m in dir(composio.connected_accounts) if not m.startswith('_')])

# Try to list accounts
accounts = composio.connected_accounts.list()
print(f"\nAccounts: {accounts}")