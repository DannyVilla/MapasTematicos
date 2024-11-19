# %%

from pathlib import Path

import branca
import folium
import geopandas as gpd
import numpy as np
import pandas as pd
from folium import FeatureGroup
from folium.plugins import MarkerCluster
from folium.plugins import Search

from Funciones import *

# %%
path_ini = Path("C:/ESyP/Mapas_COESPO/Resources/")
#path_ini = Path("/Users/4x/COESPOAX/MapasTematicos/Resources")
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

LogoCOESPO = ('images/COESPO_Logo_3.png')

# %%  LECTURA DE DATAFRAMES
df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))

df_cejm = pd.read_excel("CEJM_OK.xlsx", sheet_name='PROGRAMAS')
df_ollas = pd.read_excel("CEJM_OK.xlsx", sheet_name='Ollas')



# se agregan lat y long a los datos
df_cejm = pd.merge(df_cejm, df_Localidades, on="CVEGEO")
df_ollas = pd.merge(df_ollas, df_Localidades, on="CVEGEO")

#df_cejm_4t2019 = df_cejm[df_cejm.CAPA.eq(1)]
#df_cejm_1t2020 = df_cejm[df_cejm.CAPA.eq(2)]
#df_cejm_2t2020 = df_cejm[df_cejm.CAPA.eq(3)]
#df_cejm_3t2020 = df_cejm[df_cejm.CAPA.eq(4)]
#df_cejm_4t2020 = df_cejm[df_cejm.CAPA.eq(5)]

#df_cejm_1t2021 = df_cejm[df_cejm.CAPA.eq(6)]
#df_cejm_2t2021 = df_cejm[df_cejm.CAPA.eq(7)]
#df_cejm_3t2021 = df_cejm[df_cejm.CAPA.eq(8)]
#df_cejm_4t2021 = df_cejm[df_cejm.CAPA.eq(9)]

#df_cejm_1t2022 = df_cejm[df_cejm.CAPA.eq(10)]
#df_cejm_2t2022 = df_cejm[df_cejm.CAPA.eq(11)]
#df_cejm_3t2022 = df_cejm[df_cejm.CAPA.eq(12)]

df_2019 = df_cejm[df_cejm.CAPA.eq(1)]
df_2020 = df_cejm[df_cejm.CAPA.eq(2)]
df_2021 = df_cejm[df_cejm.CAPA.eq(3)]
df_2022 = df_cejm[df_cejm.CAPA.eq(4)]
df_2023 = df_cejm[df_cejm.CAPA.eq(5)]
df_2024_1 = df_cejm[df_cejm.CAPA.eq(6)]
df_2024_2 = df_cejm[df_cejm.CAPA.eq(7)]
df_2024_3 = df_cejm[df_cejm.CAPA.eq(8)]


# Se modifican los textos
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
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Nombre Municipio:', 'Región:']),
).add_to(m)

# ---- Imagen inferior izquierda logo COESPO
from folium.plugins import FloatImage

FloatImage(LogoCOESPO, bottom=-2, left=1).add_to(m)
# ---- Capas

# layer_0 = FeatureGroup(name='Acciones 2020', show=False)
#layer_1 = FeatureGroup(name='4to Trimestre 2019', show=False)

#layer_2 = FeatureGroup(name='1er Trimestre 2020', show=False)
#layer_3 = FeatureGroup(name='2do Trimestre 2020', show=False)
#layer_4 = FeatureGroup(name='3er Trimestre 2020', show=False)
#layer_5 = FeatureGroup(name='4o. Trimestre 2020', show=False)

#layer_6 = FeatureGroup(name='1er. Trimestre 2021', show=False)
#layer_7 = FeatureGroup(name='2o. Trimestre 2021 ', show=False)
#layer_8 = FeatureGroup(name='3er. Trimestre 2021', show=False)
#layer_9 = FeatureGroup(name='4o. Trimestre 2021', show=False)

#layer_10 = FeatureGroup(name='1er. Trimestre 2022', show=False)
#layer_11 = FeatureGroup(name='2o. Trimestre 2022', show=False)
#layer_12 = FeatureGroup(name='3er. Trimestre 2022', show=False)

layer_2019 = FeatureGroup(name='Acciones 2019', show=False)
layer_2020 = FeatureGroup(name='Acciones 2020', show=False)
layer_2021 = FeatureGroup(name='Acciones 2021', show=False)
layer_2022 = FeatureGroup(name='Acciones 2022', show=False)
layer_2023 = FeatureGroup(name='Acciones 2023', show=False)
layer_2024_1 = FeatureGroup(name='Acciones 2024 (1er Trimestre)', show=False)
layer_2024_2 = FeatureGroup(name='Acciones 2024 (2do Trimestre)', show=False)
layer_2024_3 = FeatureGroup(name='Acciones 2024 (3er Trimestre)', show=False)
layer_evidencias = FeatureGroup(name='Evidencias', show=False)

# ---- Marcadores de las actividades
#mc_4t2019 = MarkerCluster()
#mc_1t2020 = MarkerCluster()
#mc_2t2020 = MarkerCluster()
#mc_3t2020 = MarkerCluster()
#mc_4t2020 = MarkerCluster()
#mc_1t2021 = MarkerCluster()
#mc_2t2021 = MarkerCluster()
#mc_3t2021 = MarkerCluster()
#mc_4t2021 = MarkerCluster()
#mc_1t2022 = MarkerCluster()
#mc_2t2022 = MarkerCluster()
#mc_3t2022 = MarkerCluster()

mc_2019 = MarkerCluster()
mc_2020 = MarkerCluster()
mc_2021 = MarkerCluster()
mc_2022 = MarkerCluster()
mc_2023 = MarkerCluster()

mc_2024_1 = MarkerCluster()
mc_2024_2 = MarkerCluster()
mc_2024_3 = MarkerCluster()

mc_Evidencias = MarkerCluster()

pd.set_option('display.max_columns', None)

def genera_capa(df_in, mc):
    for row in df_in.itertuples():
        contenido = tarjeta_dos(row)

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/CEJM_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)


def genera_evidencia_ollas(df_in, mc):
    for row in df_in.itertuples():
        contenido = tarjeta_dos(row)

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/CEJM_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

genera_capa(df_2019, mc_2019)
genera_capa(df_2020, mc_2020)
genera_capa(df_2021, mc_2021)
genera_capa(df_2022, mc_2022)
genera_capa(df_2023, mc_2023)

genera_capa(df_2024_1, mc_2024_1)
genera_capa(df_2024_2, mc_2024_2)
genera_capa(df_2024_3, mc_2024_3)

#genera_capa(df_cejm_4t2019, mc_4t2019)
#genera_capa(df_cejm_1t2020, mc_1t2020)
#genera_capa(df_cejm_2t2020, mc_2t2020)
#genera_capa(df_cejm_3t2020, mc_3t2020)
#genera_capa(df_cejm_4t2020, mc_4t2020)
#genera_capa(df_cejm_1t2021, mc_1t2021)
#genera_capa(df_cejm_2t2021, mc_2t2021)
#genera_capa(df_cejm_3t2021, mc_3t2021)
#genera_capa(df_cejm_4t2021, mc_4t2021)
#genera_capa(df_cejm_1t2022, mc_1t2022)
#genera_capa(df_cejm_2t2022, mc_2t2022)
#genera_capa(df_cejm_3t2022, mc_3t2022)

genera_evidencia_ollas(df_ollas, mc_Evidencias)

#mc_4t2019.add_to(layer_1)
#mc_1t2020.add_to(layer_2)
#mc_2t2020.add_to(layer_3)
#mc_3t2020.add_to(layer_4)
#mc_4t2020.add_to(layer_5)
#mc_1t2021.add_to(layer_6)
#mc_2t2021.add_to(layer_7)
#mc_3t2021.add_to(layer_8)
#mc_4t2021.add_to(layer_9)
#mc_1t2022.add_to(layer_10)
#mc_2t2022.add_to(layer_11)
#mc_3t2022.add_to(layer_12)

mc_2019.add_to(layer_2019)
mc_2020.add_to(layer_2020)
mc_2021.add_to(layer_2021)
mc_2022.add_to(layer_2022)
mc_2023.add_to(layer_2023)

mc_2024_1.add_to(layer_2024_1)
mc_2024_2.add_to(layer_2024_2)
mc_2024_3.add_to(layer_2024_3)
mc_Evidencias.add_to(layer_evidencias)

layer_2019.add_to(m)
layer_2020.add_to(m)
layer_2021.add_to(m)
layer_2022.add_to(m)
layer_2023.add_to(m)

layer_2024_1.add_to(m)
layer_2024_2.add_to(m)
layer_2024_3.add_to(m)
#layer_5.add_to(m)
#layer_6.add_to(m)
#layer_7.add_to(m)
#layer_8.add_to(m)
#layer_9.add_to(m)
#layer_10.add_to(m)
#layer_11.add_to(m)
#layer_12.add_to(m)
layer_evidencias.add_to(m)

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

m.save("CEJM.html")
