import pandas as pd
import dash
from dash import html, dash_table, dcc
import plotly.graph_objects as go

dash.register_page(__name__, path='/dataset', name="Dataset")


data = pd.read_csv("new_data_5.csv")


layout = html.Div(children=[
    html.Div(children=[
        dash_table.DataTable(data=data.to_dict('records'),
                            page_size=15,
                             style_table={'overflowX': 'auto'}, 
                            style_cell={"background-color": "#4d4d4d", "border": "solid 1px lightgrey", "color": "white", "font-size": "15px", "text-align": "left"},
                            style_header={"background-color": "dodgerblue", "font-weight": "bold", "color": "white", "padding": "10px", "font-size": "18px"},
                            ),
    ], className='bg-dark')
])