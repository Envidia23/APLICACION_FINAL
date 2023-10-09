import dash
import dash_bootstrap_components as dbc

#importamos el fronted
from .navegacion.navegador import navegador

layout = dbc.Container([
    dbc.Row([
        dbc.Col(navegador,md=12, style={"background-color" : 'white'}),

    ])

])