import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# from app import app


layout = html.Div([
    html.H1("COVID-19 en el estado de Guerrero, México", style={'textAlign': 'center'}, className="display-4"),
    html.Hr(),
    html.Br(),
    html.Div([
        html.P(
            "La enfermedad por coronavirus (COVID‑19) es una enfermedad infecciosa provocada por el virus SARS-CoV-2.",
            style={"font-size": "1.25rem", 'textAlign': 'justify'},
            className="six columns"
        ),
        html.P(
            "El 30 de enero de 2020, la Organización Mundial de la Salud (OMS) declaró a la enfermedad COVID-19 como una emergencia internacional y, "
            "para el 11 de marzo, el brote de COVID-19 fue declarado como una pandemia (OMS, 2020a; OMS, 2020b). En México se confirmó el primer caso de COVID-19 el 28 de febrero,"
            " pero fue hasta el 15 de marzo que se registró el primer caso confirmado en el estado de Guerrero, ubicado al sur del país (Gobierno de México, 2020a; "
            "Gobierno del estado de Guerrero, 2020a)", style={"font-size": "1.25rem", 'textAlign': 'justify'},
            className="six columns"),
        html.P(
            "El estado de Guerrero, está clasificado como una de las entidades federativas más afectadas por la epidemia de COVID-19 en México.",
            style={"font-size": "1.25rem", 'textAlign': 'justify'},
            className="six columns"
        )
    ]),
    html.Div(id="output-div", children=[]),
])
