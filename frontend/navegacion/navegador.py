import dash
import dash_bootstrap_components as dbc
from dash import html

navegador = dbc.Container([
    html.H2('COLEGIOS AFECTADOS POR INUDACIONES'),
    html.Hr(),
    html.H6('Bienvenido a nuestra aplicación interactiva que te permite explorar la ubicación de los colegios en riesgo de sufrir inundaciones en Colombia. Esta herramienta utiliza datos geoespaciales para ayudarte a visualizar la relación entre los colegios y los cuerpos de agua, identificando aquellos que están dentro de un buffer de 500 metros de distancia de los ríos.'),
    html.H6('Instrucciones de Uso:'),
    html.H6('1.Selecciona un Departamento: Utiliza el menú desplegable para elegir un departamento específico de Colombia. Esto definirá la región que deseas explorar.'),
    html.H6('2.Explora los Colegios: Una vez que hayas seleccionado un departamento, nuestro mapa interactivo mostrará los colegios ubicados dentro de un radio de 500 metros alrededor de los ríos en esa región.'),
    html.H6('3.Información Adicional: Al hacer clic en los marcadores de los colegios, podrás obtener información adicional, como el nombre del colegio.'),
    html.H6('4.Interactúa con el Mapa: Utiliza la funcionalidad de zoom y arrastre del mapa para explorar con mayor detalle.'),
    dbc.Row([
        dbc.Col(["Juan Daniel Sandoval-20231579041"],md=3, style={'background-colo':'grey'}),
        dbc.Col(["Nestor Javier Florez-20231579058"],md=3, style={'background-colo':'gray'}),
        dbc.Col(["Andres Diaz Mazorca-20231579057"],md=3, style={'background-colo':'yellow'}),

    ])


])