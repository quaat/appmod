import numpy as np
import pandas as pd

def mean(df : pd.DataFrame) -> pd.DataFrame:
    """
    Computes the mean of each numeric column in the given DataFrame and returns
    these means as a new one-row DataFrame.
    """

    # Select only numeric columns to avoid issues with non-numeric data
    numeric_df = df.select_dtypes(include=[np.number])

    # Calculate the mean for each numeric column
    mean_series = numeric_df.mean()

    # Convert the Series (means) to a one-row DataFrame
    mean_df = pd.DataFrame([mean_series.values], columns=mean_series.index)

    return mean_df

def max(df : pd.DataFrame) :
    numeric_df = df.select_dtypes(include=[np.number])
    max_series = numeric_df.max()
    max_df = pd.DataFrame([max_series.values], columns=max_series.index)
    return max_df

def min(df : pd.DataFrame) :
    numeric_df = df.select_dtypes(include=[np.number])
    min_series = numeric_df.max()
    min_df = pd.DataFrame([min_series.values], columns=min_series.index)
    return min_df
