FROM ubuntu:latest

ENV TZ=US/Pacific

RUN ln --symbolic --no-dereference --force /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install --yes --no-install-recommends apt-utils

RUN apt-get update && \
    apt upgrade --yes && \
    apt-get install make --yes
    
RUN apt-get update && \
    apt-get install --yes --no-install-recommends \
    gettext-base \
    git \
    make \
    python3 \
    python3-dev \
    python3-pip \
    texlive-full

RUN pip install --upgrade pytest
RUN pip install black
RUN pip install -U matplotlib pandas numpy
