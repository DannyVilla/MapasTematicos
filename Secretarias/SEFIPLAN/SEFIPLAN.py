# %%

from pathlib import Path

import branca
import folium
import geopandas as gpd
import pandas as pd
from folium import FeatureGroup
from folium.plugins import Search
from numpy import int64

from Funciones import *

# %%
#path_ini = Path("C:/ESyP/Mapas_COESPO/Resources/")
path_ini = Path("/Users/4x/PycharmProjects/MapasTematicos/Resources")

pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('display.max_columns', None)

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


# %%  IMAGEN FLOTANTE

LogoCOESPO = ('images/COESPO_Logo_3.png')

# %%  LECTURA DE DATAFRAMES
df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
df['CVEGEO'] = df['CVE_ENT'] + df['CVE_MUN']
# print(df)
# df['CVEGEO'] = df.apply(lambda row: row.CVE_ENT + row.CVE_MUN, axis=1)
df['CVEGEO'] = df['CVEGEO'].astype(int64)  # ESTABA COMO FLOAT

df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))

df_hacienda = pd.read_excel("SEFIPLAN_OK.xlsx", sheet_name='HACIENDA')
df_hacienda = pd.merge(df_hacienda, df_Localidades, on="CVEGEO")

df_caev = pd.read_excel("SEFIPLAN_OK.xlsx", sheet_name='CAEV')
df_caev = pd.merge(df_caev, df_Localidades, on="CVEGEO")

df_patrimonio = pd.read_excel("SEFIPLAN_OK.xlsx", sheet_name='PATRIMONIO')
df_patrimonio = pd.merge(df_patrimonio, df_Localidades, on="CVEGEO")

df_caev_2021 = pd.read_excel("ACCIONES_CAEV_2021.xlsx", sheet_name='CAEV2021')
caev_union= pd.merge(df_caev_2021, df_Localidades, on="CVEGEO")

caev_union['FECHA'] = caev_union['FECHA'].dt.strftime('%d/%m/%Y')

df.loc[df['region'] == 'Las_Montanas', 'region'] = 'Las Montañas'
df.loc[df['region'] == 'Huasteca_Alta', 'region'] = 'Huasteca Alta'
df.loc[df['region'] == 'Huasteca_Baja', 'region'] = 'Huasteca Baja'
df.loc[df['region'] == 'Los_Tuxtlas', 'region'] = 'Los Tuxtlas'
#pd.set_option('max_columns', None)

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


# ---Mapa de clasificacion 2020

mapa20 = folium.GeoJson(
    df,
    name='Consejos',
    highlight_function=highlight,
    control=False,
    style_function=style_function,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Nombre Municipio:', 'Región:']),
).add_to(m)

# ---- Imagen inferior izquierda logo COESPO
from folium.plugins import FloatImage

FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m)
# ---- Capas

# layer_0 = FeatureGroup(name='Acciones 2020', show=False)
layer_hacienda = FeatureGroup(name='Oficinas Hacienda', show=False)
layer_caev = FeatureGroup(name='Oficinas de CAEV', show=False)
layer_patrimonio = FeatureGroup(name='Oficinas de Patrimonio del Estado', show=False)
layer_caev_2021 = FeatureGroup(name='Acciones CAEV 2021', show=False)

# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster

mc_hacienda = MarkerCluster()
mc_caev = MarkerCluster()
mc_patrimonio = MarkerCluster()
mc_caev_2021 = MarkerCluster()

def genera_capa(df_in, mc):
    for row in df_in.itertuples():
        contenido = genera_tarjeta(str(row.MUNICIPIO), str(row.DIRECCION), str(row.TEL), str(row.FOTO))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/SEFIPLAN_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        folium.Marker(location=[row.LAT, row.LON], popup=popup, icon=icon_Dependencia).add_to(
            mc)

genera_capa(df_hacienda, mc_hacienda)
genera_capa(df_caev, mc_caev)
genera_capa(df_patrimonio, mc_patrimonio)

mc_hacienda.add_to(layer_hacienda)
mc_caev.add_to(layer_caev)
mc_patrimonio.add_to(layer_patrimonio)

mc_caev_2021.add_to(layer_caev_2021)

#Acciones 2021
def funcion(df_in):
    for row in df_in.itertuples():
        contenido = genera_acciones(str(row.MUNICIPIO), str(row.TITULO), str(row.FECHA),
                                    str(row.ENLACEPUB), str(row.ENLACEFOT1), str(row.ENLACEFOT2), str(row.URL))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/SEFIPLAN_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        if row.CVEGEO >= 3000 :
                folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_caev_2021)

funcion(caev_union)

layer_hacienda.add_to(m)
layer_caev.add_to(m)
layer_patrimonio.add_to(m)
layer_caev_2021.add_to(m)

# ---- Botón de Búsqueda de Municipio
statesearch = Search(
    layer=mapa20,
    geom_type='Polygon',
    placeholder='Búsqueda de municipio',
    collapsed=False,
    search_label='NOM_MUN',
    search_zoom=10,
    weight=3
).add_to(m)
folium.LayerControl(collapsed=False).add_to(m)
m.save("SEFIPLAN.html")
