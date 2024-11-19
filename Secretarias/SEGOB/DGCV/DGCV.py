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
# CARGA SHAPE CON DATOS PARA PINTAR MUNICIPIOS
df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
df['CVEGEO'] = df.apply(lambda row: row.CVE_ENT + row.CVE_MUN, axis=1)
df['CVEGEO'] = df['CVEGEO'].apply(pd.to_numeric, errors='coerce')
df_regiones = df
df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))

df.loc[df['region'] == 'Las_Montanas', 'region'] = 'Las Montañas'
df.loc[df['region'] == 'Huasteca_Alta', 'region'] = 'Huasteca Alta'
df.loc[df['region'] == 'Huasteca_Baja', 'region'] = 'Huasteca Baja'
df.loc[df['region'] == 'Los_Tuxtlas', 'region'] = 'Los Tuxtlas'

#2021 - 2023
df_directorio = pd.read_excel("DGCyV_OK.xlsx", sheet_name='DIRECTORIO')
df_delegaciones = pd.read_excel("DGCyV_OK.xlsx", sheet_name='DELEGACIONES')
df_digitalizaciones_2021_2023 = pd.read_excel("DGCyV_OK.xlsx", sheet_name='DIGITALIZACIONES')
df_capacitaciones_2021_2023 = pd.read_excel("DGCyV_OK.xlsx", sheet_name='CAPACITACIONES')
df_promociones_2021_2023 = pd.read_excel("DGCyV_OK.xlsx", sheet_name='PROMOCIONES')
df_supervisiones_2021_2023 = pd.read_excel("DGCyV_OK.xlsx", sheet_name='SUPERVISIONES')
df_avaluos_2021_2023 = pd.read_excel("DGCyV_OK.xlsx", sheet_name='AVALUOS')
df_dictamenes_2021_2023 = pd.read_excel("DGCyV_OK.xlsx", sheet_name='DICTAMENES')
df_convenios_2022_2023 = pd.read_excel("DGCyV_OK.xlsx", sheet_name='DICTAMENES')
df_tablas_2023 = pd.read_excel("DGCyV_OK.xlsx", sheet_name='TABLAS_VALORES')
df_levantamientos_2022_2023 = pd.read_excel("DGCyV_OK.xlsx", sheet_name='LEVANTAMIENTOS')

#2024
df_directorio_2024 = pd.read_excel("DGCV_2024.xlsx", sheet_name='DIRECTORIO')
#df_delegaciones_2024 = pd.read_excel("DGCV_2024.xlsx", sheet_name='DELEGACIONES')
df_digitalizaciones_2024 = pd.read_excel("DGCV_2024.xlsx", sheet_name='DIGITALIZACIONES')
df_capacitaciones_2024 = pd.read_excel("DGCV_2024.xlsx", sheet_name='CAPACITACIONES')
df_promociones_2024 = pd.read_excel("DGCV_2024.xlsx", sheet_name='PROMOCIONES')
df_supervisiones_2024 = pd.read_excel("DGCV_2024.xlsx", sheet_name='SUPERVISIONES')
df_convenios_2024 = pd.read_excel("DGCV_2024.xlsx", sheet_name='CONVENIOS')
df_tablas_2024 = pd.read_excel("DGCV_2024.xlsx", sheet_name='TABLAS_VALORES')
df_avaluos_2024 = pd.read_excel("DGCV_2024.xlsx", sheet_name='AVALUOS')
df_dictamenes_2024 = pd.read_excel("DGCV_2024.xlsx", sheet_name='DICTAMENES')
df_levantamientos_2024 = pd.read_excel("DGCV_2024.xlsx", sheet_name='LEVANTAMIENTOS')
df_tabla_valores_2024 = pd.read_excel("DGCV_2024.xlsx", sheet_name='TABLAS_VALORES')



df_digitalizaciones_2021_2023['ACTUALIZACION'] = df_digitalizaciones_2021_2023['ACTUALIZACION'].dt.strftime('%d/%m/%Y')
df_capacitaciones_2021_2023['ACTUALIZACION'] = df_capacitaciones_2021_2023['ACTUALIZACION'].dt.strftime('%d/%m/%Y')
df_promociones_2021_2023['ACTUALIZACION'] = df_promociones_2021_2023['ACTUALIZACION'].dt.strftime('%d/%m/%Y')
df_supervisiones_2021_2023['ACTUALIZACION'] = df_supervisiones_2021_2023['ACTUALIZACION'].dt.strftime('%d/%m/%Y')
df_avaluos_2021_2023['FECHA'] = df_avaluos_2021_2023['FECHA'].dt.strftime('%d/%m/%Y')
df_dictamenes_2021_2023['FECHA'] = df_dictamenes_2021_2023['FECHA'].dt.strftime('%d/%m/%Y')
#df_convenios_2022_2023['FECHA'] = df_convenios_2022_2023['FECHA'].dt.strftime('%d/%m/%Y')
df_tablas_2023['ACTUALIZACION'] = df_tablas_2023['ACTUALIZACION'].dt.strftime('%d/%m/%Y')
df_levantamientos_2022_2023['FECHA'] = df_levantamientos_2022_2023['FECHA'].dt.strftime('%d/%m/%Y')


df_digitalizaciones_2024['ACTUALIZACION'] = df_digitalizaciones_2024['ACTUALIZACION'].dt.strftime('%d/%m/%Y')
df_capacitaciones_2024['ACTUALIZACION'] = df_capacitaciones_2024['ACTUALIZACION'].dt.strftime('%d/%m/%Y')
df_promociones_2024['ACTUALIZACION'] = df_promociones_2024['ACTUALIZACION'].dt.strftime('%d/%m/%Y')
df_supervisiones_2024['ACTUALIZACION'] = df_supervisiones_2024['ACTUALIZACION'].dt.strftime('%d/%m/%Y')
df_convenios_2024['ACTUALIZACION'] = df_convenios_2024['ACTUALIZACION'].dt.strftime('%d/%m/%Y')
df_avaluos_2024['FECHA'] = df_avaluos_2024['FECHA'].dt.strftime('%d/%m/%Y')
df_dictamenes_2024['FECHA'] = df_dictamenes_2024['FECHA'].dt.strftime('%d/%m/%Y')
#df_levantamientos_2024['FECHA'] = df_dictamenes_2024['FECHA'].dt.strftime('%d/%m/%Y')
df_tabla_valores_2024['ACTUALIZACION'] = df_tabla_valores_2024['ACTUALIZACION'].dt.strftime('%d/%m/%Y')

df_directorio = pd.merge(df_directorio,df_Localidades, left_on="CVEGEO", right_on="CVEGEO")
# %% CAMBIAR TIPO DE STR A NUMERO PARA LATITUD Y LONGITUD
df_directorio['LAT'] = df_directorio['LAT'].apply(pd.to_numeric, errors='coerce')
df_directorio['LON'] = df_directorio['LON'].apply(pd.to_numeric, errors='coerce')

df_delegaciones = pd.merge(df, df_delegaciones, left_on="CVEGEO", right_on="CVEGEO")

# se agrega latitud longitud de los municipios
df_digitalizaciones_2021_2023 = pd.merge(df_digitalizaciones_2021_2023, df_Localidades, left_on="CVEGEO", right_on="CVEGEO")
df_capacitaciones_2021_2023 = pd.merge(df_capacitaciones_2021_2023, df_Localidades, left_on="CVEGEO", right_on="CVEGEO")
df_promociones_2021_2023 = pd.merge(df_promociones_2021_2023, df_Localidades, left_on="CVEGEO", right_on="CVEGEO")
df_supervisiones_2021_2023 = pd.merge(df_supervisiones_2021_2023, df_Localidades, left_on="CVEGEO", right_on="CVEGEO")
df_avaluos_2021_2023 = pd.merge(df_avaluos_2021_2023, df_Localidades, left_on="CVEGEO", right_on="CVEGEO")
df_dictamenes_2021_2023 = pd.merge(df_dictamenes_2021_2023, df_Localidades, left_on="CVEGEO", right_on="CVEGEO")
df_convenios_2022_2023 = pd.merge(df_convenios_2022_2023, df_Localidades, left_on="CVEGEO", right_on="CVEGEO")
df_tablas_2023 = pd.merge(df_tablas_2023, df_Localidades, left_on="CVEGEO", right_on="CVEGEO")
df_levantamientos_2022_2023 = pd.merge(df_levantamientos_2022_2023, df_Localidades, left_on="CVEGEO", right_on="CVEGEO")


df_digitalizaciones_2024 = pd.merge(df_digitalizaciones_2024, df_Localidades, left_on="CVEGEO", right_on="CVEGEO")
df_capacitaciones_2024 = pd.merge(df_capacitaciones_2024, df_Localidades, left_on="CVEGEO", right_on="CVEGEO")
df_promociones_2024 = pd.merge(df_promociones_2024, df_Localidades, left_on="CVEGEO", right_on="CVEGEO")
df_supervisiones_2024 = pd.merge(df_supervisiones_2024, df_Localidades, left_on="CVEGEO", right_on="CVEGEO")
df_convenios_2024 = pd.merge(df_convenios_2024, df_Localidades, left_on="CVEGEO", right_on="CVEGEO")
df_tablas_2024 = pd.merge(df_tablas_2024, df_Localidades, left_on="CVEGEO", right_on="CVEGEO")
df_avaluos_2024 = pd.merge(df_avaluos_2024, df_Localidades, left_on="CVEGEO", right_on="CVEGEO")
df_dictamenes_2024= pd.merge(df_dictamenes_2024, df_Localidades, left_on="CVEGEO", right_on="CVEGEO")
df_levantamientos_2024 = pd.merge(df_levantamientos_2024, df_Localidades, left_on="CVEGEO", right_on="CVEGEO")
df_tabla_valores_2024 = pd.merge(df_tabla_valores_2024, df_Localidades, left_on="CVEGEO", right_on="CVEGEO")



m = folium.Map(location=[19.8727, -96.1333], zoom_start=7, prefer_canvas=True, tiles='OpenStreetMap')

# ---- Mapa Base de Veracruz
colores = df_delegaciones.set_index("CVE_MUN")["COLOR_DEL"]

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
    df_delegaciones,
    name='Cobertura Delegaciones Catastrales',
    highlight_function=highlight,
    style_function=style_function,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'DELEGACION'],
                                           aliases=['Nombre Municipio:', 'Delegación Catastral:']),
).add_to(m)

# ---- Imagen inferior izquierda logo COESPO
from folium.plugins import FloatImage

FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m)
# ---- Capas

# layer_0 = FeatureGroup(name='Acciones 2020', show=False)
layer_0 = FeatureGroup(name='Directorio de Oficinas', show=False)
layer_digitalizacionesC_2021_2023 = FeatureGroup(name='Digitalizaciones de cartografía 2021 - 2023', show=False)
layer_digitalizacionesC_2024 = FeatureGroup(name='Digitalizaciones de cartografía 2024', show=False)
layer_capacitaciones_2021_2023 = FeatureGroup(name='Capacitaciones 2021 - 2023', show=False)
layer_capacitaciones_2024 = FeatureGroup(name='Capacitaciones 2024', show=False)
layer_promociones_2021_2023 = FeatureGroup(name='Promociones 2021 - 2023', show=False)
layer_promociones_2024 = FeatureGroup(name='Promociones 2024', show=False)
layer_superviciones_2021_2023 = FeatureGroup(name='Supervisiones 2021 - 2023', show=False)
layer_superviciones_2024 = FeatureGroup(name='Supervisiones 2024', show=False)
layer_avaluos_2021_2023 = FeatureGroup(name='Avalúos 2021 - 2023', show=False)
layer_avaluos_2024 = FeatureGroup(name='Avalúos 2024', show=False)
layer_dictamenesA_2021_2023 = FeatureGroup(name='Dictámenes de Arrendamiento 2021 - 2023', show=False)
layer_dictamenesA_2024 = FeatureGroup(name='Dictámenes de Arrendamiento 2024', show=False)
layer_levantamientos_2022_2023 = FeatureGroup(name='Levantamientos 2022 - 2023', show=False)
layer_levantamientos_2024 = FeatureGroup(name='Levantamientos 2024', show=False)
layer_convenios_2022_2023 = FeatureGroup(name='Convenios de Colaboración 2022 - 2023', show=False)
layer_convenios_2024 = FeatureGroup(name='Convenios de Colaboración 2024', show=False)
layer_tabla_valores_2023 = FeatureGroup(name='Tabla de Valores 2023', show=False)
layer_tabla_valores_2024 = FeatureGroup(name='Tabla de Valores 2024', show=False)

# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster

mc_0 = MarkerCluster()
mc_digitalizacionesC_2021_2023 = MarkerCluster()
mc_digitalizacionesC_2024 = MarkerCluster()
mc_capacitaciones_2021_2023 = MarkerCluster()
mc_capacitaciones_2024 = MarkerCluster()
mc_promociones_2021_2023 = MarkerCluster()
mc_promociones_2024 = MarkerCluster()
mc_superviciones_2021_2023 = MarkerCluster()
mc_superviciones_2024 = MarkerCluster()
mc_avaluos_2021_2023 = MarkerCluster()
mc_avaluos_2024 = MarkerCluster()
mc_dictamenesA_2021_2023 = MarkerCluster()
mc_dictamenesA_2024 = MarkerCluster()
mc_levantamientos_2022_2023 = MarkerCluster()
mc_levantamientos_2024 = MarkerCluster()
mc_convenios_2022_2023 = MarkerCluster()
mc_convenios_2024 = MarkerCluster()
mc_tabla_valores_2023 = MarkerCluster()
mc_tabla_valores_2024 = MarkerCluster()

pd.set_option('display.max_columns', None)
def genera_directorio(df_in):
    for row in df_in.itertuples():
        contenido = content_directorio(str(row.MUNICIPIO), str(row.DELEGACION),
                                       str(row.DIRECCION), str(row.DELEGADO), str(row.TEL),
                                       str(row.LAT), str(row.LON), str(row.FOTO))
        icon_Dependencia = folium.features.CustomIcon('images/DGCV_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        popup = folium.Popup(html=contenido)
        folium.Marker(location=[row.LAT, row.LON], popup=popup, icon=icon_Dependencia).add_to(
            mc_0)

genera_directorio(df_directorio)

def genera(df_in, mc, capa):
    for row in df_in.itertuples():
        contenido = ""
        if capa == "digitalizaciones":
            contenido = genera_digitalizaciones(str(row.MUNICIPIO), str(row.DELEGACION), str(row.ACTUALIZACION),
                                                str(row.ACCION),
                                                str(row.DIGITALIZACIONES),
                                                str(row.FOTO))

        elif capa == "capacitaciones":
            contenido = genera_capacitaciones(str(row.MUNICIPIO), str(row.DELEGACION), str(row.FECHA), str(row.ACCION),
                                              str(row.SPB), str(row.ACTUALIZACION), str(row.FOTO))
        elif capa == "promociones":
            contenido = genera_promociones(str(row.MUNICIPIO), str(row.DELEGACION), str(row.FECHA), str(row.ACCION),
                                           str(row.ASESORIAS), str(row.ACTUALIZACION), str(row.FOTO))
        elif capa == "supervisiones":
            contenido = genera_supervisiones(str(row.MUNICIPIO), str(row.DELEGACION), str(row.FECHA), str(row.ACCION),
                                             str(row.SUPERVISIONES), str(row.ACTUALIZACION), str(row.FOTO))
        elif capa == "convenios":
            contenido = genera_convenios(str(row.MUNICIPIO), str(row.DELEGACION), str(row.FECHA), str(row.ACCION),
                                             str(row.CONVENIOS), str(row.ACTUALIZACION), str(row.FOTO))
        elif capa == "tablas":
            contenido = genera_tablas(str(row.MUNICIPIO), str(row.DELEGACION), str(row.ACCION),
                                      str(row.ASESORIAS), str(row.ACTUALIZACION), str(row.FOTO))
        elif capa == "avaluos":
            contenido = genera_avaluos(str(row.MUNICIPIO), str(row.DELEGACION), str(row.ACCION),
                                      str(row.NUM), str(row.BENEFICIADOS), str(row.FECHA), str(row.FOTO))
        elif capa == "dictamenes":
            contenido = genera_avaluos(str(row.MUNICIPIO), str(row.DELEGACION), str(row.ACCION),
                                      str(row.NUM), str(row.BENEFICIADOS), str(row.FECHA), str(row.FOTO))
        elif capa == "levantamientos":
            contenido = genera_levantamientos(row)

        elif capa == "tablavalores":
            contenido = genera_tablavalores(str(row.MUNICIPIO), str(row.DELEGACION),
                                                str(row.ACCION),
                                                str(row.ACTUALIZACION),
                                                str(row.FOTO))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/DGCV_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

# genera(df2021)
genera(df_digitalizaciones_2021_2023, mc_digitalizacionesC_2021_2023, "digitalizaciones")
genera(df_capacitaciones_2021_2023, mc_capacitaciones_2021_2023, "capacitaciones")
genera(df_promociones_2021_2023, mc_promociones_2021_2023, "promociones")
genera(df_supervisiones_2021_2023, mc_superviciones_2021_2023, "supervisiones")
genera(df_avaluos_2021_2023, mc_avaluos_2021_2023, "avaluos")
genera(df_dictamenes_2021_2023, mc_dictamenesA_2021_2023, "dictamenes")
genera(df_convenios_2022_2023, mc_convenios_2022_2023, "dictamenes")
genera(df_tablas_2023, mc_tabla_valores_2023, "tablas")
genera(df_levantamientos_2022_2023, mc_levantamientos_2022_2023, "levantamientos")


# genera(df2024)
genera(df_digitalizaciones_2024, mc_digitalizacionesC_2024, "digitalizaciones")
genera(df_capacitaciones_2024, mc_capacitaciones_2024, "capacitaciones")
genera(df_promociones_2024, mc_promociones_2024, "promociones")
genera(df_supervisiones_2024, mc_superviciones_2024, "supervisiones")
genera(df_tablas_2024, mc_tabla_valores_2024, "tablas")
genera(df_avaluos_2024, mc_avaluos_2024, "avaluos")
genera(df_dictamenes_2024, mc_dictamenesA_2024, "dictamenes")
genera(df_levantamientos_2024, mc_levantamientos_2024, "levantamientos")
genera(df_convenios_2024, mc_convenios_2024, "convenios")
genera(df_tabla_valores_2024, mc_tabla_valores_2024, "tablavalores")

mc_0.add_to(layer_0)
mc_digitalizacionesC_2021_2023.add_to(layer_digitalizacionesC_2021_2023)
mc_digitalizacionesC_2024.add_to(layer_digitalizacionesC_2024)
mc_capacitaciones_2021_2023.add_to(layer_capacitaciones_2021_2023)
mc_capacitaciones_2024.add_to(layer_capacitaciones_2024)
mc_promociones_2021_2023.add_to(layer_promociones_2021_2023)
mc_promociones_2024.add_to(layer_promociones_2024)
mc_superviciones_2021_2023.add_to(layer_superviciones_2021_2023)
mc_superviciones_2024.add_to(layer_superviciones_2024)
mc_avaluos_2021_2023.add_to(layer_avaluos_2021_2023)
mc_avaluos_2024.add_to(layer_avaluos_2024)
mc_dictamenesA_2021_2023.add_to(layer_dictamenesA_2021_2023)
mc_dictamenesA_2024.add_to(layer_dictamenesA_2024)
mc_levantamientos_2022_2023.add_to(layer_levantamientos_2022_2023)
mc_levantamientos_2024.add_to(layer_levantamientos_2024)
mc_convenios_2022_2023.add_to(layer_convenios_2022_2023)
mc_convenios_2024.add_to(layer_convenios_2024)
mc_tabla_valores_2023.add_to(layer_tabla_valores_2023)
mc_tabla_valores_2024.add_to(layer_tabla_valores_2024)

layer_0.add_to(m)
layer_digitalizacionesC_2021_2023.add_to(m)
layer_digitalizacionesC_2024.add_to(m)
layer_capacitaciones_2021_2023.add_to(m)
layer_capacitaciones_2024.add_to(m)
layer_promociones_2021_2023.add_to(m)
layer_promociones_2024.add_to(m)
layer_superviciones_2021_2023.add_to(m)
layer_superviciones_2024.add_to(m)
layer_avaluos_2021_2023.add_to(m)
layer_avaluos_2024.add_to(m)
layer_dictamenesA_2021_2023.add_to(m)
layer_dictamenesA_2024.add_to(m)
#layer_levantamientos_2021.add_to(m)
layer_levantamientos_2022_2023.add_to(m)
layer_levantamientos_2024.add_to(m)
layer_convenios_2022_2023.add_to(m)
layer_convenios_2024.add_to(m)
layer_tabla_valores_2023.add_to(m)
layer_tabla_valores_2024.add_to(m)

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
m.save("DGCV.html")
