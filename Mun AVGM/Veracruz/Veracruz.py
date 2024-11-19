from pathlib import Path

import folium
import geopandas as gpd
import pandas as pd
from folium import FeatureGroup
from folium.plugins import Search
from Funciones import *

from folium.plugins import MarkerCluster
from folium.plugins import FloatImage

path_ini = Path("C:/ESyP/Mapas_COESPO/Resources/")
pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('max_columns', None)

df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))

df_regiones = df
df_veracruz = df_regiones.loc[df_regiones["CVE_MUN"] == "193"]

df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))
df_acciones_2022 = pd.read_excel("AVGM_Veracruz_OK.xlsx", sheet_name='2022')
df_capa2 = pd.read_excel("matriz pruebas _macros.xlsx", sheet_name='mapa')

capa_base = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
capa_base['CVE_MUN'] = capa_base['CVE_MUN'].apply(pd.to_numeric, errors='coerce')
df_capa2 = pd.merge(capa_base, df_capa2, on="CVE_MUN")



# ---Mapa
m = folium.Map([19.182449441372917, -96.15503562025745], prefer_canvas=True, tiles='OpenStreetMap', zoom_start=12)
LogoCOESPO = ('COESPO_Logo_3.png')
FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m)


def style_function(feature):
    color = "#E2A9F3"
    return {
        "fillOpacity": 0.6,
        "weight": 0,
        "fillColor": color,
        "color": color,
        'line_opacity': 0.3,
    }


def highlight(feature):
    return {
        'weight': 5,
        'opacity': 0.3,
        'fillOpacity': 0.3,
        'line_opacity': 1
    }

mapa = folium.GeoJson(
    df_veracruz,
    name='Veracruz',
    highlight_function=highlight,
    style_function=style_function,
    #tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Municipio:', 'Región:']),
).add_to(m)

# ---MarkerClusters
mc_acciones_2022 = MarkerCluster()

layer_1 = FeatureGroup(name='Acciones 2022', show=True)
pd.set_option('display.max_columns', None)

def acciones(df_in):
    for row in df_in.itertuples():
        contenido = plantilla_municipios_avgm(row)

        popup = folium.Popup(html=contenido, max_width='290')

        icon_Dependencia = folium.features.CustomIcon('images/SEGOB_marcador.png', icon_size=(40, 40),
                                                        icon_anchor=(22, 59),
                                                        popup_anchor=(3, -54))

        folium.Marker(location=[row.LAT, row.LON], popup=popup, icon=icon_Dependencia).add_to(
            mc_acciones_2022)

acciones(df_acciones_2022)

mc_acciones_2022.add_to(layer_1)

layer_1.add_to(m)
m.add_child(folium.LayerControl(collapsed=False))
m.save('Veracruz_AVGM.html')
