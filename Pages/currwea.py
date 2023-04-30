from dash import Dash, html, dash_table, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import dash
import pandas as pd
import dash_daq as daq
# from dash.dependencies import Input, Output, State


dash.register_page(__name__, path='/currwea')

# def get_city_date_data(city,date):

#     df = pd.read_csv('assets/weather_data.csv')
#     df = df[df['city'] == city]

#     df = df[df['date'] == date]

#     return df

def get_curr_date():
    return '2023-05-01'

def get_layout():

    search_bar = dbc.Col([
        dbc.Row(
            [
                dbc.Input(id="city", placeholder="City", type="text", style={"width": "60%"}, className="mr-2 mb-3"),
                dbc.Button("Search", id="search_button", className="mr-2 mb-3", color="primary", style={"width": "20%"}, n_clicks=0),
            ],
            justify="center"
        ),
    ] ,align = "center")

    curr_date  = get_curr_date()

    weather_card = dbc.Card(
        [
            dbc.CardHeader("Weather"),
            dbc.CardBody(
                [
                    # html.H5(id="weather", className="card-title"),
                    html.P(
                        "Temperature",
                        className="card-text",
                    ),
                ]
            ),
        ],
        style={"width": "20rem"},
        class_name="mb-3",
    )

    uv_meter = html.Div(id = 'uv_meter', children = [
            html.H1('UV Meter', style={'textAlign': 'center'}),
            daq.Gauge(
                    id='uv-chupa',
                    showCurrentValue=True,
                    value = 0,
                    max=11,
                    min=0,
                    color={
                        "gradient": True,
                        "ranges": {
                            "green": [0, 2],
                            "yellow": [2, 5.5],
                            "orange": [5.5, 7.5],
                            "red": [7.5, 10.5],
                            "purple": [10.5, 11]
                        }
                    },
                    size=200,
                    style={'textAlign': 'center'}
                ),  
        ])

    heading_title = html.Div([
        html.H2(children='Current Weather', style={"text-align": "center"}),
        html.Hr(),])
    
    return html.Div([
        heading_title,
        search_bar,
        # html.Br(),
        weather_card, 
        uv_meter
    ])

@callback(
    Output("uv_meter", "children"),
    [Input("search_button", "n_clicks"),
    Input("city", "value")],
)
def update_output(n_clicks, city):
    if n_clicks:
        df = pd.read_csv('assets/weather_data.csv')
        val = df[(df['name'] == city) & (df['datetime'] == '01-11-2022')]['uvindex'].values[0]
        uv_meter_ = html.Div(children=[
        html.H1('UV Meter', style={'textAlign': 'center'}),
        daq.Gauge(
                id='uv-chupa',
                showCurrentValue=True,
                value = val,
                max=11,
                min=0,
                color={
                    "gradient": True,
                    "ranges": {
                        "green": [0, 2],
                        "yellow": [2, 5.5],
                        "orange": [5.5, 7.5],
                        "red": [7.5, 10.5],
                        "purple": [10.5, 11]
                    }
                },
                size=200,
                style={'textAlign': 'center', 'color': 'black'}
            )
        ])
        return uv_meter_

layout = get_layout()
