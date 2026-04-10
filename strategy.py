import pandas as pd
from indicators import zscore

class MeanReversionStrategy:
    def __init__(self, window=20, entry_z=2.0, exit_z=0.5):
        self.window = window
        self.entry_z = entry_z
        self.exit_z = exit_z

    def generate_signals(self, prices: pd.Series) -> pd.DataFrame:
        df = pd.DataFrame({'price': prices})
        df['z'] = zscore(df['price'], self.window)
        df['signal'] = 0
        df.loc[df['z'] < -self.entry_z, 'signal'] = 1   # Buy
        df.loc[df['z'] > self.entry_z, 'signal'] = -1   # Sell
        # Exit when z-score crosses zero
        # Forward fill signals for holding positions
        import numpy as np
        df['signal'] = df['signal'].replace(0, np.nan).ffill().fillna(0)
        df.loc[df['z'].abs() < self.exit_z, 'signal'] = 0
        df['signal'] = df['signal'].replace(0, np.nan).ffill().fillna(0)
        return df
