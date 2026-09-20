from composio import Composio
api_key = 'ak_QnRj-5zTCi_pvpSCRaZ4'
composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})
accounts = composio.connected_accounts.list()
for acc in accounts.items:
    if hasattr(acc, 'toolkit') and acc.toolkit.slug == 'google_search_console':
        print(f'ID: {acc.id}, Status: {acc.status}, Data: {acc.data}')