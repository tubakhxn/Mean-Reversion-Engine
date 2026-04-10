import pandas as pd

class Backtest:
    def __init__(self, signals: pd.DataFrame):
        self.signals = signals.copy()
        self.results = None

    def run(self):
        df = self.signals.copy()
        df['position'] = df['signal'].shift(1).fillna(0)
        df['returns'] = df['price'].pct_change().fillna(0)
        df['strategy_returns'] = df['position'] * df['returns']
        df['equity_curve'] = (1 + df['strategy_returns']).cumprod()
        self.results = df
        return df

    def performance_metrics(self):
        df = self.results if self.results is not None else self.run()
        total_return = df['equity_curve'].iloc[-1] - 1
        trades = df['signal'].diff().abs().sum() / 2
        wins = ((df['strategy_returns'] > 0) & (df['position'] != 0)).sum()
        win_rate = wins / trades if trades > 0 else 0
        drawdown = (df['equity_curve'] / df['equity_curve'].cummax() - 1).min()
        return {
            'Total Return': total_return,
            'Win Rate': win_rate,
            'Drawdown': drawdown,
            'Trades': trades
        }
