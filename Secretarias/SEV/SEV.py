# %%

from pathlib import Path

import branca
import folium
import geopandas as gpd
import pandas as pd
from folium import FeatureGroup
from folium.plugins import Search

from Funciones import *

# from Funciones import *

# %%
path_ini = Path("C:/ESyP/Mapas_COESPO/Resources/")
path_ini = Path("/Users/4x/COESPOAX/MapasTematicos/Resources")
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

LogoCOESPO = ('images/COESPO_Logo.png')

# %%  LECTURA DE DATAFRAMES
df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
df['CVEGEO'] = df.apply(lambda row: row.CVE_ENT + row.CVE_MUN, axis=1)
df['CVEGEO'] = df['CVEGEO'].apply(pd.to_numeric, errors='coerce')

# df['CVEGEO'] = df.apply['CVEGEO'].astype(pd.to_numeric())  # ESTABA COMO FLOAT

df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))
# df = pd.read_excel("Veracruz.xlsx", sheet_name='info')
# df_Localidades

df_delegaciones = pd.read_excel("SEV_OK.xlsx", sheet_name='Directorio_Delegaciones')
df_escuelas = pd.read_excel("SEV_OK.xlsx", sheet_name='Escuelas')
df_cobertura_del = pd.read_excel("SEV_OK.xlsx", sheet_name='Delegaciones_Cobertura')

# se agregan lat y long a los datos
df_delegaciones = pd.merge(df_delegaciones, df_Localidades, on="CVEGEO")
df_cobertura_del = pd.merge(df, df_cobertura_del, on="CVEGEO")

m = folium.Map(location=[19.8727, -96.1333], zoom_start=7, prefer_canvas=True, tiles='OpenStreetMap')

# ---- Mapa Base de Veracruz

colores = df_cobertura_del.set_index("CVE_MUN")["COLOR"]


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
    df_cobertura_del,
    name='Cobertura por Delegaciones SEV',
    highlight_function=highlight,
    style_function=style_function,
    control=True,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'DELEGACION'],
                                           aliases=['NOMBRE DEL MUNICIPIO:', 'DELEGACIÓN:']),
).add_to(m)

# ---- Imagen inferior izquierda logo COESPO
from folium.plugins import FloatImage

FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m)
# ---- Capas

LayerDelegaciones = FeatureGroup(name='Directorio Delegaciones Regionales', show=False)
LayerInicial = FeatureGroup(name='Escuelas Iniciales', show=False)
LayerPreescolar = FeatureGroup(name='Escuelas Preescolares', show=False)
LayerPrimarias = FeatureGroup(name='Escuelas Primarias', show=False)
LayerSecundarias = FeatureGroup(name='Escuelas Secundarias', show=False)
LayerBachillerato = FeatureGroup(name='Bachilleratos', show=False)
LayerProfesional = FeatureGroup(name='Profesionales', show=False)
LayerSuperior = FeatureGroup(name='Nivel Superior', show=False)

# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster

mc_delegaciones = MarkerCluster()
mc_inicial = MarkerCluster()
mc_preescolar = MarkerCluster()
mc_primarias = MarkerCluster()
mc_secundarias = MarkerCluster()
mc_bachilleratos = MarkerCluster()
mc_profesional = MarkerCluster()
mc_superior = MarkerCluster()

pd.set_option('display.max_columns', None)

for row in df_delegaciones.itertuples():
    icon_Dependencia = folium.features.CustomIcon('images/Marcador_SEV.png', icon_size=(60, 60),
                                                  icon_anchor=(22, 59),
                                                  popup_anchor=(3, -54))
    texto_mapa = content_delegaciones(str(row.Nombre_Del), str(row.Direccion), str(row.Telefono), str(row.Titular),
                                      str(row.Correo))

    popup = folium.Popup(html=texto_mapa, max_width='400')
    folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
        mc_delegaciones)


def genera_escuelas(niv, ruta, mc, df):
    for row in df.itertuples():
        if row.NIV == niv:
            texto_mapa = content_escuelas(str(row.NOMBRE_CT), str(row.DOMICILIO), str(row.NUM_EXT),
                                          str(row.TOTAL_ALUMNOS), str(row.TOTAL_PROFESORES), str(row.NIVEL),
                                          str(row.CCT))

            popup = folium.Popup(html=texto_mapa, max_width='400')
            icon_Dependencia = folium.features.CustomIcon(ruta, icon_size=(60, 60),
                                                          icon_anchor=(22, 59),
                                                          popup_anchor=(3, -54))
            folium.Marker(location=[row.LATITUD, row.LONGITUD], popup=popup, icon=icon_Dependencia).add_to(mc)

genera_escuelas(1, 'images/Iniciales.png', mc_inicial, df_escuelas)
genera_escuelas(3, 'images/Preescolares.png', mc_preescolar, df_escuelas)
genera_escuelas(4, 'images/Primarias.png', mc_primarias, df_escuelas)
genera_escuelas(6, 'images/Secundarias.png', mc_secundarias, df_escuelas)
genera_escuelas(7, 'images/Profesionales.png', mc_profesional, df_escuelas)
genera_escuelas(8, 'images/Bachilleratos.png', mc_bachilleratos, df_escuelas)
genera_escuelas(10, 'images/Superior.png', mc_superior, df_escuelas)

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
mc_delegaciones.add_to(LayerDelegaciones)
mc_inicial.add_to(LayerInicial)
mc_preescolar.add_to(LayerPreescolar)
mc_primarias.add_to(LayerPrimarias)
mc_secundarias.add_to(LayerSecundarias)
mc_profesional.add_to(LayerProfesional)
mc_bachilleratos.add_to(LayerBachillerato)
mc_superior.add_to(LayerSuperior)

LayerDelegaciones.add_to(m)
LayerInicial.add_to(m)
LayerPreescolar.add_to(m)
LayerPrimarias.add_to(m)
LayerSecundarias.add_to(m)
LayerBachillerato.add_to(m)
LayerProfesional.add_to(m)
LayerSuperior.add_to(m)

folium.LayerControl(collapsed=False).add_to(m)
m.save("SEV.html")

