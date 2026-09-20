from composio import Composio

api_key = "ak_QnRj-5zTCi_pvpSCRaZ4"
composio = Composio(api_key=api_key)

# Use the auth_config_id from existing connections
auth_config_id = "ac_upBd_Ir-ZlQy"

print("Attempting to create new GSC connection via link...")
result = composio.connected_accounts.link(
    user_id="hermes_user",
    auth_config_id=auth_config_id
)

print(f"Result: {result}")
if hasattr(result, 'redirect_url'):
    print(f"Visit this URL to complete OAuth:")
    print(f"https://connect.composio.dev{result.redirect_url}")