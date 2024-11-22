# %%

import folium
import pandas as pd
import geopandas as gpd
from geopandas import GeoDataFrame
from folium.plugins import Search
import branca
import numpy as np
from pathlib import Path
import array as arr
from Funciones import *
from folium import FeatureGroup, LayerControl, Map, Marker

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

df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))
df_capacita19 = pd.read_excel("CAPACITACION.xlsx", sheet_name='2019')
df_capacita20 = pd.read_excel("CAPACITACION.xlsx", sheet_name='2020')
df_capacita21 = pd.read_excel("CAPACITACION.xlsx", sheet_name='2021')
df_capacita22 = pd.read_excel("CAPACITACION.xlsx", sheet_name='2022')
df_capacita23 = pd.read_excel("CAPACITACION.xlsx", sheet_name='2023')
df_capacita24 = pd.read_excel("CAPACITACION.xlsx", sheet_name='2024')
df_fonden = pd.read_excel("FONDEN.xlsx", sheet_name='FONDEN')
df_brigadas = pd.read_excel("BRIGADAS.xlsx", sheet_name='BRIGADAS_MAPAS_COM')
df_equipo = pd.read_excel("EQUIPAMIENTO.xlsx", sheet_name='EQUIPO_DONADO')
df_refugios = pd.read_excel("REFUGIOS.xlsx", sheet_name='REFUGIOS_TEMPORALES')
df_refugios2 = pd.read_excel("REFUGIOS.xlsx", sheet_name='REFUGIOS_TEMPORALES_2')

df_refugios['CAPACIDAD'] = df_refugios['CAPACIDAD'].apply(pd.to_numeric, errors='coerce')

df_capacita19 = pd.merge(df_capacita19, df_Localidades, on="CVEGEO")
df_capacita20 = pd.merge(df_capacita20, df_Localidades, on="CVEGEO")
df_capacita21 = pd.merge(df_capacita21, df_Localidades, on="CVEGEO")
df_capacita22 = pd.merge(df_capacita22, df_Localidades, on="CVEGEO")
df_capacita23 = pd.merge(df_capacita23, df_Localidades, on="CVEGEO")
df_capacita24 = pd.merge(df_capacita24, df_Localidades, on="CVEGEO")
df_fonden = pd.merge(df_fonden, df_Localidades, on="CVEGEO")
df_equipo = pd.merge(df_equipo, df_Localidades, on="CVEGEO")

df_fonden['INSUMOS_ENTREGADOS'] = df_fonden.apply(lambda x: "{:,}".format(x['INSUMOS_ENTREGADOS']), axis=1)
df_fonden['DESPENSAS'] = df_fonden.apply(lambda x: "{:,}".format(x['DESPENSAS']), axis=1)
df_fonden['COBERTORES'] = df_fonden.apply(lambda x: "{:,}".format(x['COBERTORES']), axis=1)
df_fonden['COLCHONETAS'] = df_fonden.apply(lambda x: "{:,}".format(x['COLCHONETAS']), axis=1)
df_fonden['KIT_LIMPIEZA'] = df_fonden.apply(lambda x: "{:,}".format(x['KIT_LIMPIEZA']), axis=1)
df_fonden['KIT_ASEO'] = df_fonden.apply(lambda x: "{:,}".format(x['KIT_ASEO']), axis=1)
df_fonden['LAMINAS'] = df_fonden.apply(lambda x: "{:,}".format(x['LAMINAS']), axis=1)
df_fonden['LITRO_AGUA'] = df_fonden.apply(lambda x: "{:,}".format(x['LITRO_AGUA']), axis=1)
df_fonden['COSTALILLAS'] = df_fonden.apply(lambda x: "{:,}".format(x['COSTALILLAS']), axis=1)

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

# ---- Mapa Base de Veracruz
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
    name='Base',
    highlight_function=highlight,
    style_function=style_function,
    control=False,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Nombre Municipio:', 'Región:']),
).add_to(m)

# ---- Imagen inferior izquierda logo COESPO
from folium.plugins import FloatImage

FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m)
# ---- Capas

# layer_0 = FeatureGroup(name='Acciones 2020', show=False)
layer_cap19 = FeatureGroup(name='Capacitaciones 2019', show=False)
layer_cap20 = FeatureGroup(name='Capacitaciones 2020', show=False)
layer_cap21 = FeatureGroup(name='Capacitaciones 2021', show=False)
layer_cap22 = FeatureGroup(name='Capacitaciones 2022', show=False)
layer_cap23 = FeatureGroup(name='Capacitaciones 2023', show=False)
layer_cap24 = FeatureGroup(name='Capacitaciones 2024', show=False)
layer_fonden = FeatureGroup(name='Fonden 2020', show=False)
layer_equipo = FeatureGroup(name='Donación de equipamiento', show=False)
layer_brigadas = FeatureGroup(name='Brigadas y Mapas Comunitarios', show=False)
layer_refugios = FeatureGroup(name='Refugios Temporales', show=False)
layer_refugios2 = FeatureGroup(name='Refugios Temporales (Actualización 2024)', show=False)

# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster

mc_cap19 = MarkerCluster()
mc_cap20 = MarkerCluster()
mc_cap21 = MarkerCluster()
mc_cap22 = MarkerCluster()
mc_cap23 = MarkerCluster()
mc_cap24 = MarkerCluster()
mc_fonden = MarkerCluster()
mc_equipo = MarkerCluster()
mc_brigadas = MarkerCluster()
mc_refugios = MarkerCluster()
mc_refugios2 = MarkerCluster()

def genera(df_in,mc, anio):

    for row in df_in.itertuples():
        contenido = genera_tarjeta(str(row.MUNICIPIO), str(row.CURSOS_CAP), str(row.DESCRIPCION), anio)

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/PC_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

pd.set_option('display.max_columns', None)
def fonden(df_in, mc):
    for row in df_in.itertuples():
        contenido = genera_fonden(str(row.MUNICIPIO), '2020', str(row.INSUMOS_ENTREGADOS), str(row.DESPENSAS),
                                  str(row.COBERTORES), str(row.COLCHONETAS), str(row.KIT_LIMPIEZA), str(row.KIT_ASEO),
                                  str(row.LAMINAS), str(row.LITRO_AGUA), str(row.COSTALILLAS), str(row.FOTO),
                                  str(row.DECLARATORIAS),
                                  str(row.CONCEPTOS))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/PC_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)


def equipo(df_in, mc):
    for row in df_in.itertuples():
        contenido = genera_equipo(str(row.MUNICIPIO), str(row.ENTIDAD_RECEP), str(row.EQUIPO_DONADO),
                                  str(row.FOTO))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/PC_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)


def brigadas(df_in, mc):
    for row in df_in.itertuples():
        contenido = genera_brigadas(str(row.MUNICIPIO), str(row.LOCALIDAD), str(row.ANIO))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/PC_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)


def refugio(df_in, mc):
   for row in df_in.itertuples():

        contenido = genera_refugio(str(row.MUNICIPIO), str(row.NOMBRE), str(row.DIRECCION),
                                   str(row.CAPACIDADPERSONAS),str(row.CAPACIDADFAMILIAS), str(row.FOTO))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/PC_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                     popup_anchor=(3, -54))
        folium.Marker(location=[row.LAT, row.LON], popup=popup, icon=icon_Dependencia).add_to(
            mc)


genera(df_capacita19, mc_cap19,"2019")
genera(df_capacita20,  mc_cap20, "2020")
genera(df_capacita21,  mc_cap21,"2021")
genera(df_capacita22,  mc_cap22,"2022")
genera(df_capacita23,  mc_cap23,"2023")
genera(df_capacita24,  mc_cap24,"2024")
fonden(df_fonden, mc_fonden)
equipo(df_equipo, mc_equipo)
brigadas(df_brigadas, mc_brigadas)
#refugio(df_refugios, mc_refugios)
refugio(df_refugios2, mc_refugios2)

mc_cap19.add_to(layer_cap19)
mc_cap20.add_to(layer_cap20)
mc_cap21.add_to(layer_cap21)
mc_cap22.add_to(layer_cap22)
mc_cap23.add_to(layer_cap23)
mc_cap24.add_to(layer_cap24)
mc_fonden.add_to(layer_fonden)
mc_equipo.add_to(layer_equipo)
mc_brigadas.add_to(layer_brigadas)
mc_refugios.add_to(layer_refugios)
mc_refugios2.add_to(layer_refugios2)

layer_cap19.add_to(m)
layer_cap20.add_to(m)
layer_cap21.add_to(m)
layer_cap22.add_to(m)
layer_cap23.add_to(m)
layer_cap24.add_to(m)
layer_fonden.add_to(m)
layer_equipo.add_to(m)
layer_brigadas.add_to(m)
#layer_refugios.add_to(m)
layer_refugios2.add_to(m)

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

m.save("SPC.html")

# %%




