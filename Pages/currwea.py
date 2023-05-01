from dash import Dash, html, dash_table, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import dash
import pandas as pd
import dash_daq as daq
# from dash.dependencies import Input, Output, State


dash.register_page(__name__, path='/currwea')

df = pd.read_csv('assets/weather_data.csv')

# def get_city_date_data(city,date):

#     df = pd.read_csv('assets/weather_data.csv')
#     df = df[df['city'] == city]

#     df = df[df['date'] == date]

#     return df

def get_curr_date():
    return '2023-05-01'


def get_columns():
    return [{"label": i, "value": i} for i in df.columns]

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
            dbc.CardHeader('Current Stats', style = {'font-size':'25px'}),
                    # html.H5(id="weather", className="card-title"),
                    # html.P(
                    #     "Temperature",
                    #     className="card-text",
                    # ),
                    # html.H3('Current Stats'),
                    html.H5(id='main-temp', style={'padding':'7px'}),
                    html.H5(id='min-temp', style={'padding':'7px'}),
                    html.H5(id='max-temp', style={'padding':'7px'}),
                    html.H5(id='feelslike', style={'padding':'7px'}),
                    html.H5(id='humidity', style={'padding':'7px'}),
                    html.H5(id='precip', style={'padding':'7px'}),

        ],
        
        class_name="mb-3",
    )


    uv_meter = html.Div(id = 'uv_meter', children = [
            html.Div('UV Meter', style={'textAlign': 'center', 'font-size': '5px'}),
            daq.Gauge(
                    id='uv-id',
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
                    size=500,
                    style={'textAlign': 'center', 'margin': 'auto', 'margin-top': '10px', 'font-size': '10px'}
                )
        ])

    heading_title = html.Div([
        html.H2(children='Current Weather', style={"text-align": "center"}),
        html.Hr(),])
    
    org  = dbc.Row([
        dbc.Col(weather_card),
        dbc.Col(uv_meter)
    ])
    return html.Div([
        heading_title,
        search_bar,
        # html.Br(),
        org
    ])

@callback(
    Output("uv_meter", "children"),
    [Input("search_button", "n_clicks"),
    Input("city", "value")],
)
def update_output(n_clicks, city):
    if n_clicks:
        df = pd.read_csv('assets/weather_data.csv')
        # curr_date = get_curr_date()
        val = df[(df['name'] == city) & (df['datetime'] == '01-05-2023')]['uvindex'].values[0]
        uv_meter_ = html.Div(children=[
        html.H3('UV Meter', style={'textAlign': 'center'}),
        daq.Gauge(
                id='uv-id',
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
    

# html.H1(id='main-temp'),
#                     html.H3(id='min-temp'),
#                     html.H3(id='max-temp'),
#                     html.H3(id='feelslike'),
#                     html.H3(id='humidity'),
#                     html.H3(id='precip'),
@callback(
    Output("main-temp", "children"),
    Output("min-temp", "children"),
    Output("max-temp", "children"),
    Output("feelslike", "children"),
    Output("humidity", "children"),
    Output("precip", "children"),
    [Input("search_button", "n_clicks"),
    Input("city", "value")],
)
def update_data(n_clicks, city):
    if n_clicks:
        df = pd.read_csv('assets/weather_data.csv')
        curr_date = get_curr_date()
        val = df[(df['name'] == city) & (df['datetime'] == '01-05-2023')]
        curr_temp = val['temp'].values[0]
        curr_max_temp = val['tempmax'].values[0]
        curr_min_temp = val['tempmin'].values[0]
        curr_feelslike = val['feelslike'].values[0]
        curr_humidity = val['humidity'].values[0]
        curr_precip = val['precip'].values[0]

        return html.Div(f'Temperature: {curr_temp} {chr(176)}C'), html.Div(f'Max Temperature: {curr_max_temp} {chr(176)}C'), html.Div(f'Min Temperature: {curr_min_temp} {chr(176)}C'), html.Div(f'Feelslike: {curr_feelslike} {chr(176)}C'), html.Div(f'Humidity: {curr_humidity} %'), html.Div(f'Precipitation: {curr_precip} mm') 
        


layout = get_layout()
