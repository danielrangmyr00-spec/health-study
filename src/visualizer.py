import matplotlib.pyplot as plt
import pandas as pd

def plot_bloodpressure_age(df):
    """
    Plot blood pressure vs age.

    Args:
        df (pd.DataFrame): Health dataset.
    """
    plt.scatter(df["age"], df["systolic_bp"])
    plt.xlabel("Age")
    plt.ylabel("Blood Pressure")
    plt.title("Blood Pressure vs Age")
    plt.show()


def plot_bmi_bloodpressure(df):
    """
    Scatter plot showing the relationship between BMI and blood pressure.

    Args:
        df (pd.DataFrame): Health dataset with BMI column.
    """
    plt.scatter(df["BMI"], df["systolic_bp"])
    plt.xlabel("BMI")
    plt.ylabel("Blood Pressure")
    plt.title("BMI vs Blood Pressure")
    plt.show()


def plot_bloodpressure_by_agegroup(df):
    """
    Bar chart of average blood pressure per age group.

    Args:
        df (pd.DataFrame): Health dataset.
    """
    df = df.copy()
    df["AgeGroup"] = pd.cut(df["age"], bins=[0, 30, 50, 70, 100],
                            labels=["0–30", "30–50", "50–70", "70+"])

    df.groupby("AgeGroup")["systolic_bp"].mean().plot(kind="bar")
    plt.title("Average Blood Pressure per Age Group")
    plt.xlabel("Age Group")
    plt.ylabel("Mean Blood Pressure")
    plt.show()
