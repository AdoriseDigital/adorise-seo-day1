#!/usr/bin/env python3
from composio import Composio

api_key = "ak_QnRj-5zTCi_pvpSCRaZ4"
composio = Composio(api_key=api_key)
auth_configs = composio.auth_configs.list()
for ac in auth_configs.items:
    print("ID:", ac.id)
    print("Dir:", [x for x in dir(ac) if not x.startswith('_')])
    print("---")