# ψᵟ
#
#

FROM    continuumio/anaconda3

LABEL   maintainer="mdAshford"

# USER    root

# RUN apt-get update && apt-get install -y libgtk2.0-dev && \
#     rm -rf /var/lib/apt/lists/* && \
RUN    /opt/conda/bin/conda install jupyter -y && \
    /opt/conda/bin/conda install -c conda-forge jupyterlab
    # /opt/conda/bin/conda install -c menpo opencv3 -y && \
    # /opt/conda/bin/conda install numpy pandas matplotlib h5py
    # /opt/conda/bin/conda upgrade dask && \
    # pip install tensorflow imutils

RUN ["mkdir", "notebooks"]

# COPY jupyter_notebook_config.py /root/.jupyter/
# COPY run_jupyter.sh /

# Jupyter and Tensorboard ports
# EXPOSE 8888 6006
EXPOSE 8888

# Store notebooks in this mounted directory
VOLUME /notebooks

# ENTRYPOINT ["jupyter", "lab", "--allow-root","--ip=0.0.0.0", "--no-browser"]


CMD     ["jupyter lab"]
