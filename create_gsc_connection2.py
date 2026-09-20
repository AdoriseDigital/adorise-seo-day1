#!/usr/bin/env python3
from composio import Composio

api_key = "ak_QnRj-5zTCi_pvpSCRaZ4"
composio = Composio(api_key=api_key)
result = composio.connected_accounts.link(user_id="hermes_user", auth_config_id="ac_upBd_Ir-ZlQy")
print("Auth URL:", result)