import os
print('COMPOSIO_API_KEY from env:', os.environ.get('COMPOSIO_API_KEY', 'NOT SET')[:20])