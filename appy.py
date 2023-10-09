import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output
import plotly.express as px
import geopandas as gpd
from frontend.main import layout as main_layout
from backend.calculoinundacion import consultarDepartamento, departamentos

# Inicializar la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Diseño de la aplicación principal
app.layout = html.Div([
    main_layout,  # Incorporar el layout de main.py aquí
    dbc.Container(
        [
        
            dcc.Dropdown(
                options=[{'label': departamento, 'value': departamento} for departamento in departamentos['DeNombre'].unique()],
                value='Cundinamarca',
                id='departamento_consultado'
            ),
            dcc.Graph(
                id="mapa",
                style={'width': '100%', "height": "600px"},
            )
        ],
        fluid=True
    )
])

@app.callback(
    Output("mapa", "figure"),
    Input("departamento_consultado", "value")
)
def update_map(departamento_consultado):
    return consultarDepartamento(departamento_consultado)

if __name__ == '__main__':
    app.run_server(debug=True)


