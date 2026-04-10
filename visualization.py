import matplotlib.pyplot as plt
import pandas as pd

def plot_price_bands(df: pd.DataFrame, window: int):
    mean = df['price'].rolling(window, min_periods=1).mean()
    std = df['price'].rolling(window, min_periods=1).std(ddof=0)
    upper = mean + 2 * std
    lower = mean - 2 * std
    plt.figure(figsize=(12, 6))
    plt.plot(df['price'], label='Price', color='black', linewidth=1.5)
    plt.plot(mean, label='Mean', color='blue', linestyle='--')
    plt.plot(upper, label='+2 Std', color='green', linestyle=':')
    plt.plot(lower, label='-2 Std', color='red', linestyle=':')
    plt.fill_between(df.index, lower, upper, color='gray', alpha=0.1)
    plt.title('Price with Mean and Bands')
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_zscore(df: pd.DataFrame):
    plt.figure(figsize=(12, 4))
    plt.plot(df['z'], label='Z-Score', color='purple')
    plt.axhline(2, color='red', linestyle='--', alpha=0.7)
    plt.axhline(-2, color='green', linestyle='--', alpha=0.7)
    plt.axhline(0, color='black', linestyle=':')
    # Highlight entries/exits
    buy = df[df['signal'] == 1]
    sell = df[df['signal'] == -1]
    plt.scatter(buy.index, buy['z'], marker='^', color='green', label='Buy', zorder=5)
    plt.scatter(sell.index, sell['z'], marker='v', color='red', label='Sell', zorder=5)
    plt.title('Z-Score & Trade Signals')
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_equity_curve(df: pd.DataFrame):
    plt.figure(figsize=(12, 4))
    plt.plot(df['equity_curve'], color='navy', linewidth=2)
    plt.title('Equity Curve')
    plt.tight_layout()
    plt.show()
