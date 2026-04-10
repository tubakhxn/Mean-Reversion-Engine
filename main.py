import pandas as pd
import numpy as np
from strategy import MeanReversionStrategy
from backtest import Backtest
import visualization as viz

# Load your historical price data here
# Example: df = pd.read_csv('data/price.csv', index_col=0, parse_dates=True)
# For demo, generate synthetic mean-reverting price series
np.random.seed(42)
n = 500
price = np.cumsum(np.random.normal(0, 1, n)) + 100
price = pd.Series(price, name='price')

# Strategy
window = 20
strategy = MeanReversionStrategy(window=window)
signals = strategy.generate_signals(price)

# Backtest
bt = Backtest(signals)
results = bt.run()
metrics = bt.performance_metrics()

# Output
print('Performance Metrics:')
for k, v in metrics.items():
    print(f'{k}: {v:.2%}' if isinstance(v, float) else f'{k}: {v}')

# Plots
viz.plot_price_bands(results, window)
viz.plot_zscore(results)
viz.plot_equity_curve(results)
