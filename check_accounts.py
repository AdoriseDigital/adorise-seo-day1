from composio import Composio
api_key = 'ak_QnRj-5zTCi_pvpSCRaZ4'
composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})
accounts = composio.connected_accounts.list()
for a in accounts.items:
    toolkit_slug = getattr(a.toolkit, 'slug', 'N/A') if hasattr(a, 'toolkit') else 'N/A'
    print(f'{toolkit_slug}: {a.id} - {getattr(a, "status", "N/A")}')