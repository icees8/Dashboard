import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
import importlib

app = dash.Dash(__name__,use_pages=True,pages_folder="./Pages",external_stylesheets=[dbc.themes.UNITED])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
CONTENT_STYLE = {
    "margin-left"   : "18rem",
    "margin-right"  : "2rem",
    "padding"       : "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Weather Dashboard", className="display-6"),
        html.Hr(),
        html.P(
            "", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home Page"         , href="/"          , active="exact"),
                dbc.NavLink("Current Weather"   , href="/currwea"   , active="exact"),
                dbc.NavLink("Future Prediction" , href="/future"    , active="exact"),
                dbc.NavLink("Historical Data"   , href="/history"   , active="exact"),
                dbc.NavLink("Time vs Time"      , href="/timevtime" , active="exact"),
                dbc.NavLink("City vs City"   , href="/cityvcity" , active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content    = html.Div([dash.page_container],id="page-content", style=CONTENT_STYLE)
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

if __name__ == "__main__":
    app.run_server(debug=True)