import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output
import plotly.express as px
import geopandas as gpd
from frontend.main import layout as main_layout
from backend.calculoinundacion import consultarDepartamento, departamentos

# Leer el archivo de colegios
colegios = gpd.read_file('C:\\Andres\\universidad\\INGENIERIA\\PROGRMACION 2\\APLICACION 4.0\\ejercicio\\EstablecimientosEducativos.zip')

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
            ),
            html.Div(
                id='colegios_seleccionados',
                className='mt-3',  # Agregar un margen superior para separar el listado de colegios
            ),
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

@app.callback(
    Output('colegios_seleccionados', 'children'),
    Input('departamento_consultado', 'value')
)
def update_colegios_seleccionados(departamento_seleccionado):
    # Filtrar los colegios por el departamento seleccionado
    colegios_departamento = colegios[colegios['DeNombre'].str.upper() == departamento_seleccionado.upper()]

    # Crear una lista de nombres de colegios
    colegios_lista = colegios_departamento['Nombre'].tolist()

    # Crear una lista ordenada de nombres de colegios
    colegios_ordenados = [html.Li(colegio) for colegio in colegios_lista]

    # Crear una lista desordenada para mostrar los nombres de colegios
    colegios_seleccionados_lista = html.Ul(colegios_ordenados)

    return colegios_seleccionados_lista

if __name__ == '__main__':
    app.run_server(debug=True)


