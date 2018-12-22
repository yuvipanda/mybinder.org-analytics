FROM ubuntu:18.04

RUN apt-get update && apt-get install -y --fix-missing --no-install-recommends unzip wget \
    python python-pip mapserver-bin python-mapscript

# install the notebook package
# and see https://github.com/pypa/pip/issues/5599
RUN python -m pip install --no-cache --upgrade pip && \
    python -m pip install --no-cache --upgrade setuptools && \
    python -m pip install --no-cache notebook

# create user with a home directory

ENV NB_USER jovyan
ENV NB_UID 1000
ENV HOME /home/${NB_USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}

# Make sure the contents of our repo are in ${HOME}
# COPY . ${HOME}
USER root
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}

#ARG NB_USER
#ARG NB_UID
#ENV USER ${NB_USER}
#ENV HOME /home/${NB_USER}
WORKDIR ${HOME}

#RUN adduser --disabled-password \
#    --gecos "Default user" \
#    --uid ${NB_UID} \
#    ${NB_USER}

# add the notebooks
RUN wget https://github.com/geographika/OSGeoLive12-Notebooks/archive/master.zip && \
    unzip master.zip && \
    mv OSGeoLive12-Notebooks-master OSGeoLive12-Notebooks && \
    rm master.zip

# add the MapServer demo
RUN wget https://github.com/mapserver/mapserver-demo/archive/master.zip && \
    unzip master.zip && \
    mv mapserver-demo-master mapserver-demo && \	
    rm master.zip

# set a path to the MapServer demo
ENV MAPSERVER_DEMO /home/${NB_USER}/mapserver-demo

WORKDIR ${HOME}/OSGeoLive12-Notebooks