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
        
            ## Process
            The dataset used to create this model come from the US Evironmental Proctection Agency at [FuelEconomy.gov Web Services](https://fueleconomy.gov/feg/ws/index.shtml). The data, which is frequently updated, comes from August 15, 2019.

            The goal of the project was to predict fuel efficiency of a vehicle by certain physical characteristics. I would look at previous years and see how accurately my model could predict more recent fuel ratings.

            With more than 80 columns, my initial impression was that this was a feature-rich dataset perfect for a predictive modeling project. On further inspection I found many of the features were either all or mostly zeros if not completely empty.
            The dataset also lacked some critical information such as vehicle weight which can effect fuel economy.  In the end, nine original features were useful and two more were engineered.

            To narrow the scope of this project, I wanted to focus soley on non-electric, non-hybrid, and non-alternative fuel vehicles. The EPA dataset doesn't make any clean distinction between those and convetional vehicles a feature was created to do so. The model would predict the combined miles per gallon (mpg), however the ideal feature to use for this metric was 71% zeros so a feature was engineered 0% zeros.
            """,
        className='mb-4'),
        (
            html.Img(src='assets/dataframehead.png', style= {'width': '100%', 'display': 'inline-block'}, alt="Responsive image", className='img-fluid')
            #![data frame head](assets/dataframehead.pdf "Logo Title Text 1")
        ),
        dcc.Markdown(
            """
            The next step was to do a train/validate/test split based on the initial set of just under 40,000 obeservations. Next I did a drop column analyis to identify the most important features. The results of this analyis changed
            serveral times as I wrangled the data. In the end, the most important features were vehicle transmission, passenger volume (a very rough stand-in for vehicle weight) and engine displacement.

            Then I used a RandomizedSearchCV for some hyperparameter optimization. Plugged into a Random Forest Regression model, the result was an R^2 value of 91.6%.
            """
        ),

    ],
)

layout = dbc.Row([column1])

