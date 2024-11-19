from pathlib import Path
import branca
import folium
import geopandas as gpd
import pandas as pd
from folium import FeatureGroup
from folium.plugins import Search
from numpy import int64
from Funciones import *

path_ini = Path("C:/ESyP/Mapas_COESPO/Resources/")
#path_ini = Path("/Users/4x/COESPOAX/MapasTematicos/Resources")

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
        """)
LogoCOESPO = ('images/COESPO_Logo.png')

# %%  LECTURA DE DATAFRAMES
df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
df['CVEGEO'] = df['CVE_ENT'] + df['CVE_MUN']
# print(df)
# df['CVEGEO'] = df.apply(lambda row: row.CVE_ENT + row.CVE_MUN, axis=1)
df['CVEGEO'] = df['CVEGEO'].astype(int64)  # ESTABA COMO FLOAT

df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))

df_capacitacion = pd.read_excel("CEJUM_OK.xlsx", sheet_name='CAPACITACION')
df_capacitacion_2023 = pd.read_excel("CEJUM_OK.xlsx", sheet_name='CAPACITACION_2023')
df_capacitacion_2024 = pd.read_excel("CEJUM_OK.xlsx", sheet_name='CAPACITACION_2024')
df_atencion = pd.read_excel("CEJUM_OK.xlsx", sheet_name='ATENCION')
df_atencion_2023 = pd.read_excel("CEJUM_OK.xlsx", sheet_name='ATENCION_2023')
df_atencion_2024 = pd.read_excel("CEJUM_OK.xlsx", sheet_name='ATENCION_2024')
df_reuniones = pd.read_excel("CEJUM_OK.xlsx", sheet_name='REUNIONES')

df_capacitacion = pd.merge(df_capacitacion, df_Localidades, on="CVEGEO")
df_capacitacion_2023 = pd.merge(df_capacitacion_2023, df_Localidades, on="CVEGEO")
df_capacitacion_2024 = pd.merge(df_capacitacion_2024, df_Localidades, on="CVEGEO")
df_atencion = pd.merge(df_atencion, df_Localidades, on="CVEGEO")
df_atencion_2023 = pd.merge(df_atencion_2023, df_Localidades, on="CVEGEO")
df_atencion_2024 = pd.merge(df_atencion_2024, df_Localidades, on="CVEGEO")
df_reuniones = pd.merge(df_reuniones, df_Localidades, on="CVEGEO")


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

pd.set_option('max_columns', None)
m = folium.Map(location=[19.8727, -96.1333], zoom_start=7, prefer_canvas=True, tiles='OpenStreetMap')
# ---- Mapa Base de Veracruz
colores = df.set_index("CVE_MUN")["Color"]

# ---- Mapa Base de Veracruz
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

mapa = folium.GeoJson(
    df,
    name='Regiones',
    highlight_function=highlight,
    control=False,
    style_function=style_function, tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Nombre Municipio:', 'Región:']),
).add_to(m)

# ---- Imagen inferior izquierda logo COESPO
from folium.plugins import FloatImage

FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m)

# ---- Capas
layer_1 = FeatureGroup(name='Capacitaciónes 2022', show=False)
layer_2 = FeatureGroup(name='Atención 2022', show=False)
layer_3 = FeatureGroup(name='Reuniones 2022', show=False)
layer_4 = FeatureGroup(name='Capacitaciónes 2023', show=False)
layer_5 = FeatureGroup(name='Atención 2023', show=False)
layer_6 = FeatureGroup(name='Capacitaciónes 2024 (1er y 2do Trimestre)', show=False)
layer_7 = FeatureGroup(name='Atención 2024 (1er y 2do Trimestre)', show=False)

# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster

mc_1 = MarkerCluster()
mc_2 = MarkerCluster()
mc_3 = MarkerCluster()
mc_4 = MarkerCluster()
mc_5 = MarkerCluster()
mc_6 = MarkerCluster()
mc_7 = MarkerCluster()

def genera_reuniones_capacitaciones(df_in, mc):
    for row in df_in.itertuples():
        contenido = genera_tarjeta_capa(str(row.MUNICIPIO),str(row.TEMA),str(row.FECHA),str(row.DESCIPCION),str(row.FOTO),
                                   str(row.FOTO2),str(row.FOTO3))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/CEJUM_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)


def genera_atenciones(df_in, mc):
    for row in df_in.itertuples():
        contenido = genera_tarjeta_atencion(str(row.MUNICIPIO),str(row.BENEFICIADOS),str(row.ACCION),str(row.APOYO))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/CEJUM_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

genera_reuniones_capacitaciones(df_capacitacion, mc_1)
genera_atenciones(df_atencion, mc_2)
genera_reuniones_capacitaciones(df_reuniones, mc_3)

genera_reuniones_capacitaciones(df_capacitacion_2023, mc_4)
genera_atenciones(df_atencion_2023, mc_5)

genera_reuniones_capacitaciones(df_capacitacion_2024, mc_6)
genera_atenciones(df_atencion_2024, mc_7)

mc_1.add_to(layer_1)
mc_2.add_to(layer_2)
mc_3.add_to(layer_3)
mc_4.add_to(layer_4)
mc_5.add_to(layer_5)
mc_6.add_to(layer_6)
mc_7.add_to(layer_7)

layer_1.add_to(m)
layer_2.add_to(m)
layer_3.add_to(m)
layer_4.add_to(m)
layer_5.add_to(m)
layer_6.add_to(m)
layer_7.add_to(m)

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
m.save("CEJUM.html")
