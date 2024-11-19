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
df_COMUPOS = pd.read_excel("COESPO_OK.xlsx", sheet_name='COMUPOS')
df_GIPEAMS = pd.read_excel("COESPO_OK.xlsx", sheet_name='GIPEAMS')
df_JORNADAS = pd.read_excel("COESPO_OK.xlsx", sheet_name='JORNADAS')
df_FOCALIZADOS_2021 = pd.read_excel("COESPO_OK.xlsx", sheet_name='FOCALIZADOS_2021')
df_FOCALIZADOS_2022 = pd.read_excel("COESPO_OK.xlsx", sheet_name='FOCALIZADOS_2022')
df_FOCALIZADOS_2023 = pd.read_excel("COESPO_OK.xlsx", sheet_name='FOCALIZADOS_2023')
df_FOCALIZADOS_2024 = pd.read_excel("COESPO_OK.xlsx", sheet_name='FOCALIZADOS_2024')


df_VERACRUZ = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
df_VERACRUZ['CVE_MUN'] = df_VERACRUZ['CVE_MUN'].apply(pd.to_numeric, errors='coerce')

df_COMUPOS_CVE_MUN = pd.merge(df_VERACRUZ, df_COMUPOS, on="CVE_MUN")
df_GIPEAMS_CVE_MUN = pd.merge(df_VERACRUZ, df_GIPEAMS, on="CVE_MUN")
df_JORNADAS_CVE_MUN = pd.merge(df_VERACRUZ, df_JORNADAS, on="CVE_MUN")

df_FOCALIZADOS_2021_CVE_MUN = pd.merge(df_VERACRUZ, df_FOCALIZADOS_2021, on="CVE_MUN")
df_FOCALIZADOS_2022_CVE_MUN = pd.merge(df_VERACRUZ, df_FOCALIZADOS_2022, on="CVE_MUN")
df_FOCALIZADOS_2023_CVE_MUN = pd.merge(df_VERACRUZ, df_FOCALIZADOS_2023, on="CVE_MUN")
df_FOCALIZADOS_2024_CVE_MUN = pd.merge(df_VERACRUZ, df_FOCALIZADOS_2024, on="CVE_MUN")



df_COMUPOS = pd.merge(df_COMUPOS,df_Localidades, on='CVEGEO')
df_GIPEAMS = pd.merge(df_GIPEAMS,df_Localidades, on='CVEGEO')
df_JORNADAS = pd.merge(df_JORNADAS,df_Localidades, on='CVEGEO')

df_FOCALIZADOS_2021 = pd.merge(df_FOCALIZADOS_2021,df_Localidades, on='CVEGEO')
df_FOCALIZADOS_2022 = pd.merge(df_FOCALIZADOS_2022,df_Localidades, on='CVEGEO')
df_FOCALIZADOS_2023 = pd.merge(df_FOCALIZADOS_2023,df_Localidades, on='CVEGEO')
df_FOCALIZADOS_2024 = pd.merge(df_FOCALIZADOS_2024,df_Localidades, on='CVEGEO')


df_COMUPOS_CVE_MUN['FECHAINSTALACION'] = df_COMUPOS_CVE_MUN['FECHAINSTALACION'].replace("00:00:00", " ")
df_JORNADAS['FECHA'] = df_JORNADAS['FECHA'].replace("00:00:00", " ")


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

layer_COMUPOS=FeatureGroup(name='COMUPOS (2022 - 2023)',show=False)
layer_GIPEAMS=FeatureGroup(name='GIPEAMS (2018 - 2023)',show=False)
layer_JORNADAS=FeatureGroup(name='Jornadas de Atención Ciudadana (2018 - 2023)',show=False)
layer_FOCALIZADOS_2021=FeatureGroup(name='Municipios Focalizados 2021',show=False)
layer_FOCALIZADOS_2022=FeatureGroup(name='Municipios Focalizados 2022',show=False)
layer_FOCALIZADOS_2023=FeatureGroup(name='Municipios Focalizados 2023',show=False)
layer_FOCALIZADOS_2024=FeatureGroup(name='Municipios Focalizados 2024',show=False)

colores = df_regiones.set_index("CVE_MUN")["Color"]



COMUPOS = df_COMUPOS["COLOR_MP"]
GIPEAMS = df_GIPEAMS["COLOR_MP"]
JORNADAS = df_JORNADAS["COLOR_MP"]

FOCALIZADOS_2021 = df_FOCALIZADOS_2021["COLOR_MP"]
FOCALIZADOS_2022 = df_FOCALIZADOS_2022["COLOR_MP"]
FOCALIZADOS_2023 = df_FOCALIZADOS_2023["COLOR_MP"]
FOCALIZADOS_2024 = df_FOCALIZADOS_2024["COLOR_MP"]

#--------------------COMUPOS------------------------
def style_function_comupos(feature):
    color_comupos = COMUPOS.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": color_comupos,
        "color": color_comupos,
        'line_opacity': 0.2,
    }

def highlight_comupos(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.9,
        'line_opacity': 0.9
    }


MAPA_COMUPOS = folium.GeoJson(
    df_COMUPOS_CVE_MUN,
    name='COMUPOS (2022 - 2023)',
    show=False,
    highlight_function=highlight_comupos,
    style_function=style_function_comupos,
)


#--------------------GIPEAMS------------------------
def style_function_gipeams(feature):
    color_gipeams = GIPEAMS.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": color_gipeams,
        "color": color_gipeams,
        'line_opacity': 0.2,
    }

def highlight_gipeams(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.9,
        'line_opacity': 0.9
    }


MAPA_GIPEAMS = folium.GeoJson(
    df_GIPEAMS_CVE_MUN,
    name='GIPEAMS (2018 - 2023)',
    show=False,
    highlight_function=highlight_gipeams,
    style_function=style_function_gipeams,
)

#--------------------JORNADAS------------------------
def style_function_jornadas(feature):
    color_jornadas = JORNADAS.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": color_jornadas,
        "color": color_jornadas,
        'line_opacity': 0.2,
    }

def highlight_jornadas(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.9,
        'line_opacity': 0.9
    }


MAPA_JORNADAS = folium.GeoJson(
    df_JORNADAS_CVE_MUN,
    name='Jornadas de Atención Ciudadana (2018 - 2023)',
    show=False,
    highlight_function=highlight_jornadas,
    style_function=style_function_jornadas,
)


#--------------------FOCALIZADOS 2021------------------------
def style_function_2021(feature):
    color_focalizados_2021 = FOCALIZADOS_2021.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": color_focalizados_2021,
        "color": color_focalizados_2021,
        'line_opacity': 0.2,
    }

def highlight_2021(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.9,
        'line_opacity': 0.9
    }


MAPA_FOCALIZADOS_2021 = folium.GeoJson(
    df_FOCALIZADOS_2021_CVE_MUN,
    name='Municipios Focalizados 2021',
    show=False,
    highlight_function=highlight_2021,
    style_function=style_function_2021,
)


#--------------------FOCALIZADOS 2022------------------------
def style_function_2022(feature):
    color_focalizados_2022 = FOCALIZADOS_2022.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": color_focalizados_2022,
        "color": color_focalizados_2022,
        'line_opacity': 0.2,
    }

def highlight_2022(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.9,
        'line_opacity': 0.9
    }


MAPA_FOCALIZADOS_2022 = folium.GeoJson(
    df_FOCALIZADOS_2022_CVE_MUN,
    name='Municipios Focalizados 2022',
    show=False,
    highlight_function=highlight_2022,
    style_function=style_function_2022,
)

#--------------------FOCALIZADOS 2023------------------------
def style_function_2023(feature):
    color_focalizados_2023 = FOCALIZADOS_2023.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": color_focalizados_2023,
        "color": color_focalizados_2023,
        'line_opacity': 0.2,
    }

def highlight_2023(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.9,
        'line_opacity': 0.9
    }


MAPA_FOCALIZADOS_2023 = folium.GeoJson(
    df_FOCALIZADOS_2023_CVE_MUN,
    name='Municipios Focalizados 2023',
    show=False,
    highlight_function=highlight_2023,
    style_function=style_function_2023,
)

#--------------------FOCALIZADOS 2024------------------------
def style_function_2024(feature):
    color_focalizados_2024 = FOCALIZADOS_2024.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": color_focalizados_2024,
        "color": color_focalizados_2024,
        'line_opacity': 0.2,
    }

def highlight_2024(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.9,
        'line_opacity': 0.9
    }


MAPA_FOCALIZADOS_2024 = folium.GeoJson(
    df_FOCALIZADOS_2024_CVE_MUN,
    name='Municipios Focalizados 2024',
    show=False,
    highlight_function=highlight_2024,
    style_function=style_function_2024,
)


# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster
mc_COMUPOS=MarkerCluster()
mc_GIPEAMS=MarkerCluster()
mc_JORNADAS=MarkerCluster()
mc_FOCALIZADOS_2021=MarkerCluster()
mc_FOCALIZADOS_2022=MarkerCluster()
mc_FOCALIZADOS_2023=MarkerCluster()
mc_FOCALIZADOS_2024=MarkerCluster()

def genera_comupos(df_in,mc):
    for row in df_in.itertuples():
        contenido = content_COMUPOS(str(row.MUNICIPIO), str(row.REGION), str(row.PRESIDENTEMUNICIPAL), str(row.FECHAINSTALACION),
                                            str(row.FOTO))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/COESPO_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

genera_comupos(df_COMUPOS,mc_COMUPOS)

def genera_gipeams(df_in,mc):
    for row in df_in.itertuples():
        contenido = content_GIPEAMS(str(row.MUNICIPIO), str(row.REGION), str(row.ANIO), str(row.FOTO))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/COESPO_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

genera_gipeams(df_GIPEAMS,mc_GIPEAMS)


def genera_jornadas(df_in,mc):
    for row in df_in.itertuples():
        contenido = content_JORNADAS(str(row.MUNICIPIO), str(row.REGION), str(row.MUJERES), str(row.HOMBRES), str(row.TOTAL),
                                    str(row.GRUPOS), str(row.ANIO), str(row.FECHA), str(row.FOTO))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/COESPO_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

genera_jornadas(df_JORNADAS,mc_JORNADAS)


def genera_municipios_focalizados(df_in, mc, anio):
    for row in df_in.itertuples():

        contenido = content_FOCALIZADOS(str(row.REGION), str(row.MUNICIPIO),
                                        str(row.NACIMIENTOS_10_14), str(row.NACIMIENTOS_15_19),
                                        str(row.NACIMIENOS_TOTAL), str(row.TFF_10_14),
                                        str(row.TEF_15_19), anio)

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/COESPO_marcador.png', icon_size=(60, 60),
                                                        icon_anchor=(22, 59),
                                                        popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)


genera_municipios_focalizados(df_FOCALIZADOS_2021, mc_FOCALIZADOS_2021, "2021")
genera_municipios_focalizados(df_FOCALIZADOS_2022, mc_FOCALIZADOS_2022, "2022")
genera_municipios_focalizados(df_FOCALIZADOS_2023, mc_FOCALIZADOS_2023, "2023")
genera_municipios_focalizados(df_FOCALIZADOS_2024, mc_FOCALIZADOS_2024, "2024")


mc_COMUPOS.add_to(MAPA_COMUPOS)
mc_GIPEAMS.add_to(MAPA_GIPEAMS)
mc_JORNADAS.add_to(MAPA_JORNADAS)
mc_FOCALIZADOS_2021.add_to(MAPA_FOCALIZADOS_2021)
mc_FOCALIZADOS_2022.add_to(MAPA_FOCALIZADOS_2022)
mc_FOCALIZADOS_2023.add_to(MAPA_FOCALIZADOS_2023)
mc_FOCALIZADOS_2024.add_to(MAPA_FOCALIZADOS_2024)

MAPA_COMUPOS.add_to(m)
MAPA_GIPEAMS.add_to(m)
MAPA_JORNADAS.add_to(m)
MAPA_FOCALIZADOS_2021.add_to(m)
MAPA_FOCALIZADOS_2022.add_to(m)
MAPA_FOCALIZADOS_2023.add_to(m)
MAPA_FOCALIZADOS_2024.add_to(m)


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
m.save("COESPO.html")
