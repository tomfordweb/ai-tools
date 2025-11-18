Start the app by running:

```bash
docker compose up
```

If you added a package and want it installed in the very hacky way I am currently doing this, you may need to add `--build` to your command.

```bash
docker compose up --build
```

To open up a TTY in the app and write code around ollama

```bash
docker compose exec app sh
```

If you would like to download a model progmatically:

```bash
./bin/downloadModel.sh <modelName>
```
