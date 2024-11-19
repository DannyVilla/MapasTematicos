from pathlib import Path

import branca
import folium
import geopandas as gpd
import pandas as pd
from folium import FeatureGroup
from folium.plugins import Search

from Funciones import *

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
        """)
LogoCOESPO = ('images/COESPO_Logo_3.png')

# %%  LECTURA DE DATAFRAMES
df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))

df_donaciones = pd.read_excel("EDITORA_OK.xlsx", sheet_name='DONACIONES')
df_donaciones_2022 = pd.read_excel("EDITORA_OK.xlsx", sheet_name='DONACIONES_2022')
df_donaciones_2023 = pd.read_excel("EDITORA_OK.xlsx", sheet_name='DONACIONES_2023')
df_actividades = pd.read_excel("EDITORA_OK.xlsx", sheet_name='ACTIVIDADES')
df_actividades_2022 = pd.read_excel("EDITORA_OK.xlsx", sheet_name='ACTIVIDADES_2022')
df_actividades_2023 = pd.read_excel("EDITORA_OK.xlsx", sheet_name='ACTIVIDADES_2023')
df_decretos = pd.read_excel("EDITORA_OK.xlsx", sheet_name='DECRETOS_COVID')
df_gaceta_of = pd.read_excel("EDITORA_OK.xlsx", sheet_name='GACETA_OFICIAL')
df_gaceta_of_2022 = pd.read_excel("EDITORA_OK.xlsx", sheet_name='GACETA_OFICIAL_2022')
df_gaceta_of_2023 = pd.read_excel("EDITORA_OK.xlsx", sheet_name='GACETA_OFICIAL_2023')
df_gaceta_po = pd.read_excel("EDITORA_OK.xlsx", sheet_name='GACETAPODERES')

df_donaciones = pd.merge(df_donaciones, df_Localidades, on="CVEGEO")
df_donaciones_2022 = pd.merge(df_donaciones_2022, df_Localidades, on="CVEGEO")
df_donaciones_2023 = pd.merge(df_donaciones_2023, df_Localidades, on="CVEGEO")
df_actividades = pd.merge(df_actividades, df_Localidades, on="CVEGEO")
df_actividades_2022 = pd.merge(df_actividades_2022, df_Localidades, on="CVEGEO")
df_actividades_2023 = pd.merge(df_actividades_2023, df_Localidades, on="CVEGEO")
df_decretos = pd.merge(df_decretos, df_Localidades, on="CVEGEO")
df_gaceta_of = pd.merge(df_gaceta_of, df_Localidades, on="CVEGEO")
df_gaceta_of_2022 = pd.merge(df_gaceta_of_2022, df_Localidades, on="CVEGEO")
df_gaceta_of_2023 = pd.merge(df_gaceta_of_2023, df_Localidades, on="CVEGEO")
df_gaceta_po = pd.merge(df_gaceta_po, df_Localidades, on="CVEGEO")

df.loc[df['region'] == 'Las_Montanas', 'region'] = 'Las Montañas'
df.loc[df['region'] == 'Huasteca_Alta', 'region'] = 'Huasteca Alta'
df.loc[df['region'] == 'Huasteca_Baja', 'region'] = 'Huasteca Baja'
df.loc[df['region'] == 'Los_Tuxtlas', 'region'] = 'Los Tuxtlas'

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
    control=False,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Nombre Municipio:', 'Región:']),
).add_to(m)

# ---- Imagen inferior izquierda logo COESPO
from folium.plugins import FloatImage

FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m)
# ---- Capas

# layer_0 = FeatureGroup(name='Acciones 2020', show=False)
layer_1 = FeatureGroup(name='Donaciones 2021', show=False)
layer_donaciones_2022 = FeatureGroup(name='Donaciones 2022', show=False)
layer_donaciones_2023 = FeatureGroup(name='Donaciones 2023', show=False)
layer_2 = FeatureGroup(name='Acciones 2021', show=False)
layer_acciones_2022 = FeatureGroup(name='Acciones 2022', show=False)
layer_acciones_2023 = FeatureGroup(name='Acciones 2023', show=False)
layer_3 = FeatureGroup(name='Decretos COVID-19', show=False)
layer_4 = FeatureGroup(name='Publicaciones Gaceta Oficial 2021', show=False)
layer_gaceta_2022 = FeatureGroup(name='Publicaciones Gaceta Oficial 2022', show=False)
layer_gaceta_2023 = FeatureGroup(name='Publicaciones Gaceta Oficial 2023', show=False)
layer_5 = FeatureGroup(name='Publicaciones Gaceta Poderes y Organismos Autónomos', show=False)

# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster

mc_1 = MarkerCluster()
mc_donaciones_2022 = MarkerCluster()
mc_donaciones_2023 = MarkerCluster()
mc_2 = MarkerCluster()
mc_acciones_2022 = MarkerCluster()
mc_acciones_2023 = MarkerCluster()
mc_3 = MarkerCluster()
mc_4 = MarkerCluster()
mc_gaceta_2022 = MarkerCluster()
mc_gaceta_2023 = MarkerCluster()
mc_5 = MarkerCluster()

pd.set_option('display.max_columns', None)

def genera(df_in, mc, funcion,  anio):
    for row in df_in.itertuples():
        latitud = 0
        longitud = 0
        if "donaciones" in funcion:
            contenido = tarjeta_donaciones(row, anio)
        elif "actividades" in funcion:
            contenido = tarjeta_actividades(row, anio)
        elif "decretos" in funcion:
            contenido = tarjeta_decretos(row, anio)
        elif "gaceta_of" in funcion:
            contenido = tarjeta_gaceta_oficial(row, anio)
        elif "gaceta_po" in funcion:
            contenido = tarjeta_gaceta_poderes(row, anio)

        if row.LAT != 0 and row.LON != 0:
            latitud = row.LAT
            longitud = row.LON
        else:
            latitud = row.lat_decimal
            longitud = row.lon_decimal

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/EDITORA_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[latitud, longitud], popup=popup, icon=icon_Dependencia).add_to(
            mc)

genera(df_donaciones, mc_1, "donaciones", "2021")
genera(df_donaciones_2022, mc_donaciones_2022, "donaciones", "2022")
genera(df_donaciones_2023, mc_donaciones_2023, "donaciones", "2023")
genera(df_actividades, mc_2, "actividades", "2021")
genera(df_actividades_2022, mc_acciones_2022, "actividades", "2022")
genera(df_actividades_2023, mc_acciones_2023, "actividades", "2023")
genera(df_decretos, mc_3, "decretos" , "2021")
genera(df_gaceta_of, mc_4, "gaceta_of", "2021")
genera(df_gaceta_of_2022, mc_gaceta_2022, "gaceta_of", "2022")
genera(df_gaceta_of_2023, mc_gaceta_2023, "gaceta_of", "2023")
genera(df_gaceta_po, mc_5, "gaceta_po", "2021")

mc_1.add_to(layer_1)
mc_donaciones_2022.add_to(layer_donaciones_2022)
mc_donaciones_2023.add_to(layer_donaciones_2023)
mc_2.add_to(layer_2)
mc_acciones_2022.add_to(layer_acciones_2022)
mc_acciones_2023.add_to(layer_acciones_2023)
mc_3.add_to(layer_3)
mc_4.add_to(layer_4)
mc_gaceta_2022.add_to(layer_gaceta_2022)
mc_gaceta_2023.add_to(layer_gaceta_2023)
mc_5.add_to(layer_5)

layer_1.add_to(m)
layer_donaciones_2022.add_to(m)
layer_donaciones_2023.add_to(m)
layer_2.add_to(m)
layer_acciones_2022.add_to(m)
layer_acciones_2023.add_to(m)
layer_3.add_to(m)
layer_4.add_to(m)
layer_gaceta_2022.add_to(m)
layer_gaceta_2023.add_to(m)
layer_5.add_to(m)

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
m.save("EDITORA.html")
