# %%

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

#2021
df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))
df_atencion_ciudadana = pd.read_excel("DGCSJP_OK.xlsx", sheet_name='Atencion')
df_mesas = pd.read_excel("DGCSJP_OK.xlsx", sheet_name='Mesas')
df_sesiones = pd.read_excel("DGCSJP_OK.xlsx", sheet_name='Sesion')

#2022
df_mesas_2022 = pd.read_excel("DGCSJP_OK.xlsx", sheet_name='MESAS_2022')
df_capacitaciones_2022 = pd.read_excel("DGCSJP_OK.xlsx", sheet_name='CAPACITACIONES_2022')

#2023
df_atencion_ciudadana_2023 = pd.read_excel("DGCSJP_OK.xlsx", sheet_name='ATENCION_2023')
df_mesas_2023 = pd.read_excel("DGCSJP_OK.xlsx", sheet_name='MESAS_2023')
df_capacitaciones_2023 = pd.read_excel("DGCSJP_OK.xlsx", sheet_name='CAPACITACIONES_2023')

#2024
df_atencion_ciudadana_2024 = pd.read_excel("DGCSJP_OK.xlsx", sheet_name='ATENCION_2024')
df_mesas_2024 = pd.read_excel("DGCSJP_OK.xlsx", sheet_name='MESAS_2024')
df_capacitaciones_2024 = pd.read_excel("DGCSJP_OK.xlsx", sheet_name='CAPACITACIONES_2024')


#Merge 2021
df_atencion_ciudadana = pd.merge(df_atencion_ciudadana, df_Localidades, on="CVEGEO")
df_mesas = pd.merge(df_mesas, df_Localidades, on="CVEGEO")
df_sesiones = pd.merge(df_sesiones, df_Localidades, on="CVEGEO")

#Merge 2022
df_mesas_2022 = pd.merge(df_mesas_2022, df_Localidades, on="CVEGEO")
df_capacitaciones_2022 = pd.merge(df_capacitaciones_2022, df_Localidades, on="CVEGEO")

#Merge 2023
df_atencion_ciudadana_2023 = pd.merge(df_atencion_ciudadana_2023, df_Localidades, on="CVEGEO")
df_mesas_2023 = pd.merge(df_mesas_2023, df_Localidades, on="CVEGEO")
df_capacitaciones_2023 = pd.merge(df_capacitaciones_2023, df_Localidades, on="CVEGEO")

#Merge 2023
df_atencion_ciudadana_2024 = pd.merge(df_atencion_ciudadana_2024, df_Localidades, on="CVEGEO")
df_mesas_2024 = pd.merge(df_mesas_2024, df_Localidades, on="CVEGEO")
df_capacitaciones_2024 = pd.merge(df_capacitaciones_2024, df_Localidades, on="CVEGEO")

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
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Nombre Municipio:', 'Región:']),
).add_to(m)

# ---- Imagen inferior izquierda logo COESPO
from folium.plugins import FloatImage

LogoCOESPO = ('images/COESPO_Logo_3.png')
FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m)
# ---- Capas
layer_0 = FeatureGroup(name='Atención Ciudadana', show=False)
layer_1 = FeatureGroup(name='Mesas de Justicia', show=False)
layer_2 = FeatureGroup(name='Sesiones Ordinarias', show=False)

layer_3 = FeatureGroup(name='Mesas de Justicia 2022', show=False)
layer_4 = FeatureGroup(name='Capacitaciones 2022', show=False)

layer_5 = FeatureGroup(name='Mesas de Justicia 2023', show=False)
layer_6 = FeatureGroup(name='Atención Ciudadana 2023', show=False)
layer_7 = FeatureGroup(name='Capacitaciones 2023', show=False)

layer_8 = FeatureGroup(name='Mesas de Justicia 2024 (1er, 2do y 3er Trimestre)', show=False)
layer_9 = FeatureGroup(name='Atención Ciudadana 2024 (1er, 2do y 3er Trimestre)', show=False)
layer_10 = FeatureGroup(name='Capacitaciones 2024 (1er, 2do y 3er Trimestre)', show=False)



# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster

mc_0 = MarkerCluster()
mc_1 = MarkerCluster()
mc_2 = MarkerCluster()

mc_3 = MarkerCluster()
mc_4 = MarkerCluster()

mc_5 = MarkerCluster()
mc_6 = MarkerCluster()
mc_7 = MarkerCluster()

mc_8 = MarkerCluster()
mc_9 = MarkerCluster()
mc_10 = MarkerCluster()


def genera_tarjeta(df_in, mc):
    for row in df_in.itertuples():
        contenido = genera_contenido(str(row.MUNICIPIO), str(row.ACCION), str(row.NUM1),str(row.FECHA1),str(row.FOTO1),str(row.NUM2),str(row.FECHA2),str(row.FOTO2),str(row.NUM3),
                                     str(row.FECHA3),str(row.FOTO3),str(row. NUM4),str(row.FECHA4),str(row.FOTO4),str(row.NUM5),str(row.FECHA5),str(row.FOTO5),
                                     str(row.NUM6),str(row.FECHA6),str(row.FOTO6),str(row.NUM7),str(row.FECHA7),str(row.FOTO7),str(row.NUM8),str(row.FECHA8),str(row.FOTO8),
                                     str(row.NUM9),str(row.FECHA9),str(row.FOTO9),str(row.NUM10),str(row.FECHA10),str(row.FOTO10),str(row.NUM11),str(row.FECHA11),str(row.FOTO11),
                                     str(row.NUM12),str(row.FECHA12),str(row.FOTO12),str(row.NUM13),str(row.FECHA13),str(row.FOTO13),str(row.NUM14),str(row.FECHA14),str(row.FOTO14),
                                     str(row.NUM15),str(row.FECHA15),str(row.FOTO15),str(row.NUM16),str(row.FECHA16),str(row.FOTO16),str(row.NUM17),str(row.FECHA17),str(row.FOTO17),
                                     str(row. NUM18),str(row.FECHA18),str(row.FOTO18),str(row. NUM19),str(row.FECHA19),str(row.FOTO19),str(row.NUM20),str(row.FECHA20),str(row.FOTO20),
                                     str(row.NUM21),str(row.FECHA21),str(row.FOTO21),str(row.NUM22),str(row.FECHA22),str(row.FOTO22),str(row.NUM23),str(row.FECHA23),str(row.FOTO23),
                                     str(row.NUM24),str(row.FECHA24),str(row.FOTO24))
        icon_Dependencia = folium.features.CustomIcon('images/DGCSJP_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        popup = folium.Popup(html=contenido, max_width='290')
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc)

def genera_mesas_2022(df_in, mc):
    for row in df_in.itertuples():
        contenido = genera_contenidomesas_2022(str(row.MUNICIPIO), str(row.FECHA), str(row.DESCRIPCION),str(row.ASISTENTESH),str(row.ASISTENTESM),str(row.ASISTENTEST),str(row.FOTO1),str(row.FOTO2),str(row.VIDEO))
        icon_Dependencia = folium.features.CustomIcon('images/DGCSJP_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        popup = folium.Popup(html=contenido, max_width='290')
        folium.Marker(location=[row.LATITUD, row.LONGITUD], popup=popup, icon=icon_Dependencia).add_to(
            mc)

def genera_capacitaciones_2022(df_in, mc):
    for row in df_in.itertuples():
        contenido = genera_contenidocapacitaciones_2022(str(row.MUNICIPIO), str(row.FECHA), str(row.DESCRIPCION),str(row.ASISTENTESH),str(row.ASISTENTESM),str(row.ASISTENTEST),str(row.FOTO1),str(row.FOTO2),str(row.VIDEO))
        icon_Dependencia = folium.features.CustomIcon('images/DGCSJP_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        popup = folium.Popup(html=contenido, max_width='290')
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)


def genera_2023_2024(df_in, mc):
    for row in df_in.itertuples():
        contenido = tarjeta_genera_2023_2024(str(row.MUNICIPIO), str(row.FECHA), str(row.DESCRIPCION),str(row.ASISTENTESH),str(row.ASISTENTESM),str(row.ASISTENTEST),str(row.FOTO1),str(row.FOTO2),str(row.VIDEO))
        icon_Dependencia = folium.features.CustomIcon('images/DGCSJP_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        popup = folium.Popup(html=contenido, max_width='290')
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

genera_tarjeta(df_atencion_ciudadana, mc_0)
genera_tarjeta(df_mesas, mc_1)
genera_tarjeta(df_sesiones,mc_2)

genera_mesas_2022(df_mesas_2022, mc_3)
genera_capacitaciones_2022(df_capacitaciones_2022, mc_4)

genera_2023_2024(df_mesas_2023, mc_5)
genera_2023_2024(df_atencion_ciudadana_2023, mc_6)
genera_2023_2024(df_capacitaciones_2023, mc_7)

genera_2023_2024(df_mesas_2024, mc_8)
genera_2023_2024(df_atencion_ciudadana_2024, mc_9)
genera_2023_2024(df_capacitaciones_2024, mc_10)

mc_0.add_to(layer_0)
mc_1.add_to(layer_1)
mc_2.add_to(layer_2)
mc_3.add_to(layer_3)
mc_4.add_to(layer_4)
mc_5.add_to(layer_5)
mc_6.add_to(layer_6)
mc_7.add_to(layer_7)
mc_8.add_to(layer_8)
mc_9.add_to(layer_9)
mc_10.add_to(layer_10)

layer_1.add_to(m)
layer_2.add_to(m)
layer_3.add_to(m)
layer_4.add_to(m)
layer_5.add_to(m)
layer_6.add_to(m)
layer_7.add_to(m)
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

m.save("DGCSJP.html")
