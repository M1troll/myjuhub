FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y npm &&\
    ### Install tools for python
    pip install -U pip setuptools wheel

### Install requirements
COPY requirements.in /requirements.in
RUN pip install -r requirements.in

### Install npm proху fop Jupyter
RUN npm install -g configurable-http-proxy

EXPOSE 8000 8081

COPY jupyterhub_config.py /jupyterhub_config.py

ENTRYPOINT ["jupyterhub", "-f", "/jupyterhub_config.py"]
