from composio import Composio

c = Composio(api_key='ak_QnRj-5zTCi_pvpSCRaZ4', toolkit_versions={'google_search_console': '20260806_00'})
accounts = c.connected_accounts.list()
print(accounts)