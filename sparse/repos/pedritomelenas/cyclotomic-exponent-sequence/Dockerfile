FROM gapsystem/gap-docker

MAINTAINER Alexander Konovalov <alexander.konovalov@st-andrews.ac.uk>

COPY --chown=1000:1000 . $HOME

RUN git clone https://github.com/gap-packages/numericalsgps.git

RUN mv numericalsgps inst/gap*/pkg

USER gap

WORKDIR $HOME
