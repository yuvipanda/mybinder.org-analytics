FROM jupyter/base-notebook:4d19a9839c05

RUN pip install --no-cache-dir octave_kernel
USER root

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:octave/stable
RUN apt-get update
RUN apt-get install -y octave



ADD https://github.com/casadi/casadi/releases/download/3.4.5/casadi-linux-octave-v3.4.5.tar.gz /tmp/octave.tar.gz
RUN chown $NB_USER:$NB_GID /tmp/octave.tar.gz

USER $NB_UID
RUN mkdir $HOME/casadi
RUN tar -xvf /tmp/octave.tar.gz -C $HOME/casadi
RUN rm /tmp/octave.tar.gz

RUN echo "addpath('$HOME/casadi');" > $HOME/.octaverc

COPY . ${HOME}
USER root
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}
