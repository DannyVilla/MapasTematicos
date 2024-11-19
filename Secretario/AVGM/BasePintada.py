from pathlib import Path

import folium
import geopandas as gpd
import pandas as pd
from folium import FeatureGroup
from folium.plugins import Search

from Funciones import *

# %%


path_ini = Path("C:/ESyP/Mapas_COESPO/Resources/")
pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('max_columns', None)

df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))

df_regiones = df
# print(df_regiones.dtypes)
# df_regiones['CVE_MUN'] = df_regiones['CVE_MUN'].apply(pd.to_numeric, errors='coerce')
df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))
df_indicadores = pd.read_excel("matriz pruebas _macros.xlsx", sheet_name='mapa')
df_capa2 = pd.read_excel("matriz pruebas _macros.xlsx", sheet_name='mapa')

capa_base = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))

capa_base['CVE_MUN'] = capa_base['CVE_MUN'].apply(pd.to_numeric, errors='coerce')

df_capa2 = pd.merge(capa_base, df_capa2, on="CVE_MUN")

df_indicadores = pd.merge(df_indicadores, df_Localidades, on="CVEGEO")

# Se ajustan nombre de la región para desplegar
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

from folium.plugins import FloatImage

# df_regiones.loc[df_regiones['CVE_MUN'].isin(['', '', '', '', '', '', '', '', '', '', '']),['Color']]=="#C70039"

LogoCOESPO = ('COESPO_Logo_3.png')
print(df_regiones)

# ---Mapa
from folium.plugins import MarkerCluster

# print(df)
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

mc_1 = MarkerCluster()

layer_1 = FeatureGroup(name='Indicadores por Municipio', show=True)

colores = df_regiones.set_index("CVE_MUN")["Color"]
colores_avgm = df_capa2.set_index("id")["COLOR_MP"]





def style_function(feature):
    color = colores.get(int(feature["id"][-3:]), None)
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


mapa = folium.GeoJson(
    df_regiones,
    name='Regiones Veracruz',
    highlight_function=highlight,
    style_function=style_function,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Municipio:', 'Región:']),
).add_to(m3)



def style_function_avgm(feature):
    color_avgm = colores_avgm.get(int(feature["id"][-3:]), None)
    # print(color)
    # color=color.to_json()
    return {
        "fillOpacity": 0.9,
        "weight": 0,
        "fillColor": color_avgm,
        "color": color_avgm,
        'line_opacity': 0.2,
    }


def highlight_avgm(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }


print(df_capa2)
mapa_avgm = folium.GeoJson(
    df_capa2,
    name='Municipios en AVGM',
    highlight_function=highlight_avgm,
    style_function=style_function_avgm,
    tooltip=folium.features.GeoJsonTooltip(fields=['MUNICIPIO', 'REGION'], aliases=['Municipio:', 'Región:']),
).add_to(m3)

# ---Mapa del Estado de Veracruz
statesearch = Search(
    layer=mapa,
    geom_type='Polygon',
    placeholder='Búsqueda de municipio',
    collapsed=False,
    search_label='NOM_MUN',
    weight=5
).add_to(m3)

# print(df_indicadores.dtypes)
df_indicadores['TFF'] = df_indicadores.apply(lambda x: "{:,.2f}".format(x['TFF']), axis=1)
df_indicadores['TEF'] = df_indicadores.apply(lambda x: "{:,.2f}".format(x['TEF']), axis=1)
df_indicadores['PEMB_A'] = df_indicadores.apply(lambda x: "{:,.2f}".format(x['PEMB_A']), axis=1)
df_indicadores['PREZ_EDU'] = df_indicadores.apply(lambda x: "{:,.2f}".format(x['PREZ_EDU']), axis=1)
df_indicadores['POBREZA'] = df_indicadores.apply(lambda x: "{:,.2f}".format(x['POBREZA']), axis=1)
df_indicadores['POBREZAE'] = df_indicadores.apply(lambda x: "{:,.2f}".format(x['POBREZAE']), axis=1)
df_indicadores['GP_ESCOL'] = df_indicadores.apply(lambda x: "{:,.2f}".format(x['GP_ESCOL']), axis=1)
df_indicadores['PPOB_MIG'] = df_indicadores.apply(lambda x: "{:,.2f}".format(x['PPOB_MIG']), axis=1)
df_indicadores['PPOB_IND'] = df_indicadores.apply(lambda x: "{:,.2f}".format(x['PPOB_IND']), axis=1)
df_indicadores['PPOBLIE'] = df_indicadores.apply(lambda x: "{:,.2f}".format(x['PPOBLIE']), axis=1)
df_indicadores['PPOBLINE'] = df_indicadores.apply(lambda x: "{:,.2f}".format(x['PPOBLINE']), axis=1)

df_indicadores['TFF'] = df_indicadores['TFF'].astype(float, errors='raise')
df_indicadores['TEF'] = df_indicadores['TEF'].astype(float, errors='raise')
df_indicadores['PEMB_A'] = df_indicadores['PEMB_A'].astype(float, errors='raise')
df_indicadores['PREZ_EDU'] = df_indicadores['PREZ_EDU'].astype(float, errors='raise')
df_indicadores['POBREZA'] = df_indicadores['POBREZA'].astype(float, errors='raise')
df_indicadores['POBREZAE'] = df_indicadores['POBREZAE'].astype(float, errors='raise')
df_indicadores['GP_ESCOL'] = df_indicadores['GP_ESCOL'].astype(float, errors='raise')
df_indicadores['PPOB_MIG'] = df_indicadores['PPOB_MIG'].astype(float, errors='raise')
df_indicadores['PPOB_IND'] = df_indicadores['PPOB_IND'].astype(float, errors='raise')
df_indicadores['PPOBLIE'] = df_indicadores['PPOBLIE'].astype(float, errors='raise')
df_indicadores['PPOBLINE'] = df_indicadores['PPOBLINE'].astype(float, errors='raise')


# print(df_indicadores.dtypes)


def acciones(df_in):
    for row in df_in.itertuples():
        contenido = content_tarjeta(row)

        popup = folium.Popup(html=contenido, max_width='800')
        if str(row.AVGM_I) == "SI":
            icon_Dependencia = folium.features.CustomIcon('images/IVAIS_Marcador.png', icon_size=(60, 60),
                                                          icon_anchor=(22, 59),
                                                          popup_anchor=(3, -54))
        elif str(row.AVGM_I) == "NO":
            icon_Dependencia = folium.features.CustomIcon('images/SEGOB_Marcador.png', icon_size=(60, 60),
                                                          icon_anchor=(22, 59),
                                                          popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_1)


# print(df_indicadores.dtypes)
acciones(df_indicadores)

mc_1.add_to(layer_1)
layer_1.add_to(m3)

FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m3)
m3.add_child(folium.LayerControl())
m3.save('AVGM.html')
