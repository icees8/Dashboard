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
                    html.H4("Time vs Time", className="timevtime"),
                    html.P(
                        "Comparing Weather of a city at two different points of time",
                        className="timevtime2",
                    ),
                    dbc.Button("Go somewhere", color="info"),
                ]
            ),
        ],
        style={"width": "18rem"},
    )

    card2 = dbc.Card(
        [
            dbc.CardImg(src="assets/cityvcity.jpeg", top=True, style={"height": "10rem"}),
            dbc.CardBody(
                [
                    html.H4("City Comparison", className="cityvcity"),
                    html.P(
                        "Comparing Weather of two different cities.",
                        className="cityvcity2",
                    ),
                    dbc.Button("Go somewhere", color="info"),
                ]
            ),
        ],
        style={"width": "18rem"},
    )

    card3 = dbc.Card(
        [
            dbc.CardImg(src="assets/future.jpeg", top=True, style={"height": "10rem"}),
            dbc.CardBody(
                [
                    html.H4("Future Prediction", className="future"),
                    html.P(
                        "Get the weather of a city at a future date.",
                        className="future2",
                    ),
                    dbc.Button("Go somewhere", color="info"),
                ]
            ),
        ],
        style={"width": "18rem"},
    )

    card4 = dbc.Card(
        [
            dbc.CardImg(src="assets/currwea.jpeg", top=True, style={"height": "10rem"}),
            dbc.CardBody(
                [
                    html.H4("Current Weather", className="currwea"),
                    html.P(
                        "Get the current weather of a city.",
                        className="currwea2",
                    ),
                    dbc.Button("Go somewhere", color="info"),
                ]
            ),
        ],
        style={"width": "18rem"},
    )

    card5 = dbc.Card(
        [
            dbc.CardImg(src="assets/historical.jpeg", top=True, style={"height": "10rem"}),
            dbc.CardBody(
                [
                    html.H4("Card title", className="card-title"),
                    html.P(
                        "Some quick example text to build on the card title and "
                        "make up the bulk of the card's content.",
                        className="card-text",
                    ),
                    dbc.Button("Go somewhere", color="info"),
                ]
            ),
        ],
        style={"width": "18rem"},
    )

    cards = dbc.Col([
        dbc.Row(
            [
                dbc.Col(card1, width="auto"),
                dbc.Col(card2, width="auto"),
                dbc.Col(card3, width="auto"),
            ],
            justify="center"
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(card4, width="auto"),
                dbc.Col(card5, width="auto"),
            ],
            justify="center"
        ),
    ] ,align = "center")


    final_layout = html.Div([
        html.H1(children='My First App with Data', className="display-3"),
        html.Hr(),
        html.P(children='A simple sidebar layout with navigation links', className="lead"),
        cards,
    ])
    
    return final_layout