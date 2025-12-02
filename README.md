# Installation

1. Clone this repository
2. git submodule update --init

# Usage

There are a few ways to use this project. It is just a combination of tools.

## Jupyter (connect to docker or 127.0.0.1)

To boot up the jupyter project which should be able to communicate with anything on the docker network (or your network):

```
python -m venv venv
source venv/bin/activate
jupyter lab jupyter
```

You may need to mess with some ports or addresses for your setup - There should be some example notebooks in the base directory of the jupyter lab.

```
http://127.0.0.1:7869 - ollama docker project
http://127.0.0.1:11434 - self hosts ollama - probably
http://127.0.0.1:1234 - LMStudio
```

## Self Hosted Ollama Docker

There is a lot of naunce behind getting ollama running in all of the different environments. I have only run this on a linux environment to things may be different for win/mac.

From what I can tell, you can only use docker + ollama + gpu on linux.

# Usage

1. `cp env.example .env` and the variables to your preferences.
2. Determine what compose files you want to use. All are networked together so it's more about figuring out what you need.

- `docker-compose.yml` - Ollama docker and webui
- `docker-compose.jupyter.yml` - Includes jupyter labs
- `docker-compose.gpu.yml` - Allows you to use compose through gpu drivers.
- `docker-compose.app.yml` - Python and TS container for writing code. I haven't spent much time on this.

Start the app by running:

```bash
# CPU Only
docker compose up -d
# GPU
docker compose up -f docker-compose.gpu.yml up -d
```

- [Open Web UI](http://localhost:8080)

# Tools

If you would like to download a model progmatically:

```bash
./bin/downloadModel.sh <modelName>
```
