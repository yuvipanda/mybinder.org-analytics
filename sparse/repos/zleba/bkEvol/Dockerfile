#Official ROOT Docker image
FROM rootproject/root-ubuntu16

# Run the following commands as super user (root):
USER root
RUN  mkdir /bkevol  &&\
     apt-get update && \
     apt-get install -y wget \
                        libopenmpi-dev \
                        libhdf5-dev \
                        libopenblas-dev \
                        libboost-dev \
                        libopenblas-dev \
     && rm -rf /var/lib/apt/lists/*

#Instal LHAPDF
WORKDIR /
COPY installARMA.sh .
RUN ./installARMA.sh


#ENV PATH="/lhapdf/install/bin/:${PATH}"

# When starting the container and no command is started, run bash
CMD ["/bin/bash"]
