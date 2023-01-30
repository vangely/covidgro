from dash import Dash, dcc, html, Input, Output
import pandas as pd
from app import app
import dash_bootstrap_components as dbc

url = 'https://drive.google.com/file/d/1VLmHtnwqGKjffEsBa3lR8yyqq8lT8cfd/view?usp=share_link'
file_id = url.split('/')[-2]
dwn_url = 'https://drive.google.com/uc?id=' + file_id
df = pd.read_csv(dwn_url, encoding='latin')

layout = html.Div(
    [
        html.H1("Datos seleccionados del estado de Guerrero", style={'textAlign': 'center'}, className="display-4"),
        html.Hr(),
        html.P("Puede descargar el archivo en formato CSV, el cual pertenece unicamente al estado de Guerrero",
               style={"font-size": "1.25rem", 'textAlign': 'justify'}
               ),
        dbc.Button("Descargar CSV", id="btn_csv", color="primary", className="me-1"),
        dcc.Download(id="download-dataframe-csv"),
    ]
)


@app.callback(
    Output("download-dataframe-csv", "data"),
    Input("btn_csv", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_data_frame(df.to_csv, "mydf.csv")
