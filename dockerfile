FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y npm &&\
    ### Install tools for python
    pip install -U pip setuptools wheel

### Install requirements
<<<<<<< Updated upstream
COPY requirements.in /requirements.in
RUN pip install -r requirements.in

=======
COPY requirements.in .
RUN pip install -r requirements.in

COPY jupyterhub_config.py .

>>>>>>> Stashed changes
### Install npm proху fop Jupyter
RUN npm install -g configurable-http-proxy

EXPOSE 9999

<<<<<<< Updated upstream
COPY jupyterhub_config.py /jupyterhub_config.py

ENTRYPOINT ["jupyterhub", "-f", "/jupyterhub_config.py"]
=======
CMD jupyterhub -f jupyterhub_config.py --ip=0.0.0.0 --port=9999
>>>>>>> Stashed changes
