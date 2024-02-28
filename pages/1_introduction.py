import dash
import pandas as pd
from dash import html,dash_table


dash.register_page(__name__, path='/', name="Introduction")

# Example DataFrame
df = pd.read_csv("new_data_5.csv")

# Calculate the describe table
describe_table = df.describe().reset_index()

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Div(children=[
        html.H1("About Dataset"),
        
    ], className='pb-2 text-center text-primary'),
    html.Div(children=[
        html.H2("Context"),
        html.P('This is the largest retail e-commerce orders dataset from Pakistan. It contains half a million transaction records from March 2016 to August 2018. The data was collected from various e-commerce merchants as part of a research study. I am releasing this dataset as a capstone project for my data science course at Alnafi (alnafi.com/zusmani).'),
        html.P('There is a dire need for such dataset to learn about Pakistan’s emerging e-commerce potential and I hope this will help many startups in many ways.'),   
    ], className='pb-2'),
    
    html.Div(children=[
        html.H2("Content"),
        html.P('Geography: Pakistan'),
        html.P('Time period: 03/2016 – 08/2018'),
        html.P('Unit of analysis: E-Commerce Orders'),
        html.P('Dataset: The dataset contains detailed information of half a million e-commerce orders in Pakistan from March 2016 to August 2018. It contains item details, shipping method, payment method like credit card, Easy-Paisa, Jazz-Cash, cash-on-delivery, product categories like fashion, mobile, electronics, appliance etc., date of order, SKU, price, quantity, total and customer ID. This is the most detailed dataset about e-commerce in Pakistan that you can find in the Public domain.'),
        html.P('Variables: The dataset contains Item ID, Order Status (Completed, Cancelled, Refund), Date of Order, SKU, Price, Quantity, Grand Total, Category, Payment Method and Customer ID.'),   
    ], className='pb-2'),
    
    
    html.Div(children=[
        html.H2("Summary"),
        dash_table.DataTable(data=describe_table.to_dict('records'),
                            page_size=15,
                            style_table={'overflowX': 'auto'}, 
                            style_cell={"background-color": "#4d4d4d", "border": "solid 1px lightgrey", "color": "white", "font-size": "15px", "text-align": "left"},
                            style_header={"background-color": "dodgerblue", "font-weight": "bold", "color": "white", "padding": "10px", "font-size": "18px"},
                            ),
    ], className='bg-dark'),
    
    html.Div(children=[
        html.H2("Copyright"),
        html.P('The dataset and Page introduction is taken from kaggle'),
        html.A("Kaggle DataSet", href='https://www.kaggle.com/datasets/zusmani/pakistans-largest-ecommerce-dataset')
    ], className='pb-4'),
    
    
], className="bg-dark px-2 m-2")