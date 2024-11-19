

from pathlib import Path
import folium
import geopandas as gpd
import pandas as pd
from folium import FeatureGroup
from folium.plugins import Search
from Funciones import *
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

df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))
df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
df['CVEGEO'] = df.apply(lambda row: row.CVE_ENT + row.CVE_MUN, axis=1)
df['CVEGEO'] = df['CVEGEO'].apply(pd.to_numeric, errors='coerce')
df_regiones = df

df_caravanas = pd.read_excel("INVEDEP_2021.xlsx", sheet_name='CARAVANAS')
df_brigadas_2019 = pd.read_excel("INVEDEP_2021.xlsx", sheet_name='BRIGADAS_2019')
df_brigadas_2020 = pd.read_excel("INVEDEP_2021.xlsx", sheet_name='BRIGADAS_2020')
df_brigadas_2021 = pd.read_excel("INVEDEP_2021.xlsx", sheet_name='BRIGADAS_2021')
df_brigadas_2022 = pd.read_excel("INVEDEP_2021.xlsx", sheet_name='BRIGADAS_2022')
df_brigadas_2023 = pd.read_excel("INVEDEP_2021.xlsx", sheet_name='BRIGADAS_2023')
df_brigadas_2024 = pd.read_excel("INVEDEP_2021.xlsx", sheet_name='BRIGADAS_2024')

df_caravanas = pd.merge(df_caravanas, df_Localidades, on="CVEGEO")
df_brigadas_2019 = pd.merge(df_brigadas_2019, df_Localidades, on="CVEGEO")
df_brigadas_2020 = pd.merge(df_brigadas_2020, df_Localidades, on="CVEGEO")
df_brigadas_2021 = pd.merge(df_brigadas_2021, df_Localidades, on="CVEGEO")
df_brigadas_2022 = pd.merge(df_brigadas_2022, df_Localidades, on="CVEGEO")
df_brigadas_2023 = pd.merge(df_brigadas_2023, df_Localidades, on="CVEGEO")
df_brigadas_2024 = pd.merge(df_brigadas_2024, df_Localidades, on="CVEGEO")

df_caravanas['FECHA'] = df_caravanas['FECHA'].dt.strftime('%d/%m/%Y')
df_brigadas_2019['FECHA'] = df_brigadas_2019['FECHA'].dt.strftime('%d/%m/%Y')
df_brigadas_2020['FECHA'] = df_brigadas_2020['FECHA'].dt.strftime('%d/%m/%Y')
df_brigadas_2021['FECHA'] = df_brigadas_2021['FECHA'].dt.strftime('%d/%m/%Y')



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
# df_cobertura_zonas = pd.merge(df_regiones, df_zonas, on="CVEGEO")
# %% CAMBIAR TIPO DE STR A NUMERO PARA LATITUD Y LONGITUD
# df_dgt_oficinas['LAT'] = df_dgt_oficinas['LAT'].apply(pd.to_numeric, errors='coerce')
# df_dgt_oficinas['LON'] = df_dgt_oficinas['LON'].apply(pd.to_numeric, errors='coerce')
# print(df_dgt_oficinas.dtypes)
#
# # %%
#
# dfAccion3 = pd.read_csv("Accion3.csv")
# df_mapaAccion3 = pd.merge(dfAccion3, df_Localidades, on="CVEGEO")
# %%
# ---- Mapa Base de Veracruz

# Veracruz = folium.GeoJson(
#     df,
#     name='Veracruz',
#     control=False,
#     style_function=lambda feature: {
#         'fillColor': 'grey',
#         'color': 'grey',
#         'weight': 1,
#         'fillOpacity': 0.0,
#         'line_opacity': 0.0,
#         'line_color': 'grey',
#     }, tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Nombre Municipio:', 'Region:']),
# ).add_to(m)

## ---- Mapa # ---Cobertura delegaciones de tránsito
# colores = df_cobertura_zonas.set_index("CVE_MUN")["COLOR"]

# ---- Mapa Base de Veracruz
colores = df.set_index("CVE_MUN")["Color"]

def colorscale(color):
    return '"' + color + '"'

def style_function(feature):
    color = colores.get(int(feature["id"][-3:]), None)
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

mapa = folium.GeoJson(
    df,
    name='Cobertura de Zonas',
    highlight_function=highlight,
    style_function=style_function,
    control=True,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'],
                                           aliases=['Nombre Municipio:', 'Region:']),
).add_to(m)

# ---- Imagen inferior izquierda logo COESPO
from folium.plugins import FloatImage

LogoCOESPO = ('images/COESPO_Logo_3.png')
FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m)
# ---- Capas
Layer01 = FeatureGroup(name='Caravanas Culturales 2020', show=False)
Layer02 = FeatureGroup(name='Brigadas Itinerantes 2019', show=False)
Layer03 = FeatureGroup(name='Brigadas Itinerantes 2020', show=False)
Layer04 = FeatureGroup(name='Brigadas Itinerantes 2021', show=False)
Layer05 = FeatureGroup(name='Brigadas Itinerantes 2022', show=False)
Layer06 = FeatureGroup(name='Brigadas Itinerantes 2023', show=False)
Layer07 = FeatureGroup(name='Brigadas Itinerantes 2024 (1er y 2do Trimestre)', show=False)

# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster

mc_01 = MarkerCluster()
mc_02 = MarkerCluster()
mc_03 = MarkerCluster()
mc_04 = MarkerCluster()
mc_05 = MarkerCluster()
mc_06 = MarkerCluster()
mc_07 = MarkerCluster()

def genera_tarjeta(df_in,mc):
    for reg in df_in.itertuples():
        contenido = tarjeta_dos(reg)

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/INVEDEP_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        folium.Marker(location=[reg.lat_decimal, reg.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

genera_tarjeta(df_caravanas, mc_01)
genera_tarjeta(df_brigadas_2019, mc_02)
genera_tarjeta(df_brigadas_2020, mc_03)
genera_tarjeta(df_brigadas_2021, mc_04)
genera_tarjeta(df_brigadas_2022, mc_05)
genera_tarjeta(df_brigadas_2023, mc_06)
genera_tarjeta(df_brigadas_2024, mc_07)

mc_01.add_to(Layer01)
mc_02.add_to(Layer02)
mc_03.add_to(Layer03)
mc_04.add_to(Layer04)
mc_05.add_to(Layer05)
mc_06.add_to(Layer06)
mc_07.add_to(Layer07)

# mapa_c4 = folium.GeoJson(
#     df_cobertura_c4,
#     name='Cobertura Centros C4',
#     highlight_function=highlight,
#     style_function=style_function_c4,
#     control=True,
#     tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'SUBCENTRO'],
#                                            aliases=['Nombre del Municipio:', 'Subcentro:']),
# ).add_to(m)


Layer01.add_to(m)
Layer02.add_to(m)
Layer03.add_to(m)
Layer04.add_to(m)
Layer05.add_to(m)
Layer06.add_to(m)
Layer07.add_to(m)

#
# mc_Accion2.add_to(LayerAcciones2)

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

# ---- Control de Capas
# LayerAVGM.add_to(m)
# LayerPVD.add_to(m)


folium.LayerControl(collapsed=False).add_to(m)

m.save("INVEDEP.html")

# %%
