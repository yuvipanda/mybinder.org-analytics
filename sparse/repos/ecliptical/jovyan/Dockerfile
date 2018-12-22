FROM jupyter/minimal-notebook:latest

LABEL maintainer="Peter Nehrer <pnehrer@eclipticalsoftware.com>"

# Upgrade Node.js, install iPyWidgets
USER jovyan
RUN conda install -q -y -c conda-forge nodejs yarn ipywidgets

# Install Google Drive support
USER root
RUN jupyter labextension install @jupyterlab/google-drive

# Install ijavascript dependencies. See https://github.com/n-riesco/ijavascript
ENV DEBIAN_FRONTEND noninteractive
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libzmq3-dev \
    gnupg2 \
    && apt-get clean -y \
    && apt-get autoremove -y \
    && rm -rf /tmp/* /var/tmp/* \
    && rm -rf /var/lib/apt/lists/*

# Install IJavaScript
RUN yarn global add ijavascript

USER jovyan
RUN ijsinstall

# Modify startup script to run ijavascript
USER root
RUN printf "#!/bin/bash\n$(which ijsnotebook)\n" \
    > /usr/local/bin/start-notebook.sh

# Switch back to jovyan to avoid accidental container runs as root
USER jovyan
