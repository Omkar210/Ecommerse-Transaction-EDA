import numpy as np
import pandas as pd


# Load Data

df = pd.read_csv("ecommerce-transactions-raw.csv")
df.head()

# Information about Data

df.info()

df.describe()

df.describe(include='object')

# Missing Values

from enum import unique

nulls = df.isnull().sum()
duplicate = df.duplicated().sum()
dtype = df.dtypes
unique_value = df.nunique()

before_cleaning = pd.DataFrame({
    'Total Null Value' : nulls,
    'Data Value' : dtype,
    'Unique Value' : unique_value
})

print(before_cleaning)

# return_date/return_reason

before = df[['return_date','return_reason']].isnull().sum()
df['return_date'] = df['return_date'].fillna(0)
df['return_reason'] = df['return_reason'].fillna(0)
after = df[['return_date','return_reason']].isnull().sum()
print(f'Return Date/Return Reason : {before}    ->     {after}missing')

# return_amount

before = df["refund_amount"].isnull().sum()
df["refund_amount"] = df["refund_amount"].fillna(0.0)
after = df["refund_amount"].isnull().sum()
print(f"Refund Amount : {before}    ->    {after} missing")

# Shipping Cost

before = df["shipping_cost"].isnull().sum()
df["shipping_cost"] = df["shipping_cost"].fillna(0.0)
after  = df["shipping_cost"].isnull().sum()
print(f"Shipping Cost : {before}    ->    {after} missing")

# Loyalty Member

before = df['loyalty_member'].isnull().sum()
df['loyalty_member'] = df['loyalty_member'].fillna('Unknown')
after = df['loyalty_member'].isnull().sum()
print(f'Loyalty Member : {before}   ->   {after} missing')

# Delivery Date

before = df['delivery_date'].isnull().sum()
df['delivery_date'] = df['delivery_date'].fillna('Unknown')
after = df['delivery_date'].isnull().sum()
print(f'Delivery Date : {before}   ->   {after} missing')

# delivery_days

before = df["delivery_days"].isnull().sum()
df["delivery_days"] = df['delivery_days'].fillna(-1)
after  = df["delivery_days"].isnull().sum()
print(f"Shipping Cost : {before}    ->    {after} missing")

# Payment mode

before = df['payment_mode'].isnull().sum()
mode_val = df['payment_mode'].mode()[0]
df['payment_mode'] = df['payment_mode'].fillna(mode_val)
after = df['payment_mode'].isnull().sum()
print(f'Payment Mode : {before}    ->    {after} missing')

# seller_rating & customer_rating

for col in ["seller_rating", "customer_rating"]:
    before = df[col].isnull().sum()
    overall_median = df[col].median()

    df[col] = df.groupby("product_category")[col].transform(lambda x: x.fillna(x.median()))

    df[col] = df[col].fillna(overall_median)
    after = df[col].isnull().sum()
    print(f"{col}: {before}    ->    {after} missing")

# Post Cleaning Validation

from enum import unique

nulls = df.isnull().sum()
duplicate = df.duplicated().sum()
dtype = df.dtypes
unique_value = df.nunique()

after_cleaning = pd.DataFrame({
    'Total Null Value' : nulls,
    'Data Value' : dtype,
    'Unique Value' : unique_value
})

print(after_cleaning)