# %%

from pathlib import Path

import branca
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


# %%

LogoCOESPO = ('images/COESPO_Logo_3.png')

# %%  LECTURA DE DATAFRAMES
df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
print(df)
df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))
df_2020 = pd.read_excel("DIF_COMPLETO.xlsx", sheet_name='2020')

df2020 = pd.merge(df_2020, df_Localidades, on="CVEGEO")

df.loc[df['region'] == 'Las_Montanas', 'region'] = 'Las Montañas'
df.loc[df['region'] == 'Huasteca_Alta', 'region'] = 'Huasteca Alta'
df.loc[df['region'] == 'Huasteca_Baja', 'region'] = 'Huasteca Baja'
df.loc[df['region'] == 'Los_Tuxtlas', 'region'] = 'Los Tuxtlas'

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


# ---Mapa del Estado de Veracruz
mapa = folium.GeoJson(
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

# layer_0 = FeatureGroup(name='Acciones 2020', show=False)
layer_1 = FeatureGroup(name='Asignación de Materiales Desarrollo', show=False)
layer_2 = FeatureGroup(name='Desayunos Frios a Escolares', show=False)
layer_3 = FeatureGroup(name='Desayunos Escolares Calientes', show=False)
layer_4 = FeatureGroup(name='Personas en Situación de Emergencia', show=False)
layer_5 = FeatureGroup(name='Personas en Situación Vulnerable', show=False)
layer_6 = FeatureGroup(name='Programa de Pensión Alimenticia Adultos Mayores de 70', show=False)
layer_7 = FeatureGroup(name='Programa de Apoyos Funcionales', show=False)
layer_8 = FeatureGroup(name='Programa de Atención a Población en Desamparo', show=False)
layer_9 = FeatureGroup(name='Proyectos Productivos Agroalimentarios', show=False)
layer_10 = FeatureGroup(name='Proyectos Productivos Industriales', show=False)

# ---- Marcadores de las actividades
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

pd.set_option('display.max_columns', None)


def genera(df_in):
    # df['Value'] = df.apply(lambda x: "{:,}".format(x['Value']), axis=1)
    for row in df_in.itertuples():
        contenido = genera_tarjeta(str(row.MUNICIPIO), str(row.BENEFICIADOS), str(row.APOYOS), str(row.PROGRAMA),
                                   str(row.FOTO), str(row.VIDEO))

        popup = folium.Popup(html=contenido, max_width='620')
        icon_Dependencia = folium.features.CustomIcon('images/SS_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        if row.CAPA == 'Capa1':
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_1)

        if row.CAPA == 'Capa2':
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_2)

        if row.CAPA == 'Capa3':
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_3)

        if row.CAPA == 'Capa4':
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_4)

        if row.CAPA == 'Capa5':
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_5)

        if row.CAPA == 'Capa6':
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_6)

        if row.CAPA == 'Capa7':
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_7)

        if row.CAPA == 'Capa8':
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_8)

        if row.CAPA == 'Capa9':
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_9)

        if row.CAPA == 'Capa10':
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_10)


genera(df2020)

mc_1.add_to(layer_1)
mc_2.add_to(layer_2)
mc_3.add_to(layer_3)
mc_4.add_to(layer_4)
mc_5.add_to(layer_5)
mc_6.add_to(layer_6)
mc_7.add_to(layer_7)
mc_8.add_to(layer_8)
mc_9.add_to(layer_9)
mc_10.add_to(layer_10)

layer_1.add_to(m)
layer_2.add_to(m)
layer_3.add_to(m)
layer_4.add_to(m)
layer_5.add_to(m)
layer_6.add_to(m)
layer_7.add_to(m)
layer_8.add_to(m)
layer_9.add_to(m)
layer_10.add_to(m)

#
# mc_Accion2.add_to(LayerAcciones2)

# ---- Botón de Búsqueda de Municipio
statesearch = Search(
    layer=mapa,
    geom_type='Polygon',
    placeholder='Búsqueda de municipio',
    collapsed=False,
    search_label='NOM_MUN',
    search_zoom=10,
    weight=3
).add_to(m)

# ---- Control de Capas
# LayerAVGM.add_to(m)
# LayerPVD.add_to(m)


folium.LayerControl(collapsed=False).add_to(m)

m.save("DIF.html")

# %%
