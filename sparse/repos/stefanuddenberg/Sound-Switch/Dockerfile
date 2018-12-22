FROM andrewosh/binder-base
#FROM binder-project/binder:binder/images/base/Dockerfile

MAINTAINER Stefan Uddenberg <stefan.uddenberg@gmail.com>

# Install FFMPEG
RUN wget http://johnvansickle.com/ffmpeg/releases/ffmpeg-release-64bit-static.tar.xz
RUN tar xvfJ ffmpeg-release-64bit-static.tar.xz
USER root
# Note that we don't know exactly which version of ffmpeg will come down.
RUN ln ffmpeg-*-64bit-static/ffmpeg /usr/local/bin/ffmpeg

# Install dependencies
# RUN pip install simpleaudio numpy pydub