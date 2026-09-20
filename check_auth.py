#!/usr/bin/env python3
from composio import Composio

api_key = "ak_QnRj-5zTCi_pvpSCRaZ4"
composio = Composio(api_key=api_key)
auth_configs = composio.auth_configs.list()
for ac in auth_configs.items:
    if 'google' in ac.slug.lower() or 'search' in ac.slug.lower() or 'console' in ac.slug.lower():
        print(ac.id, ac.slug, ac.auth_scheme)