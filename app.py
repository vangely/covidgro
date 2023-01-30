import dash
from dash import Dash
import dash_bootstrap_components as dbc


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True,
           meta_tags=[{'name': 'viewport',
                       'content': 'width=device-width, initial-scale=1.0'}])
server = app.server

# SIDEBAR_STYLE = {
#     "position": "fixed",
#     "top": 0,
#     "left": 0,
#     "bottom": 0,
#     "width": "16rem",
#     "padding": "2rem 1rem",
#     "background-color": "#f8f9fa",
# }
# CONTENT_STYLE = {
#     "margin-left": "18rem",
#     "margin-right": "2rem",
#     "padding": "2rem 1rem",
# }
#
# sidebar = html.Div(
#     [
#         html.H2("Sidebar", className="display-4"),
#         html.Hr(),
#         html.P(
#             "Number of students per education level", className="lead"
#         ),
#         dbc.Nav(
#             [
#                 dbc.NavLink("Home", href="/", active="exact"),
#                 dbc.NavLink("Graficas", href="/pageGraficas", active="exact"),
#                 # dbc.NavLink("Page 2", href="/page-2", active="exact"),
#             ],
#             vertical=True,
#             pills=True,
#         ),
#     ],
#     style=SIDEBAR_STYLE,
# )
#
# content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)
#
# app.layout = html.Div([
#     dcc.Location(id="url"),
#     sidebar,
#     content
# ])
#
#
# @app.callback(
#     Output("page-content", "children"),
#     [Input("url", "pathname")]
# )
# def display_page(pathname):
#     if pathname == "/":
#         return [
#             html.H1('Kindergarten in Iran',
#                     style={'textAlign': 'center'})
#         ]
#     elif pathname == "/pageGraficas":
#        return pageGraficas.layout
#     elif pathname == "/page-2":
#         return [
#             html.H1('High School in Iran',
#                     style={'textAlign': 'center'}),
#             dcc.Graph(id='bargraph',
#                       figure=px.bar(df, barmode='group', x='Years',
#                                     y=['Girls High School', 'Boys High School']))
#         ]
#     # If the user tries to reach a different page, return a 404 message
#     return dbc.Jumbotron(
#         [
#             html.H1("404: Not found", className="text-danger"),
#             html.Hr(),
#             html.P(f"The pathname {pathname} was not recognised..."),
#         ]
#     )
#

