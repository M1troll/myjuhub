FROM r-base

RUN R -e "install.packages(c('repr', 'IRdisplay', 'IRkernel'), type = 'source')"
RUN R -e "install.packages('IRkernel')"

CMD R -e "IRkernel::main()" --args $DOCKERNEL_CONNECTION_FILE
