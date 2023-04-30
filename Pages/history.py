from dash import Dash, html, dash_table, dcc , callback, Input, Output
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

def get_columns():
    return [{"label": i, "value": i} for i in df.columns]

@callback(
    Output('history_graph1', 'figure'),
    [Input('history_dropdown1', 'value'),
    Input('history_dropdown2', 'value')])
def update_graph1(city1,columns):

    city_name1 = city1

    city_data1 = df[df['name'] == city_name1]

    trace1 = go.Scatter(x=city_data1['datetime'], y=city_data1[columns], name=city_name1)

    layout = go.Layout(title = f'{columns} Time Series comparison for ' + city_name1, xaxis=dict(title='Date', tickmode='linear', dtick=7), yaxis=dict(title='Temperature (C)'))

    fig = go.Figure(data=[trace1], layout=layout)
    return fig

@callback(Output('range_graph', 'figure'),
            [Input('history_dropdown1', 'value'),
            ])
def update_graph2(city1):

    city_name = city1
    city_data = df[df['name'] == city_name]

    line_data = city_data.iloc[::5, :]

    # data
    x = line_data['datetime']
    y_min = line_data['tempmin'] # minimum values
    y_max = line_data['tempmax'] # maximum values

    # create bar chart with base=min and marker.line.width=max
    fig = go.Figure(go.Bar(
                x=x,
                y=y_min,
                base=y_min, # set base to min values
                name = 'Max-Min temperature Range'
                )
            )

    fig.add_trace(go.Scatter(
        x = x,
        y = line_data['temp'],
        mode = 'lines+markers',
        name = 'Actual temperature'
    ))

    # update layout
    fig.update_layout(
        title='Temp Variations',
        xaxis_title='Date',
        yaxis_title='Temperature (C)',
    )

    # show plot
    return fig



def layout():

    dropdown1 = html.Div([
        dcc.Dropdown(
            id='history_dropdown1',
            value='Mumbai',
            options=[
                {'label': i, 'value': i} for i in get_unique_city()
            ]
        )
    ])

    dropdown2 = html.Div([
        dcc.Dropdown(
            id='history_dropdown2',
            value='temp',
            options=[
                i for i in get_columns()
            ]
        )
    ])

    graph1 = html.Div([
        dcc.Graph(id='history_graph1')
    ])

    graph2 = html.Div([
        dcc.Graph(id='range_graph')
    ])

    heading_title = html.Div([
        html.H2(children='Historical Data', style={"text-align": "center"}),
        html.Hr(),])

    return html.Div([
        # html.Div(children='NEWWWWWWWWWWWWWWWWW YOOOOOOOOOOOrk'),
        heading_title,
        html.Div(children='Select City and Feature', style={'textAlign': 'center'}),

        dropdown1,
        dropdown2,

        html.Hr(),
        graph1,
        graph2
    ])

# layout = get_layout()