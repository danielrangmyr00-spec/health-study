import numpy as np
import pandas as pd


def calculate_bmi(df):
    """
    Add BMI column to the DataFrame.

    BMI = weight (kg) / (height (m))^2

    Args:
        df (pd.DataFrame): Input health dataset.

    Returns:
        pd.DataFrame: DataFrame with a new BMI column.
    """
    df = df.copy()
    df["BMI"] = df["Weight"] / (df["Height"] / 100) ** 2
    return df


class HealthAnalyzer:
    """
    A class for performing statistical analysis on health data.

    Methods:
        mean_blood_pressure(): Returns mean blood pressure.
        age_weight_regression(): Simple linear regression using NumPy.
    """

    def __init__(self, df):
        """
        Initialize the analyzer with a dataset.

        Args:
            df (pd.DataFrame): Health dataset.
        """
        self.df = df

    def mean_blood_pressure(self):
        """
        Calculate the mean blood pressure.

        Returns:
            float: Mean blood pressure.
        """
        return self.df["BloodPressure"].mean()

    def age_weight_regression(self):
        """
        Perform linear regression using the normal equation:
            beta = (X^T X)^(-1) X^T y

        Predicts BloodPressure using Age and Weight.

        Returns:
            np.ndarray: Regression coefficients [bias, age_coeff, weight_coeff]
        """
        X = self.df[["Age", "Weight"]].values
        y = self.df["BloodPressure"].values

        # Add bias term
        X = np.c_[np.ones(X.shape[0]), X]

        # Normal equation
        beta = np.linalg.inv(X.T @ X) @ (X.T @ y)
        return beta
