from dash import Dash, html, dash_table
import dash
import pandas as pd

dash.register_page(__name__, path='/future')

def get_layout():
    return html.Div([
        html.Div(children='Nothing here! i "WONDER"!! why XD'),
    ])

layout = get_layout()