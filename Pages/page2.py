import dash
from dash import dcc, html, callback
import plotly.graph_objs as go
import requests
import pandas as pd
#64cea51bb4e313c25f7352bd32d10b19
# set up the app and layout
# app = dash.Dash(__name__)

dash.register_page(__name__, path='/page2')

def get_weather_data(city):
    # url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=64cea51bb4e313c25f7352bd32d10b19&units=metric"
    # response = requests.get(url)
    # data = response.json()

    data = {
        'coord'     : {'lon': -0.1257, 'lat': 51.5085},
        'weather'   : [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}],
        'base'      : 'stations',
        'main'      : {'temp': 11.13, 'feels_like': 10.44, 'temp_min': 9.6, 'temp_max': 12.7, 'pressure': 1013, 'humidity': 82},
        'visibility': 10000,
        'wind'      : {'speed': 4.12, 'deg': 100},
        'rain'      : {'1h': 3.37},
        'clouds'    : {'all': 75},
        'dt'        : 1682611284,
        'sys'       : {'type': 2, 'id': 2075535, 'country': 'GB', 'sunrise': 1682570439, 'sunset': 1682622928},
        'timezone'  : 3600,
        'id'        : 2643743,
        'name'      : 'London',
        'cod'       : 200
    }

    # print(data)

    # weather_data = {
    #     "City": data["name"],
    #     "Temperature": data["main"]["temp"],
    #     "Humidity": data["main"]["humidity"],
    #     "Pressure": data["main"]["pressure"],
    #     "Wind Speed": data["wind"]["speed"],
    # }

    import random

    weather_data = {
        "City": data["name"],
        "Temperature": random.randint(0, 100),
        "Humidity": random.randint(0, 100),
        "Pressure": random.randint(0, 100),
        "Wind Speed": random.randint(0, 100),
    }

    return weather_data

def create_graph(city1_data, city2_data):
    data = [
        go.Bar(name=city1_data["City"], x=list(city1_data.keys())[1:], y=list(city1_data.values())[1:]),
        go.Bar(name=city2_data["City"], x=list(city2_data.keys())[1:], y=list(city2_data.values())[1:])
    ]
    layout = go.Layout(barmode="group", title="Weather Comparison")
    fig = go.Figure(data=data, layout=layout)
    return fig

# define the callback function
@callback(
    dash.dependencies.Output("weather-graph", "figure"),
    dash.dependencies.Input("submit-button", "n_clicks"),
    [dash.dependencies.State("city-1", "value"), dash.dependencies.State("city-2", "value")],
)
def update_graph(n_clicks, city1, city2):

    print("update_graph")

    city1_data = get_weather_data(city1)
    city2_data = get_weather_data(city2)

    fig = create_graph(city1_data, city2_data)

    return fig

def layout():
    return html.Div([
        html.H1("Weather Comparison Dashboard"),
        html.Div([
            html.Label("City 1: "),
            dcc.Input(id="city-1", value="London", type="text"),
            html.Label("City 2: "),
            dcc.Input(id="city-2", value="New York", type="text"),
            html.Button(id="submit-button", n_clicks=0, children="Submit")
        ]),
        dcc.Graph(id="weather-graph"),
    ])
