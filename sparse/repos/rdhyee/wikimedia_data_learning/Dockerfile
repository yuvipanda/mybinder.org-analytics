FROM jupyter/scipy-notebook@sha256:24eff1eeafdc22f744e003771d1f40b97997b4593763a8ca2d4967b314f2879d 

USER root
RUN apt-get update && apt-get -yq dist-upgrade \
 && apt-get install -yq --no-install-recommends \
 python-lxml \
 libxml2-dev \
 libxslt1-dev \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*
        
# USER jovyan

RUN pip install lxml
RUN pip install mwclient
# RUN pip install git+git://github.com/mwclient/mwclient@v0.7.1
# RUN pip install https://bitbucket.org/rdhyee/mwclient/get/wpp.tar.bz2
# RUN pip install git+git://github.com/rdhyee/mwclient@wpp_integrate

RUN pip install responses && \
    pip install pytest && \
    pip install boltons && \
    pip install pywikibot && \
    pip install cssselect

COPY notebooks/ /home/jovyan/work
# A bit ugly but unfortunately necessary: https://github.com/docker/docker/issues/6119
USER root
RUN chown -R jovyan:users /home/jovyan/work

#USER jovyan

VOLUME ["/user/jovan/", "/data"]

