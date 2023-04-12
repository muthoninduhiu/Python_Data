import pandas as p
from matplotlib import pyplot as plt

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


# # Determine which customers made the most purchases and how much they spent in total
def customer_purchase():
    customer_data = df.groupby("Customer Name")['Total Sales'].sum()
    customer_data.to_csv('customers.csv')
    most_spendthrift_customer = customer_data.sort_values(ascending=False).head(1)
    most_spendthrift_customer.to_csv('customer_data.csv')
    # print(most_spendthrift_customer)
    return most_spendthrift_customer, customer_data


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


total_sales()
average_sale_price()
month_sales()
customer_purchase()
merge_results()
# Average sale price for each product category
avg_sale_price = average_sale_price().sort_values()
avg_sale_price.plot.bar(x='Category', y='Total Sales')
plt.title('Average Sale Price by Category')
plt.xlabel('Category')
plt.ylabel('Average Sale Price')
plt.xticks(rotation=12)
plt.show()

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
plt.yticks(fontsize=12)

# Show the plot
plt.show()

# Monthly sales trend
monthly_sales = df.groupby("Month")['Total Sales'].sum().sort_values()
monthly_sales.plot.line()
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()

# Read in the sales data from the CSV file provided in the “student materials” folder on Slack (sales_dataset.csv)
df = p.read_csv('customers.csv')

# Calculate the total sales for each customer
sales_by_customer = df.groupby("Customer Name")["Total Sales"].sum().sort_values()
# Create a horizontal bar chart to show the total sales by customer
fig, ax = plt.subplots(figsize=(10, 10))
ax.barh(sales_by_customer.index, sales_by_customer)
ax.set_xlabel('Total Purchase')
ax.set_ylabel('Customer Name')
ax.set_title('Total Purchases by Customer')
plt.show()
