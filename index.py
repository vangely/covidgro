import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import home
# from dash import html
import pageGraficas
import descargaCsv

from app import app
from app import server

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        # html.H2("Menu", className="display-4"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Covid-Gro", href="/", active="exact"),
                dbc.NavLink("Gráficas", href="/pageGraficas", active="exact"),
                dbc.NavLink("Descargas", href="/descargaCsv", active="exact"),
                # dbc.NavLink("Page 2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content
])


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def display_page(pathname):
    if pathname == "/":
        return home.layout
        # return [
        #     html.H1('COVID-19 en el estado de Guerrero, México',
        #             style={'textAlign': 'center'},className="display-4")
        # ]
    elif pathname == "/pageGraficas":
        return pageGraficas.layout
    elif pathname == "/descargaCsv":
        return descargaCsv.layout
    # elif pathname == "/page-2":
    #     return [
    #         html.H1('High School in Iran',
    #                 style={'textAlign': 'center'}),
    #     ]
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == '__main__':
    app.run_server(debug=False)
