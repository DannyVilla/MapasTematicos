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
LogoCOESPO = 'images/COESPO_Logo_3.png'

# %%  LECTURA DE DATAFRAMES
df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
# print(df)
df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))
df_actividades = pd.read_excel("CEEAIV_OK.xlsx", sheet_name='CEEAIV 2021')
df_actividades2022 = pd.read_excel("CEEAIV_OK.xlsx", sheet_name='CEEAIV 2022')
df_actividades2023 = pd.read_excel("CEEAIV_OK.xlsx", sheet_name='CEEAIV 2023')
df_actividades2024_1 = pd.read_excel("CEEAIV_OK.xlsx", sheet_name='CEEAIV 2024')
df_oficinas = pd.read_excel("CEEAIV_OK.xlsx", sheet_name='OFICINAS')

df_actividades = pd.merge(df_actividades, df_Localidades, on="CVEGEO")
df_actividades2022 = pd.merge(df_actividades2022, df_Localidades, on="CVEGEO")
df_actividades2023 = pd.merge(df_actividades2023, df_Localidades, on="CVEGEO")
df_actividades2024_1 = pd.merge(df_actividades2024_1, df_Localidades, on="CVEGEO")
df_oficinas = pd.merge(df_oficinas, df_Localidades, on='CVEGEO')

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
    control=False,
    style_function=style_function,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Nombre Municipio:', 'Región:']),
).add_to(m)

# ---- Imagen inferior izquierda logo COESPO
from folium.plugins import FloatImage

FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m)

layer_2 = FeatureGroup(name='Directorio Oficinas', show=False)
layer_1 = FeatureGroup(name='Actividades 2021', show=False)
layer_3 = FeatureGroup(name='Actividades 2022', show=False)
layer_4 = FeatureGroup(name='Actividades 2023', show=False)

layer_5 = FeatureGroup(name='Actividades 2024 (1er, 2do y 3er Trimestre)', show=False)

# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster

mc_1 = MarkerCluster()
mc_2 = MarkerCluster()
mc_3 = MarkerCluster()
mc_4 = MarkerCluster()

mc_5 = MarkerCluster()

pd.set_option('display.max_columns', None)

def genera(df_in, mc, func, anio):
    for row in df_in.itertuples():
        latitud = row.lat_decimal
        longitud = row.lon_decimal
        if func == "actividades":
            contenido = genera_actividades(str(row.MUNICIPIO), str(row.ASESORIA), str(row.PRIMER),
                                           str(row.PSICOLOGICA), str(row.REGISTROS), str(row.DICTAMENES),
                                           str(row.BENEFICIADOS),str(row.APOYOS1),str(row.APOYOS2), anio)

        longitud = row.lon_decimal
        if func == "actividades_2023_2024":
            contenido = genera_actividades_2023_2024(str(row.MUNICIPIO), str(row.ASESORIA), str(row.PRIMER_B), str(row.PRIMER_A),
                                                str(row.TRABAJO_B), str(row.TRABAJO_A), str(row.PSICOLOGICA_B), str(row.PSICOLOGICA_A),
                                                str(row.REGISTROS_B), str(row.REGISTROS_A),str(row.COMITÉ_B), str(row.COMITÉ_A), anio)


        elif func == "oficinas":
            contenido = genera_oficinas(str(row.MUNICIPIO), str(row.TEL), str(row.DIRECCION), str(row.FOTO))
            if row.LAT and row.LON:
                latitud = row.LAT
                longitud = row.LON
        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/CEAIV_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[latitud, longitud], popup=popup, icon=icon_Dependencia).add_to(
            mc)


genera(df_actividades, mc_1, "actividades", "2021")
genera(df_actividades2022, mc_3, "actividades", "2022")
genera(df_actividades2023, mc_4, "actividades", "2022")

genera(df_actividades2024_1, mc_5, "actividades_2023_2024", "2024")

genera(df_oficinas, mc_2, "oficinas", "2021")
mc_1.add_to(layer_1)
mc_2.add_to(layer_2)
mc_3.add_to(layer_3)
mc_4.add_to(layer_4)
mc_5.add_to(layer_5)

layer_2.add_to(m)
layer_1.add_to(m)
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
m.save("CEEAIV.html")
