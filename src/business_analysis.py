from src.data_loader import load_data

# Load cleaned dataset
df = load_data()

def calculate_kpis(df): #======> For KPIs part 

    total_sales = (
    df['Sales'].sum()
    )

    total_profit = (
    df['Profit'].sum()
    )

    total_orders = (
    df["Order ID"].count()
    )

    total_customers = (
    df["Customer ID"].nunique()
    )




 
    return {
        "total_sales":total_sales,
        "total_profit":total_profit,
        "total_orders":total_orders,
        "total_customers":total_customers,
        
    }

sales_by_category = (
    df.groupby("Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
    )

if __name__ == "__main__":
    print("*" * 50)
    print("\n Key Business Insights:")
    print("\n*" * 50)

    total_profit_by_region = df.groupby("Region")["Profit"].sum().sort_values(ascending=False)
    print("\nTotal Profit by Region:")
    print(total_profit_by_region.head())

    total_sales_by_category = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
    print("\nTotal Sales by Category:")
    print(total_sales_by_category.head())

    total_profit_by_category = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
    print("\nTotal Profit by Category:")
    print(total_profit_by_category.head())

    # top 10 products by sales
    top_products_by_sales = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)
    print("\nTop 10 Products by Sales:")
    print(top_products_by_sales)

    # Regional summary
    regional_summary = df.groupby("Region").agg({"Sales": "sum",
                                                  "Profit": "sum",
                                                  "Quantity": "sum"}).sort_values(by="Sales", ascending=False)

    ##############
    # Business Analysis Summary
    ##############
    # Highest sales region
    highest_sales_region = regional_summary["Sales"].index[0]
    print(f"\nHighest Sales Region: {highest_sales_region}")

    # Highest sales amount
    highest_sales_amount = regional_summary["Sales"].iloc[0]
    print(f"\nHighest Sales Amount: ${highest_sales_amount:,.2f}")

    # highest  profit region
    highest_profit_region = regional_summary["Profit"].index[0]
    print(f"\nHighest Profit Region: {highest_profit_region}")

    # highest profit amount
    highest_profit_amount = regional_summary["Profit"].iloc[0]
    print(f"\nHighest Profit Amount: ${highest_profit_amount:,.2f}")

    # highest category by sales
    highest_sales_category = sales_by_category.index[0]
    print(f"\nHighest Sales Category: {highest_sales_category}")

    # highest category by sales amount
    highest_category_sales_amount = sales_by_category.iloc[0]
    print(f"\nHighest Category Sales Amount: ${highest_category_sales_amount:,.2f}")

    # highest profit category
    highest_profit_category = total_profit_by_category.index[0]
    print(f"\nHighest Profit Category: {highest_profit_category}")

    # highest profit category amount
    highest_profit_category_amount = total_profit_by_category.iloc[0]
    print(f"\nHighest Profit Category Amount: ${highest_profit_category_amount:,.2f}")

    # best_selling_product
    best_selling_product = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).index[0]
    print(f"\nBest Selling Product: {best_selling_product}")

    # Best_selling_product_amount
    best_selling_product_amount = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).iloc[0]
    print(f"\nBest Selling Product Amount: ${best_selling_product_amount:,.2f}")

    # Most profitable product
    most_profitable_product = df.groupby("Product Name")["Profit"].sum().sort_values(ascending=False).index[0]
    print(f"\nMost Profitable Product: {most_profitable_product}")

    # Most profitable product amount
    most_profitable_product_amount = df.groupby("Product Name")["Profit"].sum().sort_values(ascending=False).iloc[0]
    print(f"\nMost Profitable Product Amount: ${most_profitable_product_amount:,.2f}")