#!/bin/bash

docker compose -f docker-compose.yml -f docker-compose.gpu.yml -f docker-compose.jupyter.yml up -d "$@"
