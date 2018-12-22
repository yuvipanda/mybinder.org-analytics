FROM rocker/geospatial:3.5.1

ENV HOME /home/rstudio
WORKDIR ${HOME}

USER ${NB_USER}

# Copy repo into ${HOME}, make user own $HOME
COPY . ${HOME}
USER root
RUN chown -R ${NB_UID}:${NB_UID} ${HOME}
USER ${NB_USER}

## run any install.R script we find
RUN if [ -f install.R ]; then R --quiet -f install.R; fi
