import plotly.express as px

charts = [ # configurations for the function that would create the charts
    {
        "chart_id": "sales_by_region",
        "dataset": "sales_by_region",
        "x": "Region",
        "y": "Sales",
        "color": "Sales",
        "metric_name": "Sales",
        "chart_type":"bar",
        "orientation": "v"

    },
    {
        "chart_id": "profit_by_region",
        "dataset": "profit_by_region",
        "x": "Region",
        "y": "Profit",
        "color": "Profit",
        "metric_name": "Profit",
        "chart_type":"bar",
        "orientation": "v"
  
    },
    {
        "chart_id": "monthly_sales",
        "dataset": "monthly_sales",
        "x": "Order Date",
        "y": "Sales",
        "metric_name": "sales",
        "chart_type":"line" 

    },
    {
        "chart_id": "sales_by_category",
        "dataset": "sales_by_category",
        "x": "Category",
        "y": "Sales",
        "color": "Sales",
        "metric_name": "Sales",
        "chart_type":"bar",
        "orientation": "v"

    },
    {
        "chart_id": "profit_by_category",
        "dataset": "profit_by_category",
        "x": "Category",
        "y": "Profit",
        "color": "Profit",
        "metric_name": "Profit",
        "chart_type":"bar",
        "orientation": "v"

    },
    {
        "chart_id": "top_10_products_by_sales",
        "dataset": "top_10_products_by_sales",
        "x": "Sales",
        "y": "Product Name",
        "color": "Sales",
        "metric_name": "Sales",
        "chart_type":"bar",
        "orientation": "h"
    },
    {
        "chart_id": "top_10_products_by_profit",
        "dataset": "top_10_products_by_profit",
        "x": "Profit",
        "y": "Product Name",
        "color": "Profit",
        "metric_name": "Profit",
        "chart_type":"bar",
        "orientation": "h"

    },
    {
        "chart_id": "sales_by_segment",
        "dataset":"sales_by_segment",
        "x": "Segment",
        "y": "Sales",
        "color": "Sales",
        "metric_name": "Sales",
        "chart_type":"bar",
        "orientation": "v"

    },
    {
        "chart_id": "profit_by_segment",
        "dataset": "profit_by_segment",
        "x": "Segment",
        "y": "Profit",
        "color": "Profit",
        "metric_name": "Profit",
        "chart_type":"bar",
        "orientation": "v"

    },
    {
        "chart_id": "sales_by_sub_category",
        "dataset": "sales_by_sub_category",
        "x": "Sub-Category",
        "y": "Sales",
        "color": "Sales",
        "metric_name": "Sales" ,
        "chart_type":"bar",
        "orientation": "v"

    },
    {
        "chart_id": "profit_by_sub_category",
        "dataset": "profit_by_sub_category",
        "x": "Sub-Category",
        "y": "Profit",
        "color": "Profit",
        "metric_name": "Profit",
        "chart_type":"bar",
        "orientation": "v"

    },
    {
        "chart_id": "discount_to_profit",
        "dataset": "discount_to_profit",
        "x":"Discount",
        "y":"Profit",
        "color":None,
        "metric_name":"Profit",
        "chart_type":"scatter"

    }
]

def summarize_data(df, group_by,value_column, top_n=None):
    summary = (
        df.groupby(group_by)[value_column]
          .sum()
          .sort_values(ascending= False)
        
        )
    if top_n:
        summary = summary.head(top_n)
    
    return summary.reset_index()   


def create_plotly_bar_chart(data, x, y , color = None, x_label=None, y_label=None, metric_name=None, orientation = "v"):

    fig = px.bar(
        data,
        x=x,
        y=y,
        color=color,
        color_continuous_scale="Blues",
        text_auto='.2s',
        orientation=orientation
    )
    if orientation == "h":
        hovermode= "closest"
        hovertemplate = (
        f"<b>%{{y}}</b><br>"
        f"{metric_name}: %{{x:$,.2f}}"
        "<extra></extra>"
    )
    else:
        hovermode = "x"
        hovertemplate = (
        f"<b>%{{x}}</b><br>"
        f"{metric_name}: %{{y:$,.2f}}"
        "<extra></extra>"
    )

    fig.update_layout(
        xaxis_title=x_label or x,
        yaxis_title=y_label or y,
        title_x=0.5,
        template="plotly_white",
        hovermode=hovermode,
        yaxis={"categoryorder": "total ascending"}
    )


    fig.update_traces(hovertemplate=hovertemplate)

 


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
        hovertemplate=f"<b>%{{x}}</b><br>{metric_name}:<b> %{{y:$,.2f}}</b><extra></extra>",
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
     hovertemplate=f"<b>%{{x}}</b><br>{metric_name}:<b> %{{y:$,.2f}}</b><extra></extra>",
    )
    return fig


def shorten_labels(series, max_length=25):
    return series.apply(
        lambda x: x if len(x) <= max_length else x[:15] + "..."
    )

####### Creating the visualizations using the functions defined above
def generate_all_figures(df):

## getting the required data for visualizations
    sales_by_region = summarize_data( df, "Region", "Sales")

    profit_by_region = summarize_data(df, "Region", "Profit")

    sales_by_category = summarize_data(df,"Category","Sales")

    profit_by_category = summarize_data(df,"Category","Profit")
    top_10_products_by_sales = summarize_data(df, "Product Name","Sales" ,top_n = 10)
    top_10_products_by_profit = summarize_data(df, "Product Name","Profit", top_n = 10)
    top_10_products_by_sales["Product Name"] = shorten_labels(top_10_products_by_sales["Product Name"])
    top_10_products_by_profit["Product Name"] = shorten_labels(top_10_products_by_profit["Product Name"])
    sales_by_segment = summarize_data(df,"Segment","Sales")
    profit_by_segment = summarize_data(df,'Segment','Profit')
    sales_by_sub_category = summarize_data(df,'Sub-Category','Sales')
    profit_by_sub_category = summarize_data(df,'Sub-Category','Profit')
    discount_to_profit = summarize_data(df,'Discount','Profit')

    monthly_sales = ( # edge case so this is handled seprately
        df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
        .sum()
        .reset_index()
    )
    ## converting the 'Order Date' column to string for better visualization
    monthly_sales["Order Date"] = monthly_sales["Order Date"].astype(str)
 
    datasets = { # ====> Stores the keys to access the various charts from the loop
    "sales_by_region": sales_by_region,
    "profit_by_region": profit_by_region,
    "monthly_sales": monthly_sales,
    "sales_by_category": sales_by_category,
    "profit_by_category": profit_by_category,
    "top_10_products_by_sales":top_10_products_by_sales,
    "top_10_products_by_profit":top_10_products_by_profit,
    "sales_by_segment":sales_by_segment,
    "profit_by_segment": profit_by_segment,
    "sales_by_sub_category": sales_by_sub_category,
    "profit_by_sub_category": profit_by_sub_category,
    "discount_to_profit" : discount_to_profit

    }


    figures = {}
    
    for chart in charts:
            if  chart["chart_type"]=="bar":
                fig = create_plotly_bar_chart(
                    data=datasets[chart["dataset"]],
                    x=chart["x"],
                    y=chart["y"],
                    color=chart.get("color"),
                    metric_name=chart["metric_name"],
                    orientation = chart.get("orientation", "v")
                )
                figures[chart["chart_id"]] = fig
                
            elif chart["chart_type"]== "line":
                fig = create_plotly_line_chart(
                    data=datasets[chart["dataset"]],
                    x=chart["x"],
                    y=chart["y"],
                    metric_name=chart["metric_name"]  
                )
                figures[chart["chart_id"]] = fig
            
            elif chart["chart_type"] == "scatter":
                fig = create_plotly_scatter_chart(
                    data=datasets[chart["dataset"]],
                    x=chart["x"],
                    y=chart["y"],
                    metric_name=chart["metric_name"]
                )

                figures[chart["chart_id"]] = fig
    return figures      



