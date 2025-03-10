import numpy as np
import pandas as pd

def mean(s: pd.Series) -> pd.Series:
    """
    Computes the mean of a numeric Series and returns
    that mean as a single-value Series.
    """
    # Calculate the mean
    mean_val = s.mean()

    # Return a single-value Series (the index label is up to you)
    return pd.Series([mean_val], index=[s.name or "mean"])

def max(s: pd.Series) -> pd.Series:
    """
    Computes the maximum of a numeric Series and returns
    that max as a single-value Series.
    """
    max_val = s.max()

    return pd.Series([max_val], index=[s.name or "max"])

def min(s: pd.Series) -> pd.Series:
    """
    Computes the minimum of a numeric Series and returns
    that min as a single-value Series.
    """
    min_val = s.min()

    return pd.Series([min_val], index=[s.name or "min"])
