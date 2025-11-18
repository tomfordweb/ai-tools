#!/bin/bash

# ./bin/downloadModel <model>
# ./bin/downloadModel gpt-oss:20b

docker compose exec ollama ollama pull "$1"
