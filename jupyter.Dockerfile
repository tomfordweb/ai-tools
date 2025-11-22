FROM quay.io/jupyter/base-notebook:x86_64-ubuntu-24.04
USER root
# Avoid prompts from apt during installation
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update
RUN apt install -y gcc python3-dev build-essential \
  && apt-get clean && \
  rm -rf /var/lib/apt/lists/*

USER $NB_UID

