import folium
from folium.plugins import Search
import pandas as pd
import geopandas as gpd
from pathlib import Path
from numpy import int64
from Funciones import *
from folium import FeatureGroup

import requests
from bs4 import BeautifulSoup

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
df_gobernador_2021 = pd.read_excel("GOBERNADOR_OK.xlsx", sheet_name='GOBERNADOR_2021')
df_gobernador_2022 = pd.read_excel("GOBERNADOR_OK.xlsx", sheet_name='GOBERNADOR_2022')
df_gobernador_2023 = pd.read_excel("GOBERNADOR_OK.xlsx", sheet_name='GOBERNADOR_2023')

df_gobernador_2021 = pd.merge(df_gobernador_2021,df_Localidades, on='CVEGEO')
df_gobernador_2022 = pd.merge(df_gobernador_2022, df_Localidades, on="CVEGEO")
df_gobernador_2023 = pd.merge(df_gobernador_2023, df_Localidades, on="CVEGEO")

df_gobernador_2021['FECHA'] = df_gobernador_2021['FECHA'].dt.strftime('%d/%m/%Y')
df_gobernador_2022['FECHA'] = df_gobernador_2022['FECHA'].dt.strftime('%d/%m/%Y')
df_gobernador_2023['FECHA'] = df_gobernador_2023['FECHA'].dt.strftime('%d/%m/%Y')

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
        'line_opacity': 0.7
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

layer_Apoyo=FeatureGroup(name='Apoyo a Ciudadanía (2021 - 2022)',show=False)
layer_Gobernabilidad=FeatureGroup(name='Gobernabilidad (Acuerdos, programas, entre otros) (2021 - 2022)',show=False)
layer_Promocion=FeatureGroup(name='Integración Familiar y Cultura de Paz (2021 - 2022)',show=False)
layer_Mesas_2022=FeatureGroup(name='Mesas Coordinación de la Paz (2021 - 2022)',show=False)

# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster
mc_Apoyo=MarkerCluster()
mc_Gobernabilidad=MarkerCluster()
mc_Promocion=MarkerCluster()
mc_Mesas_2022=MarkerCluster()

def genera_actividades(df_in):
    for row in df_in.itertuples():
        contenido = content_gobernador(str(row.MUNICIPIO), str(row.TEXTO), str(row.FECHA),
                                            str(row.CLASIFICACION),str(row.FOTO),str(row.PUB))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/GOBERNADOR_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        if row.CLASIFICACION == "Mesas Coordinación de la Paz":
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_Mesas_2022)

        elif row.CLASIFICACION == "Apoyo a ciudadanía":
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_Apoyo)

        elif row.CLASIFICACION == "Gobernabilidad(Acuerdos,programas, etc.)":
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_Gobernabilidad)

        elif row.CLASIFICACION == "Promoción turística":
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_Promocion)

genera_actividades(df_gobernador_2021)
genera_actividades(df_gobernador_2022)

####################################################

layer_Apoyo_2023=FeatureGroup(name='Apoyo a Ciudadanía (2023)',show=False)
layer_Gobernabilidad_2023=FeatureGroup(name='Gobernabilidad (Acuerdos, programas, entre otros) (2023)',show=False)
layer_Promocion_2023=FeatureGroup(name='Promociones Turisticas (2023)',show=False)
layer_Mesas_2023=FeatureGroup(name='Mesas Coordinación de la Paz (2023)',show=False)

mc_Apoyo_2023=MarkerCluster()
mc_Gobernabilidad_2023=MarkerCluster()
mc_Promocion_2023=MarkerCluster()
mc_Mesas_2023=MarkerCluster()

def genera_actividades_2023(df_in):
    for row in df_in.itertuples():
        contenido = content_gobernador_2023(str(row.MUNICIPIO), str(row.TEXTO), str(row.FECHA),str(row.URL),
                                            str(row.CLASIFICACION),str(row.FOTO),str(row.PUB))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/GOBERNADOR_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        if row.CLASIFICACION == "Mesas Coordinación de la Paz":
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_Mesas_2023)

        elif row.CLASIFICACION == "Apoyo a ciudadanía":
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_Apoyo_2023)

        elif row.CLASIFICACION == "Gobernabilidad(Acuerdos,programas, etc.)":
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_Gobernabilidad_2023)

        elif row.CLASIFICACION == "Promoción turística":
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_Promocion_2023)

genera_actividades_2023(df_gobernador_2023)

###########################################

mc_Apoyo.add_to(layer_Apoyo)
mc_Gobernabilidad.add_to(layer_Gobernabilidad)
mc_Promocion.add_to(layer_Promocion)
mc_Mesas_2022.add_to(layer_Mesas_2022)

layer_Apoyo.add_to(m)
layer_Gobernabilidad.add_to(m)
layer_Promocion.add_to(m)
layer_Mesas_2022.add_to(m)

mc_Apoyo_2023.add_to(layer_Apoyo_2023)
mc_Gobernabilidad_2023.add_to(layer_Gobernabilidad_2023)
mc_Promocion_2023.add_to(layer_Promocion_2023)
mc_Mesas_2023.add_to(layer_Mesas_2023)

layer_Apoyo_2023.add_to(m)
layer_Gobernabilidad_2023.add_to(m)
layer_Promocion_2023.add_to(m)
layer_Mesas_2023.add_to(m)

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
folium.LayerControl(collapsed=False).add_to(m)
m.save("GOBERNADOR.html")
