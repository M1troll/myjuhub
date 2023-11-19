FROM r-base

# RUN install.packages('IRkernel')

# RUN apt-get install libzmq3-dev libcurl4-openssl-dev libssl-dev jupyter-core jupyter-client
RUN R -e "install.packages(c('repr', 'IRdisplay', 'IRkernel'), type = 'source')"
# RUN R -e "install.packages(c('IRkernel', 'repr', 'IRdisplay'), repos = 'http://cran.us.r-project.org')"
# RUN R -e "IRkernel::installspec(name = 'r', displayname = 'r')"
RUN R -e "IRkernel::installspec()"
RUN jupyter labextension install @techrah/text-shortcuts

CMD R -e "IRkernel::main()" --args $DOCKERNEL_CONNECTION_FILE
