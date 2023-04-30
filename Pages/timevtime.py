from dash import Dash, html, dash_table, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import dash
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime as dt
from dash.exceptions import PreventUpdate

dash.register_page(__name__, path='/timevtime')

# def get_layout():
#     return html.Div([
#         html.Div(children='BARF BARF BARF'),
#     ])

# layout = get_layout()

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
    Output('graph1_tvt', 'figure'),
    [Input('select_date1', 'date'),
     Input('select_date2', 'date')])
def update_graph1(date1,date2):

    date_name1 = str(date2str(date1))
    date_name2 = str(date2str(date2))

    date_data1 = df[df['datetime'] == date_name1]
    date_data2 = df[df['datetime'] == date_name2]

    trace1 = go.Scatter(x=date_data1['name'], y=date_data1['temp'], name=date_name1)
    trace2 = go.Scatter(x=date_data2['name'], y=date_data2['temp'], name=date_name2)

    layout = go.Layout(title='Temperature Time Series comparison for ' + date_name1 + ' and ' + date_name2, xaxis=dict(title='City', ), yaxis=dict(title='Temperature (C)'))

    fig = go.Figure(data=[trace1, trace2], layout=layout)
    return fig

@callback(
    Output('tvt_bar_id1', 'figure'),
    [Input('dropdown1', 'value'),
     Input('select_date1', 'date'),
     Input('select_date2', 'date')])
def update_bargraph1(city, date1, date2):

    city = city

    # Define the selected date
    date1 = str(date2str(date1))
    date2 = str(date2str(date2))

    # Filter the data for the selected date and cities
    selected_data = df[(df['datetime'].isin([date1, date2])) & (df['name'] == city)]

    # Create the traces for the bar chart
    date1_data = selected_data[selected_data['datetime'] == date1]
    date2_data = selected_data[selected_data['datetime'] == date2]

    date1_trace = go.Bar(x=[date1], y=[date1_data['tempmax'].iloc[0]], name=date1)
    date2_trace = go.Bar(x=[date2], y=[date2_data['tempmax'].iloc[0]], name=date2)

    # Create the layout for the graph
    layout = go.Layout(width=600, height=500, title='Comparison of Max Temp of ' + str(city) + ' on dates ' + str(date1) + str(date2), xaxis=dict(title='Date'), yaxis=dict(title='Max Temperature (C)'))

    # Create the figure and add the traces and layout
    fig = go.Figure(data=[date1_trace, date2_trace], layout=layout)
    # fig.show()
    return fig

@callback(
    Output('tvt_bar_id2', 'figure'),
    [Input('dropdown1', 'value'),
     Input('select_date1', 'date'),
     Input('select_date2', 'date')])
def update_bargraph2(city, date1, date2):

    city = city

    # Define the selected date
    date1 = str(date2str(date1))
    date2 = str(date2str(date2))

    # Filter the data for the selected date and cities
    selected_data = df[(df['datetime'].isin([date1, date2])) & (df['name'] == city)]

    # Create the traces for the bar chart
    date1_data = selected_data[selected_data['datetime'] == date1]
    date2_data = selected_data[selected_data['datetime'] == date2]

    date1_trace = go.Bar(x=[date1], y=[date1_data['tempmin'].iloc[0]], name=date1)
    date2_trace = go.Bar(x=[date2], y=[date2_data['tempmin'].iloc[0]], name=date2)

    # Create the layout for the graph
    layout = go.Layout(width=600, height=500, title='Comparison of Min Temp of ' + str(city) + ' on dates ' + str(date1) + str(date2), xaxis=dict(title='Date'), yaxis=dict(title='Min Temperature (C)'))

    # Create the figure and add the traces and layout
    fig = go.Figure(data=[date1_trace, date2_trace], layout=layout)
    # fig.show()
    return fig

@callback(
    Output('tvt_bar_id3', 'figure'),
    [Input('dropdown1', 'value'),
     Input('select_date1', 'date'),
     Input('select_date2', 'date')])
def update_bargraph3(city, date1, date2):

    city = city

    # Define the selected date
    date1 = str(date2str(date1))
    date2 = str(date2str(date2))

    # Filter the data for the selected date and cities
    selected_data = df[(df['datetime'].isin([date1, date2])) & (df['name'] == city)]

    # Create the traces for the bar chart
    date1_data = selected_data[selected_data['datetime'] == date1]
    date2_data = selected_data[selected_data['datetime'] == date2]

    date1_trace = go.Bar(x=[date1], y=[date1_data['temp'].iloc[0]], name=date1)
    date2_trace = go.Bar(x=[date2], y=[date2_data['temp'].iloc[0]], name=date2)

    # Create the layout for the graph
    layout = go.Layout(width=600, height=500, title='Comparison of Temp of ' + str(city) + ' on dates ' + str(date1) + str(date2), xaxis=dict(title='Date'), yaxis=dict(title='Temperature (C)'))

    # Create the figure and add the traces and layout
    fig = go.Figure(data=[date1_trace, date2_trace], layout=layout)
    # fig.show()
    return fig

@callback(
    Output('tvt_bar_id4', 'figure'),
    [Input('dropdown1', 'value'),
     Input('select_date1', 'date'),
     Input('select_date2', 'date')])
def update_bargraph4(city, date1, date2):

    city = city

    # Define the selected date
    date1 = str(date2str(date1))
    date2 = str(date2str(date2))

    # Filter the data for the selected date and cities
    selected_data = df[(df['datetime'].isin([date1, date2])) & (df['name'] == city)]

    # Create the traces for the bar chart
    date1_data = selected_data[selected_data['datetime'] == date1]
    date2_data = selected_data[selected_data['datetime'] == date2]

    date1_trace = go.Bar(x=[date1], y=[date1_data['feelslike'].iloc[0]], name=date1)
    date2_trace = go.Bar(x=[date2], y=[date2_data['feelslike'].iloc[0]], name=date2)

    # Create the layout for the graph
    layout = go.Layout(width=600, height=500, title='Comparison of Temp of ' + str(city) + ' on dates ' + str(date1) + str(date2), xaxis=dict(title='Date'), yaxis=dict(title='Temperature (C)'))

    # Create the figure and add the traces and layout
    fig = go.Figure(data=[date1_trace, date2_trace], layout=layout)
    # fig.show()
    return fig

@callback(
    Output('tvt_bar_id5', 'figure'),
    [Input('dropdown1', 'value'),
     Input('select_date1', 'date'),
     Input('select_date2', 'date')])
def update_bargraph5(city, date1, date2):

    city = city

    # Define the selected date
    date1 = str(date2str(date1))
    date2 = str(date2str(date2))

    # Filter the data for the selected date and cities
    selected_data = df[(df['datetime'].isin([date1, date2])) & (df['name'] == city)]

    # Create the traces for the bar chart
    date1_data = selected_data[selected_data['datetime'] == date1]
    date2_data = selected_data[selected_data['datetime'] == date2]

    date1_trace = go.Bar(x=[date1], y=[date1_data['humidity'].iloc[0]], name=date1)
    date2_trace = go.Bar(x=[date2], y=[date2_data['humidity'].iloc[0]], name=date2)

    # Create the layout for the graph
    layout = go.Layout(width=600, height=500, title='Comparison of Humidity of ' + str(city) + ' on dates ' + str(date1) + str(date2), xaxis=dict(title='Date'), yaxis=dict(title='Humidity (%)'))

    # Create the figure and add the traces and layout
    fig = go.Figure(data=[date1_trace, date2_trace], layout=layout)
    # fig.show()
    return fig

@callback(
    Output('tvt_bar_id6', 'figure'),
    [Input('dropdown1', 'value'),
     Input('select_date1', 'date'),
     Input('select_date2', 'date')])
def update_bargraph6(city, date1, date2):

    city = city

    # Define the selected date
    date1 = str(date2str(date1))
    date2 = str(date2str(date2))

    # Filter the data for the selected date and cities
    selected_data = df[(df['datetime'].isin([date1, date2])) & (df['name'] == city)]

    # Create the traces for the bar chart
    date1_data = selected_data[selected_data['datetime'] == date1]
    date2_data = selected_data[selected_data['datetime'] == date2]

    date1_trace = go.Bar(x=[date1], y=[date1_data['precip'].iloc[0]], name=date1)
    date2_trace = go.Bar(x=[date2], y=[date2_data['precip'].iloc[0]], name=date2)

    # Create the layout for the graph
    layout = go.Layout(width=600, height=500, title='Comparison of Precipitation of ' + str(city) + ' on dates ' + str(date1) + str(date2), xaxis=dict(title='Date'), yaxis=dict(title='Precipitation'))

    # Create the figure and add the traces and layout
    fig = go.Figure(data=[date1_trace, date2_trace], layout=layout)
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
    ], style={'textAlign': 'center'})

    # dropdown2 = html.Div([
    #     dcc.Dropdown(
    #         id='dropdown2',
    #         value='Jodhpur',
    #         options=[
    #             {'label': i, 'value': i} for i in get_unique_city()
    #         ]
    #     )
    # ])

    

    # align datepicker in the center
    select_date1 = html.Div([
        html.H6('Date 1'),
        dcc.DatePickerSingle(
            id='select_date1',
            initial_visible_month='2023-01-01',
            display_format='DD-MM-YYYY',
            date='2023-01-09'
        )
    ], style={'textAlign': 'center'})

    select_date2 = html.Div([
        html.H6('Date 2'),
        dcc.DatePickerSingle(
            id='select_date2',
            initial_visible_month='2023-01-01',
            display_format='DD-MM-YYYY',
            date='2023-04-28'
        )
    ], style={'textAlign': 'center'})

    select_dates = html.Div([
        html.Div([
            html.Div([
                html.H6('Select Date 1'),
                dcc.DatePickerSingle(
                    id='date_picker_id_1',
                    initial_visible_month='2023-01-01',
                    display_format='DD-MM-YYYY',
                    date='2023-01-01'
                )
            ], style={'textAlign': 'center', 'marginRight': '50px'}),
            html.Div([
                html.H6('Date 2'),
                dcc.DatePickerSingle(
                    id='date_picker_id_2',
                    initial_visible_month='2023-01-01',
                    display_format='DD-MM-YYYY',
                    date='2023-02-01'
                )
            ], style={'textAlign': 'center'})
        ], style={'display': 'flex', 'flexDirection': 'row'})
    ])

    graph1_tvt = html.Div([
        dcc.Graph(id='graph1_tvt')
    ])

    tvt_bar1 = html.Div([
        dcc.Graph(id='tvt_bar_id1')
    ])

    tvt_bar2 = html.Div([
        dcc.Graph(id='tvt_bar_id2')
    ])

    tvt_bar3 = html.Div([
        dcc.Graph(id='tvt_bar_id3')
    ])

    tvt_bar4 = html.Div([
        dcc.Graph(id='tvt_bar_id4')
    ])

    tvt_bar5 = html.Div([
        dcc.Graph(id='tvt_bar_id5')
    ])

    tvt_bar6 = html.Div([
        dcc.Graph(id='tvt_bar_id6')
    ])

    bar_organizer = dbc.Row([
        dbc.Col(tvt_bar1, width=6),
        dbc.Col(tvt_bar2, width=6),
        dbc.Col(tvt_bar3, width=6),
        dbc.Col(tvt_bar4, width=6),
        dbc.Col(tvt_bar5, width=6),
        dbc.Col(tvt_bar6, width=6),
    ])
        
    heading_title = html.Div([
        html.H2(children='Time vs Time', style={"text-align": "center"}),
        html.Hr(),])

    return html.Div([
        heading_title,
        
        html.Div(children='Select Dates to Compare', style={'textAlign': 'center'}),

        # dropdown1,
        # dropdown2,

        # select_dates
        select_date1,
        select_date2,
        html.Hr(),

        graph1_tvt,

        html.Hr(),

        dropdown1,
        html.Hr(),

        # tvt_bar1,
        # tvt_bar2
        bar_organizer

    ])

# layout = get_layout()