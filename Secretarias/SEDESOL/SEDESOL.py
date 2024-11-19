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
df_concentrado = pd.read_excel("SEDESOL_OK.xlsx", sheet_name='CONCEN_OK')
df_programacion = pd.read_excel("SEDESOL_OK.xlsx", sheet_name='PROGRAMACION')
df_programacion_2t = pd.read_excel("SEDESOL_OK.xlsx", sheet_name='PROGRAMACION_2T')

df2020 = pd.merge(df_concentrado, df_Localidades, on="CVEGEO")
df_programacion = pd.merge(df_programacion, df_Localidades, on="CVEGEO")
df_programacion_2t = pd.merge(df_programacion_2t, df_Localidades, on="CVEGEO")

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

mapa = folium.GeoJson(
    df,
    name='Regiones',
    highlight_function=highlight,
    control=False,
    style_function=style_function,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Nombre Municipio:', 'Región:']),
).add_to(m)

# ---- Imagen inferior izquierda logo COESPO
from folium.plugins import FloatImage

FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m)
# ---- Capas
layer_1 = FeatureGroup(name='Acciones 2020', show=False)
layer_2 = FeatureGroup(name='Acciones 2022 (1°er Trimestre)', show=False)
layer_3 = FeatureGroup(name='Acciones 2022 (2°do Trimestre)', show=False)

# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster

mc_1 = MarkerCluster()
mc_2 = MarkerCluster()
mc_3 = MarkerCluster()

pd.set_option('display.max_columns', None)

df2020['B_MUJE'] = df2020.apply(lambda x: "{:,}".format(x['B_MUJE']), axis=1)
df2020['B_AUTO'] = df2020.apply(lambda x: "{:,}".format(x['B_AUTO']), axis=1)
df2020['B_PROG'] = df2020.apply(lambda x: "{:,}".format(x['B_PROG']), axis=1)
df2020['B_PISO'] = df2020.apply(lambda x: "{:,}".format(x['B_PISO']), axis=1)
df2020['B_TECH'] = df2020.apply(lambda x: "{:,}".format(x['B_TECH']), axis=1)
df2020['B_MURO'] = df2020.apply(lambda x: "{:,}".format(x['B_MURO']), axis=1)
df2020['B_CUAR'] = df2020.apply(lambda x: "{:,}".format(x['B_CUAR']), axis=1)
df2020['B_ESTU'] = df2020.apply(lambda x: "{:,}".format(x['B_ESTU']), axis=1)
df2020['B_ELEC'] = df2020.apply(lambda x: "{:,}".format(x['B_ELEC']), axis=1)

df_programacion['ME_Beneficiarios'] = df_programacion.apply(lambda x: "{:,}".format(x['ME_Beneficiarios']), axis=1)
df_programacion['MAA_Beneficiarios'] = df_programacion.apply(lambda x: "{:,}".format(x['MAA_Beneficiarios']), axis=1)
df_programacion['MAG_Beneficiarios'] = df_programacion.apply(lambda x: "{:,}".format(x['MAG_Beneficiarios']), axis=1)
df_programacion['MHI_Beneficiarios'] = df_programacion.apply(lambda x: "{:,}".format(x['MHI_Beneficiarios']), axis=1)
df_programacion['Pisos_Beneficiarios'] = df_programacion.apply(lambda x: "{:,}".format(x['Pisos_Beneficiarios']), axis=1)
df_programacion['Techos_Beneficiarios'] = df_programacion.apply(lambda x: "{:,}".format(x['Techos_Beneficiarios']), axis=1)
df_programacion['Cuartos_Beneficiarios'] = df_programacion.apply(lambda x: "{:,}".format(x['Cuartos_Beneficiarios']), axis=1)
df_programacion['Estufas_Beneficiarios'] = df_programacion.apply(lambda x: "{:,}".format(x['Estufas_Beneficiarios']), axis=1)
df_programacion['Sanitarios_Beneficiarios'] = df_programacion.apply(lambda x: "{:,}".format(x['Sanitarios_Beneficiarios']), axis=1)

df_programacion_2t['ME_Beneficiarios'] = df_programacion_2t.apply(lambda x: "{:,}".format(x['ME_Beneficiarios']), axis=1)
df_programacion_2t['MAA_Beneficiarios'] = df_programacion_2t.apply(lambda x: "{:,}".format(x['MAA_Beneficiarios']), axis=1)
df_programacion_2t['MAG_Beneficiarios'] = df_programacion_2t.apply(lambda x: "{:,}".format(x['MAG_Beneficiarios']), axis=1)
df_programacion_2t['MHI_Beneficiarios'] = df_programacion_2t.apply(lambda x: "{:,}".format(x['MHI_Beneficiarios']), axis=1)
df_programacion_2t['Pisos_Beneficiarios'] = df_programacion_2t.apply(lambda x: "{:,}".format(x['Pisos_Beneficiarios']), axis=1)
df_programacion_2t['Techos_Beneficiarios'] = df_programacion_2t.apply(lambda x: "{:,}".format(x['Techos_Beneficiarios']), axis=1)
df_programacion_2t['Cuartos_Beneficiarios'] = df_programacion_2t.apply(lambda x: "{:,}".format(x['Cuartos_Beneficiarios']), axis=1)
df_programacion_2t['Estufas_Beneficiarios'] = df_programacion_2t.apply(lambda x: "{:,}".format(x['Estufas_Beneficiarios']), axis=1)
df_programacion_2t['Sanitarios_Beneficiarios'] = df_programacion_2t.apply(lambda x: "{:,}".format(x['Sanitarios_Beneficiarios']), axis=1)

def genera(df_in):
    for row in df_in.itertuples():
        contenido = genera_tarjeta(str(row.DISTRITO), str(row.MUNICIPIO), str(row.U_SOC), str(row.DIAGNOSTICOS),
                                   str(row.JUEGOS), str(row.A_MUJE), str(row.B_MUJE), str(row.A_AUTO), str(row.B_AUTO),
                                   str(row.A_PROG), str(row.B_PROG), str(row.A_PISO), str(row.B_PISO), str(row.A_TECH),
                                   str(row.B_TECH), str(row.A_MURO), str(row.B_MURO), str(row.A_CUAR), str(row.B_CUAR),
                                   str(row.A_ESTU), str(row.B_ESTU), str(row.A_ELEC), str(row.B_ELEC))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/SEDESOL_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_1)
genera(df2020)

def genera_programa(df_in,mc):
    for row in df_in.itertuples():
        contenido = genera_tarjeta_programa(str(row.MUNICIPIO),
                                   str(row.ME_Acciones), str(row.ME_Beneficiarios), str(row.MAA_Acciones), str(row.MAA_Beneficiarios),
                                   str(row.MAG_Acciones), str(row.MAG_Beneficiarios), str(row.MHI_Acciones), str(row.MHI_Beneficiarios),
                                   str(row.Pisos), str(row.Pisos_Beneficiarios), str(row.Techos), str(row.Techos_Beneficiarios),
                                   str(row.Cuartos_Dormitorios), str(row.Cuartos_Beneficiarios),
                                   str(row.Estufas_ecológicas), str(row.Estufas_Beneficiarios), str(row.Sanitarios), str(row.Sanitarios_Beneficiarios))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/SEDESOL_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

genera_programa(df_programacion,mc_2)
genera_programa(df_programacion_2t,mc_3)

mc_1.add_to(layer_1)
mc_2.add_to(layer_2)
mc_3.add_to(layer_3)

layer_1.add_to(m)
layer_2.add_to(m)
layer_3.add_to(m)

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
folium.LayerControl(collapsed=False).add_to(m)
m.save("SEDESOL.html")

# %%
