from composio import Composio
api_key = 'ak_QnRj-5zTCi_pvpSCRaZ4'
composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})
import inspect
print(inspect.signature(composio.connected_accounts.initiate))