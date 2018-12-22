FROM python:3.6

RUN pip install --no-cache --upgrade pip && \
    pip install --no-cache notebook

ARG NB_USER
ARG NB_UID
ENV USER ${NB_USER}
ENV HOME /home/${NB_USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}

WORKDIR ${HOME}

COPY requirements.txt /${HOME}
COPY get_html.sh /${HOME}
COPY knn.ipynb /${HOME}
COPY pos.h5 /${HOME}

RUN pip3 install --no-cache -r requirements.txt  
RUN pip3 install --no-cache -U $(pip freeze | cut -d '=' -f 1)      

RUN sh get_html.sh

