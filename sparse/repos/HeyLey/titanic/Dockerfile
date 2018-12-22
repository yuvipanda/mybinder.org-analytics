FROM python:3.5.1

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
COPY titanic_kernel.ipynb /${HOME}
COPY data/test.csv /${HOME}
COPY data/train.csv /${HOME}

RUN pip3 install --no-cache -r requirements.txt  

RUN sh get_html.sh
