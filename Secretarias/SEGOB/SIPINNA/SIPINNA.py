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

df_capacitaciones = pd.read_excel("SIPINNA_OK.xlsx", sheet_name='CAPACITACIONES')
df_capacitaciones_2022 = pd.read_excel("SIPINNA_OK.xlsx", sheet_name='CAPACITACIONES_2022')
df_capacitaciones_2023 = pd.read_excel("SIPINNA_OK.xlsx", sheet_name='CAPACITACIONES_2023')
df_capacitaciones_2024 = pd.read_excel("SIPINNA_OK.xlsx", sheet_name='CAPACITACIONES_2024')
df_oficinas = pd.read_excel("SIPINNA_OK.xlsx", sheet_name='SIPINNA_MUN_2024')
df_procuradores = pd.read_excel("SIPINNA_OK.xlsx", sheet_name='PROCURADORES')

df_capacitaciones = pd.merge(df_capacitaciones, df_Localidades, on="CVEGEO")
df_capacitaciones_2022 = pd.merge(df_capacitaciones_2022, df_Localidades, on="CVEGEO")
df_capacitaciones_2023 = pd.merge(df_capacitaciones_2023, df_Localidades, on="CVEGEO")
df_capacitaciones_2024 = pd.merge(df_capacitaciones_2024, df_Localidades, on="CVEGEO")
df_oficinas = pd.merge(df_oficinas, df_Localidades, on="CVEGEO")
df_procuradores = pd.merge(df_procuradores, df_Localidades, on="CVEGEO")

def format(x):
    return "{:,}".format(x)
df_capacitaciones['MUJERES'] = df_capacitaciones['MUJERES'].apply(format)
df_capacitaciones['HOMBRES'] = df_capacitaciones['HOMBRES'].apply(format)
df_capacitaciones['TOTAL'] = df_capacitaciones['TOTAL'].apply(format)

df_capacitaciones_2022['MUJERES'] = df_capacitaciones_2022['MUJERES'].apply(format)
df_capacitaciones_2022['HOMBRES'] = df_capacitaciones_2022['HOMBRES'].apply(format)
df_capacitaciones_2022['TOTAL'] = df_capacitaciones_2022['TOTAL'].apply(format)

df_capacitaciones_2023['MUJERES'] = df_capacitaciones_2023['MUJERES'].apply(format)
df_capacitaciones_2023['HOMBRES'] = df_capacitaciones_2023['HOMBRES'].apply(format)
df_capacitaciones_2023['TOTAL'] = df_capacitaciones_2023['TOTAL'].apply(format)

df_capacitaciones_2024['MUJERES'] = df_capacitaciones_2024['MUJERES'].apply(format)
df_capacitaciones_2024['HOMBRES'] = df_capacitaciones_2024['HOMBRES'].apply(format)
df_capacitaciones_2024['TOTAL'] = df_capacitaciones_2024['TOTAL'].apply(format)

#FORMATO DE HORA Y FECHA
df_capacitaciones['FECHA'] = df_capacitaciones['FECHA'].dt.strftime('%d/%m/%Y')
df_capacitaciones_2022['FECHA'] = df_capacitaciones_2022['FECHA'].dt.strftime('%d/%m/%Y')
df_capacitaciones_2023['FECHA'] = df_capacitaciones_2023['FECHA'].dt.strftime('%d/%m/%Y')
df_capacitaciones_2024['FECHA'] = df_capacitaciones_2024['FECHA'].dt.strftime('%d/%m/%Y')


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
layer_1 = FeatureGroup(name='Titulares de Secretarías Ejecutivas de los Sistemas Municipales 2024', show=False)
layer_procuradores = FeatureGroup(name='Directorio Procuradores 2024', show=False)
layer_2 = FeatureGroup(name='Capacitaciones 2021', show=False)
layer_3 = FeatureGroup(name='Capacitaciones 2022', show=False)
layer_4 = FeatureGroup(name='Capacitaciones 2023', show=False)
layer_5 = FeatureGroup(name='Capacitaciones 2024 (1er, 2do y 3er Trimestre)', show=False)

# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster

mc_1 = MarkerCluster()
mc_2 = MarkerCluster()
mc_3 = MarkerCluster()
mc_4 = MarkerCluster()
mc_5 = MarkerCluster()
mc_procuradores = MarkerCluster()

pd.set_option('display.max_columns', None)

def genera_oficinas(df_in, mc):
    for row in df_in.itertuples():
        contenido = tarjeta_oficinas(row)

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/SIPINNA_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

def genera_procuradores(df_in, mc):
    for row in df_in.itertuples():
        contenido = tarjeta_procuradores(row)

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/SIPINNA_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

def genera_capacitaciones(df_in, mc):
    for row in df_in.itertuples():
        contenido = tarjeta_capacitaciones(row)

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/SIPINNA_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

genera_oficinas(df_oficinas, mc_1)
genera_procuradores(df_procuradores,mc_procuradores)
genera_capacitaciones(df_capacitaciones, mc_2)
genera_capacitaciones(df_capacitaciones_2022, mc_3)
genera_capacitaciones(df_capacitaciones_2023, mc_4)
genera_capacitaciones(df_capacitaciones_2024, mc_5)

mc_1.add_to(layer_1)
mc_procuradores.add_to(layer_procuradores)
mc_2.add_to(layer_2)
mc_3.add_to(layer_3)
mc_4.add_to(layer_4)
mc_5.add_to(layer_5)

layer_1.add_to(m)
layer_procuradores.add_to(m)
layer_2.add_to(m)
layer_3.add_to(m)
layer_4.add_to(m)
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
m.save("SIPINNA.html")
