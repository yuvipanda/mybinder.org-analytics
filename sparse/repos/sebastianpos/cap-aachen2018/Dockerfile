FROM gapsystem/gap-docker

MAINTAINER Sebastian Posur <sebastian.posur@uni-siegen.de>

RUN     cd /home/gap/inst/gap-4.10.0/pkg \
     && git clone https://github.com/homalg-project/CAP_project.git \
     && cd CAP_project \
     && git checkout a2549196db88e01d7f2f4fc02ada43f43835610b

COPY --chown=1000:1000 . $HOME/cap-aachen2018

USER gap

WORKDIR $HOME/cap-aachen2018/notebooks
