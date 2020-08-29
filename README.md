# cortex-multiarmed-bandit

Serving ML models in high-load manner with cortex and traffic splitter


# Step-by-step

## 1. Install `cortex` 0.19 or greater

```bash
bash -c "$(curl -sS https://raw.githubusercontent.com/cortexlabs/cortex/0.19/get-cli.sh)"
```

## 2. Setup cluster 

```bash
cortex cluster up
```

## 3. Deploy models

```bash
cortex deploy --env aws
```

