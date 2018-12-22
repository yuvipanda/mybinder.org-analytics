FROM andrewosh/binder-base

MAINTAINER telenczuk@unic.cnrs-gif.fr 

ENV NRN_VER=7.4
ENV NRN=nrn-$NRN_VER
ENV VENV=$HOME/neuron
ENV PATH=$PATH:$VENV/bin

RUN mkdir $HOME/packages

WORKDIR $HOME/packages
RUN wget http://www.neuron.yale.edu/ftp/neuron/versions/v$NRN_VER/$NRN.tar.gz
RUN tar xzf $NRN.tar.gz; rm $NRN.tar.gz


USER root
RUN apt-get update; apt-get install -y  libncurses5-dev libreadline-dev libgsl0-dev

USER main

RUN mkdir $VENV; mkdir $VENV/build; mkdir $VENV/bin
WORKDIR $VENV/build
RUN mkdir $NRN; \
    cd $NRN; \
    $HOME/packages/$NRN/configure --with-nrnpython=$HOME/anaconda/bin/python --disable-rx3d --without-iv --prefix=$VENV; \
    make; make install; \
    cd src/nrnpython; /home/main/anaconda/bin/python setup.py install; \
    cd $VENV/bin; ln -s ../x86_64/bin/nrnivmodl

WORKDIR $HOME
