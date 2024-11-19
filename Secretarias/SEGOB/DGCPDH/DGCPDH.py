# %%
from pathlib import Path

import branca
import folium
import geopandas as gpd
import pandas as pd
from folium import FeatureGroup
from folium.plugins import Search

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


# %%

LogoCOESPO = 'images/COESPO_Logo_3.png'

# %%  LECTURA DE DATAFRAMES
df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
# print(df)
df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))
df_cine_2021 = pd.read_excel("DGCPDH_OK_2021.xlsx", sheet_name='Cine-debate')
df_mesas_regionales_2021 = pd.read_excel("DGCPDH_OK_2021.xlsx", sheet_name='Mesas regionales')
df_mesas_2021 = pd.read_excel("DGCPDH_OK_2021.xlsx", sheet_name='Mesas de diálogo')
df_revista_2021 = pd.read_excel("DGCPDH_OK_2021.xlsx", sheet_name='Presentación de revista')
df_presentaciones_2021 = pd.read_excel("DGCPDH_OK_2021.xlsx", sheet_name='Presentaciones')
df_becas_2021 = pd.read_excel("DGCPDH_OK_2021.xlsx", sheet_name='Becas')

df_cursos = pd.read_excel("DGCPDH_OK.xlsx", sheet_name='CURSO')
df_conferencias = pd.read_excel("DGCPDH_OK.xlsx", sheet_name='CONFERENCIA')
df_talleres = pd.read_excel("DGCPDH_OK.xlsx", sheet_name='TALLER')
df_conversatorios = pd.read_excel("DGCPDH_OK.xlsx", sheet_name='CONVERSATORIO')
df_capacitacion = pd.read_excel("DGCPDH_OK.xlsx", sheet_name='CAPACITACION')
df_mesas = pd.read_excel("DGCPDH_OK.xlsx", sheet_name='MESAS DE TRABAJO')



df_talleres_2023 = pd.read_excel("DGCPDH_OK.xlsx", sheet_name='TALLER_2023')
df_conversatorios_2023 = pd.read_excel("DGCPDH_OK.xlsx", sheet_name='CONVERSATORIO_2023')
df_capacitacion_2023 = pd.read_excel("DGCPDH_OK.xlsx", sheet_name='CAPACITACION_2023')

df_conversatorios_2024 = pd.read_excel("DGCPDH_OK.xlsx", sheet_name='CONVERSATORIO_2024')
df_capacitacion_2024 = pd.read_excel("DGCPDH_OK.xlsx", sheet_name='CAPACITACION_2024')


df_cine_2021 = pd.merge(df_cine_2021, df_Localidades, on="CVEGEO")
df_mesas_regionales_2021 = pd.merge(df_mesas_regionales_2021, df_Localidades, on="CVEGEO")
df_mesas_2021 = pd.merge(df_mesas_2021, df_Localidades, on="CVEGEO")
df_revista_2021 = pd.merge(df_revista_2021, df_Localidades, on="CVEGEO")
df_becas_2021 = pd.merge(df_becas_2021, df_Localidades, on="CVEGEO")
df_presentaciones_2021 = pd.merge(df_presentaciones_2021, df_Localidades, on="CVEGEO")

df_cursos = pd.merge(df_cursos, df_Localidades, on="CVEGEO")
df_conferencias = pd.merge(df_conferencias, df_Localidades, on="CVEGEO")
df_talleres = pd.merge(df_talleres, df_Localidades, on="CVEGEO")
df_conversatorios = pd.merge(df_conversatorios, df_Localidades, on="CVEGEO")
df_capacitacion= pd.merge(df_capacitacion, df_Localidades, on="CVEGEO")
df_mesas = pd.merge(df_mesas, df_Localidades, on="CVEGEO")

df_talleres_2023 = pd.merge(df_talleres_2023, df_Localidades, on="CVEGEO")
df_conversatorios_2023 = pd.merge(df_conversatorios_2023, df_Localidades, on="CVEGEO")
df_capacitacion_2023= pd.merge(df_capacitacion_2023, df_Localidades, on="CVEGEO")

df_conversatorios_2024 = pd.merge(df_conversatorios_2024, df_Localidades, on="CVEGEO")
df_capacitacion_2024= pd.merge(df_capacitacion_2024, df_Localidades, on="CVEGEO")


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
    # print(color)
    # color=color.to_json()
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

# ---- Imagen inferior izquierda logo COESPO
from folium.plugins import FloatImage

FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m)
# ---- Capas

# layer_0 = FeatureGroup(name='Acciones 2020', show=False)
layer_conferencias_2022 = FeatureGroup(name='Conferencias 2022', show=False)
layer_conversatorios_2022 = FeatureGroup(name='Conversatorios 2022', show=False)
layer_conversatorios_2023 = FeatureGroup(name='Conversatorios 2023', show=False)
layer_conversatorios_2024 = FeatureGroup(name='Conversatorios 2024 (1er y 2do Trimestre)', show=False)
layer_cursos_2022 = FeatureGroup(name='Cursos 2022', show=False)
layer_talleres_2022 = FeatureGroup(name='Talleres 2022', show=False)
layer_talleres_2023 = FeatureGroup(name='Talleres 2023', show=False)
layer_capacitaciones_2022 = FeatureGroup(name='Capacitaciones', show=False)
layer_capacitaciones_2023 = FeatureGroup(name='Capacitaciones 2023', show=False)
layer_capacitaciones_2024 = FeatureGroup(name='Capacitaciones 2024 (1er y 2do Trimestre)', show=False)
layer_mesas_2022 = FeatureGroup(name='Mesas de Trabajo 2022', show=False)
layer_revista_2021 = FeatureGroup(name='Presentación de Revista 2021', show=False)
layer_presentaciones_2021 = FeatureGroup(name='Presentaciones 2021', show=False)
layer_conversatorios_2021 = FeatureGroup(name='Conversatorios 2021', show=False)
layer_mesasR_2021 = FeatureGroup(name='Mesas Regionales 2021', show=False)
layer_becas_2021 = FeatureGroup(name='Becas 2021', show=False)




# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster

mc_conferencias = MarkerCluster()
mc_conversatorios = MarkerCluster()
mc_cursos = MarkerCluster()
mc_talleres = MarkerCluster()
mc_capacitaciones = MarkerCluster()
mc_mesas = MarkerCluster()
mc_revista_2021 = MarkerCluster()
mc_presentaciones_2021 = MarkerCluster()
mc_conversatorios_2021 = MarkerCluster()
mc_mesasR_2021 = MarkerCluster()
mc_becas_2021 = MarkerCluster()
mc_talleres2023 = MarkerCluster()
mc_capacitaciones2023 = MarkerCluster()
mc_capacitaciones2024 = MarkerCluster()
mc_conversatorios2023 = MarkerCluster()
mc_conversatorios2024 = MarkerCluster()

pd.set_option('display.max_columns', None)

def genera(df_in, mc, tarjeta):
    for row in df_in.itertuples():
        if tarjeta == "cine":
            contenido = tarjeta_cine(row)
        elif tarjeta == "cursos":
            contenido = tarjeta_cursos_y_capacitaciones(row)
        elif tarjeta == "capacitaciones":
            contenido = tarjeta_cursos_y_capacitaciones(row)
        elif tarjeta == "mesas_trabajo":
            contenido = tarjeta_mesas_trabajo(row)
        elif tarjeta == "mesas_regionales":
            contenido = tarjeta_mesas(row)
        elif tarjeta == "becas":
            contenido = tarjeta_becas(row)
        elif tarjeta == "revista":
            contenido = tarjeta_revista_y_presentaciones(row)
        elif tarjeta == "presentaciones":
            contenido = tarjeta_revista_y_presentaciones(row)
        else:
            contenido = tarjeta_otros(row)

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/DGCPDH_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

genera(df_conferencias, mc_conferencias, "cursos")
genera(df_conversatorios, mc_conversatorios, "")
genera(df_cursos, mc_cursos, "cursos")
genera(df_talleres, mc_talleres, "cursos")
genera(df_capacitacion, mc_capacitaciones, "capacitaciones")
genera(df_mesas, mc_mesas, "mesas_trabajo")
genera(df_revista_2021, mc_revista_2021, "revista")
genera(df_presentaciones_2021, mc_presentaciones_2021, "presentaciones")
genera(df_conversatorios, mc_conversatorios_2021, "conversa")
genera(df_mesas_regionales_2021, mc_mesasR_2021, "mesas_regionales")
genera(df_becas_2021, mc_becas_2021, "becas")

genera(df_capacitacion_2023, mc_capacitaciones2023, "capacitaciones")
genera(df_talleres_2023, mc_talleres2023, "cursos")
genera(df_conversatorios_2023, mc_conversatorios2023, "conversa")

genera(df_capacitacion_2024, mc_capacitaciones2024, "capacitaciones")
genera(df_conversatorios_2024, mc_conversatorios2024, "conversa")

mc_conferencias.add_to(layer_conferencias_2022)
mc_conversatorios.add_to(layer_conversatorios_2022)
mc_cursos.add_to(layer_cursos_2022)
mc_talleres.add_to(layer_talleres_2022)
mc_capacitaciones.add_to(layer_capacitaciones_2022)
mc_mesas.add_to(layer_mesas_2022)
mc_revista_2021.add_to(layer_revista_2021)
mc_presentaciones_2021.add_to(layer_presentaciones_2021)
mc_conversatorios_2021.add_to(layer_conversatorios_2021)
mc_mesasR_2021.add_to(layer_mesasR_2021)
mc_becas_2021.add_to(layer_becas_2021)

mc_capacitaciones2023.add_to(layer_capacitaciones_2023)
mc_talleres2023.add_to(layer_talleres_2023)
mc_conversatorios2023.add_to(layer_conversatorios_2023)

mc_capacitaciones2024.add_to(layer_capacitaciones_2024)
mc_conversatorios2024.add_to(layer_conversatorios_2024)


layer_conferencias_2022.add_to(m)
layer_conversatorios_2022.add_to(m)
layer_conversatorios_2023.add_to(m)
layer_conversatorios_2024.add_to(m)
layer_cursos_2022.add_to(m)
layer_talleres_2022.add_to(m)
layer_talleres_2023.add_to(m)
layer_capacitaciones_2022.add_to(m)
layer_capacitaciones_2023.add_to(m)
layer_capacitaciones_2024.add_to(m)
layer_mesas_2022.add_to(m)
layer_revista_2021.add_to(m)
layer_presentaciones_2021.add_to(m)
layer_conversatorios_2021.add_to(m)
layer_mesasR_2021.add_to(m)
layer_becas_2021.add_to(m)



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

m.save("DGCPDH.html")

# %%
