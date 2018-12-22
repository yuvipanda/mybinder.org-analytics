FROM maveme/rascal-notebook:1.1

ENV NB_USER mauricio
ENV NB_UID 1000
ENV HOME /home/${NB_USER}
ENV WORKSPACE ${HOME}/workspace

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}

COPY . ${HOME}
USER root
RUN chown -R ${NB_UID} /root/
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}

WORKDIR ${HOME}

CMD ["sudo","jupyter", "notebook", "--ip", "0.0.0.0", "--allow-root"]