from pathlib import Path
import branca
import folium
import geopandas as gpd
import pandas as pd
from folium import FeatureGroup
from folium.plugins import Search
from Funciones import *

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
        """)
LogoCOESPO = ('images/COESPO_Logo_3.png')

# %%  LECTURA DE DATAFRAMES
df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))
df_oficinas = pd.read_excel("DGRPPIAGN_OK.xlsx", sheet_name='OFICINAS')
df_actividades = pd.read_excel("DGRPPIAGN_OK.xlsx", sheet_name='ACTIVIDADES')
df_actividades_2022 = pd.read_excel("DGRPPIAGN_OK.xlsx", sheet_name='ACTIVIDADES2022')
df_actividades_2023 = pd.read_excel("DGRPPIAGN_OK.xlsx", sheet_name='ACTIVIDADES2023')

df_actividades_2024_1 = pd.read_excel("DGRPPIAGN_OK.xlsx", sheet_name='ACTIVIDADES2024_1')
df_actividades_2024_2 = pd.read_excel("DGRPPIAGN_OK.xlsx", sheet_name='ACTIVIDADES2024_2')
df_actividades_2024_3 = pd.read_excel("DGRPPIAGN_OK.xlsx", sheet_name='ACTIVIDADES2024_3')

def format(x):
    return "{:,}".format(x)
df_actividades['INSCRIPCIONES'] = df_actividades['INSCRIPCIONES'].apply(format)
df_actividades['CERTIFICADOS'] = df_actividades['CERTIFICADOS'].apply(format)
df_actividades['OFICIOS'] = df_actividades['OFICIOS'].apply(format)
df_actividades['AVISOS'] = df_actividades['AVISOS'].apply(format)
df_actividades['SIGER'] = df_actividades['SIGER'].apply(format)
df_actividades['TOTAL'] = df_actividades['TOTAL'].apply(format)

df_actividades_2022['INSCRIPCIONES'] = df_actividades_2022['INSCRIPCIONES'].apply(format)
df_actividades_2022['CERTIFICADOS'] = df_actividades_2022['CERTIFICADOS'].apply(format)
df_actividades_2022['OFICIOS'] = df_actividades_2022['OFICIOS'].apply(format)
df_actividades_2022['AVISOS'] = df_actividades_2022['AVISOS'].apply(format)
df_actividades_2022['SIGER'] = df_actividades_2022['SIGER'].apply(format)
df_actividades_2022['TOTAL'] = df_actividades_2022['TOTAL'].apply(format)


df_actividades_2023['INSCRIPCIONES'] = df_actividades_2023['INSCRIPCIONES'].apply(format)
df_actividades_2023['CERTIFICADOS'] = df_actividades_2023['CERTIFICADOS'].apply(format)
df_actividades_2023['OFICIOS'] = df_actividades_2023['OFICIOS'].apply(format)
df_actividades_2023['AVISOS'] = df_actividades_2023['AVISOS'].apply(format)
df_actividades_2023['SIGER'] = df_actividades_2023['SIGER'].apply(format)
df_actividades_2023['TOTAL'] = df_actividades_2023['TOTAL'].apply(format)

df_actividades_2023['INSCRIPCIONES'] = df_actividades_2023['INSCRIPCIONES'].replace(" .0", "")
df_actividades_2023['CERTIFICADOS'] = df_actividades_2023['CERTIFICADOS'].replace(" .0", "")
df_actividades_2023['OFICIOS'] = df_actividades_2023['OFICIOS'].replace(" .0", "")
df_actividades_2023['AVISOS'] = df_actividades_2023['AVISOS'].replace(" .0", "")
df_actividades_2023['SIGER'] = df_actividades_2023['SIGER'].replace(" .0", "")
df_actividades_2023['TOTAL'] = df_actividades_2023['TOTAL'].replace(" .0", "")

df_actividades_2024_1['INSCRIPCIONES'] = df_actividades_2024_1['INSCRIPCIONES'].apply(format)
df_actividades_2024_1['CERTIFICADOS'] = df_actividades_2024_1['CERTIFICADOS'].apply(format)
df_actividades_2024_1['OFICIOS'] = df_actividades_2024_1['OFICIOS'].apply(format)
df_actividades_2024_1['AVISOS'] = df_actividades_2024_1['AVISOS'].apply(format)
df_actividades_2024_1['SIGER'] = df_actividades_2024_1['SIGER'].apply(format)
df_actividades_2024_1['TOTAL'] = df_actividades_2024_1['TOTAL'].apply(format)

df_actividades = pd.merge(df_actividades, df_Localidades, on="CVEGEO")
df_actividades_2022 = pd.merge(df_actividades_2022, df_Localidades, on="CVEGEO")
df_actividades_2023 = pd.merge(df_actividades_2023, df_Localidades, on="CVEGEO")

df_actividades_2024_1 = pd.merge(df_actividades_2024_1, df_Localidades, on="CVEGEO")
df_actividades_2024_2 = pd.merge(df_actividades_2024_2, df_Localidades, on="CVEGEO")
df_actividades_2024_3 = pd.merge(df_actividades_2024_3, df_Localidades, on="CVEGEO")
df_oficinas = pd.merge(df_oficinas, df_Localidades, on="CVEGEO")

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
layer_1 = FeatureGroup(name='Directorio de Oficinas', show=False)
layer_2 = FeatureGroup(name='Acciones 2021', show=False)
layer_3 = FeatureGroup(name='Acciones 2022', show=False)
layer_4 = FeatureGroup(name='Acciones 2023', show=False)
layer_8 = FeatureGroup(name='Acciones 2024 (1er Trimestre)', show=False)
layer_9 = FeatureGroup(name='Acciones 2024 (2do Trimestre)', show=False)
layer_10 = FeatureGroup(name='Acciones 2024 (3er Trimestre)', show=False)


# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster

mc_1 = MarkerCluster()
mc_2 = MarkerCluster()
mc_3 = MarkerCluster()
mc_4 = MarkerCluster()
mc_8 = MarkerCluster()
mc_9 = MarkerCluster()
mc_10 = MarkerCluster()

pd.set_option('display.max_columns', None)

def genera_oficinas(df_in, mc):
    for row in df_in.itertuples():
        contenido = tarjeta_oficinas(row)

        popup = folium.Popup(html=contenido,max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/DGRPPIAGN_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.LAT, row.LON], popup=popup, icon=icon_Dependencia).add_to(
            mc)


def genera_actividades(df_in, mc,periodo):
    for row in df_in.itertuples():
        contenido = tarjeta_actividades(row,periodo)

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/DGRPPIAGN_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

genera_oficinas(df_oficinas, mc_1)
genera_actividades(df_actividades, mc_2,"2021")
genera_actividades(df_actividades_2022, mc_3, "2022")
genera_actividades(df_actividades_2023, mc_4, "2023")
genera_actividades(df_actividades_2024_1, mc_8, "2024")
genera_actividades(df_actividades_2024_2, mc_9, "2024")
genera_actividades(df_actividades_2024_3, mc_10, "2024")

mc_1.add_to(layer_1)
mc_2.add_to(layer_2)
mc_3.add_to(layer_3)
mc_4.add_to(layer_4)
mc_8.add_to(layer_8)
mc_9.add_to(layer_9)
mc_10.add_to(layer_10)

layer_1.add_to(m)
layer_2.add_to(m)
layer_3.add_to(m)
layer_4.add_to(m)
layer_8.add_to(m)
layer_9.add_to(m)
layer_10.add_to(m)

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
m.save("DGRPPIAGN.html")
