# %%

import webbrowser
from pathlib import Path

import branca
import folium
import geopandas as gpd
import pandas as pd
from branca.colormap import linear
from folium import FeatureGroup
from folium.plugins import Search
from numpy import int64

from Funciones import *

# %%
#path_ini = Path("C:/ESyP/Mapas_COESPO/Resources/")
path_ini = Path("/Users/4x/COESPOAX/MapasTematicos/Resources/")

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

df_violencia_fam = pd.read_excel("violenciaFamiliar.xlsx", sheet_name='v_fam_orig')
# df_vf2020 = pd.read_excel("violenciaFamiliar.xlsx", sheet_name='2020')
# df_vf2021 = pd.read_excel("violenciaFamiliar.xlsx", sheet_name='2021')

# df_violencia_fam = pd.merge(df_violencia_fam, df_Localidades, on="CVEGEO")

#vf2020 = df_violencia_fam.query("ANIO==2020")
#vf2021 = df_violencia_fam.query("ANIO==2021")
# mes=vf2020.groupby(["MUNICIPIO", "MES"]).count()


vf2020 = pd.read_excel("violenciaFamiliar.xlsx", sheet_name='2020_TOT')
vf2021 = pd.read_excel("violenciaFamiliar.xlsx", sheet_name='2021_TOT')
vf2020 = pd.merge(df, vf2020, on="CVEGEO")
vf2021 = pd.merge(df, vf2021, on="CVEGEO")

print(vf2020)

df.loc[df['region'] == 'Las_Montanas', 'region'] = 'Las Montañas'
df.loc[df['region'] == 'Huasteca_Alta', 'region'] = 'Huasteca Alta'
df.loc[df['region'] == 'Huasteca_Baja', 'region'] = 'Huasteca Baja'
df.loc[df['region'] == 'Los_Tuxtlas', 'region'] = 'Los Tuxtlas'

pd.set_option('max_columns', None)

m = folium.Map(location=[19.8727, -96.1333], zoom_start=7, prefer_canvas=True, tiles='OpenStreetMap')

cm_vf2020 = linear.Purples_09.scale(
    vf2020['TOTAL'].min(), vf2020['TOTAL'].max())
#cm_vf2020 = cm_vf2020.to_step(index=[0, 10, 20,30,40400, 700, vf2020['TOTAL'].max()])
cm_vf2020.caption = 'Violencia familiar Jul - Dic 2020'

cm_vf2021 = linear.Purples_03.scale(
    vf2020['TOTAL'].min(),
    vf2020['TOTAL'].max(),
)




# ---- Mapa Base de Veracruz


def style_function(feature):
    color = '#CCF5B4'
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


# ---Mapa de casos violencia familiar jul - dic 2020
TipoViolenciaMap = folium.GeoJson(
    vf2020,
    name='Violencia Familiar jul - dic 2020',
    show=False,
    style_function=lambda feature: {
        'fillColor': cm_vf2020(feature['properties']['TOTAL']),
        'color': 'grey',
        'weight': 1,
        'fillOpacity': 0.9,
        'line_opacity': 0.9,
        'line_color': 'grey',
    }, tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'Femenino', 'Masculino', 'SIN DATO', 'TOTAL'],
                                              aliases=['Municipio: ', 'Mujeres: ', 'Hombres:', 'Sin Dato',
                                                       'Total: ']),
).add_to(m)

# ---Mapa de casos violencia familiar ene - jun 2021
violencia_fam2021 = folium.GeoJson(
    vf2021,
    name='Violencia Familiar ene - jun 2021',
    show=False,
    style_function=lambda feature: {
        'fillColor': cm_vf2021(feature['properties']['TOTAL']),
        'color': 'grey',
        'weight': 1,
        'fillOpacity': 0.9,
        'line_opacity': 0.9,
        'line_color': 'grey',
    }, tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'Femenino', 'Masculino', 'SIN DATO', 'TOTAL'],
                                              aliases=['Municipio: ', 'Mujeres: ', 'Hombres:', 'Sin Dato',
                                                       'Total: ']),
).add_to(m)

# ---- Imagen inferior izquierda logo COESPO
from folium.plugins import FloatImage

FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m)
# ---- Capas

# layer_0 = FeatureGroup(name='Acciones 2020', show=False)
layer_1 = FeatureGroup(name='Acciones', show=False)

# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster

mc_1 = MarkerCluster()


def acciones(df_in):
    # df['Value'] = df.apply(lambda x: "{:,}".format(x['Value']), axis=1)
    # BENEFICIADOS, ACCION, APOYO, FOTO
    for row in df_in.itertuples():
        contenido = content_tarjeta(str(row.MUNICIPIO), str(row.BENEFICIADOS), str(row.ACCION), str(row.APOYO),
                                    str(row.FOTO))

        popup = folium.Popup(html=contenido, max_width='520')
        icon_Dependencia = folium.features.CustomIcon('images/IVJ_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_1)


mc_1.add_to(layer_1)

layer_1.add_to(m)

# ---- Botón de Búsqueda de Municipio
statesearch = Search(
    layer=TipoViolenciaMap,
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

m.save("ViolenciaFam.html")
webbrowser.open("ViolenciaFam.html")
