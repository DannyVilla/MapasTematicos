import folium
import pandas as pd
import geopandas as gpd
from geopandas import GeoDataFrame
from folium.plugins import Search
import branca
import numpy as np
from pathlib import Path
import array as arr
from numpy import int64
from Funciones import *
from folium import FeatureGroup, LayerControl, Map, Marker


# %%
path_ini = Path("C:/ESyP/Mapas_COESPO/Resources/")
#path_ini = Path("/Users/4x/COESPOAX/MapasTematicos/Resources/")º

pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('display.max_columns', None)

# %%  IMAGEN FLOTANTE
LogoCOESPO = ('images/COESPO_Logo_3.png')
#Lectura de dataframes
df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
df['CVEGEO']=df['CVE_ENT']+df['CVE_MUN']
df['CVEGEO']=df['CVEGEO'].astype(int64)
df_regiones = df

#Excel de localidades
df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))
#EXCEL con datos para las capas
df_capacitacion_2022 = pd.read_excel("AGEV_OK.xlsx", sheet_name='capacitacion')
df_difusion_2022 = pd.read_excel("AGEV_OK.xlsx", sheet_name='difusion')
df_asesoria_2022 = pd.read_excel("AGEV_OK.xlsx", sheet_name='asesoria')
df_archivos_2022 = pd.read_excel("AGEV_OK.xlsx", sheet_name='archivos')

df_capacitacion_2023 = pd.read_excel("AGEV_OK.xlsx", sheet_name='CAPACITACION_2023')
df_difusion_2023 = pd.read_excel("AGEV_OK.xlsx", sheet_name='DIFUSION_2023')
df_asesoria_2023 = pd.read_excel("AGEV_OK.xlsx", sheet_name='ASESORIA_2023')
df_archivos_2023 = pd.read_excel("AGEV_OK.xlsx", sheet_name='ARCHIVOS_2023')

df_capacitacion_2024 = pd.read_excel("AGEV_OK.xlsx", sheet_name='CAPACITACION_2024')
df_difusion_2024 = pd.read_excel("AGEV_OK.xlsx", sheet_name='DIFUSION_2024')
df_asesoria_2024 = pd.read_excel("AGEV_OK.xlsx", sheet_name='ASESORIA_2024')
df_archivos_2024 = pd.read_excel("AGEV_OK.xlsx", sheet_name='ARCHIVOS_2024')

df_capacitacion_2022 = pd.merge(df_capacitacion_2022, df_Localidades, on="CVEGEO")
df_difusion_2022 = pd.merge(df_difusion_2022, df_Localidades, on="CVEGEO")
df_asesoria_2022 = pd.merge(df_asesoria_2022, df_Localidades, on="CVEGEO")
df_archivos_2022 = pd.merge(df_archivos_2022, df_Localidades, on="CVEGEO")

df_capacitacion_2023 = pd.merge(df_capacitacion_2023, df_Localidades, on="CVEGEO")
df_difusion_2023 = pd.merge(df_difusion_2023, df_Localidades, on="CVEGEO")
df_asesoria_2023 = pd.merge(df_asesoria_2023, df_Localidades, on="CVEGEO")
df_archivos_2023 = pd.merge(df_archivos_2023, df_Localidades, on="CVEGEO")

df_capacitacion_2024 = pd.merge(df_capacitacion_2024, df_Localidades, on="CVEGEO")
df_difusion_2024 = pd.merge(df_difusion_2024, df_Localidades, on="CVEGEO")
df_asesoria_2024 = pd.merge(df_asesoria_2024, df_Localidades, on="CVEGEO")
df_archivos_2024 = pd.merge(df_archivos_2024, df_Localidades, on="CVEGEO")

#df_asesoria_2022s['SOLICITUDES'] = df_asesoria_2022s['SOLICITUDES'].astype(np.int64)

df.loc[df['region'] == 'Las_Montanas', 'region'] = 'Las Montañas'
df.loc[df['region'] == 'Huasteca_Alta', 'region'] = 'Huasteca Alta'
df.loc[df['region'] == 'Huasteca_Baja', 'region'] = 'Huasteca Baja'
df.loc[df['region'] == 'Los_Tuxtlas', 'region'] = 'Los Tuxtlas'

#Se ajustan nombre de la región para desplegar
df_regiones.loc[df_regiones['region'] == 'Las_Montanas', 'region'] = 'Las Montañas'
df_regiones.loc[df_regiones['region'] == 'Huasteca_Alta', 'region'] = 'Huasteca Alta'
df_regiones.loc[df_regiones['region'] == 'Huasteca_Baja', 'region'] = 'Huasteca Baja'
df_regiones.loc[df_regiones['region'] == 'Los_Tuxtlas', 'region'] = 'Los Tuxtlas'
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

#Se definen colores para cada region
df_regiones.loc[df_regiones['region'] == 'Capital', ['Color']] = '#e8694b'
df_regiones.loc[df_regiones['region'] == 'Huasteca Alta', ['Color']] = '#7cd5a3'
df_regiones.loc[df_regiones['region'] == 'Huasteca Baja', ['Color']] = '#96B921'
df_regiones.loc[df_regiones['region'] == 'Los_Tuxtla', ['Color']] = '#5bbdbf'
df_regiones.loc[df_regiones['region'] == 'Nautla', ['Color']] = '#FDAF3F'
df_regiones.loc[df_regiones['region'] == 'Los Tuxtlas', ['Color']] = '#5bbdbf'
df_regiones.loc[df_regiones['region'] == 'Olmeca', ['Color']] = '#4f46FF'
df_regiones.loc[df_regiones['region'] == 'Papaloapan', ['Color']] = '#846789'
df_regiones.loc[df_regiones['region'] == 'Sotavento', ['Color']] = '#6e79c1'
df_regiones.loc[df_regiones['region'] == 'Totonaca', ['Color']] = '#D0D108'
df_regiones.loc[df_regiones['region'] == 'Las Montañas', ['Color']] = '#f3b8df'

# ---Mapa
from folium.plugins import MarkerCluster
m3 = folium.Map([19.5426, -96.91], zoom_start=7, prefer_canvas=True, titles='OpenStreetMap')

colores = df_regiones.set_index("CVE_MUN")["Color"]

def colorscale(color):
    return '"'+color+'"'

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

from folium.plugins import FloatImage
FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m3)

# ---Mapa del Estado de Veracruz
mapa = folium.GeoJson(
    df_regiones,
    name='Regiones',
    highlight_function=highlight,
    control=False,
    style_function=style_function, tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Nombre Municipio:', 'Región:']),
).add_to(m3)

statesearch = Search(
     layer=mapa,
     geom_type='Polygon',
     placeholder='Búsqueda de municipio',
     collapsed=False,
     search_label='NOM_MUN',
     weight=5
).add_to(m3)

#Definimos los layers
layer_capacitacion_2022 = FeatureGroup(name='Acciones de Capacitación 2022', show=False)
layer_difusion_2022 = FeatureGroup(name='Actividades de Difusión 2022', show=False)
layer_asesoria_2022 = FeatureGroup(name='Asesorías Brindadas 2022', show=False)
layer_archivo_2022 = FeatureGroup(name='Creación de Archivos 2022', show=False)
layer_capacitacion_2023 = FeatureGroup(name='Acciones de Capacitación 2023', show=False)
layer_difusion_2023 = FeatureGroup(name='Actividades de Difusión 2023', show=False)
layer_asesoria_2023 = FeatureGroup(name='Asesorías Brindadas 2023', show=False)
layer_archivo_2023 = FeatureGroup(name='Creación de Archivos 2023', show=False)
layer_capacitacion_2024 = FeatureGroup(name='Acciones de Capacitación 2024', show=False)
layer_difusion_2024 = FeatureGroup(name='Actividades de Difusión 2024', show=False)
layer_asesoria_2024 = FeatureGroup(name='Asesorías Brindadas 2024', show=False)
layer_archivo_2024 = FeatureGroup(name='Creación de Archivos 2024', show=False)

#Definimos marcadores de las actividades
from folium.plugins import MarkerCluster
mc_capacitacion_2022 = MarkerCluster()
mc_difusion_2022 = MarkerCluster()
mc_asesoria_2022 = MarkerCluster()
mc_archivo_2022 = MarkerCluster()
mc_capacitacion_2023 = MarkerCluster()
mc_difusion_2023 = MarkerCluster()
mc_asesoria_2023 = MarkerCluster()
mc_archivo_2023 = MarkerCluster()
mc_capacitacion_2024 = MarkerCluster()
mc_difusion_2024 = MarkerCluster()
mc_asesoria_2024 = MarkerCluster()
mc_archivo_2024 = MarkerCluster()


#Definiendo la función para la llamada de datos
def genera(df_in,mc):
    for row in df_in.itertuples():
        contenidototal = genera_contenido(str(row.MUNICIPIO),str(row.PROGRAMA),str(row.DESCRIPCION),str(row.CANTIDAD),str(row.FOTO))
        popup = folium.Popup(html=contenidototal, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/AGE_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc)

def genera_archivo(df_in,mc):
    for row in df_in.itertuples():

        contenido = genera_tarjeta_archivos(str(row.MUNICIPIO),str(row.PROGRAMA),str(row.FOTO))
        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/AGE_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc)


#--------------2022---------------------
genera(df_capacitacion_2022, mc_capacitacion_2022)
genera(df_difusion_2022, mc_difusion_2022)
genera(df_asesoria_2022, mc_asesoria_2022)
genera_archivo(df_archivos_2022, mc_archivo_2022)

mc_capacitacion_2022.add_to(layer_capacitacion_2022)
mc_difusion_2022.add_to(layer_difusion_2022)
mc_asesoria_2022.add_to(layer_asesoria_2022)
mc_archivo_2022.add_to(layer_archivo_2022)


#Agregamos layers al mapa
layer_capacitacion_2022.add_to(m3)
layer_difusion_2022.add_to(m3)
layer_asesoria_2022.add_to(m3)
layer_archivo_2022.add_to(m3)

#-----------2023------------
genera(df_capacitacion_2023, mc_capacitacion_2023)
genera(df_difusion_2023, mc_difusion_2023)
genera(df_asesoria_2023, mc_asesoria_2023)
genera_archivo(df_archivos_2023, mc_archivo_2023)

mc_capacitacion_2023.add_to(layer_capacitacion_2023)
mc_difusion_2023.add_to(layer_difusion_2023)
mc_asesoria_2023.add_to(layer_asesoria_2023)
mc_archivo_2023.add_to(layer_archivo_2023)


#-----------2024------------
genera(df_capacitacion_2024, mc_capacitacion_2024)
genera(df_difusion_2024, mc_difusion_2024)
genera(df_asesoria_2024, mc_asesoria_2024)
genera_archivo(df_archivos_2024, mc_archivo_2024)

mc_capacitacion_2024.add_to(layer_capacitacion_2024)
mc_difusion_2024.add_to(layer_difusion_2024)
mc_asesoria_2024.add_to(layer_asesoria_2024)
mc_archivo_2024.add_to(layer_archivo_2024)


#Agregamos layers al mapa
layer_capacitacion_2023.add_to(m3)
layer_difusion_2023.add_to(m3)
layer_asesoria_2023.add_to(m3)
layer_archivo_2023.add_to(m3)

layer_capacitacion_2024.add_to(m3)
layer_difusion_2024.add_to(m3)
layer_asesoria_2024.add_to(m3)
layer_archivo_2024.add_to(m3)

folium.LayerControl(collapsed=False).add_to(m3)
m3.save('AGEV.html')
