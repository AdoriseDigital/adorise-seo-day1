#!/usr/bin/env python3
from composio import Composio
import inspect

api_key = "ak_QnRj-5zTCi_pvpSCRaZ4"
composio = Composio(api_key=api_key)
print("link signature:", inspect.signature(composio.connected_accounts.link))
print("create signature:", inspect.signature(composio.connected_accounts.create))