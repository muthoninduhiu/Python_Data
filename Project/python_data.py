import pandas as p

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


# print(customer_name)

# category_grouped = df.groupby('Product Name')
# print(category_grouped)

#
# sales_by_product = df.groupby("Customer Name")["Sale Price"].max()
# print(sales_by_product)
#

# # Calculate the total sales for each product
def total_sales():
    # multiply the two columns quantity sold and sales price to get total sale of each product
    df["Total Sales"] = df["Quantity Sold"] * df["Sale Price"]
    print(df)

total_sales()
#
# # Determine the average sale price for each product category
# def average_sale_price():
#     print()
#
# # Identify the month with the highest sales and the month with the lowest sales
#
# # Determine which customers made the most purchases and how much they spent in total
# # Write the results of your analysis as a CSV file
