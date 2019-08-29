import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            
            ## Insights
            """
        ),
        html.Img(src='assets/PDP Heatmap.png', className='img-fluid'),
        html.Img(src='assets/shap1.png', className='img-fluid'),
        html.Img(src='assets/shap2.png', className='img-fluid'),
        html.Img(src='assets/shap3.png', className='img-fluid'),
        html.Img(src='assets/shap4.png', className='img-fluid'),
        
    ],
    md=12,
)


column2 = dbc.Col(
    [
        
    ]
)

layout = dbc.Row([column1, column2])
