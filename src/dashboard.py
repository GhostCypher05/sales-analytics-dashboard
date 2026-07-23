from dash import Dash, html, dcc, Input,Output,callback
from business_analysis import calculate_kpis
from plotly_visualization import generate_all_figures
from data_loader import load_data


# ==========================
# Colors
# ==========================

PAGE_BACKGROUND = "#f5f7fa"
CARD_BACKGROUND = "#ffffff"
PRIMARY_TEXT = "#1f2937"
BORDER_COLOR = "#e5e7eb"
ACCENT_COLOR = "#2563eb"

# ==========================
# Typography
# ==========================

FONT_FAMILY = "Arial, sans-serif"

# ==========================
# Layout
# ==========================

PADDING = "20px"
GAP = "20px"
BORDER_RADIUS = "8px"
MAX_WIDTH = "1200px"
MIN_HEIGHT = "100vh"
MARGIN_TOP = "20px"

# ==========================
# Reusable CSS
# ==========================

BORDER = f"1px solid {BORDER_COLOR}"

card_style = { # for the individual KPI points
    "border": BORDER,
    "padding": PADDING,
    "borderRadius": BORDER_RADIUS,
    "textAlign": "center",
    "flex":1
}

chart_row_style = {      #style for the div's with 2 or more contents 
                "display":"flex",
                "gap": GAP,
                "marginTop":MARGIN_TOP
            }

chart_box_style ={
    "flex": 1,
    "padding": PADDING,
    "backgroundColor":"white",
    "border": BORDER,
    "borderRadius": BORDER_RADIUS,
    "marginTop":MARGIN_TOP
}

page_style = {
    "maxWidth": MAX_WIDTH,
    "margin": "0 auto",
    "padding": "24px",
    "backgroundColor": "#f5f7fa",
    "minHeight": MIN_HEIGHT,
    "fontFamily": FONT_FAMILY,

}

GRAPH_CONFIG ={"displayModeBar":False} 

df = load_data()
kpis = calculate_kpis(df)
 
figures = generate_all_figures(df)

regions = sorted(df["Region"].unique()) # =====> for the dropdown 

region_options = [{"label": "All", "value": "All"}]

region_options.extend(
    [
        {"label": region, "value": region}
        for region in regions
    ]
)

app = Dash(__name__)



def create_kpi_card(title, value, value_id): # functions to create a KPI card
    return html.Div( 
            children =[
                html.H4(title),
                html.H2(value,id = value_id)
            ],
            style = card_style
            )

def create_chart_box(title, figure): # function to create a single chart view
    return html.Div(
        children=[
            html.H2(title),
            dcc.Graph(figure = figure,config =GRAPH_CONFIG,
                      style = {
                          "height":"400px"
                      })
        ],
        style = chart_box_style
    )



## Creating the app layout

app.layout = html.Div(
    children=[
        html.H1("Sales Analytics Dashboard",
                style = {
                    "textAlign":"center",
                    "marginBottom":"30px"
                }
                ),
        html.Div(
            children =[
                html.Label(
                    "Region",
                    style={
                        "fontWeight":"bold",
                        "marginBottom": "8px"
                    }
                ),
                dcc.Dropdown(
                id ="region_dropdown",
                options=region_options,
                value= "All",
                clearable=False,
            )
            ],
            style ={
                "marginBottom":"30px"
            }

        ),
        html.Div(
            children=[
               create_kpi_card(
                    "Total Sales",
                    f"${kpis['total_sales']:,.2f}",
                    "total_sales"
                ),
                create_kpi_card(
                     "Total Profit",
                     f"${kpis['total_profit']:,.2f}",
                     "total_profit"
                ),

                create_kpi_card(
                     "Total Orders",
                     f"{kpis['total_orders']:,}",
                     "total_orders"
                ),

                create_kpi_card(
                    "Total Customers",
                    f"{kpis['total_customers']:,}",
                    "total_customers"
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
            ],
            style = chart_row_style
        )
    ],
    style = page_style

)
@callback(
    Output("total_sales", "children"),
    Input("region_dropdown","value")
)

def update_total_sales(selected_region):

    if selected_region == "All":
        filtered_df = df
    else:
        filtered_df = df[df["Region"]== selected_region]

    kpis = calculate_kpis(filtered_df)

    return f"${kpis['total_sales']:,.2f}"

if __name__ == "__main__":
    app.run(debug=True)


