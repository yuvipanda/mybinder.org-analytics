FROM andrewosh/binder-base:1.0

MAINTAINER Michael Wilber <mwilber@mjwilber.org>

USER main

RUN /home/main/anaconda2/bin/pip install --upgrade setuptools pip || true

RUN /home/main/anaconda2/bin/pip install bokeh==0.10.0
RUN /home/main/anaconda2/bin/pip install simplejson
RUN /home/main/anaconda2/bin/pip install bokeh_image_explore

RUN /home/main/anaconda2/bin/conda install -y -c https://conda.anaconda.org/gcr snack
