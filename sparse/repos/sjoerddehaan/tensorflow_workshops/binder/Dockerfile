FROM jupyter/tensorflow-notebook:033056e6d164
MAINTAINER Sjoerd de Haan
USER jovyan
RUN pip install tensorflow==1.3.0 tensorflow-tensorboard==0.1.8 jupyter-tensorboard==0.1.4 RISE jupyter_contrib_nbextensions
RUN jupyter-nbextension install rise --py --sys-prefix 
RUN jupyter-nbextension enable rise --py --sys-prefix
RUN jupyter contrib nbextension install --sys-prefix
RUN jupyter nbextension enable --py widgetsnbextension
RUN jupyter nbextension enable python-markdown/main
RUN jupyter nbextension enable codefolding/main 
RUN jupyter nbextension enable hinterland/hinterland
RUN jupyter nbextension enable python-markdown/main
RUN jupyter nbextension enable toc2/main
RUN jupyter nbextension enable spellchecker/main
RUN jupyter nbextension enable collapsible_headings/main
RUN git clone https://github.com/sjoerddehaan/tensorflow_workshops
