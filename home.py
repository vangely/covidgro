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
            "para el 11 de marzo, el brote de COVID-19 fue declarado como una pandemia. En México se confirmó el primer caso de COVID-19 el 28 de febrero,"
            " pero fue hasta el 15 de marzo que se registró el primer caso confirmado en el estado de Guerrero, ubicado al sur del país (Gobierno de México, 2020a; "
            "Gobierno del estado de Guerrero, 2020a)", style={"font-size": "1.25rem", 'textAlign': 'justify'},
            className="six columns"),
        html.P(
            "El estado de Guerrero, está clasificado como una de las entidades federativas más afectadas por la epidemia de COVID-19 en México.",
            style={"font-size": "1.25rem", 'textAlign': 'justify'},
            className="six columns"
        ),
        html.Br(),
        html.P("Se considera un área de especial interés para realizar un análisis exploratorio de datos a través de "
               "algoritmos de machine learning, que permitan identificar los patrones de comportamiento de las personas "
               "que han sido afectadas, con el propósito de identificar los sectores de la población con mayor vulnerabilidad. "
               "Para el propósito del presente trabajo, se analizarán los datos públicos registrados con respecto a la población "
               "afectada por coronavirus en el estado de Guerrero, con el propósito de conocer las vulnerabilidades de la población,"
               " los sectores que más han padecido sus efectos; así como las comorbilidades asociadad al COVID-19. ",
               style={"font-size": "1.25rem", "textAlign": "justify"},
               className="six columns"
               )
    ], style={"margin-top": "2rem",
              "margin-left": "5rem",
              # "margin-left": "auto",
              "margin-right": "5rem", }),
    html.Div(id="output-div", children=[]),
])
