import plotly.express as px
from data_loader import load_data

df = load_data()

## getting the required data for visualizations
sales_by_region = (
    df.groupby("Region")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .reset_index()
)

profit_by_region = (
    df.groupby("Region")["Profit"]
      .sum()
      .sort_values(ascending=False)
      .reset_index()
)

sales_by_category = (
    df.groupby("Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .reset_index()
)

profit_by_category = (
    df.groupby("Category")["Profit"]
      .sum()
      .sort_values(ascending=False)
      .reset_index()
)

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
      .sum()
      .reset_index()
)
## converting the 'Order Date' column to string for better visualization
monthly_sales["Order Date"] = monthly_sales["Order Date"].astype(str)


top_10_products_by_sales = (
    df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
      .reset_index()
)


top_10_products_by_profit = (
    df.groupby("Product Name")["Profit"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
      .reset_index()
)

sales_by_segment = (
    df.groupby("Segment")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .reset_index()
)

profit_by_segment = (
    df.groupby('Segment')['Profit']
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

sales_by_sub_category = (
    df.groupby('Sub-Category')['Sales']
      .sum()
      .sort_values(ascending=False)
      .reset_index()
)

profit_by_sub_category = (
    df.groupby('Sub-Category')['Profit']
    .sum()
    .sort_values(ascending=False)
    .reset_index()

)
discount_to_profit = (
    df.groupby('Discount')['Profit']
    .sum()
    .sort_values()
    .reset_index()
)

def create_plotly_bar_chart(data, x, y , color = None, x_label=None, y_label=None, metric_name=None):
    fig = px.bar(
        data,
        x=x,
        y=y,
        color=color,
        color_continuous_scale="Blues",
        text_auto='.2s'
    )

    fig.update_layout(
        xaxis_title=x_label or x,
        yaxis_title=y_label or y,
        title_x=0.5,
        template="plotly_white",
        hovermode="x",
    )
    fig.update_traces(
        hovertemplate=f"<b>%{{x}}</b><br>{metric_name}: %{{y:$,.2f}}<extra></extra>",
    )

    return fig

def create_plotly_line_chart(data, x, y, x_label=None, y_label=None, metric_name=None):
    fig = px.line(
        data,
        x=x,
        y=y,
        
        markers=True,
    )

    fig.update_layout(
        xaxis_title=x_label or x,
        yaxis_title=y_label or y,
        title_x=0.5,
        template="plotly_white",
        hovermode="x",
    )
    fig.update_traces(
        hovertemplate=f"<b>%{{x}}</b><br>{metric_name}: %{{y:$,.2f}}<extra></extra>",
    )

    return fig

def create_plotly_scatter_chart(data, x, y, x_label = None, y_label = None, metric_name=None):
    fig = px.scatter(
        data,
        x=x,
        y=y,
        
    )
    fig.update_layout(
        xaxis_title=x_label or x,
        yaxis_title=y_label or y,
        title_x=0.5,
        template="plotly_white",
        hovermode="closest",
    )
    fig.update_traces(
        hovertemplate=f"<b>%{{x}}</b><br>{metric_name}: %{{y:$,.2f}}<extra></extra>",
    )
    return fig


####### Creating the visualizations using the functions defined above

charts = [
    {
        "chart_id": "sales_by_region",
        "data": sales_by_region,
        "title": "Total Sales by Region",
        "x": "Region",
        "y": "Sales",
        "color": "Sales",
        "metric_name": "Sales",
        "chart_type":"bar"
    },
    {
        "chart_id": "profit_by_region",
        "data": profit_by_region,
        "title": "Total Profit by Region",
        "x": "Region",
        "y": "Profit",
        "color": "Profit",
        "metric_name": "Profit",
        "chart_type":"bar"   
    },
    {
        "chart_id": "monthly_sales",
        "data":monthly_sales,
        "title": "monthly sales trend",
        "x": "Order Date",
        "y": "Sales",
        "metric_name": "sales",
        "chart_type":"line" 

    },
    {
        "chart_id": "sales_by_category",
        "data": sales_by_category,
        "title": "Total Sales by Category",
        "x": "Category",
        "y": "Sales",
        "color": "Sales",
        "metric_name": "Sales",
        "chart_type":"bar"
    },
    {
        "chart_id": "profit_by_category",
        "data": profit_by_category,
        "title": "Total Profit by Category",
        "x": "Category",
        "y": "Profit",
        "color": "Profit",
        "metric_name": "Profit",
        "chart_type":"bar"
    },
    {
        "chart_id": "top_10_products_by_sales",
        "data": top_10_products_by_sales,
        "title": "Top 10 Products by Sales",
        "x": "Product Name",
        "y": "Sales",
        "color": "Sales",
        "metric_name": "Sales",
        "chart_type":"bar"
    },
    {
        "chart_id": "top_10_products_by_profit",
        "data": top_10_products_by_profit,
        "title": "Top 10 Products by Profit",
        "x": "Product Name",
        "y": "Profit",
        "color": "Profit",
        "metric_name": "Profit",
        "chart_type":"bar"
    },
    {
        "chart_id": "sales_by_segment",
        "data": sales_by_segment,
        "title": "Total Sales by Segment",
        "x": "Segment",
        "y": "Sales",
        "color": "Sales",
        "metric_name": "Sales",
        "chart_type":"bar"
    },
    {
        "chart_id": "profit_by_segment",
        "data": profit_by_segment,
        "title": "Profits from each segment",
        "x": "Segment",
        "y": "Profit",
        "color": "Profit",
        "metric_name": "Profit",
        "chart_type":"bar"
    },
    {
        "chart_id": "sales_by_sub_category",
        "data": sales_by_sub_category,
        "title": "Sales by different Sub Categories",
        "x": "Sub-Category",
        "y": "Sales",
        "color": "Sales",
        "metric_name": "Sales" ,
        "chart_type":"bar"
    },
    {
        "chart_id": "profit_by_sub_category",
        "data": profit_by_sub_category,
        "title": "Profit by different Sub Categories",
        "x": "Sub-Category",
        "y": "Profit",
        "color": "Profit",
        "metric_name": "Profit",
        "chart_type":"bar" 
    },
    {
        "chart_id": "discount_to_profit",
        "data": discount_to_profit,
        "title": "Discount to profit relationship",
        "x":"Discount",
        "y":"Profit",
        "color":"none",
        "metric_name":"Profit",
        "chart_type":"scatter"

    }
]

def generate_all_figures(df):
    
    figures = {}
    
    for chart in charts:
            if  chart["chart_type"]=="bar":
                fig = create_plotly_bar_chart(
                    data=chart["data"],
                    x=chart["x"],
                    y=chart["y"],
                    color=chart.get("color"),
                    metric_name=chart["metric_name"],
                )
                figures[chart["chart_id"]] = fig
                
            elif chart["chart_type"]== "line":
                fig = create_plotly_line_chart(
                    data=chart["data"],
                    x=chart["x"],
                    y=chart["y"],
                    metric_name=chart["metric_name"]  
                )
                figures[chart["chart_id"]] = fig
            
            elif chart["chart_type"] == "scatter":
                fig = create_plotly_scatter_chart(
                    data=chart["data"],
                    x=chart["x"],
                    y=chart["y"],
                    metric_name=chart["metric_name"]
                )
                figures[chart["chart_id"]] = fig
    return figures      