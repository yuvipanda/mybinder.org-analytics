FROM jupyter/base-notebook

USER root

RUN apt-get update && apt-get install -yq --no-install-recommends \
    git  \
    software-properties-common  \
    libssl-dev  \
    libzmq3-dev  \
    python-dev  \
    python-pip  \
    python-zmq  \
    sudo  \
    libgraphicsmagick1-dev  \
    nodejs  \
    libfftw3-dev  \
    sox  \
    libsox-dev  \
    libsox-fmt-all  \
    build-essential  \
    gcc  \
    g++  \
    curl  \
    cmake  \
    libreadline-dev  \
    git-core  \
    libjpeg-dev  \
    libpng-dev  \
    ncurses-dev  \
    imagemagick  \
    libzmq3-dev  \
    gfortran  \
    unzip  \
    gnuplot  \
    gnuplot-x11  \
    ipython  \
    libreadline-dev \
    libhdf5-dev \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Switch back to jovyan to avoid accidental container runs as root
USER $NB_UID

RUN git clone https://github.com/torch/distro.git ~/torch --recursive

WORKDIR /home/$NB_USER/torch

RUN ./install.sh -b

RUN ~/torch/install/bin/luarocks install torch && \
    ~/torch/install/bin/luarocks install nn && \
    ~/torch/install/bin/luarocks install optim && \
    ~/torch/install/bin/luarocks install lua-cjson && \
    ~/torch/install/bin/luarocks install totem

WORKDIR /home/$NB_USER

RUN git clone https://github.com/deepmind/torch-hdf5 && cd torch-hdf5 && ~/torch/install/bin/luarocks make hdf5-0-0.rockspec

# python dependencies
RUN pip install matplotlib
RUN pip install ipywidgets && jupyter nbextension enable --py widgetsnbextension && jupyter labextension install @jupyter-widgets/jupyterlab-manager


RUN git clone https://github.com/jcjohnson/torch-rnn.git

COPY . ${HOME}

# missing torch-rnn
