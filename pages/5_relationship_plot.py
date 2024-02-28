import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/relationship_line', name="Relationship Line Plot")

df = pd.read_csv("new_data_5.csv")

def create_line_chart(x_axis="created_at", y_axis="price"):
    fig = px.line(data_frame=df, x=x_axis, y=y_axis, height=600)
    fig.update_traces(line=dict(color='#25a5c4'))  # Line color
    fig.update_layout(
        plot_bgcolor='#212529',  # Background color
        paper_bgcolor='#212529',  # Plot area background color
        xaxis=dict(gridcolor='#5a6066', title=dict(font=dict(color='#c7c7c7'))),  # X-axis grid color and title text color
        yaxis=dict(gridcolor='#5a6066', title=dict(font=dict(color='#c7c7c7'))),  # Y-axis grid color and title text color
        font=dict(color='#c7c7c7')
    )
    return fig

columns = ["status", "created_at", "sku", "price", "qty_ordered", "grand_total", "increment_id", "category_name_1","sales_commission_code","discount_amount","payment_method","Working Date","BI Status","MV","Year","Month","Customer Since","M-Y","FY","Customer ID",]

x_axis = dcc.Dropdown(
    id="x_axis",
    options=[{'label': col, 'value': col} for col in columns],
    value="created_at",
    clearable=False,
    style={'backgroundColor': '#b3b3b3', 'color': '#333333'}
)

y_axis = dcc.Dropdown(
    id="y_axis",
    options=[{'label': col, 'value': col} for col in columns],
    value="price",
    clearable=False,
    style={'backgroundColor': '#b3b3b3', 'color': '#333333'}
)

layout = html.Div(children=[
    html.Br(),
    "X-Axis", x_axis, 
    "Y-Axis", y_axis,
    dcc.Graph(id="line")
])

@callback(Output("line", "figure"), [Input("x_axis", "value"),Input("y_axis", "value"), ])
def update_line_chart(x_axis, y_axis):
    return create_line_chart(x_axis, y_axis)
