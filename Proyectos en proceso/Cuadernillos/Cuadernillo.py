# %%
import folium
from folium.plugins import Search
import pandas as pd
import geopandas as gpd
from geopandas import GeoDataFrame
import matplotlib.pyplot

import branca
import numpy as np
from pathlib import Path
import array as arr
from numpy import int64
from Funciones import *
from folium import FeatureGroup, LayerControl, Map, Marker
from branca.element import Element
from branca.element import MacroElement
from jinja2 import Template


# %%
path_ini = Path("C:/ESyP/Mapas_COESPO/Resources/")
pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('display.max_columns', None)

# %%  IMAGEN FLOTANTE
LogoCOESPO = ('images/COESPO_Logo_3.png')
#Lectura de dataframes
df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
df['CVEGEO']=df['CVE_ENT']+df['CVE_MUN']
df['CVEGEO']=df['CVEGEO'].astype(int64)
df_regiones = df

#Excel de localidades
df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))

#Excel de todas las actas
df_cuadernillo = pd.read_excel("BASE CUADERNILLOS.xlsx", sheet_name='BASE_COMPLETA')


def format(x):
    return "{:.0%}".format(x*10)
df_cuadernillo['ProPob21Porcentaje'] = df_cuadernillo['ProPob21Porcentaje'].apply(format)


dfunion = pd.merge(df_cuadernillo,df_Localidades, on='CVEGEO')

df.loc[df['region'] == 'Las_Montanas', 'region'] = 'Las Montañas'
df.loc[df['region'] == 'Huasteca_Alta', 'region'] = 'Huasteca Alta'
df.loc[df['region'] == 'Huasteca_Baja', 'region'] = 'Huasteca Baja'
df.loc[df['region'] == 'Los_Tuxtlas', 'region'] = 'Los Tuxtlas'
pd.set_option('max_columns', None)

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

# ---- Mapa Base de Veracruz
colores = df.set_index("CVE_MUN")["Color"]

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
        'line_opacity': 0.7,
    }

mapa20 = folium.GeoJson(
    df,
    name='Regiones',
    highlight_function=highlight,
    style_function=style_function,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Nombre Municipio:', 'Región:']),
).add_to(m)

# ---- Imagen inferior izquierda logo COESPO
from folium.plugins import FloatImage

FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m)
# ---- Capas

#layer_0 = FeatureGroup(name='Acciones 2020', show=False)
layer_Apoyo=FeatureGroup(name='MUNICIPIOS',show=True)

# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster
mc_Apoyo=MarkerCluster()

def funcion(df_in):

    for row in df_in.itertuples():
        contenido = genera_cuadernillo(str(row.MUNICIPIO), str(row.ProPob21), str(row.ProPob21Porcentaje))

        popup = folium.Popup(html=contenido, max_width='850')
        icon_Dependencia = folium.features.CustomIcon('images/COESPO_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        if row.CVEGEO >= 3000:
                folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_Apoyo)

funcion(dfunion)

mc_Apoyo.add_to(layer_Apoyo)
layer_Apoyo.add_to(m)

# ---- Botón de Búsqueda de Municipio
statesearch = Search(
    layer=mapa20,
    geom_type='Polygon',
    placeholder='Búsqueda de municipio',
    collapsed=False,
    search_label='NOM_MUN',
    search_zoom=10,
    weight=3
).add_to(m)

folium.LayerControl(collapsed=True).add_to(m)
m.save("Cuadernillo.html")