FROM jupyter/scipy-notebook:92fe05d1e7e5
MAINTAINER Sjoerd de Haan
USER jovyan
COPY requirements.txt /home/jovyan/
RUN pip install -r ~/requirements.txt
#RUN pip install numpy==1.14.0 tensorflow==1.5 tensorflow-tensorboard==1.5.0 jupyter-tensorboard==0.1.5 RISE jupyter_contrib_nbextensions keras==2.1.3 xgboost==0.7.post3
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
ENV PYTHONPATH="${HOME}:${PYTHONPATH}"
RUN git clone https://github.com/sjoerddehaan/ml-course-2018/
RUN cd ml-course-2018
