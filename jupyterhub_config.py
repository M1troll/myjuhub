import os

c = get_config()

c.Spawner.args = ["--allow-root"]
c.JupyterHub.hub_ip = '127.0.0.1'

# Users
c.Authenticator.whitelist = {'sar1tasa', 'tmp_user'}
c.Authenticator.admin_users = {'sar1tasa'}

c.LocalAuthenticator.create_system_users = True
