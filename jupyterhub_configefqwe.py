import os

c = get_config()

c.JupyterHub.hub_ip = '127.0.0.1'
c.LocalAuthenticator.create_system_users = True

