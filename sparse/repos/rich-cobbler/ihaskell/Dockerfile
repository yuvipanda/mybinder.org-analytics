#FROM fpco/stack-build
FROM jupyter/datascience-notebook

LABEL maintainer="rich.cobbler@gmail.com"

USER root

# Install all necessary Ubuntu packages
#RUN apt-get update && apt-get install -y python3-pip libgmp-dev libmagic-dev libtinfo-dev libzmq3-dev libcairo2-dev libpango1.0-dev libblas-dev liblapack-dev gcc g++ && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
	DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
		netbase \
		haskell-stack \
		build-essential \
		libzmq3-dev \
		libncurses5-dev \
		pkg-config \
		zlib1g-dev

USER jovyan
RUN stack upgrade --binary-only # this upgrades the user's local stack
ENV PATH=$HOME/.local/bin:$PATH
RUN stack --install-ghc --resolver lts-12.7 install ihaskell
RUN ihaskell install --stack
CMD stack exec /usr/local/bin/start-notebook.sh
# Install Jupyter notebook
#RUN pip3 install -U jupyter

#ENV LANG en_US.UTF-8
#ENV NB_USER jovyan
#ENV NB_UID 1000
#ENV HOME /home/${NB_USER}

#RUN adduser --disabled-password \
#    --gecos "Default user" \
#    --uid ${NB_UID} \
#    ${NB_USER}

#COPY . ${HOME}
#USER root
#RUN chown -R ${NB_UID} ${HOME}
#USER ${NB_USER}
#
#ENV PATH $(stack path --local-install-root)/bin:$(stack path --snapshot-install-root)/bin:$(stack path --compiler-bin):${HOME}/.local/bin:${PATH}
#ENV GHC_PACKAGE_PATH $(stack path --ghc-package-path)
#RUN stack config set system-ghc --global true
#RUN stack install ihaskell
#RUN ihaskell install --stack

#WORKDIR ${HOME}

# Specify the default command to run
#CMD ["jupyter", "notebook", "--ip", "0.0.0.0"]
