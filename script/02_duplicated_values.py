import numpy as np
import pandas as pd

# Load Data
df = pd.read_csv("ecommerce-transactions-raw.csv")
df.head()

# Information of Data
df.info()

df.describe()

df.describe(include='object')

# Before Duplicate Handled

total = df.duplicated().sum()
dupli_tid = df.duplicated(subset='transaction_id').sum()
unique_tid = df['transaction_id'].nunique()

print(f'Total Duplicate : {total}, \nTransaction ID Duplicate : {dupli_tid}, \nUnique Transaction ID : {unique_tid}')

# Removing Duplicate Transaction ID

df.drop_duplicates(subset='transaction_id', keep='first',inplace=True)

# Post Validating Duplicated Values
total_dup = df.duplicated().sum()
dup_remove_tid = df.duplicated(subset='transaction_id').sum()
print(f'Total Duplicate : {total_dup}, \nTransaction ID Duplicate : {dup_remove_tid}')
