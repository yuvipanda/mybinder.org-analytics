#
# Dockerfile to add an R kernel in binder
#

# Pull base image.
FROM andrewosh/binder-base

MAINTAINER Alex Williams <alex.h.willia@gmail.com>

# Switch to root to install stuff
USER root
RUN apt-get update 

# Install R kernel to Jupyter notebook
RUN conda install -y -c r ipython-notebook r-irkernel

# Switch back to non-root user
USER main
