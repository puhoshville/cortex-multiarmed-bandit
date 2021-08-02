# cortex-multiarmed-bandit

Serving ML models in high-load manner with cortex and traffic splitter


# Step-by-step

## 1. Install `cortex` 0.39.1 or greater

```bash
# install the CLI
bash -c "$(curl -sS https://raw.githubusercontent.com/cortexlabs/cortex/v0.39.1/get-cli.sh)
```

!More actual information you can find here: https://docs.cortex.dev

## 2. Setup cluster 

```bash
cortex cluster up
```

## 3. Deploy models

```bash
cortex deploy --env aws
```

# Different models

We have two separate files: `model_a.py` and `model_b.py`. Model A returns random positive numbers, Model B – negative.
So, we always can identify the model – it will help us later.
 
## Build model images

For each model we have to create separate docker container. 
For this purpose we use [Docker's multi-stage builds](https://docs.docker.com/develop/develop-images/multistage-build/).

This images use the base, but serves different models.

For building Model A:
```bash
docker build . --target model-b -t cortex-bandit:model-a
```

For building Model B:
```bash
docker build . --target model-b -t cortex-bandit:model-a
```

## Check images

To make sure image working correctly we can run it locally:
```bash
docker run --rm -it -p 8080:8080 cortex-bandit:model-a
``` 

And do some requests:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"msg": "hello world"}' localhost:8080
```

We will se something like this:
```
$ curl -X POST -H "Content-Type: application/json" -d '{"msg": "hello world"}' localhost:8080
78
```