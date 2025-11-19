1. Copy `env.example` and update the variables to your preference

Start the app by running:

```bash
docker compose up
# or
docker compose -f docker-compose.yml -f docker-compose.jupyter.yml
```

These two projects are exposed depending on your docker command.

- http://localhost:8080 - Open Web UI
- http://localhost:8888?token=<YOUR JUPYTER TOKEN> - Opens jupyter lab

To open up a TTY in the app and write code around ollama

```bash
docker compose exec app sh
```

If you would like to download a model progmatically:

```bash
./bin/downloadModel.sh <modelName>
```
