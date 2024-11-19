import folium
import pandas as pd
import geopandas as gpd
from geopandas import GeoDataFrame
from folium.plugins import Search
import branca
import numpy as np
from pathlib import Path
import array as arr

from numpy import int64

from Funciones import *

from folium import FeatureGroup, LayerControl, Map, Marker

# %%
path_ini = Path("C:/ESyP/Mapas_COESPO/Resources/")
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
LogoCOESPO = ('images/COESPO_Logo_3.png')

# %%  LECTURA DE DATAFRAMES
df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
df['CVEGEO']=df['CVE_ENT']+df['CVE_MUN']
#print(df)
#df['CVEGEO'] = df.apply(lambda row: row.CVE_ENT + row.CVE_MUN, axis=1)
df['CVEGEO']=df['CVEGEO'].astype(int64)#ESTABA COMO FLOAT

df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))


df_concentrado2020 = pd.read_excel("SEDECOP_OK.xlsx", sheet_name='CONCENTRADO_VAL')
df_concentrado2021 = pd.read_excel("SEDECOP_OK.xlsx", sheet_name='CONCENTRADO_VAL2021')
df_concentrado2022 = pd.read_excel("SEDECOP_OK.xlsx", sheet_name='CONCENTRADO_VAL2022')

df_concentrado2020 = pd.merge(df_concentrado2020, df_Localidades, on="CVEGEO")
df_concentrado2021 = pd.merge(df_concentrado2021, df_Localidades, on ="CVEGEO")
df_concentrado2022 = pd.merge(df_concentrado2022, df_Localidades, on ="CVEGEO")

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
layer_1 = FeatureGroup(name='Acciones 2020', show=False)
layer_2 = FeatureGroup(name='Acciones 2021', show=False)
layer_3 = FeatureGroup(name='Acciones 2022', show=False)


# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster

mc_1 = MarkerCluster()
mc_2 = MarkerCluster()
mc_3 = MarkerCluster()

pd.set_option('display.max_columns', None)

def generay(df_in,mc, anio):
        for row in df_in.itertuples():
            if row.DATOS != "VACIO":
                contenido = genera_tarjeta2021(str(row.MUNICIPIO), str(row.PROG1),str(row.DESC1), str(row.BEN1), str(row.FOTO1),
                                                                 str(row.PROG2),str(row.DESC2), str(row.BEN2), str(row.FOTO2),
                                                                 str(row.PROG3),str(row.DESC3), str(row.BEN3), str(row.FOTO3),
                                                                 str(row.PROG4),str(row.DESC4), str(row.BEN4), str(row.FOTO4),
                                                                 str(row.PROG5),str(row.DESC5), str(row.BEN5), str(row.FOTO5),
                                                                 str(row.PROG6),str(row.DESC6), str(row.BEN6), str(row.FOTO6),
                                                                 str(row.PROG7),str(row.DESC7), str(row.BEN7), str(row.FOTO7),
                                                                 str(row.PROG8),str(row.DESC8), str(row.BEN8), str(row.FOTO8),
                                                                 str(row.PROG9),str(row.DESC9), str(row.BEN9), str(row.FOTO9),
                                                                 str(row.PROG10),str(row.DESC10), str(row.BEN10), str(row.FOTO10),
                                                                 str(row.PROG11),str(row.DESC11), str(row.BEN11), str(row.FOTO11),
                                                                 str(row.PROG12),str(row.DESC12), str(row.BEN12), str(row.FOTO12),
                                                                 str(row.PROG13),str(row.DESC13), str(row.BEN13), str(row.FOTO13), anio)
                popup = folium.Popup(html=contenido, max_width='290')
                icon_Dependencia = folium.features.CustomIcon('images/SEDECOP_marcador.png', icon_size=(60, 60),
                                                              icon_anchor=(22, 59),
                                                              popup_anchor=(3, -54))
                folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                    mc)

generay(df_concentrado2020, mc_1, "2020")
generay(df_concentrado2021,mc_2, "2021")


def genera_2022(df_in, mc, anio):
    for row in df_in.itertuples():
        if row.DATOS != "VACIO":
            contenido = genera_tarjeta2022(str(row.MUNICIPIO), str(row.CAP), str(row.HV), str(row.TIENDA_HV), str(row.COD_BAR), str(row.EST_DE_CONT),
                                           str(row.REG_DE_MARCA), str(row.LOGO_E_IMAGEN), str(row.VINC_COM), str(row.FOROS_Y_EXPOS), str(row.PAAV), str(row.ASIST_TEC_ART),
                                           str(row.ASIST_TEC_EMP), str(row.DIS_DE_EMB), str(row.TERMIN_DE_COBRO), str(row.ART_IMPULSO_A_LA_PROD), str(row.SUMAS), anio)

            popup = folium.Popup(html=contenido, max_width='290')
            icon_Dependencia = folium.features.CustomIcon('images/SEDECOP_marcador.png', icon_size=(60, 60),
                                                          icon_anchor=(22, 59),
                                                          popup_anchor=(3, -54))
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc)

genera_2022(df_concentrado2022,mc_3, "2022")

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
m.save("SEDECOP.html")

# %%
