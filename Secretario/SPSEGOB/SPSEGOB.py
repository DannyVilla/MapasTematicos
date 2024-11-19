# %%

import folium
import pandas as pd
import geopandas as gpd
from geopandas import GeoDataFrame
from folium.plugins import Search
import branca
import numpy as np
from pathlib import Path
import array as arr
from Funciones import *
from folium import FeatureGroup, LayerControl, Map, Marker

# %%
path_ini = Path("C:/ESyP/Mapas_COESPO/Resources/")
pd.options.display.float_format = '{:,.2f}'.format

from branca.element import MacroElement
from jinja2 import Template


class BindColormap(MacroElement):
    """Binds a colormap to a given layer.

    Parameters
    ----------
    colormap : branca.colormap.ColorMap
        The colormap to bind.
    """

    def __init__(self, layer, colormap):
        super(BindColormap, self).__init__()
        self.layer = layer
        self.colormap = colormap
        self._template = Template(u"""
        {% macro script(this, kwargs) %}
            {{this.colormap.get_name()}}.svg[0][0].style.display = 'block';
            {{this._parent.get_name()}}.on('overlayadd', function (eventLayer) {
                if (eventLayer.layer == {{this.layer.get_name()}}) {
                    {{this.colormap.get_name()}}.svg[0][0].style.display = 'block';
                }});
            {{this._parent.get_name()}}.on('overlayremove', function (eventLayer) {
                if (eventLayer.layer == {{this.layer.get_name()}}) {
                    {{this.colormap.get_name()}}.svg[0][0].style.display = 'none';
                }});
        {% endmacro %}
        """)  # noqa

LogoCOESPO = ('images/COESPO_Logo_3.png')

# %%  LECTURA DE DATAFRAMES
df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))


dfsegob = pd.read_excel("SPSEGOB_OK.xlsx", sheet_name='SP')
dfsegob = pd.merge(dfsegob,df_Localidades,on="CVEGEO")

df.loc[df['region'] == 'Las_Montanas', 'region'] = 'Las Montañas'
df.loc[df['region'] == 'Huasteca_Alta', 'region'] = 'Huasteca Alta'
df.loc[df['region'] == 'Huasteca_Baja', 'region'] = 'Huasteca Baja'
df.loc[df['region'] == 'Los_Tuxtlas', 'region'] = 'Los Tuxtlas'

# Se definen colores para cada region
df.loc[df['region'] == 'Capital', ['Color']] = '#e8694b'
df.loc[df['region'] == 'Huasteca Alta', ['Color']] = '#7cd5a3'
df.loc[df['region'] == 'Huasteca Baja', ['Color']] = '#96B921'
df.loc[df['region'] == 'Los_Tuxtla', ['Color']] = '#5bbdbf'
df.loc[df['region'] == 'Nautla', ['Color']] = '#FDAF3F'
df.loc[df['region'] == 'Los Tuxtlas', ['Color']] = '#5bbdbf'
df.loc[df['region'] == 'Olmeca', ['Color']] = '#4f46FF'
df.loc[df['region'] == 'Papaloapan', ['Color']] = '#846789'
df.loc[df['region'] == 'Sotavento', ['Color']] = '#6e79c1'
df.loc[df['region'] == 'Totonaca', ['Color']] = '#D0D108'
df.loc[df['region'] == 'Las Montañas', ['Color']] = '#f3b8df'

m = folium.Map(location=[19.8727, -96.1333], zoom_start=7, prefer_canvas=True, tiles='OpenStreetMap')

from folium.plugins import MarkerCluster
mc_1 = MarkerCluster()
mc_2 = MarkerCluster()
mc_3 = MarkerCluster()
mc_4 = MarkerCluster()
mc_5 = MarkerCluster()

layer_1 = FeatureGroup(name='Directoras', show=False)
layer_2 = FeatureGroup(name='Subdirectoras', show=False)
layer_3 = FeatureGroup(name='Jefas de Departamento', show=False)
layer_4 = FeatureGroup(name='Jefas de Oficina', show=False)
layer_5 = FeatureGroup(name='Operativas', show=False)

# ---- Mapa Base de Veracruz
colores = df.set_index("CVE_MUN")["Color"]

# ---- Mapa Base de Veracruz
def colorscale(color):
    return '"' + color + '"'

def style_function(feature):
    color = colores.get(int(feature["id"][-3:]), None)
    # print(color)
    # color=color.to_json()
    return {
        "fillOpacity": 0.5,
        "weight": 0,
        "fillColor": color,
        "color": color,
        'line_opacity': 0.2,
    }

def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }

# ---Mapa del Estado de Veracruz
mapa = folium.GeoJson(
    df,
    name='Base',
    highlight_function=highlight,
    style_function=style_function,
    control=False,
).add_to(m)

# ---- Imagen inferior izquierda logo COESPO
from folium.plugins import FloatImage
FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m)


def acciones(df_in):
    for row in df_in.itertuples():
        contenido = content_directorio(str(row.NOMBRE), str(row.AREA), str(row.CARGO), str(row.NIVEL))
        popup = folium.Popup(html=contenido, max_width='800')

        icon_Dependencia = folium.features.CustomIcon('images/marcador_SEGOB.png', icon_size=(70, 70),
                                                           icon_anchor=(22, 59),
                                                           popup_anchor=(3, -54))

        if row.CLASIFICACION == 'Directoras':
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_1)

        elif row.CLASIFICACION == 'Subdirectoras':
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_2)

        elif row.CLASIFICACION == 'Jefas de Departamento':
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_3)

        elif row.CLASIFICACION == 'Jefas de Oficina':
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_4)

        elif row.CLASIFICACION == 'Operativas':
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_5)

acciones(dfsegob)

tablamujeres = ('images/SEGOB.png')
from folium.plugins import FloatImage
FloatImage(tablamujeres, bottom=20, left=-2).add_to(m)


mc_1.add_to(layer_1)
mc_2.add_to(layer_2)
mc_3.add_to(layer_3)
mc_4.add_to(layer_4)
mc_5.add_to(layer_5)

layer_1.add_to(m)
layer_2.add_to(m)
layer_3.add_to(m)
layer_4.add_to(m)
layer_5.add_to(m)

pd.set_option('display.max_columns', None)

folium.LayerControl(collapsed=False).add_to(m)
m.save("SPSEGOB.html")
