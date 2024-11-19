import folium
import pandas as pd
import geopandas as gpd
from geopandas import GeoDataFrame
from folium.plugins import Search
import branca
import numpy as np
from pathlib import Path
import array as arr
from realce import *

from folium import FeatureGroup, LayerControl, Map, Marker

# %%



#path_ini = Path("C:/ESyP/Mapas_COESPO/Resources/")
path_ini = Path("/Users/4x/COESPOAX/MapasTematicos/Resources")
pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('max_columns', None)

df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
print(df)
df_regiones = df

df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))
df_alcaldesas2013 = pd.read_excel("alcaldesas.xlsx", sheet_name='2013')

#Se ajustan nombre de la región para desplegar
df_regiones.loc[df_regiones['region'] == 'Las_Montanas', 'region'] = 'Las Montañas'
df_regiones.loc[df_regiones['region'] == 'Huasteca_Alta', 'region'] = 'Huasteca Alta'
df_regiones.loc[df_regiones['region'] == 'Huasteca_Baja', 'region'] = 'Huasteca Baja'
df_regiones.loc[df_regiones['region'] == 'Los_Tuxtlas', 'region'] = 'Los Tuxtlas'
df_Capital = df_regiones.loc[df_regiones['region'] == 'Capital']
df_Huasteca_alta = df_regiones.loc[df_regiones['region'] == 'Huasteca Alta']
df_Huasteca_baja = df_regiones.loc[df_regiones['region'] == 'Huasteca Baja']
df_Los_Tuxtla = df_regiones.loc[df_regiones['region'] == 'Los Tuxtla']
df_Nautla = df_regiones.loc[df_regiones['region'] == 'Nautla']
df_Los_Tuxtlas = df_regiones.loc[df_regiones['region'] == 'Los Tuxtlas']
df_Olmeca = df_regiones.loc[df_regiones['region'] == 'Olmeca']
df_Papaloapan = df_regiones.loc[df_regiones['region'] == 'Papaloapan']
df_Sotavento = df_regiones.loc[df_regiones['region'] == 'Sotavento']
df_Totonaca = df_regiones.loc[df_regiones['region'] == 'Totonaca']
df_Las_Montanas = df_regiones.loc[df_regiones['region'] == 'Las Montañas']

#Se definen colores para cada region
df_regiones.loc[df_regiones['region'] == 'Capital', ['Color']] = '#e8694b'
df_regiones.loc[df_regiones['region'] == 'Huasteca Alta', ['Color']] = '#7cd5a3'
df_regiones.loc[df_regiones['region'] == 'Huasteca Baja', ['Color']] = '#96B921'
df_regiones.loc[df_regiones['region'] == 'Los_Tuxtla', ['Color']] = '#5bbdbf'
df_regiones.loc[df_regiones['region'] == 'Nautla', ['Color']] = '#FDAF3F'
df_regiones.loc[df_regiones['region'] == 'Los Tuxtlas', ['Color']] = '#5bbdbf'
df_regiones.loc[df_regiones['region'] == 'Olmeca', ['Color']] = '#4f46FF'
df_regiones.loc[df_regiones['region'] == 'Papaloapan', ['Color']] = '#846789'
df_regiones.loc[df_regiones['region'] == 'Sotavento', ['Color']] = '#6e79c1'
df_regiones.loc[df_regiones['region'] == 'Totonaca', ['Color']] = '#D0D108'
df_regiones.loc[df_regiones['region'] == 'Las Montañas', ['Color']] = '#f3b8df'


from folium.plugins import FloatImage

LogoCOESPO = ('COESPO_Logo_3.png')

# ---Mapa
from folium.plugins import MarkerCluster

m3 = folium.Map([19.5426, -96.91], zoom_start=7)

# ---MarkerClusters para cada región de Veracruz
mc_Capital = MarkerCluster()
mc_Las_Montanas = MarkerCluster()
mc_Huasteca_alta = MarkerCluster()
mc_Huasteca_baja = MarkerCluster()
mc_Nautla = MarkerCluster()
mc_Los_Tuxtlas = MarkerCluster()
mc_Olmeca = MarkerCluster()
mc_Papaloapan = MarkerCluster()
mc_Sotavento = MarkerCluster()
mc_Totonaca = MarkerCluster()

colores = df_regiones.set_index("CVE_MUN")["Color"]
print(colores)

def colorscale(color):
    return '"'+color+'"'

def style_function(feature):
    color = colores.get(int(feature["id"][-3:]), None)
    #print(color)
    #color=color.to_json()
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
    df_regiones,
    name='Regiones Veracruz',
    highlight_function=highlight,
    style_function=style_function, tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Nombre Municipio:', 'Región:']),
).add_to(m3)
print(df_regiones)

statesearch = Search(
     layer=mapa,
     geom_type='Polygon',
     placeholder='Búsqueda de municipio',
     collapsed=False,
     search_label='NOM_MUN',
     weight=5
).add_to(m3)

FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m3)
m3.add_child(folium.LayerControl())
m3.save('BasePintada.html')