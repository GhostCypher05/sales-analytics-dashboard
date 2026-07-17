import matplotlib.pyplot as plt
import textwrap

from data_loader import load_data

df = load_data()

def create_bar_chart(data, title, xlabel, ylabel, filename, wrap_labels=False):
    plt.figure(figsize=(8, 5))
    bars = plt.bar(data.index, data.values, color='steelblue')

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f'${height:,.0f}',
            ha='center',
            va='bottom',
            fontsize=9
        )

    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.show()


def create_line_chart(data, title, xlabel, ylabel, filename):
    plt.figure(figsize=(10, 5))
    plt.plot(
    data.index.astype(str),
    data.values,
    marker="o",
    linewidth=2,
    )
    plt.title(title, fontsize=14, fontweight="bold")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.xticks(rotation=45)

    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()

    plt.savefig(filename, dpi=300)

    plt.show()

def create_horizontal_bar_chart(data, title, xlabel, ylabel, filename, wrap_labels=False, wrap_width=25, figsize=(14, 8)):
    if wrap_labels:
        labels = [
            textwrap.fill(label, width=wrap_width) if len(label) > wrap_width else label
            for label in data.index
        ]
    else:
        labels = data.index

    plt.figure(figsize=figsize)

    bars = plt.barh(labels, data.values, color="steelblue")

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    for bar in bars:
        width = bar.get_width()
        plt.text(
            width + 500,
            bar.get_y() + bar.get_height() / 2,
            f'${width:,.0f}',
            ha='left',
            va='center',
            fontsize=9
        )

    plt.grid(axis="x", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.show()


def create_scatter_plot(x_data, y_data, title, xlabel, ylabel, filename):
    plt.figure(figsize=(10, 6))
    plt.scatter(x_data, y_data, alpha=0.7)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.show()

sales_by_region = (
    df.groupby("Region")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

profit_by_region = (
    df.groupby("Region")["Profit"]
      .sum()
      .sort_values(ascending=False)
)

sales_by_category = (
    df.groupby("Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

profit_by_category = (
    df.groupby("Category")["Profit"]
      .sum()
      .sort_values(ascending=False)
)

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()
)

top_products_sales = (
    df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

top_products_profit = (
    df.groupby("Product Name")["Profit"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

sales_by_segment = (
    df.groupby("Segment")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

profit_by_segment = (
    df.groupby("Segment")["Profit"]
      .sum()
      .sort_values(ascending=False)
)

sales_by_sub_category = (
    df.groupby("Sub-Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

profit_by_sub_category = (
    df.groupby("Sub-Category")["Profit"]
      .sum()
      .sort_values(ascending=False)
)



## chart generation


create_bar_chart(
    sales_by_region,
    "Regional Sales Performance",
    "Region",
    "Sales ($)",
    "sales_by_region.png"
)

create_bar_chart(
    profit_by_region,
    "Regional Profit Performance",
    "Region",
    "Profit ($)",
    "profit_by_region.png"
)

create_bar_chart(
    sales_by_category,
    "Sales by Category",
    "Category",
    "Sales ($)",
    "sales_by_category.png"
)

create_bar_chart(
    profit_by_category,
    "Profit by Category",
    "Category",
    "Profit ($)",
    "profit_by_category.png"
)


create_line_chart(
    monthly_sales,
    "Monthly Sales Trend",
    "Month",
    "Sales ($)",
    "monthly_sales_trend.png"   
)

create_horizontal_bar_chart(top_products_sales,
    "Top 10 Products by Sales",
    "Sales ($)", "Product Name",
    "top_products_sales.png",
    wrap_labels=True
)

create_horizontal_bar_chart(top_products_profit,
    "Top 10 Products by Profit",
    "Profit ($)", "Product Name",
    "top_products_profit.png",
    wrap_labels=True,
)

create_bar_chart(sales_by_segment,
    "Sales by Customer Segment",
    "Segment",
    "Sales ($)",
    "sales_by_segment.png"
)

create_bar_chart(profit_by_segment,
    "Profit by Customer Segment",
    "Segment",
    "Profit ($)",
    "profit_by_segment.png"
)

create_horizontal_bar_chart(sales_by_sub_category,
    "Sales by Sub-Category",
    "Sales ($)", "Sub-Category",
    "sales_by_sub_category.png",
    wrap_labels=True
)

create_horizontal_bar_chart(profit_by_sub_category,
    "Profit by Sub-Category",
    "Profit ($)", "Sub-Category",
    "profit_by_sub_category.png",
    wrap_labels=True
)

create_scatter_plot(
    df['Discount'],
    df['Profit'],
    "Discount vs Profit",
    "Discount",
    "Profit",
    "discount_vs_profit.png"
)
