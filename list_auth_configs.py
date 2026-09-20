from composio import Composio

api_key = "ak_QnRj-5zTCi_pvpSCRaZ4"
composio = Composio(api_key=api_key, toolkit_versions={'google_search_console': '20260806_00'})

# List all auth configs
auth_configs = composio.auth_configs.list()
print(f"Auth configs count: {len(auth_configs.items)}")
for ac in auth_configs.items:
    print(f"  ID: {ac.id}")
    for attr in dir(ac):
        if not attr.startswith('_'):
            try:
                val = getattr(ac, attr)
                if val is not None and not callable(val):
                    print(f"    {attr}: {val}")
            except:
                pass
    print()