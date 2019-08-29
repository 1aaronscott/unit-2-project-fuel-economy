import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
import pandas as pd
from app import app
from numpy import arange

randomforest = load('assets/randomforest.joblib')

column1 = dbc.Col(
    [
        html.H2('Predicted MPG', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')        
    ]
)

column2 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Choose the features of a potential vehicle.

            """
        ),
        dcc.Markdown("## Inputs"),
        dcc.Markdown("#### Cylinders"),
        dcc.Slider(
            id='Cylinders',
            min=2,
            max=16,
            step=1,
            value=4,
            marks={n: str(n) for n in range(2, 16, 2)},
            className='mb-5',
        ),
#        dcc.Markdown("#### Cylinders"),
#        dcc.Dropdown(
#            id='Cylinders',
#            options = [
#                {'label': '2', 'value': 2},
#                {'label': '3', 'value': 3},
#                {'label': '4', 'value': 4},
#                {'label': '5', 'value': 5},
#                {'label': '6', 'value': 6},
#                {'label': '8', 'value': 8},
#                {'label': '10', 'value': 10},
#                {'label': '12', 'value': 12},
#                {'label': '16', 'value': 16},
#            ],
#            value = 4,
#        ),
        dcc.Markdown("#### Engine Displacement"),
        dcc.Slider(
            id='Engine_Displacement', 
            min=0.9, 
            max=8.4, 
            step=.1, 
            value=1.5, 
            marks={n: str(n) for n in arange(.9,8.4,1.5)}, 
            className='mb-5', 
        ), 
        dcc.Markdown("#### Model Year"),
        dcc.Slider(
            id='Year',
            min=2008,
            max=2020,
            step=1,
            value=2008,
            marks={n: str(n) for n in range(2008, 2020, 2)},
            className='mb-5',
        ),
#        dcc.Dropdown(
#            id='Engine_Displacement',
#            options = [
#                {'label': '0.9', 'value': '0.9'},
#                {'label': '1. ', 'value': '1. '},
#                {'label': '1.1', 'value': '1.1'},
#                {'label': '1.2', 'value': '1.2'},
#                {'label': '1.3', 'value': '1.3'},
#                {'label': '1.4', 'value': '1.4'},
#                {'label': '1.5', 'value': '1.5'},
#                {'label': '1.6', 'value': '1.6'},
#                {'label': '1.7', 'value': '1.7'},
#                {'label': '1.8', 'value': '1.8'},
#                {'label': '1.9', 'value': '1.9'},
#                {'label': '2. ', 'value': '2. '},
#                {'label': '2.1', 'value': '2.1'},
#                {'label': '2.2', 'value': '2.2'},
#                {'label': '2.3', 'value': '2.3'},
#                {'label': '2.4', 'value': '2.4'},
#                {'label': '2.5', 'value': '2.5'},
#                {'label': '2.6', 'value': '2.6'},
#                {'label': '2.7', 'value': '2.7'},
#                {'label': '2.8', 'value': '2.8'},
#                {'label': '2.9', 'value': '2.9'},
#                {'label': '3. ', 'value': '3. '},
#                {'label': '3.1', 'value': '3.1'},
#                {'label': '3.2', 'value': '3.2'},
#                {'label': '3.3', 'value': '3.3'},
#                {'label': '3.4', 'value': '3.4'},
#                {'label': '3.5', 'value': '3.5'},
#                {'label': '3.6', 'value': '3.6'},
#                {'label': '3.7', 'value': '3.7'},
#                {'label': '3.8', 'value': '3.8'},
#                {'label': '3.9', 'value': '3.9'},
#                {'label': '4. ', 'value': '4. '},
#                {'label': '4.1', 'value': '4.1'},
#                {'label': '4.2', 'value': '4.2'},
#                {'label': '4.3', 'value': '4.3'},
#                {'label': '4.4', 'value': '4.4'},
#                {'label': '4.5', 'value': '4.5'},
#                {'label': '4.6', 'value': '4.6'},
#                {'label': '4.7', 'value': '4.7'},
#                {'label': '4.8', 'value': '4.8'},
#                {'label': '4.9', 'value': '4.9'},
#                {'label': '5. ', 'value': '5. '},
#                {'label': '5.2', 'value': '5.2'},
#                {'label': '5.3', 'value': '5.3'},
#                {'label': '5.4', 'value': '5.4'},
#                {'label': '5.5', 'value': '5.5'},
#                {'label': '5.6', 'value': '5.6'},
#                {'label': '5.7', 'value': '5.7'},
#                {'label': '5.8', 'value': '5.8'},
#                {'label': '5.9', 'value': '5.9'},
#                {'label': '6. ', 'value': '6. '},
#                {'label': '6.1', 'value': '6.1'},
#                {'label': '6.2', 'value': '6.2'},
#                {'label': '6.3', 'value': '6.3'},
#                {'label': '6.4', 'value': '6.4'},
#                {'label': '6.5', 'value': '6.5'},
#                {'label': '6.6', 'value': '6.6'},
#                {'label': '6.7', 'value': '6.7'},
#                {'label': '6.8', 'value': '6.8'},
#                {'label': '7. ', 'value': '7. '},
#                {'label': '7.4', 'value': '7.4'},
#                {'label': '8. ', 'value': '8. '},
#                {'label': '8.3', 'value': '8.3'},
#                {'label': '8.4', 'value': '8.4'},
#            ],
#            value = 0.9,
#        ),
        dcc.Markdown("#### Drive Type"),
        dcc.Dropdown(
            id='Drive',
            options = [
                {'label': 'Rear-Wheel Drive', 'value': 'Rear-Wheel Drive'},
                {'label': 'Front-Wheel Drive', 'value': 'Front-Wheel Drive'},
                {'label': '4-Wheel or All-Wheel Drive', 'value': '4-Wheel or All-Wheel Drive'},
                {'label': 'All-Wheel Drive', 'value': 'All-Wheel Drive'},
                {'label': '4-Wheel Drive', 'value': '4-Wheel Drive'},
                {'label': 'Part-time 4-Wheel Drive', 'value': 'Part-time 4-Wheel Drive'},
                {'label': '2-Wheel Drive', 'value': '2-Wheel Drive'},
            ],
            value = 'Front-Wheel Drive',
        ),
        dcc.Markdown("#### Fuel Type"),
        dcc.Dropdown(
            id='Fuel_Type',
            options = [
                {'label': 'Regular', 'value': 'Regular'},
                {'label': 'Premium', 'value': 'Premius'},
                {'label': 'Diesel', 'value': 'Diesel'},
                {'label': 'CNG', 'value': 'CNG'},
                {'label': 'Midgrade', 'value': 'Midgrade'},
            ],
            value = 'Regular',
        ),
#        dcc.Markdown("#### Model Year"),
#        dcc.Dropdown(
#            id='Year',
#            options = [
#                {'label': '2008', 'value': 2008},
#                {'label': '2009', 'value': 2009},
#                {'label': '2010', 'value': 2010},
#                {'label': '2011', 'value': 2011},
#                {'label': '2012', 'value': 2012},
#                {'label': '2013', 'value': 2013},
#                {'label': '2014', 'value': 2014},
#                {'label': '2015', 'value': 2015},
#                {'label': '2016', 'value': 2016},
#                {'label': '2017', 'value': 2017},
#                {'label': '2018', 'value': 2018},
#                {'label': '2019', 'value': 2019},
#                {'label': '2020', 'value': 2020},
#            ],
#            value = 2008,
#        ),
        dcc.Markdown("#### Vehicle Type"),
        dcc.Dropdown(
            id='Vehicle_Class',
            options = [
                {'label': 'Two Seaters', 'value': 'Two Seaters'},
                {'label': 'Subcompact Cars', 'value': 'Subcompact Cars'},
                {'label': 'Vans', 'value': 'Vans'},
                {'label': 'Compact Cars', 'value': 'Compact Cars'},
                {'label': 'Midsize Cars', 'value': 'Midsize Cars'},
                {'label': 'Large Cars', 'value': 'Large Cars'},
                {'label': 'Small Station Wagons', 'value': 'Small Station Wagons'},
                {'label': 'Midsize-Large Station Wagons', 'value': 'Midsize-Large Station Wagons'},
                {'label': 'Small Pickup Trucks', 'value': 'Small Pickup Trucks'},
                {'label': 'Standard Pickup Trucks', 'value': 'Standard Pickup Trucks'},
                {'label': 'Special Purpose Vehicle 2WD', 'value': 'Special Purpose Vehicle 2WD'},
                {'label': 'Special Purpose Vehicles', 'value': 'Special Purpose Vehicles'},
                {'label': 'Minicompact Cars', 'value': 'Minicompact Cars'},
                {'label': 'Special Purpose Vehicle 4WD', 'value': 'Special Purpose Vehicle 4WD'},
                {'label': 'Midsize Station Wagons', 'value': 'Midsize Station Wagons'},
                {'label': 'Small Pickup Trucks 2WD', 'value': 'Small Pickup Trucks 2WD'},
                {'label': 'Standard Pickup Trucks 2WD', 'value': 'Standard Pickup Trucks 2WD'},
                {'label': 'Standard Pickup Trucks 4WD', 'value': 'Standard Pickup Trucks 4WD'},
                {'label': 'Vans,  Cargo Type', 'value': 'Vans,  Cargo Type'},
                {'label': 'Vans,  Passenger Type', 'value': 'Vans,  Passenger Type'},
                {'label': 'Minivan - 2WD', 'value': 'Minivan - 2WD'},
                {'label': 'Sport Utility Vehicle - 4WD', 'value': 'Sport Utility Vehicle - 4WD'},
                {'label': 'Minivan - 4WD', 'value': 'Minivan - 4WD'},
                {'label': 'Sport Utility Vehicle - 2WD', 'value': 'Sport Utility Vehicle - 2WD'},
                {'label': 'Small Pickup Trucks 4WD', 'value': 'Small Pickup Trucks 4WD'},
                {'label': 'Special Purpose Vehicle', 'value': 'Special Purpose Vehicle'},
                {'label': 'Standard Pickup Trucks/2wd', 'value': 'Standard Pickup Trucks/2wd'},
                {'label': 'Vans Passenger', 'value': 'Vans Passenger'},
                {'label': 'Special Purpose Vehicles/2wd', 'value': 'Special Purpose Vehicles/2wd'},
                {'label': 'Special Purpose Vehicles/4wd', 'value': 'Special Purpose Vehicles/4wd'},
                {'label': 'Small Sport Utility Vehicle 4WD', 'value': 'Small Sport Utility Vehicle 4WD'},
                {'label': 'Standard Sport Utility Vehicle 2WD', 'value': 'Standard Sport Utility Vehicle 2WD'},
                {'label': 'Standard Sport Utility Vehicle 4WD', 'value': 'Standard Sport Utility Vehicle 4WD'},
                {'label': 'Small Sport Utility Vehicle 2WD', 'value': 'Small Sport Utility Vehicle 2WD'},
            ],
            value = 'Midsize Cars',
        ),
        dcc.Markdown("#### Transmission Type"),
        dcc.Dropdown(
            id='Transmission',
            options = [
                {'label': 'Manual 5-spd', 'value': 'Manual 5-spd'},
                {'label': 'Automatic 3-spd', 'value': 'Automatic 3-spd'},
                {'label': 'Automatic 4-spd', 'value': 'Automatic 4-spd'},
                {'label': 'Automatic 5-spd', 'value': 'Automatic 5-spd'},
                {'label': 'Manual 4-spd', 'value': 'Manual 4-spd'},
                {'label': 'Manual 3-spd', 'value': 'Manual 3-spd'},
                {'label': 'Manual 6-spd', 'value': 'Manual 6-spd'},
                {'label': 'Automatic (S5)', 'value': 'Automatic (S5)'},
                {'label': 'Automatic (variable gear ratios)', 'value': 'Automatic (variable gear ratios)'},
                {'label': 'Automatic 6-spd', 'value': 'Automatic 6-spd'},
                {'label': 'Automatic (S6)', 'value': 'Automatic (S6)'},
                {'label': 'Automatic (S4)', 'value': 'Automatic (S4)'},
                {'label': 'Automatic 7-spd', 'value': 'Automatic 7-spd'},
                {'label': 'Automatic (S7)', 'value': 'Automatic (S7)'},
                {'label': 'Automatic (S8)', 'value': 'Automatic (S8)'},
                {'label': 'Automatic (AM5)', 'value': 'Automatic (AM5)'},
                {'label': 'Automatic (AM6)', 'value': 'Automatic (AM6)'},
                {'label': 'Automatic (AV-S7)', 'value': 'Automatic (AV-S7)'},
                {'label': 'Automatic (AM7)', 'value': 'Automatic (AM7)'},
                {'label': 'Manual 7-spd', 'value': 'Manual 7-spd'},
                {'label': 'Automatic (AV-S6)', 'value': 'Automatic (AV-S6)'},
                {'label': 'Automatic (L4)', 'value': 'Automatic (L4)'},
                {'label': 'Automatic (L3)', 'value': 'Automatic (L3)'},
                {'label': 'Automatic (AV-S8)', 'value': 'Automatic (AV-S8)'},
                {'label': 'Automatic 8-spd', 'value': 'Automatic 8-spd'},
                {'label': 'Automatic (AM-S6)', 'value': 'Automatic (AM-S6)'},
                {'label': 'Automatic (AM-S7)', 'value': 'Automatic (AM-S7)'},
                {'label': 'Automatic 9-spd', 'value': 'Automatic 9-spd'},
                {'label': 'Automatic (S9)', 'value': 'Automatic (S9)'},
                {'label': 'Automatic (AM8)', 'value': 'Automatic (AM8)'},
                {'label': 'Automatic (AM-S8)', 'value': 'Automatic (AM-S8)'},
                {'label': 'Automatic (AM-S9)', 'value': 'Automatic (AM-S9)'},
                {'label': 'Automatic (S10)', 'value': 'Automatic (S10)'},
                {'label': 'Automatic (AV-S10)', 'value': 'Automatic (AV-S10)'},
                {'label': 'Automatic 10-spd', 'value': 'Automatic 10-spd'},
            ],
            value = 'Automatic 6-spd',
        ),
        dcc.Markdown("#### Passenger Volume 2"),
        dcc.Dropdown(
            id='Passenger_Vol_2D',
            options = [
                {'label': '0', 'value': 0}
            ],
            value = 0,
        ),
        dcc.Markdown("#### Passenger Volume 4"),
        dcc.Dropdown(
            id='Passenger_Vol_4D',
            options = [
                {'label': '0', 'value': 0}
            ],
            value = 0,
        ),
        dcc.Markdown('#### Conventional'),
        dcc.Dropdown(
            id='Conventional',
            options = [
                {'label': 'True', 'value': 'True'},
            ],
            value = 'True',
        ),
#        dcc.Markdown("#### Predicted MPG"),
#        html.H2('Predicted MPG', className='mb-5'),
#        html.Div(id='prediction-content', className='lead'),
       ],
    md=12,
)


layout = dbc.Row([column1, column2])
#layout = dbc.Row([column1])

@app.callback(
    Output('prediction-content', 'children'),
    [Input('Cylinders', 'value'), Input('Engine_Displacement', 'value'), Input('Drive', 'value'),
     Input('Fuel_Type', 'value'), Input('Passenger_Vol_2D', 'value'), Input('Passenger_Vol_4D', 'value'),
     Input('Year', 'value'), Input('Vehicle_Class', 'value'), Input('Transmission', 'value')]
)
def predict(cylinders, displacement, drive, fuel, pv2, pv4, year, trans, vehicle, conventional=True):
   df = pd.DataFrame(
       columns=['Cylinders', 'Engine_Displacement', 'Drive', 'Fuel_Type', 'Passenger_Vol_2D', 
                'Passenger_Vol_4D', 'Year', 'Transmission', 'Vehicle_Class', 'Conventional'],
       data=[[cylinders, displacement, drive, fuel, 0, 0, year, trans, vehicle, True]])
   y_pred = randomforest.predict(df)[0]
   return f'{y_pred:.1f} MPG'
