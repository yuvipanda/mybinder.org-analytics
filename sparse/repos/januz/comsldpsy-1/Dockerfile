FROM rocker/tidyverse:3.5.0

# required
MAINTAINER Janosch Linkersdörfer <linkersdoerfer@mailbox.org>

## binder configuration
## from: https://github.com/rocker-org/binder/blob/master/3.5.0/Dockerfile

ENV NB_USER rstudio
ENV NB_UID 1000
ENV VENV_DIR /srv/venv

# Set ENV for all programs...
ENV PATH ${VENV_DIR}/bin:$PATH
# And set ENV for R! It doesn't read from the environment...
RUN echo "PATH=${PATH}" >> /usr/local/lib/R/etc/Renviron

# The `rsession` binary that is called by nbrsessionproxy to start R doesn't seem to start
# without this being explicitly set
ENV LD_LIBRARY_PATH /usr/local/lib/R/lib

ENV HOME /home/${NB_USER}
WORKDIR ${HOME}

RUN apt-get update && \
    apt-get -y install python3-venv python3-dev && \
    apt-get purge && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create a venv dir owned by unprivileged user & set up notebook in it
# This allows non-root to install python libraries if required
RUN mkdir -p ${VENV_DIR} && chown -R ${NB_USER} ${VENV_DIR}

USER ${NB_USER}
RUN python3 -m venv ${VENV_DIR} && \
    # Explicitly install a new enough version of pip
    pip3 install pip==9.0.1 && \
    pip3 install --no-cache-dir \
         nbrsessionproxy==0.6.1 && \
    jupyter serverextension enable --sys-prefix --py nbrsessionproxy && \
    jupyter nbextension install    --sys-prefix --py nbrsessionproxy && \
    jupyter nbextension enable     --sys-prefix --py nbrsessionproxy

RUN R --quiet -e "devtools::install_github('IRkernel/IRkernel')" && \
    R --quiet -e "IRkernel::installspec(prefix='${VENV_DIR}')"

CMD jupyter notebook --ip 0.0.0.0


## compendium-specific configuration

USER root

# install newer package versions
RUN install2.r -e -r 'https://mran.microsoft.com/snapshot/2018-12-01' \
    drake \
    ggplot2 \
    redcapAPI \
    haven \
    sjmisc

# install research compendium
COPY . /comsldpsy

# go into the repo directory
RUN . /etc/environment \
    && R -e "devtools::install('/comsldpsy', dep=TRUE)"
