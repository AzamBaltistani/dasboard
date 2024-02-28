import dash
import plotly.express as px

from dash import Dash, html, dcc

templates = ['ggplot2', 'seaborn', 'simple_white', 'plotly','plotly_white', 'plotly_dark', 'presentation', 'xgridoff','ygridoff', 'gridon', 'none']
px.defaults.template = templates[0]


app = Dash(__name__, pages_folder='pages', use_pages=True, external_stylesheets=["https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"])

app.layout = html.Div(
    [
        html.H1("Pakistan's Largest E-Commerce Dataset", className='text-center fw-bold fs-1'),
      
        html.Div(children=[
            dcc.Link(page['name'],href=page['relative_path'], className='btn btn-outline-info p-2 m-2 rounded-0') for page in dash.page_registry.values()
        ], className='bg-dark m-2'),
        
        html.Div(children=[
                
            dash.page_container
                
        ], className="bg-dark")   

    ],
    className='px-2 mx-auto bg-dark text-light min-vh-100'
)


if __name__  == '__main__':
    app.run(debug=True)