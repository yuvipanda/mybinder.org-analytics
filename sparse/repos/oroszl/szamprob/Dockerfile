FROM andrewosh/binder-base:latest

USER root
RUN conda install -c conda-forge ipywidgets
RUN pip install plotly
RUN /home/main/anaconda2/envs/python3/bin/pip install plotly
USER main
WORKDIR $HOME/notebooks

