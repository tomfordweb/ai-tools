# I guess this is supposed to be like a minimal image you can hack on top of.
FROM alpine:latest

RUN apk update
RUN apk add python3 py3-pip typescript npm
RUN ln -sf /usr/bin/python3 /usr/bin/python

WORKDIR /app

COPY requirements.txt .

RUN pip install langchain langchain-ollama ollama --break-system-packages

WORKDIR /app/src
