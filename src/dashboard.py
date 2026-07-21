from dash import Dash, html, dcc
from business_analysis import total_sales, total_orders, total_customers, total_profit
from plotly_visualization import generate_all_figures



figures = generate_all_figures()

app = Dash(__name__)


card_style = { # for the individual KPI points
    "border": "1px solid lightgray",
    "padding": "20px",
    "borderRadius": "8px",
    "textAlign": "center",
    "flex":1
}

chart_row_style = {      #style for the div's with 2 or more contents 
                "display":"flex",
                "gap": "20px",
                "marginTop": "20px"
            }

chart_box_style ={
    "flex": 1,
    "padding": "20px",
    "backgroundColor":"white",
    "border": "1px solid #e5e7eb",
    "borderRadius": "10px"
}

page_style = {
    "padding": "24px",
    "backgroundColor": "#f5f5f5",
    "minHeight": "100vh"
}


def create_kpi_card(title, value): # functions to create a KPI card
    return html.Div( 
            children =[
                html.H4(title),
                html.H2(value)
            ],
            style = card_style
            )

def create_chart_box(title, figure): # function to create a single chart view
    return html.Div(
        children=[
            html.H2(title),
            dcc.Graph(figure = figure)
        ],
        style = chart_box_style
    )



## Creating the app layout

app.layout = html.Div(
    children=[
        html.H1("Sales Analytics Dashboard"),
        html.Div(
            children=[
               create_kpi_card(
                    "Total Sales",
                    f"${total_sales:,.2f}"
                ),
                create_kpi_card(
                     "Total Profit",
                     f"${total_profit:,.2f}"
                ),

                create_kpi_card(
                     "Total Orders",
                     f"{total_orders:,}"
                ),

                create_kpi_card(
                    "Total Customers",
                    f"{total_customers:,}"
                )
            ],
            style= chart_row_style
        ),
        
        create_chart_box('Monthly Sales trend', figures['monthly_sales']),

        html.Div(
            children=[# comparison of sales by region and category
                create_chart_box('Sales by Region', figures['sales_by_region']),
                create_chart_box('Sales by Category', figures['sales_by_category'])
            ],
            style = chart_row_style
        ),
        html.Div( # comparison of profit by region and category
            children=[
                create_chart_box('Profit by Region', figures['profit_by_region']),
                create_chart_box('Profit by Category', figures['profit_by_category'])
            ],
            style = chart_row_style
        ),
        html.Div(
            children=[
                create_chart_box('Discount vs Profit',figures['discount_to_profit'])
            ]
        )
    ],
    style = page_style

)

if __name__ == "__main__":
    app.run(debug=True)
