from pathlib import Path
import folium
import geopandas as gpd
import pandas as pd
from folium import FeatureGroup
from folium.plugins import Search

from Funciones import *

# %%
path_ini = Path("C:/ESyP/Mapas_COESPO/Resources/")
pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('display.max_columns', None)

df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
df['CVEGEO'] = df.apply(lambda row: row.CVE_ENT + row.CVE_MUN, axis=1)
# print(df.dtypes)
df['CVEGEO'] = df['CVEGEO'].apply(pd.to_numeric, errors='coerce')
# print(df.dtypes)
df_regiones = df

df_regiones.loc[df_regiones['region'] == 'Las_Montanas', 'region'] = 'Las Montañas'
df_regiones.loc[df_regiones['region'] == 'Huasteca_Alta', 'region'] = 'Huasteca Alta'
df_regiones.loc[df_regiones['region'] == 'Huasteca_Baja', 'region'] = 'Huasteca Baja'
df_regiones.loc[df_regiones['region'] == 'Los_Tuxtlas', 'region'] = 'Los Tuxtlas'
df_regiones['Color'] = 'grey'
df_regiones.loc[df_regiones['region'] == 'Capital', ['Color']] = '#e8694b'
df_regiones.loc[df_regiones['region'] == 'Huasteca Alta', ['Color']] = '#7cd5a3'
df_regiones.loc[df_regiones['region'] == 'Huasteca Baja', ['Color']] = '#96B921'
df_regiones.loc[df_regiones['region'] == 'Los_Tuxtla', ['Color']] = '#5bbdbf'
df_regiones.loc[df_regiones['region'] == 'Nautla', ['Color']] = '#FDAF3F'
df_regiones.loc[df_regiones['region'] == 'Los Tuxtlas', ['Color']] = '#5bbdbf'
df_regiones.loc[df_regiones['region'] == 'Olmeca', ['Color']] = '#d6ecf8'
df_regiones.loc[df_regiones['region'] == 'Papaloapan', ['Color']] = '#846789'
df_regiones.loc[df_regiones['region'] == 'Sotavento', ['Color']] = '#6e79c1'
df_regiones.loc[df_regiones['region'] == 'Totonaca', ['Color']] = '#D0D108'
df_regiones.loc[df_regiones['region'] == 'Las Montañas', ['Color']] = '#f3b8df'

df_Capital = df_regiones.loc[df_regiones['region'] == 'Capital']
df_Huasteca_alta = df_regiones.loc[df_regiones['region'] == 'Huasteca Alta']
df_Huasteca_baja = df_regiones.loc[df_regiones['region'] == 'Huasteca Baja']
df_Los_Tuxtla = df_regiones.loc[df_regiones['region'] == 'Los Tuxtla']
df_Nautla = df_regiones.loc[df_regiones['region'] == 'Nautla']
df_Los_Tuxtlas = df_regiones.loc[df_regiones['region'] == 'Los Tuxtlas']
df_Olmeca = df_regiones.loc[df_regiones['region'] == 'Olmeca']
df_Papaloapan = df_regiones.loc[df_regiones['region'] == 'Papaloapan']
df_Sotavento = df_regiones.loc[df_regiones['region'] == 'Sotavento']
df_Totonaca = df_regiones.loc[df_regiones['region'] == 'Totonaca']
df_Las_Montanas = df_regiones.loc[df_regiones['region'] == 'Las Montañas']

# %%

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
# %%

LogoCOESPO = ('images/COESPO_Logo_3.png')
df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))

# %%
df_2021 = pd.read_excel("CPVCC_OK.xlsx", sheet_name="2021")
df_2022 = pd.read_excel("CPVCC_OK.xlsx", sheet_name="2022")
df_2023 = pd.read_excel("CPVCC_OK.xlsx", sheet_name="2023")
df_2024 = pd.read_excel("CPVCC_OK.xlsx", sheet_name="2024")

df_2021 = pd.merge(df_2021, df_Localidades, on="CVEGEO")
df_2022 = pd.merge(df_2022, df_Localidades, on="CVEGEO")
df_2023 = pd.merge(df_2023, df_Localidades, on="CVEGEO")
df_2024 = pd.merge(df_2024, df_Localidades, on="CVEGEO")

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

mapa = folium.GeoJson(
    df,
    name='Regiones',
    highlight_function=highlight,
    control=False,
    style_function=style_function, tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Nombre Municipio:', 'Región:']),
).add_to(m)

# ---- Imagen inferior izquierda logo COESPO
from folium.plugins import FloatImage

LogoCOESPO = ('images/COESPO_Logo_3.png')
FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m)
# ---- Capas

Layer_2021 = FeatureGroup(name='Acciones 2021', show=False)
Layer_2022_1 = FeatureGroup(name='Acciones 2022', show=False)
Layer_2023 = FeatureGroup(name='Acciones 2023', show=False)
Layer_2024 = FeatureGroup(name='Acciones 2024 (1er, 2do y 3er Trimestre)', show=False)

# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster

mc_2021 = MarkerCluster()
mc_2022_1 = MarkerCluster()
mc_2023 = MarkerCluster()
mc_2024 = MarkerCluster()

def genera_tarjeta(df_in, mc):
    for row in df_in.itertuples():
        contenido = genera_contenido(str(row.MUNICIPIO), str(row.FECHA), str(row.TIPO), str(row.EVENTO),
                                     str(row.FOTO1), str(row.FOTO2), str(row.VIDEO))
        icon_Dependencia = folium.features.CustomIcon('images/CPVCC_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        popup = folium.Popup(html=contenido, max_width='290')
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

genera_tarjeta(df_2021, mc_2021)
genera_tarjeta(df_2022, mc_2022_1)
genera_tarjeta(df_2023, mc_2023)
genera_tarjeta(df_2024, mc_2024)

mc_2021.add_to(Layer_2021)
mc_2022_1.add_to(Layer_2022_1)
mc_2023.add_to(Layer_2023)
mc_2024.add_to(Layer_2024)

Layer_2021.add_to(m)
Layer_2022_1.add_to(m)
Layer_2023.add_to(m)
Layer_2024.add_to(m)

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
m.save("CPVCC.html")
