import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.

There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smaller size screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Value Proposition

            Peak Oil. Remember that? No one talks about that anymore and with the state of the world we may never even get there. But just in case we do, this web app will attempt to model fuel economy based on published, historical
            data from the Environmental Protection Agency. Since they are still by far the most common, the focus is on conventional fuel-type vehicles.

            """
        ),
        dcc.Link(dbc.Button('What is my MPG?', color='primary'), href='/predictions')
#            Emphasize how the app will benefit users. Don't emphasize the underlying technology.
#
#            ✅ RUN is a running app that adapts to your fitness levels and designs personalized workouts to help you improve your running.
#
#            ❌ RUN is the only intelligent running app that uses sophisticated deep neural net machine learning to make your run smarter because we believe in ML driven workouts.
#
#            ❌MPG is an app for exploring the fuel economy rating from the EPA.


    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])
