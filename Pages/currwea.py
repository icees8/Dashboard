from dash import Dash, html, dash_table, dcc
import dash_bootstrap_components as dbc
import dash
import pandas as pd

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
                dbc.Button("Search", id="search_button", className="mr-2 mb-3", color="primary", style={"width": "20%"}),
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

    return html.Div([
        search_bar,
        # html.Br(),
        weather_card
    ])

layout = get_layout()