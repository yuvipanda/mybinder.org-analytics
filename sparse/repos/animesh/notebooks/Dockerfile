# Instruction from https://appstore.ioudaas.no/docs/about-packages/deep-learning-tools/about.html
#Image name from https://github.com/Uninett/helm-charts/blob/master/repos/stable/deep-learning-tools/values.yaml 
FROM	quay.io/uninett/deep-learning-tools:20181022-047bbc1

# Install system packages
USER 	root
RUN 	apt-get update && apt-get install -y apt-utils vim psmisc openssh-server libopenmpi-dev git-core gcc   build-essential golang-go  libxml2-dev libcurl4-openssl-dev libssl-dev r-cran-rcpp
# install mono
RUN	apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
RUN	apt-get install -y apt-transport-https
RUN	echo "deb https://download.mono-project.com/repo/ubuntu stable-bionic main" | sudo tee /etc/apt/sources.list.d/mono-official-stable.list
RUN	apt-get update && apt-get install -y mono-devel
# Install other packages
USER 	notebook
RUN 	pip install altair 
RUN 	pip install pyro-ppl



