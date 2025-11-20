 FROM quay.io/jupyter/base-notebook:x86_64-ubuntu-24.04

RUN pip install --quiet --no-cache-dir langchain langchain-ollama ollama 
