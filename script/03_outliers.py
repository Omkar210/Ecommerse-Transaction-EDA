import numpy as np
import pandas as pd


# Load Data

df = pd.read_csv("ecommerce-transactions-raw.csv")
df.head()

# Information about Data

df.info()

df.describe()

df.describe(include='object')

# Outliers Detection

