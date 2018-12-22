# The existing docker image should be deployable on binder - we just need
# to copy the content across to the $HOME directory ... see
# https://mybinder.readthedocs.io/en/latest/dockerfile.html#when-should-you-use-a-dockerfile
# for details

# SHA tagging would be better
FROM lmoresi/stripy:0.7

ENV NB_USER jovyan
ENV NB_UID 1000
ENV HOME /home/${NB_USER}

# tidy up

USER root

RUN mkdir .scratch || true
RUN mv litho1pt0-src .scratch || true
RUN mv stripy-src    .scratch || true
RUN mv external      .scratch || true
RUN mv scripts       .scratch || true
RUN mv Notebooks     .scratch
RUN mv .scratch/Notebooks/* .

## This is not used by binder
ADD run-jupyter.sh .run-jupyter.sh

## Set config options ??
RUN rm -rf .jupyter || true
RUN mkdir  .jupyter
ADD jupyter_notebook_config.py .jupyter/jupyter_notebook_config.py


RUN chown -R ${NB_UID} ${HOME}

USER ${NB_USER}

ENTRYPOINT ["/usr/local/bin/tini", "--", "/usr/local/bin/xvfbrun.sh"]
CMD ./.run-jupyter.sh
