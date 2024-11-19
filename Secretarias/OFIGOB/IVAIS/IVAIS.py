# %%

import array as arr
from pathlib import Path

import branca
import folium
import geopandas as gpd
import numpy as np
import pandas as pd
from Funciones import *
from folium import FeatureGroup, LayerControl, Map, Marker
from folium.plugins import Search
from geopandas import GeoDataFrame
from numpy import int64

# %%
path_ini = Path("C:/ESyP/Mapas_COESPO/Resources/")
pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('display.max_columns', None)

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


# %%  IMAGEN FLOTANTE

LogoCOESPO = ('images/COESPO_Logo_3.png')

# %%  LECTURA DE DATAFRAMES
df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
df['CVEGEO'] = df['CVE_ENT'] + df['CVE_MUN']
df['CVEGEO'] = df['CVEGEO'].astype(int64)  # ESTABA COMO FLOAT

df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))

df_expoarte = pd.read_excel("IVAIS_OK.xlsx", sheet_name='EXPO_ARTE')
df_tabla_inpi = pd.read_excel("IVAIS_OK.xlsx", sheet_name='TABLA_INPI')
df_alfabetizacion = pd.read_excel("IVAIS_OK.xlsx", sheet_name='ALFABETIZACION')
df_soc_coop = pd.read_excel("IVAIS_OK.xlsx", sheet_name='SOC_COOP')
df_covid = pd.read_excel("IVAIS_OK.xlsx", sheet_name='COVID-19')

dfexpoarte = pd.merge(df_expoarte, df_Localidades, on="CVEGEO")
df_tablainpi = pd.merge(df, df_tabla_inpi, on='CVEGEO', how='left')
dfalfabetizacion = pd.merge(df_alfabetizacion, df_Localidades, on="CVEGEO")
dfsoccoop = pd.merge(df_soc_coop, df_Localidades, on="CVEGEO")
dfcovid = pd.merge(df_covid, df_Localidades, on="CVEGEO")

df.loc[df['region'] == 'Las_Montanas', 'region'] = 'Las Montañas'
df.loc[df['region'] == 'Huasteca_Alta', 'region'] = 'Huasteca Alta'
df.loc[df['region'] == 'Huasteca_Baja', 'region'] = 'Huasteca Baja'
df.loc[df['region'] == 'Los_Tuxtlas', 'region'] = 'Los Tuxtlas'

# Se definen colores para cada region
df_tablainpi['COLOR_20'] = '#F5DBB4'
df_tablainpi['COLOR_21'] = '#F5DBB4'

df_tablainpi.loc[df_tablainpi['TIPO20'] == 'INDIGENA', ['COLOR_20']] = '#A20500'
df_tablainpi.loc[df_tablainpi['TIPO21'] == 'INDIGENA', ['COLOR_21']] = '#A20500'
df_tablainpi.loc[df_tablainpi['TIPO20'] == 'PRESENCIA', ['COLOR_20']] = '#E34521'
df_tablainpi.loc[df_tablainpi['TIPO21'] == 'PRESENCIA', ['COLOR_21']] = '#E34521'
# print(df_tablainpi)
df_tablainpi['CLAS_2020'] = df_tablainpi['CLAS_2020'].fillna('Municipio con población indígena dispersa')
df_tablainpi['CLAS_2021'] = df_tablainpi['CLAS_2021'].fillna('Municipio con población indígena dispersa')
df_tablainpi['NOTA'] = df_tablainpi['NOTA'].fillna(
    '<b>Municipio con POBLACIÓN INDÍGENA DISPERSA.</b><br> Contar con menos del 40% de Población Indígena  y <br>más de 150 indígenas entre su población total.')
df_tablainpi['NOTA21'] = df_tablainpi['NOTA21'].fillna(
    '<b>Municipio con POBLACIÓN INDÍGENA DISPERSA.</b><br> Contar con menos del 40% de Población Indígena  y <br>más de 150 indígenas entre su población total.')
# print(df_tablainpi)


pd.set_option('max_columns', None)

m = folium.Map(location=[19.8727, -96.1333], zoom_start=7, prefer_canvas=True, tiles='OpenStreetMap')

# ---- Mapa Base de Veracruz

colores20 = df_tablainpi.set_index("CVE_MUN")["COLOR_20"]
colores21 = df_tablainpi.set_index("CVE_MUN")["COLOR_21"]

def colorscale(color):
    # print(color)
    return '"' + color + '"'


def style_function20(feature):
    color = colores20.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": color,
        "color": color,
        'line_opacity': 0.2,
    }


def style_function21(feature):
    color = colores21.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.8,
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

# ---Mapa de clasificacion 2020
# print(df_tablainpi)
mapa20 = folium.GeoJson(
    df_tablainpi,
    name='Clasificacion 2020',
    highlight_function=highlight,
    style_function=style_function20,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region', 'CLAS_2020', 'NOTA21'],
                                           aliases=['Nombre Municipio:', 'Región:', 'Clasificación 2020:', 'Nota:']),
).add_to(m)
mapa21 = folium.GeoJson(
    df_tablainpi,
    name='Clasificacion 2021',
    highlight_function=highlight,
    style_function=style_function21,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region', 'CLAS_2021', 'NOTA21'],
                                           aliases=['Nombre Municipio:', 'Región:', 'Clasificación 2021:', 'Nota:']),
).add_to(m)

# ---- Imagen inferior izquierda logo COESPO
from folium.plugins import FloatImage

FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m)

# layer_0 = FeatureGroup(name='Acciones 2020', show=False)
layer_1 = FeatureGroup(name='Expo Arte 2019', show=False)
layer_2 = FeatureGroup(name='Expo Arte 2020', show=False)
layer_6 = FeatureGroup(name='Expo Arte 2021', show=False)
layer_7 = FeatureGroup(name='Expo Arte 2022', show=False)
layer_3 = FeatureGroup(name='Alfabetización', show=False)
layer_4 = FeatureGroup(name='Sociedades Cooperativas', show=False)
layer_5 = FeatureGroup(name='Acciones COVID-19', show=False)

# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster

mc_1 = MarkerCluster()
mc_2 = MarkerCluster()
mc_6 = MarkerCluster()
mc_7 = MarkerCluster()
mc_tabla20 = MarkerCluster()
mc_tabla21 = MarkerCluster()
mc_3 = MarkerCluster()
mc_4 = MarkerCluster()
mc_5 = MarkerCluster()


def genera(df_in):
    for row in df_in.itertuples():
        contenido = genera_tarjeta(str(row.nom_mun), str(row.LUGAR), str(row.EVENTO), str(row.CAPA), str(row.FECHA),
                                   str(row.GRUPOS), str(row.FOTO1), str(row.FOTO2), str(row.FOTO3), str(row.FOTO4))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/IVAIS_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        if row.CAPA == 2019:

            if str(row.CVEGEO) == '90140001' or str(row.CVEGEO) == '90150001':

                folium.Marker(location=[row.LATESP, row.LONGESP], popup=popup, icon=icon_Dependencia).add_to(
                    mc_1)
            else:
                folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                    mc_1)

        if row.CAPA == 2020:
            if row.CVEGEO == 90140001 or row.CVEGEO == 90150001:
                folium.Marker(location=[row.LATESP, row.LONGESP], popup=popup, icon=icon_Dependencia).add_to(
                    mc_2)
            else:
                folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                    mc_2)

        if row.CAPA == 2021:
            if str(row.CVEGEO) == 90140001 or str(row.CVEGEO) == 90150001:

                folium.Marker(location=[row.LATESP, row.LONGESP], popup=popup, icon=icon_Dependencia).add_to(
                    mc_6)
            else:
                folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                    mc_6)

        if row.CAPA == 2022:
            if str(row.CVEGEO) == 90140001 or str(row.CVEGEO) == 90150001:

                folium.Marker(location=[row.LATESP, row.LONGESP], popup=popup, icon=icon_Dependencia).add_to(
                    mc_7)
            else:
                folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                    mc_7)



def alfabetizacion(df_in):
    for row in df_in.itertuples():
        contenido = genera_tabla_alfabetizacion(str(row.nom_mun), str(row.DESCRIPCION), str(row.A19), str(row.A20),
                                                str(row.A21), str(row.NOTA))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/IVAIS_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_3)


def sociedades(df_in):
    for row in df_in.itertuples():
        contenido = genera_sociedades(str(row.nom_mun), str(row.MUN_PART), str(row.ACCION), str(row.ACTIVIDAD),
                                      str(row.M_2020), str(row.H_2020), str(row.T_2020), str(row.M_2021),
                                      str(row.H_2021), str(row.T_2021))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/IVAIS_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_4)


def covid(df_in):
    for row in df_in.itertuples():
        contenido = genera_covid(str(row.nom_mun), str(row.REGION), str(row.LENGUA), str(row.DESCRIPCION),
                                 str(row.A_2020), str(row.C_2020), str(row.V_2020), str(row.A_2021), str(row.C_2021),
                                 str(row.V_2021))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/IVAIS_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_5)

genera(dfexpoarte)
alfabetizacion(dfalfabetizacion)
sociedades(dfsoccoop)
covid(dfcovid)

mc_1.add_to(layer_1)
mc_2.add_to(layer_2)
mc_6.add_to(layer_6)
mc_7.add_to(layer_7)
mc_3.add_to(layer_3)
mc_4.add_to(layer_4)
mc_5.add_to(layer_5)

layer_1.add_to(m)
layer_2.add_to(m)
layer_6.add_to(m)
layer_7.add_to(m)
layer_3.add_to(m)
layer_4.add_to(m)
layer_5.add_to(m)

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

m.save("IVAIS.html")
