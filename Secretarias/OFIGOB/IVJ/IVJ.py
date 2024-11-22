from pathlib import Path
import branca
import folium
import geopandas as gpd
import pandas as pd
from folium import FeatureGroup
from folium.plugins import Search
from numpy import int64

from Funciones import *
import webbrowser
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
        """)

LogoCOESPO = ('images/COESPO_Logo_3.png')

# %%  LECTURA DE DATAFRAMES
df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
df['CVEGEO'] = df['CVE_ENT'] + df['CVE_MUN']
df['CVEGEO'] = df['CVEGEO'].astype(int64)

df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))
df_acciones_2021 = pd.read_excel("IVJ_OK.xlsx", sheet_name='ACCIONES 2021')
df_acciones_2022 = pd.read_excel("IVJ_OK.xlsx", sheet_name='ACCIONES 2022')
df_acciones_2023 = pd.read_excel("IVJ_OK.xlsx", sheet_name='ACCIONES 2023')
df_acciones_2024 = pd.read_excel("IVJ_OK.xlsx", sheet_name='ACCIONES 2024')

df_acciones_2021 = pd.merge(df_acciones_2021, df_Localidades, on="CVEGEO")
df_acciones_2022 = pd.merge(df_acciones_2022, df_Localidades, on="CVEGEO")
df_acciones_2023 = pd.merge(df_acciones_2023, df_Localidades, on="CVEGEO")
df_acciones_2024 = pd.merge(df_acciones_2024, df_Localidades, on="CVEGEO")

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
#                                           style=(
#                                              'background-color:#900C3F;'
#                                               'font-family:sans-serif; '
#                                               'font-size:12px;'
#                                               'color:white;'
#                                               'padding:10px'))


# ---- Imagen inferior izquierda logo COESPO
from folium.plugins import FloatImage

FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m)
# ---- Capas
layer_2021 = FeatureGroup(name='Acciones 2021', show=False)
layer_2022 = FeatureGroup(name='Acciones 2022', show=False)
layer_2023 = FeatureGroup(name='Acciones 2023', show=False)
layer_2024 = FeatureGroup(name='Acciones 2024 (1er, 2do y 3er Trimestre)', show=False)

# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster

mc_2021 = MarkerCluster()
mc_2022 = MarkerCluster()
mc_2023 = MarkerCluster()
mc_2024 = MarkerCluster()


def acciones(df_in,mc):
    for row in df_in.itertuples():
        contenido = content_tarjeta(str(row.MUNICIPIO), str(row.BENEFICIADOS), str(row.ACCION), str(row.APOYO),
                                    str(row.FOTO))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/IVJ_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

acciones(df_acciones_2021,mc_2021)
acciones(df_acciones_2022,mc_2022)
acciones(df_acciones_2023,mc_2023)
acciones(df_acciones_2024,mc_2024)

mc_2021.add_to(layer_2021)
mc_2022.add_to(layer_2022)
mc_2023.add_to(layer_2023)
mc_2024.add_to(layer_2024)

layer_2021.add_to(m)
layer_2022.add_to(m)
layer_2023.add_to(m)
layer_2024.add_to(m)

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
m.save("IVJ.html")

