import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/distribution', name="Distribution")

df = pd.read_csv("new_data_5.csv")


def create_distribution(col_name="status"):
    fig = px.histogram(data_frame=df, x=col_name, height=600)
    fig.update_traces(marker=dict(color='#25a5c4'))  # Bar color
    fig.update_layout(
        plot_bgcolor='#212529',  # Background color
        paper_bgcolor='#212529',  # Plot area background color
        xaxis=dict(gridcolor='#c7c7c7', title=dict(font=dict(color='#c7c7c7'))),  # X-axis grid color and title text color
        yaxis=dict(gridcolor='#c7c7c7', title=dict(font=dict(color='#c7c7c7'))),  # Y-axis grid color and title text color
        font=dict(color='#c7c7c7')
    )
    return fig


columns = ["status", "created_at", "sku", "price", "qty_ordered", "grand_total", "increment_id", "category_name_1","sales_commission_code","discount_amount","payment_method","Working Date","BI Status","MV","Year","Month","Customer Since","M-Y","FY","Customer ID",]
# dd = dcc.Dropdown(id="dist_column", options=columns, value="status", clearable=False)
dd = dcc.Dropdown(
    id="dist_column",
    options=[{'label': col, 'value': col} for col in columns],
    value="status",
    clearable=False,
    style={'backgroundColor': '#b3b3b3', 'color': '#333333'}
)

layout = html.Div(children=[
    html.Br(),
    html.P("Select Column:"),
    dd,
    dcc.Graph(id="histogram")
], className='bg-dark')


@callback(Output("histogram", "figure"), [Input("dist_column", "value"), ])
def update_histogram(dist_column):
    return create_distribution(dist_column)

