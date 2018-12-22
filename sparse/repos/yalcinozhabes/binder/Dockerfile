FROM andrewosh/binder-base

MAINTAINER Yalcin Ozhabes <yalcinozhabes@gmail.com>

USER root

# Add dependency
RUN apt-get update
RUN apt-get install -y graphviz nano
ADD jdftx /home/main/jdftx

USER main
ENV PYTHONPATH /home/main/jdftx:$PYTHONPATH

# Install requirements for Python 2
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Install requirements for Python 3
RUN /home/main/anaconda2/envs/python3/bin/pip install -r requirements.txt

#install chemview
#RUN git clone https://github.com/gabrielelanaro/chemview
#WORKDIR chemview
#RUN /home/main/anaconda2/envs/python3/bin/pip install .
ADD chemview /home/main/anaconda2/envs/python3/lib/python3.5/site-packages/chemview/
ADD chemview-js /home/main/anaconda2/envs/python3/lib/python3.5/site-packages/chemview/static/
