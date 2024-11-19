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
df.loc[df['region'] == 'Las_Montanas', 'region'] = 'Las Montañas'
df.loc[df['region'] == 'Huasteca_Alta', 'region'] = 'Huasteca Alta'
df.loc[df['region'] == 'Huasteca_Baja', 'region'] = 'Huasteca Baja'
df.loc[df['region'] == 'Los_Tuxtlas', 'region'] = 'Los Tuxtlas'

df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))
df_capacita = pd.read_excel("STPSP_OK.xlsx", sheet_name='CAPACITACION')
df_ferias = pd.read_excel("STPSP_OK.xlsx", sheet_name='FERIAS')
df_icatver = pd.read_excel("STPSP_OK.xlsx", sheet_name='ICATVER')
df_cclv = pd.read_excel("STPSP_OK.xlsx", sheet_name='CCLV')
df_trabajadores = pd.read_excel("STPSP_OK.xlsx", sheet_name='TRABAJADORES')
df_mov_int = pd.read_excel("STPSP_OK.xlsx", sheet_name='MOVILIDAD_INTERNA')
df_mov_laboral = pd.read_excel("STPSP_OK.xlsx", sheet_name='MOVILIDAD_LABORAL')


df_capacita = pd.merge(df_capacita, df_Localidades, on="CVEGEO")
df_ferias = pd.merge(df_ferias, df_Localidades, on="CVEGEO")
df_icatver = pd.merge(df_icatver, df_Localidades, on="CVEGEO")
df_cclv = pd.merge(df_cclv, df_Localidades, on="CVEGEO")
df_trabajadores = pd.merge(df_trabajadores, df_Localidades, on="CVEGEO")
df_mov_int = pd.merge(df_mov_int, df_Localidades, on="CVEGEO")
df_mov_laboral = pd.merge(df_mov_laboral, df_Localidades, on="CVEGEO")

df_capacita['BENEFICIADOS'] = df_capacita['BENEFICIADOS'].apply(pd.to_numeric, errors='coerce')
df_capacita['BENEFICIADOS'] = df_capacita.apply(lambda x: "{:,}".format(x['BENEFICIADOS']), axis=1)
df_ferias['BENEFICIADOS'] = df_ferias.apply(lambda x: "{:,}".format(x['BENEFICIADOS']), axis=1)

m = folium.Map(location=[19.8727, -96.1333], zoom_start=7, prefer_canvas=True, tiles='OpenStreetMap')

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

layer_capacitacion = FeatureGroup(name='Capacitaciones 2022 - 2024', show=False)
layer_ferias = FeatureGroup(name='Ferias de Empleo 2022 - 2024', show=False)
layer_icatver = FeatureGroup(name='ICATVER 2023 - 2024', show=False)
layer_cclv = FeatureGroup(name='Directorio CCLV 2024', show=False)
layer_trabajadores = FeatureGroup(name='Programa Trabajadores Agrícolas 2022 - 2024', show=False)
layer_mov_int = FeatureGroup(name='Movilidad Laboral Interna 2022 - 2024', show=False)
layer_mov_laboral  = FeatureGroup(name='Mecanismo de Movilidad Laboral 2022 - 2024', show=False)

# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster

mc_capacitacion = MarkerCluster()
mc_ferias = MarkerCluster()
mc_icatver = MarkerCluster()
mc_cclv = MarkerCluster()
mc_trabajadores = MarkerCluster()
mc_mov_int = MarkerCluster()
mc_mov_laboral = MarkerCluster()

pd.set_option('display.max_columns', None)

def trabajadores_movilidad(df_in, mc):
    for row in df_in.itertuples():
        contenido = genera_trabajadores_movilidad(str(row.MUNICIPIO), str(row.BENEFICIADOS), str(row.ACCION),
                                                   str(row.FOTO), str(row.AÑO))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/STPSP_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

def capacitacion(df_in, mc):
    for row in df_in.itertuples():
        contenido = genera_tarjeta(str(row.MUNICIPIO), str(row.BENEFICIADOS), str(row.TEMA),
                                   str(row.FOTO), str(row.AÑO))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/STPSP_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

def ferias(df_in, mc):
    for row in df_in.itertuples():
        contenido = genera_feria(str(row.MUNICIPIO), str(row.APOYO), str(row.BENEFICIADOS),
                                 str(row.FOTO), str(row.AÑO))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/STPSP_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

def icatver(df_in, mc):
    for row in df_in.itertuples():
        contenido = genera_icatver(str(row.MUNICIPIO), str(row.FECHA), str(row.ACCION),str(row.BENEFICIADOS),
                                   str(row.FOTO))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/STPSP_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

def cclv(df_in, mc):
    for row in df_in.itertuples():
        contenido = genera_cclv(str(row.DELEGACION), str(row.NOMBRE), str(row.DIRECCION),
                                   str(row.JURISDICCION), str(row.EMAIL), str(row.TEL),
                                   str(row.FOTO))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/STPSP_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

trabajadores_movilidad(df_trabajadores, mc_trabajadores)
trabajadores_movilidad(df_mov_int, mc_mov_int)
trabajadores_movilidad(df_mov_laboral, mc_mov_laboral)
capacitacion(df_capacita, mc_capacitacion)
ferias(df_ferias, mc_ferias)
icatver(df_icatver,mc_icatver)
cclv(df_cclv,mc_cclv)

mc_trabajadores.add_to(layer_trabajadores)
mc_mov_int.add_to(layer_mov_int)
mc_mov_laboral.add_to(layer_mov_laboral)
mc_capacitacion.add_to(layer_capacitacion)
mc_ferias.add_to(layer_ferias)
mc_icatver.add_to(layer_icatver)
mc_cclv.add_to(layer_cclv)

layer_trabajadores.add_to(m)
layer_mov_int.add_to(m)
layer_mov_laboral.add_to(m)
layer_capacitacion.add_to(m)
layer_ferias.add_to(m)
layer_icatver.add_to(m)
layer_cclv.add_to(m)

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
m.save("STPSP.html")
