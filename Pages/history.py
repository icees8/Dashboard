from dash import Dash, html, dash_table, dcc
import dash_bootstrap_components as dbc
import dash
import plotly.graph_objs as go
import pandas as pd

dash.register_page(__name__, path='/history')

df = pd.read_csv('assets/weather_data.csv')

def get_city_date_data(city,date):

    df = df[df['name'] == city]
    df = df[df['date'] == date]

    return df

def get_unique_city():
    return list(df['name'].unique())
    # return ['hua','hui','we']

def update_graph1(city1):
    # filter the dataframe to only include the temperature data for the desired city
    city_name = 'Mumbai'
    city_data = df[df['name'] == city_name]

    # create a trace for the temperature data
    trace = go.Scatter(x=city_data['datetime'], y=city_data['temp'], name='Temperature')
    # create the layout for the graph
    layout = go.Layout(title='Temperature Time Series for ' + city_name, xaxis=dict(title='Date', tickmode='linear', dtick=7), yaxis=dict(title='Temperature (C)'))

    # create the figure and add the trace and layout
    fig = go.Figure(data=[trace], layout=layout)

    # display the graph
    return fig

def layout():

    dropdown1 = html.Div([
        dcc.Dropdown(
            id='dropdown1',
            value='Mumbai',
            options=[
                {'label': i, 'value': i} for i in get_unique_city()
            ]
        )
    ])

    graph1 = html.Div([
        dcc.Graph(id='graph1')
    ])



    return html.Div([
        html.Div(children='NEWWWWWWWWWWWWWWWWW YOOOOOOOOOOOrk'),
        dropdown1,
        html.Hr(),
        graph1,
    ])

# layout = get_layout()