# %%

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
pd.set_option('display.max_columns', None)

df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
df['CVEGEO'] = df.apply(lambda row: row.CVE_ENT + row.CVE_MUN, axis=1)
df['CVEGEO'] = df['CVEGEO'].apply(pd.to_numeric, errors='coerce')
df_regiones = df

df_regiones.loc[df_regiones['region'] == 'Las_Montanas', 'region'] = 'Las Montañas'
df_regiones.loc[df_regiones['region'] == 'Huasteca_Alta', 'region'] = 'Huasteca Alta'
df_regiones.loc[df_regiones['region'] == 'Huasteca_Baja', 'region'] = 'Huasteca Baja'
df_regiones.loc[df_regiones['region'] == 'Los_Tuxtlas', 'region'] = 'Los Tuxtlas'
# df_regiones['Color'] = 'grey'
# df_regiones.loc[df_regiones['region'] == 'Capital', ['Color']] = '#e8694b'
# df_regiones.loc[df_regiones['region'] == 'Huasteca Alta', ['Color']] = '#7cd5a3'
# df_regiones.loc[df_regiones['region'] == 'Huasteca Baja', ['Color']] = '#96B921'
# df_regiones.loc[df_regiones['region'] == 'Los_Tuxtla', ['Color']] = '#5bbdbf'
# df_regiones.loc[df_regiones['region'] == 'Nautla', ['Color']] = '#FDAF3F'
# df_regiones.loc[df_regiones['region'] == 'Los Tuxtlas', ['Color']] = '#5bbdbf'
# df_regiones.loc[df_regiones['region'] == 'Olmeca', ['Color']] = '#d6ecf8'
# df_regiones.loc[df_regiones['region'] == 'Papaloapan', ['Color']] = '#846789'
# df_regiones.loc[df_regiones['region'] == 'Sotavento', ['Color']] = '#6e79c1'
# df_regiones.loc[df_regiones['region'] == 'Totonaca', ['Color']] = '#D0D108'
# df_regiones.loc[df_regiones['region'] == 'Las Montañas', ['Color']] = '#f3b8df'

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


# %%

LogoCOESPO = ('images/COESPO_Logo_3.png')

df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))

# %%

df_dgpr = pd.read_excel("Delegaciones DGPR 2022.xlsx", sheet_name='Delegaciones')
df_zonas = df_dgpr[["CVEGEO", "MUNICIPIO", "ZONA", "DELEGACION", "COLOR_DEL"]]
delegados = pd.read_excel("Delegaciones DGPR 2022.xlsx", sheet_name='Delegados')
representantes = pd.read_excel("Delegaciones DGPR 2022.xlsx", sheet_name='Representantes')
directorio_dgpr = pd.read_excel("Delegaciones DGPR 2022.xlsx", sheet_name='DGPR')

delegados = pd.merge(delegados, df_Localidades, on="CVEGEO")


df_cobertura_zonas = pd.merge(df_regiones, df_zonas, on="CVEGEO")
representantes.to_excel("df_monitor.xlsx")

# %% CAMBIAR TIPO DE STR A NUMERO PARA LATITUD Y LONGITUD
# df_dgt_oficinas['LAT'] = df_dgt_oficinas['LAT'].apply(pd.to_numeric, errors='coerce')
# df_dgt_oficinas['LON'] = df_dgt_oficinas['LON'].apply(pd.to_numeric, errors='coerce')
#
# # %%
#
# dfAccion3 = pd.read_csv("Accion3.csv")
# df_mapaAccion3 = pd.merge(dfAccion3, df_Localidades, on="CVEGEO")
# %%

m = folium.Map(location=[19.8727, -96.1333], zoom_start=7, prefer_canvas=True, tiles='OpenStreetMap')

# ---- Mapa Base de Veracruz

# Veracruz = folium.GeoJson(
#     df,
#     name='Veracruz',
#     control=False,
#     style_function=lambda feature: {
#         'fillColor': 'grey',
#         'color': 'grey',
#         'weight': 1,
#         'fillOpacity': 0.0,
#         'line_opacity': 0.0,
#         'line_color': 'grey',
#     }, tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Nombre Municipio:', 'Region:']),
# ).add_to(m)

## ---- Mapa # ---Cobertura delegaciones de tránsito
colores = df_cobertura_zonas.set_index("CVE_MUN")["COLOR_DEL"]


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


mapa = folium.GeoJson(
    df_cobertura_zonas,
    name='Cobertura de Zonas',
    highlight_function=highlight,
    style_function=style_function,
    control=True,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'ZONA'],
                                           aliases=['Nombre Municipio:', 'Zona:']),
).add_to(m)

## ---- Mapa # ---Cobertura CENTROS C4

# colores_c4 = df_cobertura_c4.set_index("CVE_MUN")["COLOR"]
#
#
# def colorscale(color):
#     return '"' + color + '"'
#
#
# def style_function_c4(feature):
#     color = colores_c4.get(int(feature["id"][-3:]), None)
#     # color = '#581845'
#     return {
#         "fillOpacity": 0.6,
#         "weight": 0,
#         "fillColor": color,
#         "color": color,
#         'line_opacity': 0.2,
#     }


# ---- Imagen inferior izquierda logo COESPO
from folium.plugins import FloatImage

LogoCOESPO = ('images/COESPO_Logo_3.png')
FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m)
# ---- Capas
Layer01 = FeatureGroup(name='Directorio Delegados', show=False)
Layer02 = FeatureGroup(name='Directorio  Representantes de Gobierno', show=False)
Layer03 = FeatureGroup(name='Directorio DGPR', show=False)

# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster

mc_01 = MarkerCluster()
mc_02 = MarkerCluster()
mc_03 = MarkerCluster()


def genera_tarjeta(df_in, mc):
    for reg in df_in.itertuples():
        contenido = content_tarjeta(str(reg.ZONA), str(reg.DELEGACION), str(reg.DELEGADO), str(reg.OFICINA),
                                    str(reg.CELULAR), str(reg.DIR), str(reg.MPIOS_ATEN),
                                    str(reg.FOTO))
        icon_Dependencia = folium.features.CustomIcon('images/DGPR_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        popup = folium.Popup(html=contenido, max_width='auto')
        if reg.LAT != 0 or reg.LON != 0:
            folium.Marker(location=[reg.LAT, reg.LON], popup=popup, icon=icon_Dependencia).add_to(
                mc)

        else:
            folium.Marker(location=[reg.lat_decimal, reg.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc)


def genera_representantes(df_in, mc):
    for reg in df_in.itertuples():
        contenido = content_representantes(str(reg.ZONA), str(reg.DELEGACION), str(reg.REPRESENTANTE), str(reg.OFICINA),
                                           str(reg.CELULAR), str(reg.DIR), str(reg.FOTO),str(reg.DELEGACIONES))
        icon_Dependencia = folium.features.CustomIcon('images/DGPR_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        popup = folium.Popup(html=contenido, max_width='290')
        if reg.LAT != 0 or reg.LON != 0:
            folium.Marker(location=[reg.LAT, reg.LON], popup=popup, icon=icon_Dependencia).add_to(
                mc)

        else:
            folium.Marker(location=[reg.lat_decimal, reg.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc)

def genera_directorio(df_in, mc):
    for reg in df_in.itertuples():
        contenido = content_directorio(str(reg.NOMBRE), str(reg.PUESTO),str(reg.TEL),
                                           str(reg.DIR), str(reg.FOTO))
        icon_Dependencia = folium.features.CustomIcon('images/DGPR_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        popup = folium.Popup(html=contenido, max_width='290')
        if reg.LAT != 0 or reg.LON != 0:
            folium.Marker(location=[reg.LAT, reg.LON], popup=popup, icon=icon_Dependencia).add_to(
                mc)

        else:
            folium.Marker(location=[reg.lat_decimal, reg.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc)


genera_tarjeta(delegados, mc_01)
genera_representantes(representantes, mc_02)
genera_directorio(directorio_dgpr, mc_03)

mc_01.add_to(Layer01)
mc_02.add_to(Layer02)
mc_03.add_to(Layer03)

# mapa_c4 = folium.GeoJson(
#     df_cobertura_c4,
#     name='Cobertura Centros C4',
#     highlight_function=highlight,
#     style_function=style_function_c4,
#     control=True,
#     tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'SUBCENTRO'],
#                                            aliases=['Nombre del Municipio:', 'Subcentro:']),
# ).add_to(m)


Layer01.add_to(m)
Layer02.add_to(m)
Layer03.add_to(m)

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

m.save("DGPR.html")

# %%
