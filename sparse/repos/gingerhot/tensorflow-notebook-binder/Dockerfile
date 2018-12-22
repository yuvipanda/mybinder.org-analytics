FROM jupyter/tensorflow-notebook:8d9388cac562

USER root

ADD tensorflow-example.ipynb $HOME/work/
RUN chown -R $NB_USER:$NB_GID $HOME/work

USER $NB_USER
