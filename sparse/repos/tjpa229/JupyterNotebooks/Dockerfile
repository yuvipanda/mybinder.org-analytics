FROM tjpa229/jupyternotebooks

USER root

# install Jupyter Notebook 5 (Debian package is 4.2.3) and bash kernel
RUN pip3 install --no-cache-dir notebook==5.* bash_kernel \
  && python3 -m bash_kernel.install
