# myjuhub
It's just a my juhub

# Installing project for developing on local PC

You have to have the following tools installed prior initializing the project:

- [docker](https://docs.docker.com/engine/installation/)
- [docker-compose](https://docs.docker.com/compose/install/)
- [pyenv](https://github.com/pyenv/pyenv)
- [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)


## Prepare python env using virtualenv

Create separate python virtual environment if you are going to run it in
    local:

    ```bash
    pyenv install `pyenv latest 3.11` --skip-existing
    pyenv virtualenv 3.11 shcool
    pyenv local shcool
    pyenv shell shcool
    ```

pip install -r requirements.in
npm install -g configurable-http-proxy
python3 -m pip install --upgrade jupyterlab
python3 -m pip install --upgrade notebook
