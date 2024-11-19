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

from branca.element import MacroElement
from jinja2 import Template


class BindColormap(MacroElement):
    """Binds a colormap to a given layer.[url=https://flic.kr/p/2pHmhpU][img]https://live.staticflickr.com/65535/53632831994_493f112c89_k.jpg[/img][/url][url=https://flic.kr/p/2pHmhpU]SIOP-OP-PF-009/2024-DGCCYCE[/url] by [url=https://www.flickr.com/photos/194842989@N02/]Dirección General de Construcción de Caminos y Carreteras Estatales[/url], en Flickr

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

# %%  LECTURA DE DATAFRAMES
df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))

df_obras2019=pd.read_excel("SIOP_COMPLETO.xlsx", sheet_name='OBRAS2019')
df_obras2020=pd.read_excel("SIOP_COMPLETO.xlsx", sheet_name='OBRAS2020')
df_obras2021=pd.read_excel("SIOP_COMPLETO.xlsx", sheet_name='OBRAS2021')
df_obras2022=pd.read_excel("SIOP_COMPLETO.xlsx", sheet_name='OBRAS2022')
df_obras2023=pd.read_excel("SIOP_COMPLETO.xlsx", sheet_name='OBRAS2023')
df_obras2024=pd.read_excel("SIOP_COMPLETO.xlsx", sheet_name='OBRAS2024')

df_obras2019 = pd.merge(df_obras2019, df_Localidades, on="CVEGEO")
df_obras2020 = pd.merge(df_obras2020, df_Localidades, on="CVEGEO")
df_obras2021 = pd.merge(df_obras2021, df_Localidades, on="CVEGEO")
df_obras2022 = pd.merge(df_obras2022, df_Localidades, on="CVEGEO")
df_obras2023 = pd.merge(df_obras2023, df_Localidades, on="CVEGEO")
df_obras2024 = pd.merge(df_obras2024, df_Localidades, on="CVEGEO")


def format(x):


    return "{:,}".format(x)
df_obras2019['BENEFICIADOS'] = df_obras2019['BENEFICIADOS'].apply(format)
df_obras2020['BENEFICIADOS'] = df_obras2020['BENEFICIADOS'].apply(format)
df_obras2021['BENEFICIADOS'] = df_obras2021['BENEFICIADOS'].apply(format)
df_obras2022['BENEFICIADOS'] = df_obras2022['BENEFICIADOS'].apply(format)
df_obras2023['BENEFICIADOS'] = df_obras2023['BENEFICIADOS'].apply(format)
df_obras2024['BENEFICIADOS'] = df_obras2024['BENEFICIADOS'].apply(format)

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
layer_obras2019 = FeatureGroup(name='Obras del 2019', show=False)
layer_obras2020 = FeatureGroup(name='Obras del 2020', show=False)
layer_obras2021 = FeatureGroup(name='Obras del 2021', show=False)
layer_obras2022 = FeatureGroup(name='Obras del 2022', show=False)
layer_obras2023 = FeatureGroup(name='Obras del 2023', show=False)
layer_obras2024 = FeatureGroup(name='Obras del 2024 (1er y 2do Trimestre)', show=False)


# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster
mc_obras2019 = MarkerCluster()
mc_obras2020 = MarkerCluster()
mc_obras2021 = MarkerCluster()
mc_obras2022 = MarkerCluster()
mc_obras2023 = MarkerCluster()
mc_obras2024 = MarkerCluster()

def genera(df_in,mc,anio):
    for row in df_in.itertuples():
        contenido = genera_tarjeta(str(row.MUNICIPIO), str(row.PROGRAMA),str(row.BENEFICIADOS), str(row.CLASIFICACION), str(row.PRODUCTO),
                                   str(row.FOTO1), str(row.FOTO2),anio)

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/SIOP_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

genera(df_obras2019, mc_obras2019, "2019")
genera(df_obras2020, mc_obras2020, "2020")
genera(df_obras2021, mc_obras2021, "2021")
genera(df_obras2022, mc_obras2022, "2022")
genera(df_obras2023, mc_obras2023, "2023")
genera(df_obras2024, mc_obras2024, "2024")

pd.set_option('display.max_columns', None)

mc_obras2019.add_to(layer_obras2019)
mc_obras2020.add_to(layer_obras2020)
mc_obras2021.add_to(layer_obras2021)
mc_obras2022.add_to(layer_obras2022)
mc_obras2023.add_to(layer_obras2023)
mc_obras2024.add_to(layer_obras2024)

layer_obras2019.add_to(m)
layer_obras2020.add_to(m)
layer_obras2021.add_to(m)
layer_obras2022.add_to(m)
layer_obras2023.add_to(m)
layer_obras2024.add_to(m)

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
m.save("SIOP.html")
