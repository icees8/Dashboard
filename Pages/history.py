from dash import Dash, html, dash_table
import dash
import pandas as pd

dash.register_page(__name__, path='/history')

def get_layout():
    return html.Div([
        html.Div(children='MEEEEEEEEOOOOWWWWW'),
    ])

layout = get_layout()