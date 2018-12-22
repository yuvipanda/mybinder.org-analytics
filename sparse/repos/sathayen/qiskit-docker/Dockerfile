FROM ubuntu:16.04

# The user name inside the container will be "qiskitter" 

ENV QISKIT_USER=qiskitter
ENV QX_API_TOKEN="UPDATE_THIS_API_TOKEN"

RUN useradd --create-home -s /bin/bash $QISKIT_USER

ENV QISKIT_DIR=/home/$QISKIT_USER

WORKDIR $QISKIT_DIR

COPY requirements.txt $QISKIT_DIR
COPY setup_qiskit_dev.sh $QISKIT_DIR
COPY examples $QISKIT_DIR/examples
COPY quiz $QISKIT_DIR/quiz

RUN apt-get update && apt-get install -q -y sudo wget bzip2 git build-essential libssl-dev libffi-dev python3-dev python3-pip 

RUN pip3 install pip --upgrade 
RUN pip3 install -r requirements.txt
 
RUN chmod +x setup_qiskit_dev.sh && ./setup_qiskit_dev.sh

# ------------------------------------------------------------------------------
# Change the owner to $QISKIT_USER , the -R option recursively changes ownership
# for all sub-dirs
# ------------------------------------------------------------------------------
RUN chown -R $QISKIT_USER:$QISKIT_USER /home/$QISKIT_USER/
RUN usermod -aG sudo $QISKIT_USER
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# Switch to the new user
USER $QISKIT_USER

CMD [ "jupyter" , "notebook",  "--ip=0.0.0.0", "--port=8888", "--no-browser" ]

# This can image can be run as (update the token value) 
# docker run -it --env QX_API_TOKEN="your_api_token" -p 8888:8888 <NAME_OF_THIS_IMAGE>:TAG

