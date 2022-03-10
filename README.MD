# steps

1. python3 -m venv portfolioEnv
2. pip install portVision

```python

from portVision.portfolio import returns, utils

from portVision.handler import datahandler

universe = ["GLD","TLT","IWM"]

data = datahandler.get_close(universe)

port = utils.build_portfolio(data)

```
