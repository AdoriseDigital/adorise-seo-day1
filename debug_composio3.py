from composio import Composio
api_key = 'ak_QnRj-5zTCi_pvpSCRaZ4'
composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})
# List auth configs
auth_configs = composio.auth_configs.list()
for ac in auth_configs.items:
    print(f'ID: {ac.id}, Name: {ac.name}, Toolkit: {ac.toolkit.slug if hasattr(ac, "toolkit") else "N/A"}')