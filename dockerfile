FROM python:3.11-slim

WORKDIR /hub

RUN apt-get update && \
    apt-get install -y npm &&\
    ### Install tools for python
    pip install -U pip setuptools wheel

### Install npm proху fop Jupyter
RUN npm install -g configurable-http-proxy

EXPOSE 8000 8081

### Install requirements
COPY requirements.in /hub/requirements.in
RUN pip install -r requirements.in

COPY jupyterhub_config.py /hub/jupyterhub_config.py

CMD ["jupyterhub -f /hub/jupyterhub_config.py"]
