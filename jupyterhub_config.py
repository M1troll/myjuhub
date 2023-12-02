import os

c = get_config()

c.Spawner.args = ["--allow-root"]
c.Spawner.cmd = "/myjuhub/bin/jupyterhub-singleuser"
c.JupyterHub.hub_ip = '127.0.0.1'

c.PAMAuthenticator.open_sessions = False

# Users
c.Authenticator.admin_users = {'sar1tasa', 'tmp'}
c.PAMAuthenticator.admin_groups = {'myjuhub'}
c.LocalAuthenticator.group_whitelist = ['myjuhub']
c.LocalAuthenticator.create_system_users = True

# Auth rules
c.JupyterHub.authenticator_class = "dummy"
c.DummyAuthenticator.password = "123"








