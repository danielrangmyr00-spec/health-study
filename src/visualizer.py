import matplotlib.pyplot as plt
import pandas as pd

def plot_bloodpressure_age(df):
    """
    Scatterplot: Blood pressure vs Age.

    Args:
        df (pd.DataFrame): Health dataset.
    """
    plt.figure(figsize=(8,5))
    plt.scatter(df["age"], df["systolic_bp"])
    plt.xlabel("Age")
    plt.ylabel("Blood Pressure")
    plt.title("Blood Pressure vs Age")
    plt.grid(True)
    plt.show()


def plot_bmi_bloodpressure(df):
    """
    Scatter plot: BMI vs Blood pressure.

    Args:
        df (pd.DataFrame): Health dataset with BMI column.
    """
    plt.figure(figsize=(8,5))
    plt.scatter(df["BMI"], df["systolic_bp"])
    plt.xlabel("BMI")
    plt.ylabel("Blood Pressure")
    plt.title("BMI vs Blood Pressure")
    plt.grid(True)
    plt.show()


def plot_bloodpressure_by_agegroup(df):
    """
    Bar chart: Mean Blood pressure per age group.

    Args:
        df (pd.DataFrame): Health dataset.
    """
    df = df.copy()
    df["AgeGroup"] = pd.cut(
        df["age"], 
        bins=[0, 30, 50, 70, 100],
        labels=["0–30", "30–50", "50–70", "70+"])

   
    plt.figure(figsize=(8,5))
    df.groupby("AgeGroup", observed=True)["systolic_bp"].mean().plot(kind="bar", color="skyblue")
    plt.title("Average Blood Pressure per Age Group")
    plt.xlabel("Age Group")
    plt.ylabel("Mean Blood Pressure")
    plt.grid(True)
    plt.show()
