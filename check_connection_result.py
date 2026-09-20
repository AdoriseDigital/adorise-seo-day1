#!/usr/bin/env python3
from composio import Composio

api_key = "ak_QnRj-5zTCi_pvpSCRaZ4"
composio = Composio(api_key=api_key)
result = composio.connected_accounts.link(user_id="hermes_user", auth_config_id="ac_upBd_Ir-ZlQy")
print("Result object:", result)
print("Dir:", [x for x in dir(result) if not x.startswith('_')])
for attr in [x for x in dir(result) if not x.startswith('_')]:
    try:
        val = getattr(result, attr)
        print(f"  {attr}: {val}")
    except:
        pass