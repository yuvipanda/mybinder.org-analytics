FROM jupyter/scipy-notebook:137a295ff71b
RUN pip install --no-cache-dir notebook==5.*
RUN pip install plotly 
ENV NB_USER jovyan
ENV NB_UID 1000
ENV HOME /home/${NB_USER}

USER root
COPY . ${HOME}
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}

CMD ["jupyter", "notebook", "--ip", "0.0.0.0"]

