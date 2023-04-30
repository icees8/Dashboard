from dash import Dash, html, dash_table, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import dash
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime as dt
from dash.exceptions import PreventUpdate


dash.register_page(__name__, path='/cityvcity')

df = pd.read_csv('assets/weather_data.csv')

def get_city_date_data(city,date):

    df = df[df['name'] == city]
    df = df[df['date'] == date]

    return df

def date2str(date):
    return dt.strptime(date, '%Y-%m-%d').strftime('%d-%m-%Y')

def str2date(date):
    return dt.strptime(date, '%d-%m-%Y').strftime('%Y-%m-%d')

def get_unique_city():
    return list(df['name'].unique())
    # return ['hua','hui','we']

@callback(
    Output('graph1', 'figure'),
    [Input('dropdown1', 'value'),
    Input('dropdown2', 'value')])
def update_graph1(city1,city2):

    city_name1 = city1
    city_name2 = city2

    city_data1 = df[df['name'] == city_name1]
    city_data2 = df[df['name'] == city_name2]

    trace1 = go.Scatter(x=city_data1['datetime'], y=city_data1['temp'], name=city_name1)
    trace2 = go.Scatter(x=city_data2['datetime'], y=city_data2['temp'], name=city_name2)

    layout = go.Layout(title='Temperature Time Series comparison for ' + city_name1 + ' and ' + city_name2, xaxis=dict(title='Date', tickmode='linear', dtick=7), yaxis=dict(title='Temperature (C)'))

    fig = go.Figure(data=[trace1, trace2], layout=layout)
    return fig

@callback(
    Output('bar_graph_id1', 'figure'),
    [Input('dropdown1', 'value'),
    Input('dropdown2', 'value'),
    Input('date_picker_id', 'date')]
    )
def update_bargraph1(city1,city2,date):

    city1 = city1
    city2 = city2

    # Define the selected date
    selected_date = str(date2str(date))

    # Filter the data for the selected date and cities
    selected_data = df[(df['name'].isin([city1, city2])) & (df['datetime'] == selected_date)]

    # Create the traces for the bar chart
    city1_data = selected_data[selected_data['name'] == city1]
    city2_data = selected_data[selected_data['name'] == city2]

    try:
        city1_trace = go.Bar(x=[city1], y=[city1_data['tempmax'].iloc[0]], name=city1)
        city2_trace = go.Bar(x=[city2], y=[city2_data['tempmax'].iloc[0]], name=city2)
    except:
        raise PreventUpdate

    # Create the layout for the graph
    layout = go.Layout(width=600, height=500, title='Comparison of Max Temp for Two Cities on {}'.format(selected_date), xaxis=dict(title='City'), yaxis=dict(title='Max Temperature (C)'))

    # Create the figure and add the traces and layout
    fig = go.Figure(data=[city1_trace, city2_trace], layout=layout)
    # fig.show()
    return fig

@callback(
    Output('bar_graph_id2', 'figure'),
    [Input('dropdown1', 'value'),
    Input('dropdown2', 'value'),
    Input('date_picker_id', 'date')])
def update_bargraph2(city1,city2,date):

    city1 = city1
    city2 = city2

    # Define the selected date
    selected_date = str(date2str(date))

    # Filter the data for the selected date and cities
    selected_data = df[(df['name'].isin([city1, city2])) & (df['datetime'] == selected_date)]

    # Create the traces for the bar chart
    city1_data = selected_data[selected_data['name'] == city1]
    city2_data = selected_data[selected_data['name'] == city2]

    city1_trace = go.Bar(x=[city1], y=[city1_data['tempmin'].iloc[0]], name=city1)
    city2_trace = go.Bar(x=[city2], y=[city2_data['tempmin'].iloc[0]], name=city2)

    # Create the layout for the graph
    layout = go.Layout(width=600, height=500, title='Comparison of Min Temp for Two Cities on {}'.format(selected_date), xaxis=dict(title='City'), yaxis=dict(title='Min Temperature (C)'))

    # Create the figure and add the traces and layout
    fig = go.Figure(data=[city1_trace, city2_trace], layout=layout)
    # fig.show()
    return fig

@callback(
    Output('bar_graph_id3', 'figure'),
    [Input('dropdown1', 'value'),
    Input('dropdown2', 'value'),
    Input('date_picker_id', 'date')])
def update_bargraph3(city1,city2,date):

    city1 = city1
    city2 = city2

    # Define the selected date
    selected_date = str(date2str(date))

    # Filter the data for the selected date and cities
    selected_data = df[(df['name'].isin([city1, city2])) & (df['datetime'] == selected_date)]

    # Create the traces for the bar chart
    city1_data = selected_data[selected_data['name'] == city1]
    city2_data = selected_data[selected_data['name'] == city2]

    city1_trace = go.Bar(x=[city1], y=[city1_data['temp'].iloc[0]], name=city1)
    city2_trace = go.Bar(x=[city2], y=[city2_data['temp'].iloc[0]], name=city2)

    # Create the layout for the graph
    layout = go.Layout(width=600, height=500, title='Comparison of Temp for Two Cities on {}'.format(selected_date), xaxis=dict(title='City'), yaxis=dict(title=' Temperature (C)'))

    # Create the figure and add the traces and layout
    fig = go.Figure(data=[city1_trace, city2_trace], layout=layout)

    # fig.show()
    return fig

@callback(
    Output('bar_graph_id4', 'figure'),
    [Input('dropdown1', 'value'),
    Input('dropdown2', 'value'),
    Input('date_picker_id', 'date')])
def update_bargraph4(city1,city2,date):

    city1 = city1
    city2 = city2

    # Define the selected date
    selected_date = str(date2str(date))

    # Filter the data for the selected date and cities
    selected_data = df[(df['name'].isin([city1, city2])) & (df['datetime'] == selected_date)]

    # Create the traces for the bar chart
    city1_data = selected_data[selected_data['name'] == city1]
    city2_data = selected_data[selected_data['name'] == city2]

    city1_trace = go.Bar(x=[city1], y=[city1_data['feelslike'].iloc[0]], name=city1)
    city2_trace = go.Bar(x=[city2], y=[city2_data['feelslike'].iloc[0]], name=city2)

    # Create the layout for the graph
    layout = go.Layout(width=600, height=500, title='Comparison of Feels Like for Two Cities on {}'.format(selected_date), xaxis=dict(title='City'), yaxis=dict(title='Feels Like (C)'))

    # Create the figure and add the traces and layout
    fig = go.Figure(data=[city1_trace, city2_trace], layout=layout)

    # fig.show()
    return fig

@callback(
    Output('bar_graph_id5', 'figure'),
    [Input('dropdown1', 'value'),
    Input('dropdown2', 'value'),
    Input('date_picker_id', 'date')])
def update_bargraph5(city1,city2,date):

    city1 = city1
    city2 = city2

    # Define the selected date
    selected_date = str(date2str(date))

    # Filter the data for the selected date and cities
    selected_data = df[(df['name'].isin([city1, city2])) & (df['datetime'] == selected_date)]

    # Create the traces for the bar chart
    city1_data = selected_data[selected_data['name'] == city1]
    city2_data = selected_data[selected_data['name'] == city2]

    city1_trace = go.Bar(x=[city1], y=[city1_data['humidity'].iloc[0]], name=city1)
    city2_trace = go.Bar(x=[city2], y=[city2_data['humidity'].iloc[0]], name=city2)

    # Create the layout for the graph
    layout = go.Layout(width=600, height=500, title='Comparison of Humidity for Two Cities on {}'.format(selected_date), xaxis=dict(title='City'), yaxis=dict(title='Humidity (%)'))

    # Create the figure and add the traces and layout
    fig = go.Figure(data=[city1_trace, city2_trace], layout=layout)

    # fig.show()
    return fig

@callback(
    Output('bar_graph_id6', 'figure'),
    [Input('dropdown1', 'value'),
    Input('dropdown2', 'value'),
    Input('date_picker_id', 'date')])
def update_bargraph6(city1,city2,date):

    city1 = city1
    city2 = city2

    # Define the selected date
    selected_date = str(date2str(date))

    # Filter the data for the selected date and cities
    selected_data = df[(df['name'].isin([city1, city2])) & (df['datetime'] == selected_date)]

    # Create the traces for the bar chart
    city1_data = selected_data[selected_data['name'] == city1]
    city2_data = selected_data[selected_data['name'] == city2]

    city1_trace = go.Bar(x=[city1], y=[city1_data['precip'].iloc[0]], name=city1)
    city2_trace = go.Bar(x=[city2], y=[city2_data['precip'].iloc[0]], name=city2)

    # Create the layout for the graph
    layout = go.Layout(width=600, height=500, title='Comparison of Percipitation for Two Cities on {}'.format(selected_date), xaxis=dict(title='City'), yaxis=dict(title='Percipitation (%)'))

    # Create the figure and add the traces and layout
    fig = go.Figure(data=[city1_trace, city2_trace], layout=layout)
    # fig.show()
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

    dropdown2 = html.Div([
        dcc.Dropdown(
            id='dropdown2',
            value='Jodhpur',
            options=[
                {'label': i, 'value': i} for i in get_unique_city()
            ]
        )
    ])

    graph1 = html.Div([
        dcc.Graph(id='graph1')
    ])

    # align datepicker in the center
    select_date = html.Div([
        html.H4('Select a Date'),
        dcc.DatePickerSingle(
            id='date_picker_id',
            initial_visible_month='2023-01-01',
            display_format='DD-MM-YYYY',
            date='2023-01-01'
        )
    ], style={'textAlign': 'center'})


    bar_graph1 = html.Div([
        dcc.Graph(id='bar_graph_id1')
    ])

    bar_graph2 = html.Div([
        dcc.Graph(id='bar_graph_id2')
    ])

    bar_graph3 = html.Div([
        dcc.Graph(id='bar_graph_id3')
    ])

    bar_graph4 = html.Div([
        dcc.Graph(id='bar_graph_id4')
    ])

    bar_graph5 = html.Div([
        dcc.Graph(id='bar_graph_id5')
    ])

    bar_graph6 = html.Div([
        dcc.Graph(id='bar_graph_id6')
    ])

    bar_organizer = dbc.Row([
        dbc.Col(bar_graph1, width=6),
        dbc.Col(bar_graph2, width=6),
        dbc.Col(bar_graph3, width=6),
        dbc.Col(bar_graph4, width=6),
        dbc.Col(bar_graph5, width=6),
        dbc.Col(bar_graph6, width=6),
    ])
        

    heading_title = html.Div([
        html.H2(children='Time vs Time', style={"text-align": "center"}),
        html.Hr(),])
    
    return html.Div([
        heading_title,
        html.Div(children='Select Cities to Compare', style={'textAlign': 'center'}),

        dropdown1,
        dropdown2,

        html.Hr(),

        graph1,

        html.Hr(),

        select_date,
        bar_organizer

    ])

# layout = get_layout()