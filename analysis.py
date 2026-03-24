import pandas as pd

df = pd.read_csv("cleaned_data.csv")

print(df.head())
print(df.shape)

total_revenue = df['price'].sum()
print("Total Revenue:", total_revenue)

top_products = df.groupby('product_id')['price'].sum().sort_values(ascending=False).head(10)
print(top_products)

top_cities = df.groupby('customer_city')['price'].sum().sort_values(ascending=False).head(10)
print(top_cities)

df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

df['month'] = df['order_purchase_timestamp'].dt.month

monthly_sales = df.groupby('month')['price'].sum()

print(monthly_sales)

import matplotlib.pyplot as plt

monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.show()

category_sales = df.groupby('product_category_name')['price'].sum().sort_values(ascending=False).head(10)

print(category_sales)

df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
df['order_estimated_delivery_date'] = pd.to_datetime(df['order_estimated_delivery_date'])

df['delay'] = (df['order_delivered_customer_date'] - df['order_estimated_delivery_date']).dt.days

print(df['delay'].describe())

import seaborn as sns

sns.barplot(x=category_sales.values, y=category_sales.index)
plt.title("Top Categories by Revenue")
plt.show()