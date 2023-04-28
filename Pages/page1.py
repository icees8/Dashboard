from dash import Dash, html, dash_table
import dash
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

dash.register_page(__name__, path='/page1')

def get_layout():
    return html.Div([
        html.Div(children='My First App with Data'),
        dash_table.DataTable(data=df.to_dict('records'), page_size=10)
    ])

layout = get_layout()