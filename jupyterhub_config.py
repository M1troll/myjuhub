import os

c = get_config()

c.Spawner.args = ["--allow-root"]
c.JupyterHub.hub_ip = '127.0.0.1'

# Users
c.Authenticator.admin_users = {'sar1tasa', 'tmp'}
c.PAMAuthenticator.admin_groups = {'sar1tasa'}
c.LocalAuthenticator.create_system_users = True

c.JupyterHub.authenticator_class = "dummy"
c.DummyAuthenticator.password = "123"
