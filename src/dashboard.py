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
MAX_WIDTH = "1400px"
MIN_HEIGHT = "100vh"
MARGIN_TOP = "20px"
CHART_SPACING = "30px"
CHART_HEIGHT = "400px"

# ==========================
# Reusable CSS
# ==========================

BORDER = f"1px solid {BORDER_COLOR}"
GRAPH_CONFIG ={"displayModeBar":False} 

card_style = { # for the individual KPI points
    "boxShadow": "0 2px 8px rgba(0,0,0,0.08)",
    "border": BORDER,
    "padding": PADDING,
    "borderRadius": BORDER_RADIUS,
    "textAlign": "center",
    "flex":1
}

chart_row_style = {      #style for the div's with 2 or more contents 
                "display":"flex",
                "gap": GAP,
                "marginTop":MARGIN_TOP,
                "flexWrap":"wrap"
            }

chart_box_style ={
    "flex": "1 1 600px",
    "padding": PADDING,
    "backgroundColor":CARD_BACKGROUND,
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
server = app.server



def create_kpi_card(title, value, value_id): # functions to create a KPI card
    return html.Div( 
            children =[
                html.H4(title,
                style = {
                    "color": "#6b7280",
                    "fontWeight": "normal",
                    "marginBotton":"10px"
                }
            ),
                html.H2(value,
                        id = value_id,
                         style={
                            "color": PRIMARY_TEXT,
                            "fontWeight": "bold",
                            "margin": 0
                            }
                        )
            ],
            style = card_style
            )

def create_chart_box(title, figure, graph_id): # function to create a single chart view
    return html.Div(
        children=[
            html.H2(title),
            dcc.Graph(figure = figure,config =GRAPH_CONFIG,
                      id = graph_id,
                      style = {
                          "height":CHART_HEIGHT
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
                    "marginBottom":CHART_SPACING
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
                style={
                    "width": "300px",
                    "marginBottom": CHART_SPACING
                }
            )
            ],
            style ={
                "marginBottom":CHART_SPACING
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
        
        create_chart_box('Monthly Sales trend', figures['monthly_sales'], "monthly_sales_trend"),

        html.Div(
            children=[# comparison of sales by region and category
                create_chart_box('Sales by Region($)', figures['sales_by_region'],"sales_by_region"),
                create_chart_box('Profit by Region($)', figures['profit_by_region'],"profit_by_region")
            ],
            style = chart_row_style
        ),
        html.Div( # comparison of profit by region and category
            children=[
                create_chart_box('Sales by Category($)', figures['sales_by_category'],"sales_by_category"),
                create_chart_box('Profit by Category($)', figures['profit_by_category'],"profit_by_category")
            
            ],
            style = chart_row_style
        ),

        create_chart_box("Top 10 Products by Sales", figures["top_10_products_by_sales"],"top_10_products_by_sales"),

        create_chart_box("Top 10 Products by Profit", figures["top_10_products_by_profit"], "top_10_products_by_profit"),
        
        html.Div(children=[

        create_chart_box("Sales by Segment", figures["sales_by_segment"],"sales_by_segment"),
        create_chart_box("Profit by Segment", figures["profit_by_segment"], "profit_by_segment")

        ],style=chart_row_style
       
        ),
        html.Div(children=[
        create_chart_box("Sales by Sub-Category", figures["sales_by_sub_category"],"sales_by_subcategory"),
        create_chart_box("Profit by Sub-Category", figures["profit_by_sub_category"], "profit_by_subcategory")

        ],style=chart_row_style
       
        ),
        html.Div(
            children=[
                create_chart_box('Discount vs Profit',figures['discount_to_profit'],"discount_to_profit")
            ],
            style = chart_row_style
        )
    ],
    style = page_style

)
@callback(
    Output("total_sales", "children"),
    Output("total_profit", "children"),
    Output("total_orders", "children"),
    Output("total_customers", "children"),
    Output("monthly_sales_trend","figure"),
    Output("sales_by_region", "figure"),
    Output("sales_by_category", "figure"),
    Output("profit_by_region","figure"),
    Output("profit_by_category", "figure"),
    Output("top_10_products_by_sales", "figure"),
    Output("top_10_products_by_profit", "figure"),
    Output("sales_by_segment", "figure"),
    Output("profit_by_segment", "figure"),
    Output("sales_by_subcategory", "figure"),
    Output("profit_by_subcategory", "figure"),
    Output("discount_to_profit", "figure"),

    Input("region_dropdown","value")
)

def update_dashboard_data(selected_region): # =====> call back function that filters and returns data based 
                                        #selected value

    if selected_region == "All":
        filtered_df = df
    else:
        filtered_df = df[df["Region"]== selected_region]

    kpis = calculate_kpis(filtered_df)
    figures = generate_all_figures(filtered_df)

    return (f"${kpis['total_sales']:,.2f}", # returning the kpis
            f"${kpis['total_profit']:,.2f}",
            f"{kpis['total_orders']:,}",
            f"{kpis['total_customers']:,}",

            
            #returning the figures 
            figures["monthly_sales"],
            figures["sales_by_region"],
            figures["sales_by_category"],
            figures["profit_by_region"],
            figures["profit_by_category"],
            figures["top_10_products_by_sales"],
            figures["top_10_products_by_profit"],
            figures["sales_by_segment"],
            figures["profit_by_segment"],
            figures["sales_by_sub_category"],
            figures["profit_by_sub_category"],
            figures["discount_to_profit"],
            )

if __name__ == "__main__":
    app.run(debug=False)


