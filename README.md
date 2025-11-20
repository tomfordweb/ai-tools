This is a docker ollama setup. There is a lot of naunce behind getting ollama running in all of the different environments.

You can get by on CPU compute, but its not very performant. Basically. You can only get ollama + docker + cuda on Linux.

# Usage

1. `cp env.example .env` and the variables to your preferences.
2. Determine what compose files you want to use.

- `docker-compose.yml` - Base image
- `docker-compose.jupyter.yml` - Includes jupyter labs
- `docker-compose.gpu.yml` - Allows you to use compose through gpu drivers.

Start the app by running:

```bash
# CPU Only
docker compose up -d
# CPU and Jupyter
docker compose up -f docker-compose.jupyter.yml up -d
# GPU and Jupyter
docker compose \
 -f docker-compose.yml \
 -f docker-compose.jupyter.yml \
 -f docker-compose.gpu.yml \
 up -d
```

These two projects are exposed depending on your docker command.

- http://localhost:8080 - Open Web UI
- http://localhost:8888?token=<YOUR JUPYTER TOKEN> - Opens jupyter lab. Which seems to be a better experience for hacking scripts together.

To open up a TTY in the app and write code around ollama

```bash
docker compose exec app sh
```

If you would like to download a model progmatically:

```bash
./bin/downloadModel.sh <modelName>
```
