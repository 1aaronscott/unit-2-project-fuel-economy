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
            The data provided from the EPA is not the best for predicting fuel economy ratings. The way the [EPA generates its ratings](https://www.youtube.com/embed/oeEy9xqFG_0) using a dynamometer (a treadmill
            for vehicles) is independent of physical characteristics. As a result the dataset only provides some useful features, omits others, and provides others but doesn't make them mandatory leading to 
            sparsely populated data. Nevertheless, I made a model which demonstrates certain relationships especially with engine size.

            This partial dependence plot shows the significant impact of engine size as measured by piston displacement. There is less of an impact from vehicle size (as approximated by passenger cabin volume).
            The effect of vehicle size is clearest with larger engines and less so with smaller engines. However, larger vehicles in the real world will almost always have larger engines.
            """
        ),
        html.Img(src='assets/PDP Heatmap.png', style= {'width': '100%', 'display': 'inline-block'}, alt="Responsive image", className='img-fluid'),
        dcc.Markdown(
            """
            Below are four randomly generated Shapley plots. They show how some similar values for the same features might have differing impact on the final MPG. This could indicate the presence of 
            confounding variables.
            """
        ),
        html.Img(src='assets/shap1.png', alt="Responsive image", className='img-fluid'),
        html.Img(src='assets/shap2.png', alt="Responsive image", className='img-fluid'),
        html.Img(src='assets/shap3.png', alt="Responsive image", className='img-fluid'),
        html.Img(src='assets/shap4.png', alt="Responsive image", className='img-fluid'),
        
    ],
    md=12,
)


column2 = dbc.Col(
    [
        
    ]
)

layout = dbc.Row([column1, column2])
