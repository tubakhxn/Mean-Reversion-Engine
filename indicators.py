import pandas as pd
import numpy as np

def rolling_mean(series: pd.Series, window: int) -> pd.Series:
    return series.rolling(window=window, min_periods=1).mean()

def rolling_std(series: pd.Series, window: int) -> pd.Series:
    return series.rolling(window=window, min_periods=1).std(ddof=0)

def zscore(series: pd.Series, window: int) -> pd.Series:
    mean = rolling_mean(series, window)
    std = rolling_std(series, window)
    return (series - mean) / std
