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
from numpy import int64

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
img_tabla = ('images/tabla_sf.png')

# %%  LECTURA DE DATAFRAMES
df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
df['CVEGEO']=df['CVE_ENT']+df['CVE_MUN']
df['CVEGEO']=df['CVEGEO'].astype(int64)

df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))

df_cejm_1t = pd.read_excel("CEJM_OK.xlsx", sheet_name='1T2021')
df_ollas_2019 = pd.read_excel("ollas.xlsx", sheet_name='2019')
df_ollas_2020 = pd.read_excel("ollas.xlsx", sheet_name='2020')
df_ollas_2021 = pd.read_excel("ollas.xlsx", sheet_name='2021')
df_ollas_2022 = pd.read_excel("ollas.xlsx", sheet_name='2022')

cols=['BENEFICIADOS']
df_cejm_1t[cols] = df_cejm_1t[cols].applymap(np.int64)
df_cejm_1t['BENEFICIADOS'] = df_cejm_1t.apply(lambda x: "{:,}".format(x['BENEFICIADOS']), axis=1)

# se agregan lat y long a los datos
df_cejm = pd.merge(df_cejm_1t, df_Localidades, on="CVEGEO")
df_ollas_2019=pd.merge(df, df_ollas_2019, on="CVEGEO")

df_cejm_4t2019 = df_cejm[df_cejm.CAPA.eq(1)]
df_cejm_1t2020 = df_cejm[df_cejm.CAPA.eq(2)]
df_cejm_2t2020 = df_cejm[df_cejm.CAPA.eq(3)]
df_cejm_3t2020 = df_cejm[df_cejm.CAPA.eq(4)]
df_cejm_4t2020 = df_cejm[df_cejm.CAPA.eq(5)]

df_cejm_1t2021 = df_cejm[df_cejm.CAPA.eq(6)]
df_cejm_2t2021 = df_cejm[df_cejm.CAPA.eq(7)]
df_cejm_3t2021 = df_cejm[df_cejm.CAPA.eq(8)]
df_cejm_4t2021 = df_cejm[df_cejm.CAPA.eq(9)]


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




def style_function_PRD_2016(feature):
    return {
        "fillOpacity": 0.8,
        "weight": 0,
        "fillColor": "#9e005d",
        'line_opacity': 0.2,
    }

def highlight_PRD_2016(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.9,
        'line_opacity': 0.9
    }

mapa_ollas_2019 = folium.GeoJson(
    df_ollas_2019,
    name='OLLAS 2019',
    show=False,
    highlight_function=highlight_PRD_2016,
    style_function=style_function_PRD_2016,
)



# ---- Imagen inferior izquierda logo COESPO
from folium.plugins import FloatImage

FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m)
FloatImage(img_tabla, bottom=40, left=0).add_to(m)
# ---- Capas

# layer_0 = FeatureGroup(name='Acciones 2020', show=False)
# layer_1 = FeatureGroup(name='4o. Trimestre 2019', show=False)
# layer_2 = FeatureGroup(name='1er. Trimestre 2020', show=False)
# layer_3 = FeatureGroup(name='2o. Trimestre 2020', show=False)
# layer_4 = FeatureGroup(name='3er. Trimestre 2020', show=False)
# layer_5 = FeatureGroup(name='4o. Trimestre 2020', show=False)
# layer_6 = FeatureGroup(name='1er. Trimestre 2021', show=False)
# layer_7 = FeatureGroup(name='2o. Trimestre 2021 ', show=False)
# layer_8 = FeatureGroup(name='3er. Trimestre 2021', show=False)
# layer_9 = FeatureGroup(name='4o. Trimestre 2021', show=False)

layer_10 = FeatureGroup(name='Ollas construidas 2019', show=False)
layer_11 = FeatureGroup(name='Ollas construidas 2020', show=False)
layer_12 = FeatureGroup(name='Ollas construidas 2021', show=False)
layer_13 = FeatureGroup(name='Ollas construidas 2022', show=False)


# ---- Marcadores de las actividades
mc_4t2019 = MarkerCluster()
mc_1t2020 = MarkerCluster()
mc_2t2020 = MarkerCluster()
mc_3t2020 = MarkerCluster()
mc_4t2020 = MarkerCluster()
mc_1t2021 = MarkerCluster()
mc_2t2021 = MarkerCluster()
mc_3t2021 = MarkerCluster()
mc_4t2021 = MarkerCluster()


mc_2019 = MarkerCluster()
mc_2020 = MarkerCluster()
mc_2021 = MarkerCluster()
mc_2022 = MarkerCluster()




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


def genera_capa_ollas(df_in, mc):
    for row in df_in.itertuples():
        contenido = tarjeta_ollas(row)

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/CEJM_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        folium.Marker(location=[row.LAT, row.LON], popup=popup, icon=icon_Dependencia).add_to(
            mc)

# genera_capa(df_cejm_4t2019, mc_4t2019)
# genera_capa(df_cejm_1t2020, mc_1t2020)
# genera_capa(df_cejm_2t2020, mc_2t2020)
# genera_capa(df_cejm_3t2020, mc_3t2020)
# genera_capa(df_cejm_4t2020, mc_4t2020)
# genera_capa(df_cejm_1t2021, mc_1t2021)
# genera_capa(df_cejm_2t2021, mc_2t2021)
# genera_capa(df_cejm_3t2021, mc_3t2021)
# genera_capa(df_cejm_4t2021, mc_4t2021)
genera_capa_ollas(df_ollas_2019, mc_2019)
genera_capa_ollas(df_ollas_2020, mc_2020)
genera_capa_ollas(df_ollas_2021, mc_2021)
genera_capa_ollas(df_ollas_2022, mc_2022)



# mc_4t2019.add_to(layer_1)
# mc_1t2020.add_to(layer_2)
# mc_2t2020.add_to(layer_3)
# mc_3t2020.add_to(layer_4)
# mc_4t2020.add_to(layer_5)
# mc_1t2021.add_to(layer_6)
# mc_2t2021.add_to(layer_7)
# mc_3t2021.add_to(layer_8)
# mc_4t2021.add_to(layer_9)

mc_2019.add_to(layer_10)
mc_2020.add_to(layer_11)
mc_2021.add_to(layer_12)
mc_2022.add_to(layer_13)




# layer_1.add_to(m)
# layer_2.add_to(m)
# layer_3.add_to(m)
# layer_4.add_to(m)
# layer_5.add_to(m)
# layer_6.add_to(m)
# layer_7.add_to(m)
# layer_8.add_to(m)
# layer_9.add_to(m)


layer_10.add_to(mapa_ollas_2019)
layer_11.add_to(m)
layer_12.add_to(m)
layer_13.add_to(m)

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

m.save("Ollas.html")
