from composio import Composio

api_key = "ak_QnRj-5zTCi_pvpSCRaZ4"
composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})

accounts = composio.connected_accounts.list()
print(f"Total accounts: {len(accounts.items)}")

for acc in accounts.items:
    print(f"\nID: {acc.id}")
    print(f"  Toolkit: {acc.toolkit.slug if hasattr(acc, 'toolkit') else 'N/A'}")
    print(f"  Status: {acc.status}")
    print(f"  Account: {acc.account_name if hasattr(acc, 'account_name') else 'N/A'}")
    print(f"  Created: {acc.created_at}")
    if hasattr(acc, 'state') and acc.state:
        val = acc.state.val if hasattr(acc.state, 'val') else None
        if val and hasattr(val, 'status'):
            print(f"  State status: {val.status}")