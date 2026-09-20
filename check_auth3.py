#!/usr/bin/env python3
from composio import Composio

api_key = "ak_QnRj-5zTCi_pvpSCRaZ4"
composio = Composio(api_key=api_key)
auth_configs = composio.auth_configs.list()
for ac in auth_configs.items:
    if hasattr(ac, 'toolkit') and ac.toolkit:
        if 'google' in str(ac.toolkit).lower() or 'search' in str(ac.toolkit).lower() or 'console' in str(ac.toolkit).lower():
            print("ID:", ac.id)
            print("Toolkit:", ac.toolkit)
            print("Auth scheme:", ac.auth_scheme)
            print("---")