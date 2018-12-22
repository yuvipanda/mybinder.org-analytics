FROM ubuntu:trusty

MAINTAINER John Foster <johntfosterjr@gmail.com>

ENV NB_USER default
ENV NB_UID 1000
ENV HOME /home/${NB_USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}

RUN apt-get -yq update; \
    apt-get -yq install build-essential \
                        git \
                        wget

RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ${HOME}/miniconda.sh

RUN chown -R ${NB_USER} ${HOME}

USER ${NB_USER}

WORKDIR ${HOME}

#Install conda
RUN bash miniconda.sh -b -p $HOME/miniconda; \
    export PATH="$HOME/miniconda/bin:$PATH"; \
    hash -r; \
    conda config --set always_yes yes --set changeps1 no; \
    conda update -q conda; \
    conda info -a; \
    conda install matplotlib; \
    conda install -c conda-forge jupyter_contrib_nbextensions; \
    conda install -c conda-forge ipywidgets; \
    conda upgrade nbformat

ENV PATH ${HOME}/miniconda/bin:${PATH}

RUN pip install --no-cache-dir notebook
RUN pip install --no-cache-dir RISE
RUN jupyter-nbextension install rise --py --sys-prefix
RUN jupyter-nbextension enable rise --py --sys-prefix
RUN jupyter nbextension enable hide_input/main --sys-prefix
RUN jupyter nbextension enable init_cell/main --sys-prefix

ENV CONDA_HOME ${HOME}/miniconda

USER root
RUN mkdir ${HOME}/notebooks
COPY *.ipynb ${HOME}/notebooks/
COPY images ${HOME}/notebooks/images
COPY rise.css ${HOME}/notebooks/
RUN chown -R ${NB_USER} ${HOME}/notebooks
RUN rm miniconda.sh
WORKDIR ${HOME}/notebooks
USER ${NB_USER}
RUN jupyter trust ${HOME}/notebooks/*.ipynb

CMD jupyter notebook --ip 0.0.0.0
