import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from app import app
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

# app = Dash(__name__)

url = 'https://drive.google.com/file/d/1VLmHtnwqGKjffEsBa3lR8yyqq8lT8cfd/view?usp=share_link'
file_id = url.split('/')[-2]
dwn_url = 'https://drive.google.com/uc?id=' + file_id
df = pd.read_csv(dwn_url, encoding='latin')
print(df.head())


def obtenerSIPadecimientos(tupla, total_re):
    neumonia = tupla[(tupla["NEUMONIA"] == 'SI')]
    diabetes = tupla[(tupla["DIABETES"] == 'SI')]
    epoc = tupla[(tupla["EPOC"] == 'SI')]
    asma = tupla[(tupla["ASMA"] == 'SI')]
    inmusupr = tupla[(tupla["INMUSUPR"] == 'SI')]
    hipertension = tupla[(tupla["HIPERTENSION"] == 'SI')]
    otra_com = tupla[(tupla["OTRA_COM"] == 'SI')]
    cardiovascular = tupla[(tupla["CARDIOVASCULAR"] == 'SI')]
    obesidad = tupla[(tupla["OBESIDAD"] == 'SI')]
    renal = tupla[(tupla["RENAL_CRONICA"] == 'SI')]
    tabaquismo = tupla[(tupla["TABAQUISMO"] == 'SI')]

    dfPadecimientos = pd.DataFrame({'Padecimientos': ['NEUMONIA', 'DIABETES', 'EPOC', 'ASMA', 'INMUSUPR',
                                                      'HIPERTENSION', 'OTRA_COM', 'CARDIOVASCULAR', 'OBESIDAD',
                                                      'RENAL_CRONICA', 'TABAQUISMO'],
                                    'Cantidad': [len(neumonia), len(diabetes), len(epoc), len(asma), len(inmusupr),
                                                 len(hipertension), len(otra_com), len(cardiovascular), len(obesidad),
                                                 len(renal), len(tabaquismo)],
                                    'Porcentaje': [obtenerPorcentaje(len(neumonia), total_re),
                                                   obtenerPorcentaje(len(diabetes), total_re),
                                                   obtenerPorcentaje(len(epoc), total_re),
                                                   obtenerPorcentaje(len(asma), total_re),
                                                   obtenerPorcentaje(len(inmusupr), total_re),
                                                   obtenerPorcentaje(len(hipertension), total_re),
                                                   obtenerPorcentaje(len(otra_com), total_re),
                                                   obtenerPorcentaje(len(cardiovascular), total_re),
                                                   obtenerPorcentaje(len(obesidad), total_re),
                                                   obtenerPorcentaje(len(renal), total_re),
                                                   obtenerPorcentaje(len(tabaquismo), total_re)]})
    return dfPadecimientos


def obtenerPorcentaje(nDat, totRes):
    resPorcen = (100 / int(totRes)) * int(nDat)
    return round(resPorcen, 4)


totalHabEstado = 3540685

total_rows = len(df.axes[0])  # ===> Axes of 0 is for a row
porcentajeRegDeToH = (100 / int(totalHabEstado)) * int(total_rows)
print(total_rows, " de registros, equivalente a ", round(porcentajeRegDeToH, 2),
      "% de su total de habitantes en el 2020")

print("\n\n**** FALLECIDOS QUE REQUIRIERON UCI:\n")
soloDefunciones = df[(df["FECHA_DEF"] != '9999-99-99')]
total_fallecidos = len(soloDefunciones.axes[0])
soloUICDef = soloDefunciones[(soloDefunciones["UCI"] == 'SI')]
cantindadMP2 = soloUICDef[(soloUICDef["SEXO"] == 'M')]
cantindadHP2 = soloUICDef[(soloUICDef["SEXO"] == 'H')]
resDefUIC = soloUICDef.groupby(['SEXO']).size()
print(resDefUIC)
# print(soloUICDef["SEXO"])
print(total_fallecidos, " de fallecidos, equivalente a ", round((100 / int(total_rows)) * int(total_fallecidos), 2),
      "% del total de registros")

print("\n\n**** PORCENTAJE DEFUNCIONES DEL TOTAL DE REGISTROS:\n")
print("MUJERES: ", round((100 / int(total_rows)) * int(len(cantindadMP2.axes[0])), 6), "% -  HOMBRES: ",
      round((100 / int(total_rows)) * int(len(cantindadHP2.axes[0])), 6), "%")

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# ENTIDAD_NAC


layout = html.Div([
    # html.Div([
    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5("Muestra de población", className="card-title",
                                style={"textAlign": "center", "font-size": "1.5rem"}),
                        html.P(f"{totalHabEstado}", style={"textAlign": "center", "font-size": "2rem"}),
                        # dbc.Button("Go somewhere", color="primary"),
                    ]
                ), style={"border": "none"}
            ), width=4, className="shadow p-3 mb-5 bg-white rounded col-lg-3 col-md-6 col-sm-12 col-xs-12",
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5("Hombres fallecidos", className="card-title",
                                style={"textAlign": "center", "font-size": "1.5rem"}),
                        html.P(f"{resDefUIC['H']}", style={"textAlign": "center", "font-size": "2rem"}),
                        # dbc.Button("Go somewhere", color="primary"),
                    ]
                ), style={"border": "none"}
            ), width=3, className="shadow p-3 mb-5 bg-white rounded col-lg-3 col-md-6 col-sm-12 col-xs-12",
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5("Mujeres fallecidas", className="card-title",
                                style={"textAlign": "center", "font-size": "1.5rem"}),
                        html.P(f"{resDefUIC['M']}", style={"textAlign": "center", "font-size": "2rem"}),
                        # dbc.Button("Go somewhere", color="primary"),
                    ]
                ), style={"border": "none"}
            ), width=3, className="shadow p-3 mb-5 bg-white rounded col-lg-3 col-md-6 col-sm-12 col-xs-12",
        ),
    ], className="row justify-content-evenly"),
    # ]),
    html.Br(),
    html.Br(),
    html.Div(html.Div([
        html.P('Tipos de Gráficas:'),
        html.Br(),
        dcc.Dropdown(
            id='opciones', clearable=False,
            value="edad",
            options=[
                {'label': 'Fallecimiento por género', 'value': 'edad'},
                {'label': 'Población Indígena', 'value': 'indigena'},
                {'label': 'Padecimientos asociados al COVID', 'value': 'padecimientos'},
                {'label': 'Hospitalizaciones', 'value': 'hospital'},
            ],
        )
    ])),
    # html.Div(html.Div([
    #
    # ]
    # )),
    html.Div(id="output-div", children=[]),
])


@app.callback(
    Output('output-div', 'children'),
    Input('opciones', 'value')
)
# print(resultadoUICPorPadecimientos)
# def graficas():

def update_output(value):
    if value == "edad":
        print("EDADES")
        # soloUICDef.groupby('SEXO')['ID_REGISTRO'].size()
        # eje_x = resDefUIC[0].tolist()
        # ## Valores para el eje y
        # eje_y = resDefUIC[0].tolist()
        colores = ["Hombres", "Mujeres"]
        figGen = px.bar(x=['Hombres', 'Mujeres'], y=[resDefUIC['H'], resDefUIC['M']],
                        color=colores, color_discrete_map={'Hombres': '#30BFDD', 'Mujeres': '#F7C0BB'})
        return [
            html.Div([
                html.Br(),
                html.Br(),
                # html.H1("Padecimientos que la población indigena contrajo", style={'textAlign': 'center'},
                #         className="display-4"),
                html.Div([dcc.Graph(figure=figGen)], className="six columns"),
            ])
        ]

        # Selección opción de Padecimientos Asociados al COVID - Pastel
    if value == 'indigena':
        print("Ingena")
        print("\n\n**** PADECIMIENTOS EN INDIGENAS:\n")
        soloIndigenas = df[(df["INDIGENA"] == 'SI')]
        resultadoPadComunesInd = obtenerSIPadecimientos(soloIndigenas, total_rows)
        print(resultadoPadComunesInd)

        # figIndig = px.bar(x=resultadoPadComunesInd['Padecimientos'], y=resultadoPadComunesInd['Cantidad'])
        figIndig = px.scatter(x=resultadoPadComunesInd['Padecimientos'], y=resultadoPadComunesInd['Cantidad'])
        return [
            html.Div([
                # html.Div([
                #     html.H1('Enfermedad que mas padecieron:')
                # ]),
                html.Br(),
                html.Br(),
                html.H1("Padecimientos que la población indígena contrajo", style={'textAlign': 'center'},
                        className="display-4"),
                html.Div([dcc.Graph(figure=figIndig)], className="six columns"),
                # html.Div([dcc.Graph(figure=figBarras)], className="six columns"),
                # fig.show(), className="six columns"
            ])
        ]
    if value == 'padecimientos':
        # print("HOLA")
        # 1.- ¿Que tipo de padecimiento hace que las personas infectadas requieran ingresar a una unidad de cuidados intesivo?
        print("\n\n**** UIC POR PADECIMIENTO:\n")
        soloUCI = df[(df["UCI"] == 'SI')]
        resultadoUICPorPadecimientos = obtenerSIPadecimientos(soloUCI, total_rows)
        print(resultadoUICPorPadecimientos)
        fig = px.pie(values=resultadoUICPorPadecimientos['Cantidad'],
                     names=resultadoUICPorPadecimientos['Padecimientos'])
        figBarras = px.bar(x=resultadoUICPorPadecimientos['Padecimientos'], y=resultadoUICPorPadecimientos['Cantidad'])
        suma_padecimientos = 0
        for padecimiento in resultadoUICPorPadecimientos['Cantidad']:
            suma_padecimientos += padecimiento
        print(suma_padecimientos)
        # fig.show()
        return [
            html.Div([
                html.Br(),
                html.Br(),
                html.H1("Padecimientos que provocaron ingreso a UCI", style={'textAlign': 'center'},
                        className="display-4"),
                html.Div([
                    html.Br(),
                    html.Br(),
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5("Total de personas que sufrieron padecimientos", className="card-title",
                                        style={"textAlign": "center", "font-size": "1.5rem"}),
                                html.P(f"{suma_padecimientos}", style={"textAlign": "center", "font-size": "2rem"}),
                                # dbc.Button("Go somewhere", color="primary"),
                            ]
                        ), className="w-50",
                    ),
                ], style={'align-content': 'center'}),
                html.Br(),

                html.Br(),
                html.Div([
                    html.Div([dcc.Graph(figure=fig)], className="six columns", style={'align-content': 'center', }),
                    html.Div([dcc.Graph(figure=figBarras)], className="six columns"),
                ], style={'align-content': 'center'})
                # fig.show(), className="six columns"
            ], style={'align-content': 'center'}),
        ]
    if value == 'hospital':
        print("Hospital")
        # 3.- ¿Que porcentaje por padecimiento requirio hospitalizacion?
        print("\n\n**** PADECIMIENTOS CON HOSPITALIZACION:\n")
        soloHosp = df[(df["TIPO_PACIENTE"] == 'hosp')]
        resultadoUICPorPadecimientos = obtenerSIPadecimientos(soloHosp, total_rows)
        print(resultadoUICPorPadecimientos)
        figSex = go.Figure(data=[
            go.Scatter(x=resultadoUICPorPadecimientos['Padecimientos'], y=resultadoUICPorPadecimientos['Cantidad'])])
        return [
            html.Div([
                html.Br(),
                html.Br(),
                html.H1("Padecimientos que requirieron hospitalizaciones", style={'textAlign': 'center'},
                        className="display-4"),
                html.Div([dcc.Graph(figure=figSex)], className="six columns"),
                # html.Div([dcc.Graph(figure=figBarras)], className="six columns"),
                # fig.show(), className="six columns"
            ])
        ]  # return [

# if __name__ == '__main__':
#     app.run_server(debug=False)
