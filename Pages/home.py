from dash import Dash, html, dash_table
import dash_bootstrap_components as dbc
import dash
import pandas as pd

dash.register_page(__name__, path='/')

def layout():
    card1 = dbc.Card(
        [
            dbc.CardImg(src="assets/timevtime.jpg", top=True, style={"height": "10rem"}),
            dbc.CardBody(
                [
                    html.H4("Time vs Time", className="card-title"),
                    html.P(
                        "Comparing Weather of a city at two different points of time",
                        className="card-text",
                    ),
                    dbc.Button("Explore", color="info", href="/timevtime"),
                ]
            ),
        ],
        style={"width": "20rem"},
        class_name="mb-3",
    )

    card2 = dbc.Card(
        [
            dbc.CardImg(src="assets/cityvcity.jpeg", top=True, style={"height": "10rem"}),
            dbc.CardBody(
                [
                    html.H4("City Comparison", className="card-title"),
                    html.P(
                        "Comparing Weather of two different cities.",
                        className="card-text",
                    ),
                    dbc.Button("Explore", color="info", href="/cityvcity"),
                ]
            ),
        ],
        style={"width": "20rem"},
        class_name="mb-3",
    )

    card3 = dbc.Card(
        [
            dbc.CardImg(src="assets/future.jpeg", top=True, style={"height": "10rem"}),
            dbc.CardBody(
                [
                    html.H4("Future Prediction", className="card-title"),
                    html.P(
                        "Get the weather of a city at a future date.",
                        className="card-text",
                    ),
                    dbc.Button("Explore", color="info", href="/future"),
                ]
            ),
        ],
        style={"width": "20rem"},
        class_name="mb-3",
    )

    card4 = dbc.Card(
        [
            dbc.CardImg(src="assets/currwea.jpeg", top=True, style={"height": "10rem"}),
            dbc.CardBody(
                [
                    html.H4("Current Weather", className="card-title"),
                    html.P(
                        "Get the current weather of the given city.",
                        className="card-text",
                    ),
                    dbc.Button("Explore", color="info", href="/currwea"),
                ]
            ),
        ],
        style={"width": "20rem"},
        class_name="mb-3",
    )

    card5 = dbc.Card(
        [
            dbc.CardImg(src="assets/historical.jpeg", top=True, style={"height": "10rem"}),
            dbc.CardBody(
                [
                    html.H4("Historical Data", className="card-title"),
                    html.P(
                        "Get the historical weather data of a given city.",
                        className="card-text",
                    ),
                    dbc.Button("Explore", color="info", href="/history"),
                ]
            ),
        ],
        style={"width": "20rem"},
        class_name="mb-3",
    )

    cards = dbc.Col([
        dbc.Row(
            [
                dbc.Col(card4, width="auto"),
                dbc.Col(card3, width="auto"),
                dbc.Col(card5, width="auto"),
                dbc.Col(card1, width="auto"),
                dbc.Col(card2, width="auto"),
            ],
            justify="center"
        ),
    ] ,align = "center")


    final_layout = html.Div([
        html.H1(children='My First App with Data', className="display-3"),
        html.Hr(),
        # html.P(children='A simple sidebar layout with navigation links', className="lead"),
        cards,
    ])
    
    return final_layout