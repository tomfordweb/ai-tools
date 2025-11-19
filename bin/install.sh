#!/bin/bash

# self hosted
./bin/downloadModel.sh "gpt-oss:20b" 
./bin/downloadModel.sh "llama3.2:1b"
./bin/downloadModel.sh "gemma3:270m" 
./bin/downloadModel.sh "gemma3:1b"
./bin/downloadModel.sh "codellama"

# cloud
./bin/downloadModel.sh "glm-4.6"

