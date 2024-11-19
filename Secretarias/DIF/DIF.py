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

LogoCOESPO = 'images/COESPO_Logo_3.png'

# %%  LECTURA DE DATAFRAMES
df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))
df_desayunos_frios = pd.read_excel("DIF_COMPLETO_2022.xlsx", sheet_name='DESAYUNOS_FRIOS')
df_desayunos_calientes = pd.read_excel("DIF_COMPLETO_2022.xlsx", sheet_name='DESAYUNOS_CALIENTES')
df_apoyos_funcionales = pd.read_excel("DIF_COMPLETO_2022.xlsx", sheet_name='APOYOS_FUNCIONALES')
df_poblacion_desamparo = pd.read_excel("DIF_COMPLETO_2022.xlsx", sheet_name='POBLACION_DESAMPARO')
df_proyectos_agroalimentarios = pd.read_excel("DIF_COMPLETO_2022.xlsx", sheet_name='PROYECTOS_AGROALIMENTARIOS')
df_proyectos_industriales = pd.read_excel("DIF_COMPLETO_2022.xlsx", sheet_name='PROYECTOS_INDUSTRIALES')
df_asistencia_social = pd.read_excel("DIF_COMPLETO_2022.xlsx", sheet_name='ASISTENCIA_SOCIAL')

df_desayunos_frios = pd.merge(df_desayunos_frios, df_Localidades, on='CVEGEO')
df_desayunos_calientes = pd.merge(df_desayunos_calientes, df_Localidades, on='CVEGEO')
df_apoyos_funcionales = pd.merge(df_apoyos_funcionales, df_Localidades, on='CVEGEO')
df_poblacion_desamparo = pd.merge(df_poblacion_desamparo, df_Localidades, on='CVEGEO')
df_proyectos_agroalimentarios = pd.merge(df_proyectos_agroalimentarios, df_Localidades, on='CVEGEO')
df_proyectos_industriales = pd.merge(df_proyectos_industriales, df_Localidades, on='CVEGEO')
df_asistencia_social = pd.merge(df_asistencia_social, df_Localidades, on='CVEGEO')

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

Layer_Desayunos_Frios = FeatureGroup(name='Desayunos Fríos a Escolares 2022-2023', show=False)
Layer_Desayunos_Calientes = FeatureGroup(name='Desayunos Escolares Calientes 2022-2023', show=False)
Layer_Apoyos_Funcionales = FeatureGroup(name='Programa de Apoyos Funcionales 2022-2023', show=False)
Layer_Poblacion_Desamparo = FeatureGroup(name='Programa de Atención a Población en Desamparo 2022-2023', show=False)
Layer_Productos_Agroalimentarios = FeatureGroup(name='Proyectos Productivos Agroalimentarios 2022', show=False)
Layer_Productos_Industriales = FeatureGroup(name='Proyectos Productivos Industriales 2022-2023', show=False)
Layer_Asistencia_Social = FeatureGroup(name='Programa de Asistencia Social Alimentaria a Personas de Atención Prioritaria 2022-2023', show=False)


# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster

mc_desayunos_frios = MarkerCluster()
mc_desayunos_calientes = MarkerCluster()
mc_apoyos_funcionales = MarkerCluster()
mc_poblacion_desamparo = MarkerCluster()
mc_proyectos_agroalimentarios = MarkerCluster()
mc_proyectos_industriales = MarkerCluster()
mc_asistencia_social = MarkerCluster()


pd.set_option('display.max_columns', None)


def genera(df_in, mc):
    # df['Value'] = df.apply(lambda x: "{:,}".format(x['Value']), axis=1)
    for row in df_in.itertuples():
        contenido = genera_tarjeta(str(row.MUNICIPIO), str(row.BENEFICIADOS), str(row.APOYOS), str(row.PROGRAMA),
                                   str(row.FOTO), str(row.VIDEO), str(row.ANIO))

        popup = folium.Popup(html=contenido, max_width='300')
        icon_Dependencia = folium.features.CustomIcon('images/DIF_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)


df_desayunos_frios['BENEFICIADOS'] = df_desayunos_frios.apply(lambda x: "{:,}".format(x['BENEFICIADOS']), axis=1)
df_desayunos_frios['APOYOS'] = df_desayunos_frios.apply(lambda x: "{:,}".format(x['APOYOS']), axis=1)

df_desayunos_calientes['BENEFICIADOS'] = df_desayunos_calientes.apply(lambda x: "{:,}".format(x['BENEFICIADOS']), axis=1)
df_desayunos_calientes['APOYOS'] = df_desayunos_calientes.apply(lambda x: "{:,}".format(x['APOYOS']), axis=1)


df_poblacion_desamparo['BENEFICIADOS'] = df_poblacion_desamparo.apply(lambda x: "{:,}".format(x['BENEFICIADOS']), axis=1)
df_poblacion_desamparo['APOYOS'] = df_poblacion_desamparo.apply(lambda x: "{:,}".format(x['APOYOS']), axis=1)

genera(df_desayunos_frios, mc_desayunos_frios)
genera(df_desayunos_calientes, mc_desayunos_calientes)
genera(df_apoyos_funcionales, mc_apoyos_funcionales)
genera(df_poblacion_desamparo, mc_poblacion_desamparo)
genera(df_proyectos_agroalimentarios, mc_proyectos_agroalimentarios)
genera(df_proyectos_industriales, mc_proyectos_industriales)
genera(df_asistencia_social, mc_asistencia_social)


mc_desayunos_frios.add_to(Layer_Desayunos_Frios)
mc_desayunos_calientes.add_to(Layer_Desayunos_Calientes)
mc_apoyos_funcionales.add_to(Layer_Apoyos_Funcionales)
mc_poblacion_desamparo.add_to(Layer_Poblacion_Desamparo)
mc_proyectos_agroalimentarios.add_to(Layer_Productos_Agroalimentarios)
mc_proyectos_industriales.add_to(Layer_Productos_Industriales)
mc_asistencia_social.add_to(Layer_Asistencia_Social)


Layer_Desayunos_Frios.add_to(m)
Layer_Desayunos_Calientes.add_to(m)
Layer_Apoyos_Funcionales.add_to(m)
Layer_Poblacion_Desamparo.add_to(m)
Layer_Productos_Agroalimentarios.add_to(m)
Layer_Productos_Industriales.add_to(m)
Layer_Asistencia_Social.add_to(m)


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
m.save("DIF.html")
