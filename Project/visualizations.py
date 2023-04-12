from matplotlib import pyplot as plt

from Project.python_data import average_sale_price, total_sales

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



