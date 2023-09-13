# Configuration file for JupyterHub
import os

c = get_config()  # noqa: F821

c.Authenticator.admin_users = ['anton']
c.Authenticator.delete_invalid_users = True


c.LocalAuthenticator.create_system_users=True

# c.Spawner.default_url = '/spawners'

# # Spawn single-user servers as Docker containers
# c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
# c.DockerSpawner.container_image = 'jupyter/scipy-notebook'
# c.DockerSpawner.extra_create_kwargs.update({'command': 'start-singleuser.sh'})
# network_name = 'jupyterhub'
# c.DockerSpawner.use_internal_ip = True
# c.DockerSpawner.network_name = network_name
# c.DockerSpawner.extra_host_config = {'network_mode': network_name}
# notebook_dir = '/home/jovyan/work'
# c.DockerSpawner.notebook_dir = notebook_dir
# c.DockerSpawner.volumes = {'jupyterhub-user-{username}': notebook_dir}
# c.DockerSpawner.extra_create_kwargs.update({'volume_driver': 'local'})
# c.DockerSpawner.remove_containers = True
# c.DockerSpawner.debug = True

# # User containers will access hub by container name on the Docker network
# c.JupyterHub.hub_ip = network_name
# c.JupyterHub.hub_port = 8080
