from dash import Dash, html, dash_table
import dash
import pandas as pd

dash.register_page(__name__, path='/currwea')

def get_layout():
    return html.Div([
        html.Div(children='Its Rainy'),
    ])

layout = get_layout()