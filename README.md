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

