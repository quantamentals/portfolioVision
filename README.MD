# steps

1. python3 -m venv portfolioEnv
2. pip install portVision

```python

from portVision.portfolio import returns, utils

from portVision.handler import datahandler

universe = ["GLD","TLT","IWM"]

port = utils.build_portfolio(universe)

```

## To dos

1. add start and end params to build portfolio
