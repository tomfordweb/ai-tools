This is a docker ollama setup. There is a lot of naunce behind getting ollama running in all of the different environments.

You can get by on CPU compute, but its not very performant. Basically. You can only get ollama + docker + cuda on Linux.

# Installation

1. Get your ollama or jupyter setup going.
2. Clone this repository
3. git submodule update --init

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
# CPU and Jupyter
docker compose up -f docker-compose.jupyter.yml up -d
# GPU and Jupyter
docker compose \
 -f docker-compose.yml \
 -f docker-compose.jupyter.yml \
 -f docker-compose.gpu.yml \
 up -d
# Everything
docker compose \
 -f docker-compose.yml \
 -f docker-compose.jupyter.yml \
 -f docker-compose.gpu.yml \
 -f docker-compose.app.yml \
 up -d
```

These two projects are exposed depending on your docker command.

- http://localhost:8080 - Open Web UI
- http://localhost:8888?token=<YOUR JUPYTER TOKEN> - Opens jupyter lab. Which seems to be a better experience for hacking scripts together.

If you want to write code:

```bash
docker compose exec app sh

# JS
echo 'console.log("hello world");' >> hello.ts
npx tsx hello.ts

# Python
python ./someScript
```

If you would like to download a model progmatically:

```bash
./bin/downloadModel.sh <modelName>
```
