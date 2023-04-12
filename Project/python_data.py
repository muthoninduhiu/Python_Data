import pandas as p
from matplotlib import pyplot as plt
from pandas import DataFrame

# Use Pandas to read in the sales data from the CSV file provided in the
# “student materials” folder on Slack (sales_dataset.csv)
df = p.read_csv('sales_dataset.csv')

# print(df.head())
categories = df['Category']
product = df['Product Name']
quantity = df['Quantity Sold']
month = df['Month']
customer_name = df["Customer Name"]
sales = df['Sale Price']

df["Total Sales"] = df["Quantity Sold"] * df["Sale Price"]


# # Calculate the total sales for each product
def total_sales():
    # multiply the two columns quantity sold and sales price to get total sale of each product
    sales_by_product = df.groupby("Product Name")["Total Sales"].sum()
    sales_by_product.to_csv('product_total_sales.csv')
    # print(sales_by_product)
    return sales_by_product



# Determine the average sale price for each product category
def average_sale_price():
    # group each product by category
    average_sale_categories = df.groupby("Category")['Total Sales'].mean()
    # print(average_sale_categories)
    average_sale_categories.to_csv('category_average_price.csv')
    return average_sale_categories


# # Identify the month with the highest sales and the month with the lowest sales
def month_sales():
    monthly_sales = df.groupby("Month")['Total Sales'].sum()
    # Sort the DataFrame by total sales in descending order to find the highest month
    highest_monthly_sale = monthly_sales.sort_values(ascending=False).head(1).to_csv('highest_monthly_sale.csv')

    # Sort the DataFrame by total sales in ascending order to find the lowest month
    lowest_monthly_sale = monthly_sales.sort_values().head(1).to_csv('lowest_monthly_sale.csv')
    # print(highest_monthly_sale)
    # print(lowest_monthly_sale)
    # Return the highest and lowest months
    return highest_monthly_sale, lowest_monthly_sale

