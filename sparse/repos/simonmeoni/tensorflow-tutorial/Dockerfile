FROM python:3.5.6-stretch
RUN pip install tensorflow
RUN pip install nteract_on_jupyter
RUN jupyter serverextension enable nteract_on_jupyter
RUN mkdir /tf
WORKDIR /tf
EXPOSE 8888
CMD jupyter nteract --ip=0.0.0.0 --allow-root
