from pathlib import Path

import folium
import geopandas as gpd
import pandas as pd
from folium import FeatureGroup
from folium.plugins import Search, FloatImage
from numpy import int64

from Funciones import *
from folium.plugins import MarkerCluster


# %%

#path_ini = Path("C:/ESyP/Mapas_COESPO/Resources/")
path_ini = Path("/Users/4x/COESPOAX/MapasTematicos/Resources/")

pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('max_columns', None)

df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
df_regiones = df
df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))

poligonos_maestro = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
poligonos_maestro['CVEGEO']=poligonos_maestro['CVE_ENT']+poligonos_maestro['CVE_MUN']
poligonos_maestro['CVEGEO']=poligonos_maestro['CVEGEO'].astype(int64)#ESTABA COMO FLOAT


#MAPA BASE
m3 = folium.Map([19.5426, -96.91], zoom_start=7)

LogoCOESPO = ('images/COESPO_Logo_3.png')
presidentasnueva = ('images/presidentas municipales.png')
#FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m3)
FloatImage(presidentasnueva, bottom=5, left=-1).add_to(m3)

# Se modifican los textos
df_regiones.loc[df_regiones['region'] == 'Las_Montanas', 'region'] = 'Las Montañas'
df_regiones.loc[df_regiones['region'] == 'Huasteca_Alta', 'region'] = 'Huasteca Alta'
df_regiones.loc[df_regiones['region'] == 'Huasteca_Baja', 'region'] = 'Huasteca Baja'
df_regiones.loc[df_regiones['region'] == 'Los_Tuxtlas', 'region'] = 'Los Tuxtlas'
pd.set_option('max_columns', None)

# Se definen colores para cada region
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

m = folium.Map(location=[19.8727, -96.1333], zoom_start=7, prefer_canvas=True, tiles='OpenStreetMap')

# ---- Mapa Base de Veracruz

colores = df_regiones["Color"]


def colorscale(color):
    return '"' + color + '"'


def style_function(feature):
    color = colores.get(int(feature["id"][-3:]), None)
    # print(color)
    # color=color.to_json()
    return {
        "fillOpacity": 0.9,
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
    name='Regiones',
    show=False,
    highlight_function=highlight,
    style_function=style_function,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Nombre Municipio:', 'Región:']),
).add_to(m3)

# ---HERRAMIENTA BÚSQUEDA
statesearch = Search(
    layer=mapa,
    geom_type='Polygon',
    placeholder='Búsqueda de municipio',
    collapsed=False,
    search_label='NOM_MUN',
    weight=5
).add_to(m3)




## CAPA 2014

df_2014 = pd.read_excel("ALCALDESAS_COESPO.xlsx", sheet_name='2014-2017')

poligo_AVE_2014 = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
poligo_AVE_2014['CVEGEO'] = poligo_AVE_2014['CVE_ENT']+poligo_AVE_2014['CVE_MUN']
poligo_AVE_2014['CVEGEO'] = poligo_AVE_2014['CVEGEO'].astype(int64)

df_2014=pd.merge(poligo_AVE_2014,df_2014,on="CVEGEO")
df_2014=pd.merge(df_2014,df_Localidades,on="CVEGEO")


# FILTROS df_pri2014 = df_capa2014.loc[(df_capa2014[''] =="")]
df_AVE_2014 = df_2014.loc[(df_2014['PARTIDO'] =="AVE")]
df_PRI_PVEM_NA_2014 = df_2014.loc[(df_2014['PARTIDO'] =="PRI-PVEM-NA")]
df_PAN_2014 = df_2014.loc[(df_2014['PARTIDO'] =="PAN")]

# MARCADORES 2014
mc_ave_2014 = MarkerCluster()
mc_pri_pvem_na_2014 = MarkerCluster()
mc_pan_2014 = MarkerCluster()

df_AVE_2014.reset_index(drop=True,inplace=True)

def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }

colores_2014 = df_2014["COLOR_MP"]
def style_function_2014(feature):
    color_2014 = colores_2014.get(int(feature["id"][-3:]), None)
#
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": color_2014,
        "color": color_2014,
        'line_opacity': 0.2,
    }

#
mapa_2014 = folium.GeoJson(
    df_2014,
    name='[26] Municipios con Presidentas Municipales 2014-2017',
    show=False,
    highlight_function=highlight,
    style_function=style_function_2014,
    tooltip=folium.features.GeoJsonTooltip(fields=['MUNICIPIO', 'REGION'], aliases=['Municipio:', 'Región:']),
).add_to(m3)


colores_AVE_2014 = df_AVE_2014["COLOR_MP"]
def style_function_AVE_2014(feature):
    color_AVE_2014 = colores_AVE_2014.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.9,
        "weight": 0,
        "fillColor": color_AVE_2014,
        "color": color_AVE_2014,
        'line_opacity': 0.2,
    }

ave_2014 = folium.GeoJson(
    df_AVE_2014,
    name='AVE 2014 - 2017 [1]',
    style_function=style_function_AVE_2014,
    show=False,
    highlight_function=highlight,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Municipio:', 'Región:']),
)


df_PRI_PVEM_NA_2014.reset_index(drop=True,inplace=True)
colores_PRI_PVEM_NA_2014 = df_PRI_PVEM_NA_2014["COLOR_MP"]
print(colores_PRI_PVEM_NA_2014)
def style_function_PRI_PVEM_NA_2014(feature):
    color_PRI_PVEM_NA_2014 = colores_PRI_PVEM_NA_2014.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.9,
        "weight": 0,
        "fillColor": color_PRI_PVEM_NA_2014,
        "color": color_PRI_PVEM_NA_2014,
        'line_opacity': 0.2,
    }

pri_pvem_na_2014 = folium.GeoJson(
    df_PRI_PVEM_NA_2014,
    name='PRI-PVEM-NA 2014 - 2017 [18]',
    style_function=style_function_PRI_PVEM_NA_2014,
    show=False,
    highlight_function=highlight,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Municipio:', 'Región:']),
)

colores_PAN_2014 = df_PAN_2014["COLOR_MP"]
def style_function_PAN_2014(feature):
    color_PAN_2014 = colores_PAN_2014.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.9,
        "weight": 0,
        "fillColor": color_PAN_2014,
        "color": color_PAN_2014,
        'line_opacity': 0.2,
    }

pan_2014 = folium.GeoJson(
    df_PAN_2014,
    name='PAN 2014 - 2017 [7]',
    style_function=style_function_PAN_2014,
    show=False,
    highlight_function=highlight,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Municipio:', 'Región:']),
)


#####              CAPA 2018               #####
#SE CARGAN DF DE POLIGONOS Y DE UBICACION
df_2018 = pd.read_excel("ALCALDESAS_COESPO.xlsx", sheet_name='2018-2021')
poligo_2018 = poligonos_maestro.copy(deep=True)
df_2018=pd.merge(poligo_2018,df_2018,on="CVEGEO")
df_2018=pd.merge(df_2018,df_Localidades,on="CVEGEO")

# DF CON FILTROS                       df_pri2018 = df_capa2018.loc[(df_capa2018[''] =="")]
df_MC_2018=df_2018.loc[df_2018['PARTIDO']=="MC"]
df_MORENA_2018=df_2018.loc[df_2018['PARTIDO']=="MORENA"]
df_NUEVA_ALIANZA_2018=df_2018.loc[df_2018['PARTIDO']=="NUEVA ALIANZA"]
df_PAN_2018=df_2018.loc[df_2018['PARTIDO']=="PAN"]
df_PRD_2018=df_2018.loc[df_2018['PARTIDO']=="PRD"]
df_PRI_2018=df_2018.loc[df_2018['PARTIDO']=="PRI"]
df_PVEM_2018=df_2018.loc[df_2018['PARTIDO']=="PVEM"]

mc_MC_2018=MarkerCluster()
mc_MORENA_2018=MarkerCluster()
mc_NUEVA_ALIANZA_2018=MarkerCluster()
mc_PAN_2018=MarkerCluster()
mc_PRD_2018=MarkerCluster()
mc_PRI_2018=MarkerCluster()
mc_PVEM_2018=MarkerCluster()


colores_2018 = df_2018["COLOR_MP"]
def style_function_2018(feature):
    color_2018 = colores_2018.get(int(feature["id"][-3:]), None)
#
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": color_2018,
        "color": color_2018,
        'line_opacity': 0.2,
    }
#
#
mapa_2018 = folium.GeoJson(
    df_2018,
    name='[56] Municipios con Presidentas Municipales 2018-2022',
    show=False,
    highlight_function=highlight,
    style_function=style_function_2018,
    tooltip=folium.features.GeoJsonTooltip(fields=['MUNICIPIO', 'REGION'], aliases=['Municipio:', 'Región:']),
).add_to(m3)


colores_MC_2018 = df_MC_2018["COLOR_MP"]

def style_function_MC_2018(feature):
    color_MC_2018 = colores_MC_2018.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.9,
        "weight": 0,
        "fillColor": color_MC_2018,
        "color": color_MC_2018,
        'line_opacity': 0.2,
    }

mc_2018 = folium.GeoJson(
    df_MC_2018,
    name='MC 2018 - 2021 [1]',
    style_function=style_function_MC_2018,
    show=False,
    highlight_function=highlight,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Municipio:', 'Región:']),
)


colores_MORENA_2018 = df_MORENA_2018["COLOR_MP"]

def style_function_MORENA_2018(feature):
    color_MORENA_2018 = colores_MORENA_2018.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.9,
        "weight": 0,
        "fillColor": color_MORENA_2018,
        "color": color_MORENA_2018,
        'line_opacity': 0.2,
    }

morena_2018 = folium.GeoJson(
    df_MORENA_2018,
    name='MORENA 2018 - 2021 [3]',
    style_function=style_function_MORENA_2018,
    show=False,
    highlight_function=highlight,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Municipio:', 'Región:']),
)

colores_NUEVA_ALIANZA_2018 = df_NUEVA_ALIANZA_2018["COLOR_MP"]

def style_function_NUEVA_ALIANZA_2018(feature):
    color_NUEVA_ALIANZA_2018 = colores_NUEVA_ALIANZA_2018.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.9,
        "weight": 0,
        "fillColor": color_NUEVA_ALIANZA_2018,
        "color": color_NUEVA_ALIANZA_2018,
        'line_opacity': 0.2,
    }

nueva_alianza_2018 = folium.GeoJson(
    df_NUEVA_ALIANZA_2018,
    name='NUEVA_ALIANZA 2018 - 2021 [1]',
    style_function=style_function_NUEVA_ALIANZA_2018,
    show=False,
    highlight_function=highlight,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Municipio:', 'Región:']),
)


colores_PAN_2018 = df_PAN_2018["COLOR_MP"]

def style_function_PAN_2018(feature):
    color_PAN_2018 = colores_PAN_2018.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.9,
        "weight": 0,
        "fillColor": color_PAN_2018,
        "color": color_PAN_2018,
        'line_opacity': 0.2,
    }

pan_2018 = folium.GeoJson(
    df_PAN_2018,
    name='PAN 2018 - 2021 [20]',
    style_function=style_function_PAN_2018,
    show=False,
    highlight_function=highlight,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Municipio:', 'Región:']),
)

colores_PRD_2018 = df_PRD_2018["COLOR_MP"]

def style_function_PRD_2018(feature):
    color_PRD_2018 = colores_PRD_2018.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.9,
        "weight": 0,
        "fillColor": color_PRD_2018,
        "color": color_PRD_2018,
        'line_opacity': 0.2,
    }

prd_2018 = folium.GeoJson(
    df_PRD_2018,
    name='PRD 2018 - 2021 [16]',
    style_function=style_function_PRD_2018,
    show=False,
    highlight_function=highlight,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Municipio:', 'Región:']),
)

colores_PRI_2018 = df_PRI_2018["COLOR_MP"]

def style_function_PRI_2018(feature):
    color_PRI_2018 = colores_PRI_2018.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.9,
        "weight": 0,
        "fillColor": color_PRI_2018,
        "color": color_PRI_2018,
        'line_opacity': 0.2,
    }

pri_2018 = folium.GeoJson(
    df_PRI_2018,
    name='PRI 2018 - 2021 [11]',
    style_function=style_function_PRI_2018,
    show=False,
    highlight_function=highlight,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Municipio:', 'Región:']),
)

colores_PVEM_2018 = df_PVEM_2018["COLOR_MP"]

def style_function_PVEM_2018(feature):
    color_PVEM_2018 = colores_PVEM_2018.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.9,
        "weight": 0,
        "fillColor": color_PVEM_2018,
        "color": color_PVEM_2018,
        'line_opacity': 0.2,
    }

pvem_2018 = folium.GeoJson(
    df_PVEM_2018,
    name='PVEM 2018 - 2021 [4]',
    style_function=style_function_PVEM_2018,
    show=False,
    highlight_function=highlight,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Municipio:', 'Región:']),
)



#capa 2022
df_2022 = pd.read_excel("ALCALDESAS_COESPO.xlsx", sheet_name='2022-2025')
poligo_2022 = poligonos_maestro.copy(deep=True)
df_2022=pd.merge(poligo_2022,df_2022,on="CVEGEO")
df_2022=pd.merge(df_2022,df_Localidades,on="CVEGEO")

# DF CON FILTROS                       df_pri2022 = df_capa2022.loc[(df_capa2022[''] =="")]

df_FUERZA_POR_MEXICO_2022=df_2022.loc[df_2022['PARTIDO']=="FUERZA POR MÉXICO"]
df_MORENA_2022=df_2022.loc[df_2022['PARTIDO']=="MORENA"]
df_PAN_2022=df_2022.loc[df_2022['PARTIDO']=="PAN"]
df_PES_2022=df_2022.loc[df_2022['PARTIDO']=="PES"]
df_PRD_2022=df_2022.loc[df_2022['PARTIDO']=="PRD"]
df_PRI_2022=df_2022.loc[df_2022['PARTIDO']=="PRI"]
df_PT_2022=df_2022.loc[df_2022['PARTIDO']=="PT"]
df_PVEM_2022=df_2022.loc[df_2022['PARTIDO']=="PVEM"]


mc_FUERZA_POR_MEXICO_2022=MarkerCluster()
mc_MORENA_2022=MarkerCluster()
mc_PAN_2022=MarkerCluster()
mc_PES_2022=MarkerCluster()
mc_PRD_2022=MarkerCluster()
mc_PRI_2022=MarkerCluster()
mc_PT_2022=MarkerCluster()
mc_PVEM_2022=MarkerCluster()


colores_2022 = df_2022["COLOR_MP"]
def style_function_2022(feature):
    color_2022 = colores_2022.get(int(feature["id"][-3:]), None)
#
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": color_2022,
        "color": color_2022,
        'line_opacity': 0.2,
    }
#
#
mapa_2022 = folium.GeoJson(
    df_2022,
    name='[51] Municipios con Presidentas Municipales 2022-2025',
    show=False,
    highlight_function=highlight,
    style_function=style_function_2022,
    tooltip=folium.features.GeoJsonTooltip(fields=['MUNICIPIO', 'REGION'], aliases=['Municipio:', 'Región:']),
).add_to(m3)



colores_FUERZA_POR_MEXICO_2022 = df_FUERZA_POR_MEXICO_2022["COLOR_MP"]

def style_function_FUERZA_POR_MEXICO_2022(feature):
    color_FUERZA_POR_MEXICO_2022 = colores_FUERZA_POR_MEXICO_2022.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.9,
        "weight": 0,
        "fillColor": color_FUERZA_POR_MEXICO_2022,
        "color": color_FUERZA_POR_MEXICO_2022,
        'line_opacity': 0.2,
    }

fuerza_por_mexico_2022 = folium.GeoJson(
    df_FUERZA_POR_MEXICO_2022,
    name='FUERZA POR MÉXICO 2022 - 2025 [1]',
    style_function=style_function_FUERZA_POR_MEXICO_2022,
    show=False,
    highlight_function=highlight,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Municipio:', 'Región:']),
)


colores_MORENA_2022 = df_MORENA_2022["COLOR_MP"]

def style_function_MORENA_2022(feature):
    color_MORENA_2022 = colores_MORENA_2022.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.9,
        "weight": 0,
        "fillColor": color_MORENA_2022,
        "color": color_MORENA_2022,
        'line_opacity': 0.2,
    }

morena_2022 = folium.GeoJson(
    df_MORENA_2022,
    name='MORENA 2022 - 2025 [21]',
    style_function=style_function_MORENA_2022,
    show=False,
    highlight_function=highlight,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Municipio:', 'Región:']),
)


colores_PAN_2022 = df_PAN_2022["COLOR_MP"]

def style_function_PAN_2022(feature):
    color_PAN_2022 = colores_PAN_2022.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.9,
        "weight": 0,
        "fillColor": color_PAN_2022,
        "color": color_PAN_2022,
        'line_opacity': 0.2,
    }

pan_2022 = folium.GeoJson(
    df_PAN_2022,
    name='PAN 2022 - 2025 [6]',
    style_function=style_function_PAN_2022,
    show=False,
    highlight_function=highlight,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Municipio:', 'Región:']),
)


colores_PES_2022 = df_PES_2022["COLOR_MP"]

def style_function_PES_2022(feature):
    color_PES_2022 = colores_PES_2022.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.9,
        "weight": 0,
        "fillColor": color_PES_2022,
        "color": color_PES_2022,
        'line_opacity': 0.2,
    }

pes_2022 = folium.GeoJson(
    df_PES_2022,
    name='PES_2022 - 2025 [1]',
    style_function=style_function_PES_2022,
    show=False,
    highlight_function=highlight,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Municipio:', 'Región:']),
)

colores_PRD_2022 = df_PRD_2022["COLOR_MP"]

def style_function_PRD_2022(feature):
    color_PRD_2022 = colores_PRD_2022.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.9,
        "weight": 0,
        "fillColor": color_PRD_2022,
        "color": color_PRD_2022,
        'line_opacity': 0.2,
    }

prd_2022 = folium.GeoJson(
    df_PRD_2022,
    name='PRD 2022 - 2025 [4]',
    style_function=style_function_PRD_2022,
    show=False,
    highlight_function=highlight,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Municipio:', 'Región:']),
)

colores_PRI_2022 = df_PRI_2022["COLOR_MP"]

def style_function_PRI_2022(feature):
    color_PRI_2022 = colores_PRI_2022.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.9,
        "weight": 0,
        "fillColor": color_PRI_2022,
        "color": color_PRI_2022,
        'line_opacity': 0.2,
    }

pri_2022 = folium.GeoJson(
    df_PRI_2022,
    name='PRI 2022 - 2025 [4]',
    style_function=style_function_PRI_2022,
    show=False,
    highlight_function=highlight,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Municipio:', 'Región:']),
)


colores_PT_2022 = df_PT_2022["COLOR_MP"]

def style_function_PT_2022(feature):
    color_PT_2022 = colores_PT_2022.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.9,
        "weight": 0,
        "fillColor": color_PT_2022,
        "color": color_PT_2022,
        'line_opacity': 0.2,
    }

pt_2022 = folium.GeoJson(
    df_PT_2022,
    name='PT 2022 - 2025 [4]',
    style_function=style_function_PT_2022,
    show=False,
    highlight_function=highlight,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Municipio:', 'Región:']),
)


colores_PVEM_2022 = df_PVEM_2022["COLOR_MP"]

def style_function_PVEM_2022(feature):
    color_PVEM_2022 = colores_PVEM_2022.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.9,
        "weight": 0,
        "fillColor": color_PVEM_2022,
        "color": color_PVEM_2022,
        'line_opacity': 0.2,
    }

pvem_2022 = folium.GeoJson(
    df_PVEM_2022,
    name='PVEM 2022 - 2025 [10]',
    style_function=style_function_PVEM_2022,
    show=False,
    highlight_function=highlight,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Municipio:', 'Región:']),
)


#funciones

def alcaldesas_2014(df_in):
    for row in df_in.itertuples():
        contenido = content_directorio(row.NOMBRE, row.PARTIDO, row.FOTO,row.REGION, row.MUNICIPIO)
        popup = folium.Popup(html=contenido, max_width='400')

        icon_Dependencia = folium.features.CustomIcon('images/alcaldesas_marcador3.png', icon_size=(65, 65),
                                                          icon_anchor=(22, 59),
                                                          popup_anchor=(3, -54))
        if row.PARTIDO=='PRI-PVEM-NA':
            mc=mc_pri_pvem_na_2014
        elif row.PARTIDO=='AVE':
            mc=mc_ave_2014
        elif row.PARTIDO=='PAN':
            mc=mc_pan_2014
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

def alcaldesas_2018(df_in):
    for row in df_in.itertuples():
        contenido = content_directorio(row.NOMBRE, row.PARTIDO, row.FOTO,row.REGION, row.MUNICIPIO)
        popup = folium.Popup(html=contenido, max_width='400')

        icon_Dependencia = folium.features.CustomIcon('images/alcaldesas_marcador3.png', icon_size=(65, 65),
                                                          icon_anchor=(22, 59),
                                                          popup_anchor=(3, -54))
        if row.PARTIDO == 'MC':
            mc = mc_MC_2018
        elif row.PARTIDO == 'MORENA':
            mc = mc_MORENA_2018
        elif row.PARTIDO == 'NUEVA ALIANZA':
            mc = mc_NUEVA_ALIANZA_2018
        elif row.PARTIDO == 'PAN':
            mc = mc_PAN_2018
        elif row.PARTIDO == 'PRD':
            mc = mc_PRD_2018
        elif row.PARTIDO == 'PRI':
            mc = mc_PRI_2018
        elif row.PARTIDO == 'PVEM':
            mc = mc_PVEM_2018

        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

def alcaldesas_2022(df_in):
    for row in df_in.itertuples():
        contenido = content_directorio(row.NOMBRE, row.PARTIDO, row.FOTO,row.REGION, row.MUNICIPIO)
        popup = folium.Popup(html=contenido, max_width='400')

        icon_Dependencia = folium.features.CustomIcon('images/alcaldesas_marcador3.png', icon_size=(65, 65),
                                                          icon_anchor=(22, 59),
                                                          popup_anchor=(3, -54))
        if row.PARTIDO == "FUERZA POR MÉXICO":
            mc = mc_FUERZA_POR_MEXICO_2022
        elif row.PARTIDO == "MORENA":
            mc = mc_MORENA_2022
        elif row.PARTIDO == "PAN":
            mc = mc_PAN_2022
        elif row.PARTIDO == "PES":
            mc = mc_PES_2022
        elif row.PARTIDO == "PRD":
            mc = mc_PRD_2022
        elif row.PARTIDO == "PRI":
            mc = mc_PRI_2022
        elif row.PARTIDO == "PT":
            mc = mc_PT_2022
        elif row.PARTIDO == "PVEM":
            mc = mc_PVEM_2022

        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)


alcaldesas_2014(df_2014)
alcaldesas_2018(df_2018)
alcaldesas_2022(df_2022)

mc_ave_2014.add_to(ave_2014)
mc_pri_pvem_na_2014.add_to(pri_pvem_na_2014)
mc_pan_2014.add_to(pan_2014)

mc_MC_2018.add_to(mc_2018)
mc_MORENA_2018.add_to(morena_2018)
mc_NUEVA_ALIANZA_2018.add_to(nueva_alianza_2018)
mc_PAN_2018.add_to(pan_2018)
mc_PRD_2018.add_to(prd_2018)
mc_PRI_2018.add_to(pri_2018)
mc_PVEM_2018.add_to(pvem_2018)


mc_FUERZA_POR_MEXICO_2022.add_to(fuerza_por_mexico_2022)
mc_MORENA_2022.add_to(morena_2022)
mc_PAN_2022.add_to(pan_2022)
mc_PES_2022.add_to(pes_2022)
mc_PRD_2022.add_to(prd_2022)
mc_PRI_2022.add_to(pri_2022)
mc_PT_2022.add_to(pt_2022)
mc_PVEM_2022.add_to(pvem_2022)


ave_2014.add_to(m3)
pri_pvem_na_2014.add_to(m3)
pan_2014.add_to(m3)

mc_2018.add_to(m3)
morena_2018.add_to(m3)
nueva_alianza_2018.add_to(m3)
pan_2018.add_to(m3)
prd_2018.add_to(m3)
pri_2018.add_to(m3)
pvem_2018.add_to(m3)

fuerza_por_mexico_2022.add_to(m3)
morena_2022.add_to(m3)
pan_2022.add_to(m3)
pes_2022.add_to(m3)
prd_2022.add_to(m3)
pri_2022.add_to(m3)
pt_2022.add_to(m3)
pvem_2022.add_to(m3)


m3.add_child(folium.LayerControl(collapsed=False))
#
m3.save('ALCPART.html')