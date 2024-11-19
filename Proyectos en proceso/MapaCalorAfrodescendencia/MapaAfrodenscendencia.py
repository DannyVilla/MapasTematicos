from pathlib import Path

import folium

#Librería para mapa de calor##########################
from folium.plugins import HeatMap
import geopy

from urllib.request import urlopen
import plotly.express as px

import geopandas as gpd


import pandas as pd
from folium import FeatureGroup
from folium.plugins import Search

from Funciones import *

# %%
path_ini = Path("C:/ESyP/Mapas_COESPO/Resources/")
pd.options.display.float_format = '{:,.2f}'.format

df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
df['CVEGEO'] = df.apply(lambda row: row.CVE_ENT + row.CVE_MUN, axis=1)
df['CVEGEO'] = df['CVEGEO'].apply(pd.to_numeric, errors='coerce')
df_regiones = df


df_regiones.loc[df_regiones['region'] == 'Las_Montanas', 'region'] = 'Las Montañas'
df_regiones.loc[df_regiones['region'] == 'Huasteca_Alta', 'region'] = 'Huasteca Alta'
df_regiones.loc[df_regiones['region'] == 'Huasteca_Baja', 'region'] = 'Huasteca Baja'
df_regiones.loc[df_regiones['region'] == 'Los_Tuxtlas', 'region'] = 'Los Tuxtlas'
df_regiones['Color'] = 'grey'


# %%

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
df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))

df_afrodescendencia = pd.read_excel("AFRODESCENDENCIA_OK.xlsx", sheet_name='AFRO_CANTIDAD')

# Cambiar formato de columna
df_afrodescendencia['PORCENTAJE'] = df_afrodescendencia.apply(lambda x: "{:,}%".format(x['PORCENTAJE']), axis=1)
df_afrodescendencia['TOTAL'] = df_afrodescendencia.apply(lambda x: "{:,}".format(x['TOTAL']), axis=1)
df_afrodescendencia['AFRODENSCENDIENTES'] = df_afrodescendencia.apply(lambda x: "{:,}".format(x['AFRODENSCENDIENTES']), axis=1)

df_afrodescendencia = pd.merge(df, df_afrodescendencia, on="CVEGEO")



# %% CAMBIAR TIPO DE STR A NUMERO PARA LATITUD Y LONGITUD
m = folium.Map(location=[19.8727, -96.1333], zoom_start=7, prefer_canvas=True, tiles='OpenStreetMap')

# ---- Mapa Base de Veracruz
Veracruz = folium.GeoJson(
    df,
    name='Veracruz',
    control=False,
    style_function=lambda feature: {
        'fillColor': 'grey',
        'color': 'grey',
        'weight': 1,
        'fillOpacity': 0.0,
        'line_opacity': 0.0,
        'line_color': 'grey',
    }, tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Nombre Municipio:', 'Region:']),
).add_to(m)

## ---- Mapa # ---
colores = df_afrodescendencia.set_index("CVEMUN")["COLOR"]

def colorscale(color):
    return '"' + color + '"'

def style_function(feature):
    color = colores.get(int(feature["id"][-3:]), None)
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


#mapaAfrodescendencia = folium.GeoJson(
#    df_afrodescendencia,
#    name='AFRODESDENCENCIA GENERAL',
#    highlight_function=highlight,
#    style_function=style_function,
#    control=True,
#    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'REGION','TOTAL','AFRODENSCENDIENTES','PORCENTAJE'],
#                                           aliases=['Nombre Municipio:', 'Region:','Total de personas:','Personas Afrodescendientes:', 'Porcentaje:']),
#).add_to(m)

# ---- Imagen inferior izquierda logo COESPO
from folium.plugins import FloatImage

LogoCOESPO = ('images/COESPO_Logo_3.png')
FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m)

#def genera_tarjeta(df_in, mc):
#    for row in df_in.itertuples():
#        contenido = content_tarjeta(str(row.REGION), str(row.MUNICIPIO), str(row.PORCENTAJE), str(row.TOTAL), str(row.AFRODENSCENDIENTES), str(row.PORCENTAJE), str(row.COLOR))
#        icon_Dependencia = folium.features.CustomIcon('images/SSP_Marcador.png', icon_size=(60, 60),
#                                                      icon_anchor=(22, 59),
#                                                      popup_anchor=(3, -54))
#
#        popup = folium.Popup(html=contenido, max_width='800')
#        folium.Marker(location=[row.LAT, row.LON], popup=popup, icon=icon_Dependencia).add_to(
#            mc)


state_geo = df_regiones
state_data = pd.read_excel("AFRODESCENDENCIA_OK.xlsx", sheet_name='AFRO_CANTIDAD')

folium.features.Choropleth(
    geo_data=state_geo,
    name="Cantidad de Afrodescendencia",
    data=state_data,
    highlight_function=highlight,
    style_function=style_function,
    control=True,
    columns=["MUNICIPIO", "PORCENTAJE"],
    key_on="properties.NOM_MUN",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=1,
    legend_name="Afrodescendencia (%)",
).add_to(m)

Afrodescendencia = folium.GeoJson(
    df_afrodescendencia,
    name='Afrodescendencia',
    control=False,
    style_function=lambda feature: {
        'fillColor': 'grey',
        'color': 'grey',
        'weight': 1,
        'fillOpacity': 0.0,
        'line_opacity': 0.0,
        'line_color': 'grey',
    },  tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'REGION','TOTAL','AFRODENSCENDIENTES','PORCENTAJE'],
                                         aliases=['Nombre Municipio:', 'Region:','Total de personas:','Personas Afrodescendientes:', 'Porcentaje:']),
).add_to(m)


# ---- Botón de Búsqueda de Municipio
statesearch = Search(
    layer=Veracruz,
    geom_type='Polygon',
    placeholder='Búsqueda de municipio',
    collapsed=False,
    search_label='NOM_MUN',
    search_zoom=10,
    weight=3
).add_to(m)

folium.LayerControl(collapsed=False).add_to(m)
m.save("AfrodescendienteEstatal.html")
