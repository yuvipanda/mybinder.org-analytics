FROM jupyter/scipy-notebook

USER $NB_UID
RUN mkdir /home/$NB_USER/tmp

# Install Calysto Processing
RUN	pip install --upgrade calysto_processing --user && \
	python3 -m calysto_processing install --user

user root
# Download and extract Processing
RUN cd /tmp && \
    wget http://download.processing.org/processing-3.4-linux64.tgz && \
    tar zxvf processing-3.4-linux64.tgz -C /usr/local/

USER $NB_UID

# Ensure processing-java command can be used from anywhere
ENV PATH="/usr/local/processing-3.4:${PATH}"

RUN rm -r /home/$NB_USER/tmp
RUN rm -r /home/$NB_USER/work

ADD --chown=1000:100 getstarted.ipynb /home/$NB_USER/
