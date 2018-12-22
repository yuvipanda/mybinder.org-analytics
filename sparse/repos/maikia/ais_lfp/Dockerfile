FROM btel/nrnpython:nrn7.4py2.7

MAINTAINER telenczuk@unic.cnrs-gif.fr 

# Make sure the contents of our repo are in ${HOME}
COPY . ${HOME}
USER root
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}

RUN cd $HOME/libs/calcs; python setup.py install --user
RUN cd $HOME/libs/neuroneap; python setup.py install --user

USER root
RUN pip install numpy matplotlib scipy
USER ${NB_USER}

RUN cd $HOME/data/HallermannEtAl2012/; \
    nrnivmodl
