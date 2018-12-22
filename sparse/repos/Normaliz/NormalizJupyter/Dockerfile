FROM normaliz/normaliz:v3.6.0

ENTRYPOINT []

RUN pip3 install --no-cache-dir notebook==5.*

COPY ./jupyter_notebook_config.py /home/norm/.jupyter/jupyter_notebook_config.py

COPY *.ipynb /home/norm/

ENV PATH /home/norm/.local/bin:${PATH}
