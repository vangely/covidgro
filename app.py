import dash
from dash import Dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True,
           meta_tags=[{'name': 'viewport',
                       'content': 'width=device-width, initial-scale=1.0'}])
server = app.server