from pathlib import Path

import folium
import geopandas as gpd
import pandas as pd
from folium import FeatureGroup
from folium.plugins import Search

from Funciones import *
# %%

path_ini = Path("C:/ESyP/Mapas_COESPO/Resources/")
#path_ini = Path("/Users/4x/COESPOAX/MapasTematicos/Resources")
pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('max_columns', None)

df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))


distrito_federal=gpd.read_file("DF/DISTRITO_FEDERAL.shp")
colores_f = ['#e8694b', '#7cd5a3', '#96B921', '#5bbdbf', '#FDAF3F', '#5bbdbf', '#4f46FF', '#846789', '#6e79c1',
           '#D0D108', '#f3b8df','#B704C6','#C61E04','#C61E04','#2A04C6','#18DF0E','#F5F50D','#0DEEF5','#5AA7A9','#F6DB14']
ids=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']
distrito_federal['Color']=colores_f
distrito_federal['indice']=ids


distrito_local=gpd.read_file("DL/DISTRITO_LOCAL.shp")
colores_l = ['#e8694b', '#7cd5a3', '#96B921', '#5bbdbf', '#FDAF3F', '#5bbdbf', '#4f46FF', '#846789', '#6e79c1',
           '#D0D108', '#f3b8df','#B704C6','#C61E04','#C61E04','#2A04C6','#18DF0E','#F5F50D','#0DEEF5','#5AA7A9',
             '#F6DB14','#e8694b', '#7cd5a3', '#96B921', '#5bbdbf', '#FDAF3F', '#5bbdbf', '#4f46FF', '#846789', '#6e79c1','#18DF0E']
ids_l=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19','20',
       '21', '22', '23', '24', '25', '26', '27', '28', '29']
distrito_local['Color']=colores_l
distrito_local['indice']=ids_l

df_LOCAL = pd.read_csv("csv/DistritosLocales.csv")
df_FEDERAL = pd.read_csv("csv/DistritosFederales.csv")

#TODO LO ESTATAL
df_E2008 = pd.read_excel("DIPUTADASPARTIDO_OK.xlsx", sheet_name='ESTATAL_2008')
df_E2010 = pd.read_excel("DIPUTADASPARTIDO_OK.xlsx", sheet_name='ESTATAL_2010')
df_E2013 = pd.read_excel("DIPUTADASPARTIDO_OK.xlsx", sheet_name='ESTATAL_2013')
df_E2016 = pd.read_excel("DIPUTADASPARTIDO_OK.xlsx", sheet_name='ESTATAL_2016')
df_E2018 = pd.read_excel("DIPUTADASPARTIDO_OK.xlsx", sheet_name='ESTATAL_2018')
df_E2021 = pd.read_excel("DIPUTADASPARTIDO_OK.xlsx", sheet_name='ESTATAL_2021')

#TODO LO FEDERAL
df_F2009 = pd.read_excel("DIPUTADASPARTIDO_OK.xlsx", sheet_name='FEDERAL_2009')
df_F2012 = pd.read_excel("DIPUTADASPARTIDO_OK.xlsx", sheet_name='FEDERAL_2012')
df_F2015 = pd.read_excel("DIPUTADASPARTIDO_OK.xlsx", sheet_name='FEDERAL_2015')
df_F2018 = pd.read_excel("DIPUTADASPARTIDO_OK.xlsx", sheet_name='FEDERAL_2018')
df_F2021 = pd.read_excel("DIPUTADASPARTIDO_OK.xlsx", sheet_name='FEDERAL_2021')


df_E2021PROPORCIONAL = pd.read_excel("DIPUTADASPARTIDO_OK.xlsx", sheet_name='REPPROP')

capa_base2013 = gpd.read_file("DL/DISTRITO_LOCAL.shp")
capa_base2016 = gpd.read_file("DL/DISTRITO_LOCAL.shp")
capa_base2018 = gpd.read_file("DL/DISTRITO_LOCAL.shp")
capa_base2021 = gpd.read_file("DL/DISTRITO_LOCAL.shp")

print(capa_base2013)

capa_base2013['DISTRITO_L'] = capa_base2013['DISTRITO_L'].apply(pd.to_numeric, errors='coerce')
capa_base2016['DISTRITO_L'] = capa_base2016['DISTRITO_L'].apply(pd.to_numeric, errors='coerce')
capa_base2018['DISTRITO_L'] = capa_base2018['DISTRITO_L'].apply(pd.to_numeric, errors='coerce')
capa_base2021['DISTRITO_L'] = capa_base2021['DISTRITO_L'].apply(pd.to_numeric, errors='coerce')

df_capa2013 = pd.merge(capa_base2013, df_E2013, on="DISTRITO_L")
df_capa2016 = pd.merge(capa_base2016, df_E2016, on="DISTRITO_L")
df_capa2018 = pd.merge(capa_base2018, df_E2018, on="DISTRITO_L")
df_capa2021 = pd.merge(capa_base2021, df_E2021, on="DISTRITO_L")


#-----------2013--------------------
df_PRI_2013 = df_capa2013.loc[(df_capa2013['PARTIDO'] =="PRI")]
df_PVEM_2013 = df_capa2013.loc[(df_capa2013['PARTIDO'] =="PVEM")]

#-----------2016--------------------
df_PAN_2016 = df_capa2016.loc[(df_capa2016['PARTIDO'] =="PAN")]
df_MORENA_2016 = df_capa2016.loc[(df_capa2016['PARTIDO'] =="MORENA")]
df_PRD_2016 = df_capa2016.loc[(df_capa2016['PARTIDO'] =="PRD")]

#-----------2018--------------------
df_PRI_2018 = df_capa2018.loc[(df_capa2018['PARTIDO'] =="PRI")]
df_MC_2018 = df_capa2018.loc[(df_capa2018['PARTIDO'] =="MC")]
df_PAN_2018 = df_capa2018.loc[(df_capa2018['PARTIDO'] =="PAN")]
df_MORENA_2018 = df_capa2018.loc[(df_capa2018['PARTIDO'] =="MORENA")]
df_PT_2018 = df_capa2018.loc[(df_capa2018['PARTIDO'] =="PT")]
df_PRD_2018 = df_capa2018.loc[(df_capa2018['PARTIDO'] =="PRD")]
df_PVEM_2018 = df_capa2018.loc[(df_capa2018['PARTIDO'] =="PVEM")]
df_PES_2018 = df_capa2018.loc[(df_capa2018['PARTIDO'] =="PES")]

#-----------2021--------------------
df_MC_2021 = df_capa2021.loc[(df_capa2021['PARTIDO'] =="MC")]
df_PAN_2021 = df_capa2021.loc[(df_capa2021['PARTIDO'] =="PAN")]
df_MORENA_2021 = df_capa2021.loc[(df_capa2021['PARTIDO'] =="MORENA")]
df_PT_2021 = df_capa2021.loc[(df_capa2021['PARTIDO'] =="PT")]
df_PRD_2021 = df_capa2021.loc[(df_capa2021['PARTIDO'] =="PRD")]
df_PVEM_2021 = df_capa2021.loc[(df_capa2021['PARTIDO'] =="PVEM")]
df_PES_2021 = df_capa2021.loc[(df_capa2021['PARTIDO'] =="PES")]

#ESTATALES
distrito_local = pd.merge(distrito_local,df_LOCAL, on="DISTRITO_L")

df_E2008 = pd.merge(df_E2008, df_LOCAL, on="DISTRITO_L")
df_E2010 = pd.merge(df_E2010, df_LOCAL, on="DISTRITO_L")
df_E2013 = pd.merge(df_E2013, df_LOCAL, on="DISTRITO_L")
df_E2016 = pd.merge(df_E2016, df_LOCAL, on="DISTRITO_L")
df_E2018 = pd.merge(df_E2018, df_LOCAL, on="DISTRITO_L")
df_E2021 = pd.merge(df_E2021, df_LOCAL, on="DISTRITO_L")

df_E2021PROPORCIONAL = pd.merge(df_E2021PROPORCIONAL, df_LOCAL, on="DISTRITO_L")

print(df_E2021PROPORCIONAL)

LogoCOESPO = ('images/COESPO_Logo_3.png')
#
m3 = folium.Map([19.5426, -96.91], zoom_start=7)#
from folium.plugins import MarkerCluster
mc_1 = MarkerCluster()
mc_2 = MarkerCluster()
mc_3 = MarkerCluster()
mc_4 = MarkerCluster()
mc_5 = MarkerCluster()
mc_6 = MarkerCluster()
mc_7 = MarkerCluster()
mc_8 = MarkerCluster()
mc_9 = MarkerCluster()
mc_10 = MarkerCluster()
mc_11 = MarkerCluster()
mc_12 = MarkerCluster()
mc_13 = MarkerCluster()
mc_14 = MarkerCluster()
mc_15 = MarkerCluster()
mc_16 = MarkerCluster()
mc_17 = MarkerCluster()
mc_18 = MarkerCluster()
mc_19 = MarkerCluster()
mc_20 = MarkerCluster()
mc_21 = MarkerCluster()
mc_22 = MarkerCluster()
mc_23 = MarkerCluster()
mc_24 = MarkerCluster()
mc_25 = MarkerCluster()
mc_26 = MarkerCluster()
mc_27 = MarkerCluster()
mc_28 = MarkerCluster()
mc_29 = MarkerCluster()
mc_30 = MarkerCluster()
mc_31 = MarkerCluster()
mc_32 = MarkerCluster()

mc_33 = MarkerCluster()

#Layer para Estatales
layer_1 = FeatureGroup(name='PRI 2013 [8]', show=False)
layer_2 = FeatureGroup(name='MC 2013 ', show=False)
layer_3 = FeatureGroup(name='PAN 2013 [2]', show=False)
layer_4 = FeatureGroup(name='MORENA 2013 ', show=False)
layer_5 = FeatureGroup(name='PT 2013 ', show=False)
layer_6 = FeatureGroup(name='PRD 2013 [1]', show=False)
layer_7 = FeatureGroup(name='PVEM 2013 [1]', show=False)
layer_8 = FeatureGroup(name='PES 2013 ', show=False)

layer_9 = FeatureGroup(name='PRI 2016 [2]', show=False)
layer_10 = FeatureGroup(name='MC 2016 ', show=False)
layer_11 = FeatureGroup(name='PAN 2016 [8]', show=False)
layer_12 = FeatureGroup(name='MORENA 2016 [7]', show=False)
layer_13 = FeatureGroup(name='PT 2016 ', show=False)
layer_14 = FeatureGroup(name='PRD 2016 [2]', show=False)
layer_15 = FeatureGroup(name='PVEM 2016 ', show=False)
layer_16 = FeatureGroup(name='PES 2016 ', show=False)

layer_17 = FeatureGroup(name='PRI 2018 [1]', show=False)
layer_18 = FeatureGroup(name='MC 2018 [1]', show=False)
layer_19 = FeatureGroup(name='PAN 2018 [6]', show=False)
layer_20 = FeatureGroup(name='MORENA 2018 [11]', show=False)
layer_21 = FeatureGroup(name='PT 2018 [2]', show=False)
layer_22 = FeatureGroup(name='PRD 2018 [2]', show=False)
layer_23 = FeatureGroup(name='PVEM 2018 [1]', show=False)
layer_24 = FeatureGroup(name='PES 2018 [1]', show=False)

layer_25 = FeatureGroup(name='PRI 2021 [2]', show=False)
layer_26 = FeatureGroup(name='MC 2021 [2]', show=False)
layer_27 = FeatureGroup(name='PAN 2021 [3]', show=False)
layer_28 = FeatureGroup(name='MORENA 2021 [13]', show=False)
layer_29 = FeatureGroup(name='PT 2021 [1]', show=False)
layer_30 = FeatureGroup(name='PRD 2021 [2]', show=False)
layer_31 = FeatureGroup(name='PVEM 2021 [2]', show=False)
layer_32 = FeatureGroup(name='PES 2021 ', show=False)

layer_pluris_2021 = FeatureGroup(name='Rep. Proporcional 2021', show=False)

colores_l = distrito_local["Color"]
def style_function(feature):
    color = colores_l.get(int(feature["id"][-3:]), None)
    # print(color)
    # color=color.to_json()
    return {
        "fillOpacity": 0.6,
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


Distritos = folium.GeoJson(
    distrito_local,
    name='Distritos',
    highlight_function=highlight,
    style_function=style_function,
).add_to(m3)

###Capa2013
#colores = distrito_local.set_index("DISTRITO_L")["Color"]
colores_2013 = df_capa2013["COLOR_MP"]

def style_function_2013(feature):
    color_2013 = colores_2013.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": color_2013,
        "color": color_2013,
        'line_opacity': 0.2,
    }

def highlight_2013(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.9,
        'line_opacity': 0.9
    }

mapa_2013 = folium.GeoJson(
    df_capa2013,
    name='[12] Distritos con Diputadas Locales 2013',
    highlight_function=highlight_2013,
    style_function=style_function_2013,
).add_to(m3)

###Capa2016
#colores = distrito_local.set_index("DISTRITO_L")["Color"]

colores_2016 = df_capa2016["COLOR_MP"]

def style_function_2016(feature):
    color_2016 = colores_2016.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": color_2016,
        "color": color_2016,
        'line_opacity': 0.2,
    }


def highlight_2016(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.9,
        'line_opacity': 0.9
    }

mapa_2016 = folium.GeoJson(
    df_capa2016,
    name='[19] Distritos con Diputadas Locales 2016',
    highlight_function=highlight_2016,
    style_function=style_function_2016,
).add_to(m3)

###Capa2018
#colores = distrito_local.set_index("DISTRITO_L")["Color"]
colores_2018 = df_capa2018["COLOR_MP"]

def style_function_2018(feature):
    color_2018 = colores_2018.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": color_2018,
        "color": color_2018,
        'line_opacity': 0.2,
    }


def highlight_2018(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.9,
        'line_opacity': 0.9
    }

mapa_2018 = folium.GeoJson(
    df_capa2018,
    name='[25] Distritos con Diputadas Locales 2018',
    highlight_function=highlight_2018,
    style_function=style_function_2018,
).add_to(m3)

###Capa2021
#colores = distrito_local.set_index("DISTRITO_L")["Color"]
colores_2021 = df_capa2021["COLOR_MP"]

def style_function_2021(feature):
    color_2021 = colores_2021.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": color_2021,
        "color": color_2021,
        'line_opacity': 0.2,
    }


def highlight_2021(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.9,
        'line_opacity': 0.9
    }


mapa_2021 = folium.GeoJson(
    df_capa2021,
    name='[25] Distritos con Diputadas Locales 2021',
    highlight_function=highlight_2021,
    style_function=style_function_2021,
).add_to(m3)



#-----------------------------------------------------------MAPAS 2013---------------------------------------------
colores_PRI_2013 = df_PRI_2013["COLOR_MP"]

def style_function_PRI_2013(feature):
    color_PRI_2013 = colores_PRI_2013.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": color_PRI_2013,
        "color": color_PRI_2013,
        'line_opacity': 0.2,
    }

def highlight_PRI_2013(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.9,
        'line_opacity': 0.9
    }

mapa_PRI_2013 = folium.GeoJson(
    df_PRI_2013,
    name='PRI 2013 [8]',
    show=False,
    highlight_function=highlight_PRI_2013,
    style_function=style_function_PRI_2013,
)


colores_PVEM_2013 = df_PVEM_2013["COLOR_MP"]

def style_function_PVEM_2013(feature):
    color_PVEM_2013 = colores_PVEM_2013.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": color_PVEM_2013,
        "color": color_PVEM_2013,
        'line_opacity': 0.2,
    }

def highlight_PVEM_2013(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.9,
        'line_opacity': 0.9
    }

mapa_PVEM_2013 = folium.GeoJson(
    df_PVEM_2013,
    name='PVEM 2013 [1]',
    show=False,
    highlight_function=highlight_PVEM_2013,
    style_function=style_function_PVEM_2013,
)


#-------------------------------MAPAS 2016----------------------------------

colores_MORENA_2016 = df_MORENA_2016["COLOR_MP"]

def style_function_MORENA_2016(feature):
    color_MORENA_2016 = colores_MORENA_2016.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": color_MORENA_2016,
        "color": color_MORENA_2016,
        'line_opacity': 0.2,
    }

def highlight_MORENA_2016(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.9,
        'line_opacity': 0.9
    }

mapa_MORENA_2016 = folium.GeoJson(
    df_MORENA_2016,
    name='MORENA 2016 [7]',
    show=False,
    highlight_function=highlight_MORENA_2016,
    style_function=style_function_MORENA_2016,
)

colores_PAN_2016 = df_PAN_2016["COLOR_MP"]

def style_function_PAN_2016(feature):
    color_PAN_2016 = colores_PAN_2016.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": color_PAN_2016,
        "color": color_PAN_2016,
        'line_opacity': 0.2,
    }

def highlight_PAN_2016(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.9,
        'line_opacity': 0.9
    }

mapa_PAN_2016 = folium.GeoJson(
    df_PAN_2016,
    name='PAN 2016 [8]',
    show = False,
    highlight_function=highlight_PAN_2016,
    style_function=style_function_PAN_2016,
)

colores_PRD_2016 = df_PRD_2016["COLOR_MP"]

def style_function_PRD_2016(feature):
    color_PRD_2016 = colores_PRD_2016.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": color_PRD_2016,
        "color": color_PRD_2016,
        'line_opacity': 0.2,
    }

def highlight_PRD_2016(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.9,
        'line_opacity': 0.9
    }

mapa_PRD_2016 = folium.GeoJson(
    df_PRD_2016,
    name='PRD 2016 [2]',
    show=False,
    highlight_function=highlight_PRD_2016,
    style_function=style_function_PRD_2016,
)

#-------------------------------MAPAS 2018----------------------------------
colores_MORENA_2018 = df_MORENA_2018["COLOR_MP"]

def style_function_MORENA_2018(feature):
    color_MORENA_2018 = colores_MORENA_2018.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": color_MORENA_2018,
        "color": color_MORENA_2018,
        'line_opacity': 0.2,
    }

def highlight_MORENA_2018(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.9,
        'line_opacity': 0.9
    }

mapa_MORENA_2018 = folium.GeoJson(
    df_MORENA_2018,
    name='MORENA 2018 [11]',
    show=False,
    highlight_function=highlight_MORENA_2018,
    style_function=style_function_MORENA_2018,
)


colores_PAN_2018 = df_PAN_2018["COLOR_MP"]

def style_function_PAN_2018(feature):
    color_PAN_2018 = colores_PAN_2018.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": color_PAN_2018,
        "color": color_PAN_2018,
        'line_opacity': 0.2,
    }

def highlight_PAN_2018(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.9,
        'line_opacity': 0.9
    }

mapa_PAN_2018 = folium.GeoJson(
    df_PAN_2018,
    name='PAN 2018 [6]',
    show=False,
    highlight_function=highlight_PAN_2018,
    style_function=style_function_PAN_2018,
)

colores_PRD_2018 = df_PRD_2018["COLOR_MP"]

def style_function_PRD_2018(feature):
    color_PRD_2018 = colores_PRD_2018.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": color_PRD_2018,
        "color": color_PRD_2018,
        'line_opacity': 0.2,
    }

def highlight_PRD_2018(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.9,
        'line_opacity': 0.9
    }

mapa_PRD_2018 = folium.GeoJson(
    df_PRD_2018,
    name='PRD 2018 [2]',
    show=False,
    highlight_function=highlight_PRD_2018,
    style_function=style_function_PRD_2018,
)

colores_MC_2018 = df_MC_2018["COLOR_MP"]

def style_function_MC_2018(feature):
    color_MC_2018 = colores_MC_2018.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": color_MC_2018,
        "color": color_MC_2018,
        'line_opacity': 0.2,
    }

def highlight_MC_2018(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.9,
        'line_opacity': 0.9
    }

mapa_MC_2018 = folium.GeoJson(
    df_MC_2018,
    name='MC 2018 [1]',
    show=False,
    highlight_function=highlight_MC_2018,
    style_function=style_function_MC_2018,
)

colores_PT_2018 = df_PT_2018["COLOR_MP"]

def style_function_PT_2018(feature):
    color_PT_2018 = colores_PT_2018.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": color_PT_2018,
        "color": color_PT_2018,
        'line_opacity': 0.2,
    }

def highlight_PT_2018(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.9,
        'line_opacity': 0.9
    }

mapa_PT_2018 = folium.GeoJson(
    df_PT_2018,
    name='PT 2018 [2]',
    show=False,
    highlight_function=highlight_PT_2018,
    style_function=style_function_PT_2018,
)

colores_PES_2018 = df_PES_2018["COLOR_MP"]

def style_function_PES_2018(feature):
    color_PES_2018 = colores_PES_2018.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": color_PES_2018,
        "color": color_PES_2018,
        'line_opacity': 0.2,
    }

def highlight_PES_2018(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.9,
        'line_opacity': 0.9
    }

mapa_PES_2018 = folium.GeoJson(
    df_PES_2018,
    name='PES 2018 [1]',
    show=False,
    highlight_function=highlight_PES_2018,
    style_function=style_function_PES_2018,
)
colores_PT_2021 = df_PT_2021["COLOR_MP"]

def style_function_PT_2021(feature):
    color_PT_2021 = colores_PT_2021.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": color_PT_2021,
        "color": color_PT_2021,
        'line_opacity': 0.2,
    }

def highlight_PT_2021(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.9,
        'line_opacity': 0.9
    }

mapa_PT_2021 = folium.GeoJson(
    df_PT_2021,
    name='PT 2021 [1]',
    show=False,
    highlight_function=highlight_PT_2021,
    style_function=style_function_PT_2021,
)

colores_MORENA_2021 = df_MORENA_2021["COLOR_MP"]

def style_function_MORENA_2021(feature):
    color_MORENA_2021 = colores_MORENA_2021.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": color_MORENA_2021,
        "color": color_MORENA_2021,
        'line_opacity': 0.2,
    }

def highlight_MORENA_2021(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.9,
        'line_opacity': 0.9
    }

mapa_MORENA_2021 = folium.GeoJson(
    df_MORENA_2021,
    name='MORENA 2021 [13]',
    show=False,
    highlight_function=highlight_MORENA_2021,
    style_function=style_function_MORENA_2021,
)



def acciones(df_in,anio):
    for row in df_in.itertuples():
        contenido = content_directorio(str(row.NOMBRE), str(row.PARTIDO), str(row.ANIO), str(row.ENTIDAD), str(row.FOTO),anio)
        popup = folium.Popup(html=contenido, max_width='800')

        icon_Dependencia = folium.features.CustomIcon('images/diputadas_marcador.png', icon_size=(70, 70),
                                                           icon_anchor=(22, 59),
                                                           popup_anchor=(3, -54))

        if row.PARTIDO == 'PRI' and row.ANIO == 2013:

            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_1)


        elif row.PARTIDO == 'MC' and row.ANIO == 2013:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_2)

        elif row.PARTIDO == 'PAN' and row.ANIO == 2013:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_3)

        elif row.PARTIDO == 'MORENA' and row.ANIO == 2013:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_4)

        elif row.PARTIDO == 'PT' and row.ANIO == 2013:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_5)

        elif row.PARTIDO == 'PRD' and row.ANIO == 2013:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_6)

        elif row.PARTIDO == 'PVEM' and row.ANIO == 2013:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_7)

        elif row.PARTIDO == 'PES' and row.ANIO == 2013:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_8)

###2016
        if row.PARTIDO == 'PRI' and row.ANIO == 2016:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_9)

        elif row.PARTIDO == 'MC' and row.ANIO == 2016:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_10)

        elif row.PARTIDO == 'PAN' and row.ANIO == 2016:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_11)

        elif row.PARTIDO == 'MORENA' and row.ANIO == 2016:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_12)

        elif row.PARTIDO == 'PT' and row.ANIO == 2016:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_13)

        elif row.PARTIDO == 'PRD' and row.ANIO == 2016:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_14)

        elif row.PARTIDO == 'PVEM' and row.ANIO == 2016:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_15)

        elif row.PARTIDO == 'PES' and row.ANIO == 2016:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_16)

###2018
        if row.PARTIDO == 'PRI' and row.ANIO == 2018:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_17)

        elif row.PARTIDO == 'MC' and row.ANIO == 2018:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_18)

        elif row.PARTIDO == 'PAN' and row.ANIO == 2018:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_19)

        elif row.PARTIDO == 'MORENA' and row.ANIO == 2018:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_20)

        elif row.PARTIDO == 'PT' and row.ANIO == 2018:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_21)

        elif row.PARTIDO == 'PRD' and row.ANIO == 2018:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_22)

        elif row.PARTIDO == 'PVEM' and row.ANIO == 2018:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_23)

        elif row.PARTIDO == 'PES' and row.ANIO == 2018:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_24)

###2021
        if row.PARTIDO == 'PRI' and row.ANIO == 2021:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_25)

        elif row.PARTIDO == 'MC' and row.ANIO == 2021:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_26)

        elif row.PARTIDO == 'PAN' and row.ANIO == 2021:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_27)

        elif row.PARTIDO == 'MORENA' and row.ANIO == 2021:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_28)

        elif row.PARTIDO == 'PT' and row.ANIO == 2021:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_29)

        elif row.PARTIDO == 'PRD' and row.ANIO == 2021:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_30)

        elif row.PARTIDO == 'PVEM' and row.ANIO == 2021:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_31)

        elif row.PARTIDO == 'PES' and row.ANIO == 2021:
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_32)
#Estatales
#acciones(df_E2008,'2008')
#acciones(df_E2010,'2010')
acciones(df_E2013,'2013')
acciones(df_E2016,'2016')
acciones(df_E2018,'2018')
acciones(df_E2021,'2021')


def genera_proporcional(df_in):
    for row in df_in.itertuples():
        contenido = content_proporcional(str(row.NOMBRE), str(row.PARTIDO), str(row.ENTIDAD),str(row.NOMBRE1), str(row.PARTIDO1), str(row.ENTIDAD1),
                                         str(row.NOMBRE2), str(row.PARTIDO2), str(row.ENTIDAD2),str(row.NOMBRE3), str(row.PARTIDO3), str(row.ENTIDAD3),
                                         str(row.NOMBRE4), str(row.PARTIDO4), str(row.ENTIDAD4),str(row.NOMBRE5), str(row.PARTIDO5), str(row.ENTIDAD5),
                                         str(row.NOMBRE6), str(row.PARTIDO6), str(row.ENTIDAD6),str(row.NOMBRE7), str(row.PARTIDO7), str(row.ENTIDAD7),
                                         str(row.NOMBRE8), str(row.PARTIDO8), str(row.ENTIDAD8),str(row.NOMBRE9), str(row.PARTIDO9), str(row.ENTIDAD9),
                                         str(row.NOMBRE10), str(row.PARTIDO10), str(row.ENTIDAD10),str(row.NOMBRE11), str(row.PARTIDO11), str(row.ENTIDAD11),
                                         str(row.NOMBRE12), str(row.PARTIDO12), str(row.ENTIDAD12))

        popup = folium.Popup(html=contenido, max_width='800')

        icon_Dependencia = folium.features.CustomIcon('images/diputadas_marcador.png', icon_size=(70, 70),
                                                           icon_anchor=(22, 59),
                                                           popup_anchor=(3, -54))

        if row.ENTIDAD == 'Rep. Proporcional':

            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_33)

genera_proporcional(df_E2021PROPORCIONAL)

tabladiputadas = ('images/Diputadas1.png')
#tabladiputadas2 = ('images/diputadas_tabla.png')
from folium.plugins import FloatImage

FloatImage(tabladiputadas, bottom=1, left=-2).add_to(m3)
#FloatImage(tabladiputadas2, bottom=5, left=-1).add_to(m3)


mc_1.add_to(mapa_PRI_2013)
mc_2.add_to(layer_2)
mc_3.add_to(layer_3)
mc_4.add_to(layer_4)
mc_5.add_to(layer_5)
mc_6.add_to(layer_6)
mc_7.add_to(mapa_PVEM_2013)
mc_8.add_to(layer_8)

mc_9.add_to(layer_9)
mc_10.add_to(layer_10)
mc_11.add_to(mapa_PAN_2016)
mc_12.add_to(mapa_MORENA_2016)
mc_13.add_to(layer_13)
mc_14.add_to(mapa_PRD_2016)
mc_15.add_to(layer_15)
mc_16.add_to(layer_16)



mc_17.add_to(layer_17)
mc_18.add_to(mapa_MC_2018)
mc_19.add_to(mapa_PAN_2018)
mc_20.add_to(mapa_MORENA_2018)
mc_21.add_to(mapa_PT_2018)
mc_22.add_to(mapa_PRD_2018)
mc_23.add_to(layer_23)
mc_24.add_to(mapa_PES_2018)

mc_25.add_to(layer_25)
mc_26.add_to(layer_26)
mc_27.add_to(layer_27)
mc_28.add_to(mapa_MORENA_2021)
mc_29.add_to(mapa_PT_2021)
mc_30.add_to(layer_30)
mc_31.add_to(layer_31)
mc_32.add_to(layer_32)

mc_33.add_to(layer_pluris_2021)


mapa_PRI_2013.add_to(m3)
#layer_2.add_to(m3)
layer_3.add_to(m3)
#layer_4.add_to(m3)
#layer_5.add_to(m3)
layer_6.add_to(m3)
mapa_PVEM_2013.add_to(m3)
#layer_8.add_to(m3)

layer_9.add_to(m3)
#layer_10.add_to(m3)
mapa_PAN_2016.add_to(m3)
mapa_MORENA_2016.add_to(m3)
#layer_13.add_to(m3)
mapa_PRD_2016.add_to(m3)
#layer_15.add_to(m3)
#layer_16.add_to(m3)

layer_17.add_to(m3)
mapa_MC_2018.add_to(m3)
mapa_PAN_2018.add_to(m3)
mapa_MORENA_2018.add_to(m3)
mapa_PT_2018.add_to(m3)
mapa_PRD_2018.add_to(m3)
layer_23.add_to(m3)
mapa_PES_2018.add_to(m3)

layer_25.add_to(m3)
layer_26.add_to(m3)
layer_27.add_to(m3)
mapa_MORENA_2021.add_to(m3)
mapa_PT_2021.add_to(m3)
layer_30.add_to(m3)
layer_31.add_to(m3)
#layer_32.add_to(m3)

layer_pluris_2021.add_to(m3)

# ---- Botón de Búsqueda de Municipio
statesearch = Search(
    layer=Distritos,
    geom_type='Polygon',
    placeholder='Búsqueda de distrito',
    collapsed=False,
    search_label='nom_dis',
    search_zoom=10,
    weight=3
).add_to(m3)


m3.add_child(folium.LayerControl(collapsed=False))
m3.save('Mapa_Diputadas.html')
