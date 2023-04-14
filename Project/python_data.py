"""
This program reads in sales data from a CSV file and performs various data analysis tasks,
such as calculating total sales by product, determining the average sale price by product category,
identifying the month with the highest and lowest sales, and determining the customers who made the
 most purchases and how much they spent in total. The program then merges the results of these
 analyses into a single DataFrame and writes it to a CSV file.

The program also includes several functions to plot the results of these analyses using Matplotlib.

Functions:
- total_sales: calculates the total sales for each product
- average_sale_price: determines the average sale price for each product category
- month_sales: identifies the month with the highest and lowest sales
- customer_purchase: determines which customers made the most purchases and how much they spent in total
- merge_results: reads in the individual CSV files produced by the above functions, renames their columns,
 concatenates them into a single DataFrame, and writes it to a CSV file
- plot_average_sale: plots the average sale price for each product category
- show_products_sales: plots the total sales for each product
- show_monthly_trend: plots the monthly sales trend
- show_customer_purchase: plots the total sales for each customer

"""
import pandas as p
from matplotlib import pyplot as plt

# Use Pandas to read in the sales data from the CSV file provided in the
# “student materials” folder on Slack (sales_dataset.csv)
df = p.read_csv('sales_dataset.csv')

# print(df.head())
# categories = df['Category']
# product = df['Product Name']
# quantity = df['Quantity Sold']
# month = df['Month']
# customer_name = df["Customer Name"]
# sales = df['Sale Price']
# define a new column with the total sales
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


# # Determine which customers made the most purchases and how much they spent in total
def customer_purchase():
    customer_data = df.groupby("Customer Name")['Total Sales'].sum()
    customer_data.to_csv('customers.csv')
    most_spendthrift_customer = customer_data.sort_values(ascending=False).head(1)
    most_spendthrift_customer.to_csv('customer_data.csv')
    # print(most_spendthrift_customer)
    return most_spendthrift_customer


def merge_results():
    # Read in the individual CSV files
    sales_by_product = p.read_csv('product_total_sales.csv')
    avg = p.read_csv('category_average_price.csv')
    highest_monthly_sales = p.read_csv('highest_monthly_sale.csv')
    lowest_monthly_sales = p.read_csv('lowest_monthly_sale.csv')
    customer_data = p.read_csv('customer_data.csv')

    # Rename the columns of each DataFrame
    sales_by_product = sales_by_product.rename(columns={'Total Sales': 'Sales by Product'})
    avg = avg.rename(columns={'Total Sales': 'Category Average Price'})
    highest_monthly_sales = highest_monthly_sales.rename(columns={'Total Sales': 'Highest Monthly Sales'})
    lowest_monthly_sales = lowest_monthly_sales.rename(columns={'Total Sales': 'Lowest Monthly Sales'})
    customer_data = customer_data.rename(columns={'Total Sales': 'Highest Customer Sales'})

    # Concatenate the DataFrames along a common axis (in this case, axis=1 since we want to join them horizontally)
    merged_data = p.concat(
        [sales_by_product, avg, highest_monthly_sales, lowest_monthly_sales, customer_data], axis=1)

    # Write the merged data to a CSV file
    merged_data.to_csv('merged_data.csv', index=False)


def plot_average_sale():
    # Average sale price for each product category
    avg_sale_price = average_sale_price().sort_values()
    avg_sale_price.plot.bar(x='Category', y='Total Sales')
    plt.title('Average Sale Price by Category')
    plt.xlabel('Category')
    plt.ylabel('Average Sale Price')
    plt.xticks(rotation=12)
    plt.show()


def show_products_sales():
    # Get the total sales by product
    total_product_price = total_sales().sort_values()

    # Create a horizontal bar plot
    plt.figure(figsize=(10, 6))
    ax = total_product_price.plot.barh(x='Product Name', y='Total Sales')

    # Set title and axis labels
    plt.title('Product Sale Trend', fontsize=18)
    plt.xlabel('Total Sale', fontsize=14)
    plt.ylabel('Product', fontsize=14)

    # Add grid lines
    ax.grid(axis='x')

    # Increase font size of tick labels
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=7)

    # Show the plot
    plt.show()


def show_monthly_trend():
    # Monthly sales trend
    monthly_sales = df.groupby("Month")['Total Sales'].sum().sort_values()
    monthly_sales.plot.line()
    plt.title('Monthly Sales Trend')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.show()


def show_customer_purchase():
    # Read in the sales data from the CSV file provided in the “student materials” folder on Slack (sales_dataset.csv)
    data_frame = p.read_csv('customers.csv')

    # Calculate the total sales for each customer
    sales_by_customer = data_frame.groupby("Customer Name")["Total Sales"].sum().sort_values()
    # Create a horizontal bar chart to show the total sales by customer
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.barh(sales_by_customer.index, sales_by_customer)
    ax.set_xlabel('Total Purchase')
    ax.set_ylabel('Customer Name')
    ax.set_title('Total Purchases by Customer')
    ax.grid(axis='x')
    plt.show()

# TODO:
# def customer_product_relation():
#     # Group by customer and product and calculate the total sales for each combination
#     customer_product_data = df.groupby(["Customer Name", "Product Name"])["Total Sales"].sum()
#
#     # Reshape the data to have customers as rows and products as columns
#     customer_product_pivot = customer_product_data.unstack(level=-1)
#
#     # Fill any missing values with 0
#     customer_product_pivot = customer_product_pivot.fillna(0)
#
#     # Write the customer-product relation data to a CSV file
#     customer_product_pivot.to_csv('customer_product_relation.csv')
#     return customer_product_pivot
#
#
# def plot_customer_product_relation():
#     # Get the customer-product relation data
#     customer_product_pivot = customer_product_relation()
#
#     # Create the plot
#     fig, ax = plt.subplots()
#     im = ax.imshow(customer_product_pivot, cmap='Blues')
#
#     # Set the axis labels and title
#     ax.set_xlabel('Product Name')
#     ax.set_ylabel('Customer Name')
#     ax.set_title('Customer-Product Relation')
#
#     # Create a color bar
#     cbar = ax.figure.colorbar(im, ax=ax)
#
#     # Rotate the x-axis labels to make them more readable
#     plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
#              rotation_mode="anchor")
#
#     # Show the plot
#     plt.show()


if __name__ == '__main__':
    total_sales()
    average_sale_price()
    month_sales()
    customer_purchase()
    merge_results()
    plot_average_sale()
    show_products_sales()
    show_monthly_trend()
    show_customer_purchase()
