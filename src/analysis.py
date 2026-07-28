from src.data_loader import load_data

# Load cleaned dataset
df = load_data()

print("=" * 50)
print("KEY PERFORMANCE INDICATORS")
print("=" * 50)

# Total Sales
total_sales = df["Sales"].sum()

# Total Profit
total_profit = df["Profit"].sum()

# Profit Margin
profit_margin = (total_profit / total_sales) * 100

# Total Orders
total_orders = df["Order ID"].nunique()

#total_quantity sold
total_quantity_sold = df["Quantity"].sum()

# Average Order Value
average_order_value = total_sales / total_orders

# Average Profit Per Order
average_profit_per_order = total_profit / total_orders

#Average Items per order 
average_items_per_order = total_quantity_sold / total_orders

print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Profit Margin: {profit_margin:.2f}%")
print(f"Total Orders: {total_orders:,}")
print(f"Average Order Value: ${average_order_value:,.2f}")
print(f"Average Profit Per Order: ${average_profit_per_order:,.2f}")
print(f"Average Items Per Order: {average_items_per_order:,.2f}")
