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

#libreria para graficos
import matplotlib.pyplot as plt

#Declaración del estilo de metplotlib
plt.style.use("bmh")

# %%
#path_ini = Path("C:/ESyP/Mapas_COESPO/Resources/")
path_ini = Path("/Users/4x/COESPOAX/MapasTematicos/Resources/")

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
df_actividades = pd.read_excel("INVEDEM_OK.xlsx", sheet_name='ACTIVIDADES')
df_oficinas = pd.read_excel("INVEDEM_OK.xlsx", sheet_name='OFICINAS')

df_actividades = pd.merge(df_actividades, df_Localidades, on="CVEGEO")
df_oficinas = pd.merge(df_oficinas, df_Localidades, on="CVEGEO")

#df_asesorias['SOLICITUDES'] = df_asesorias['SOLICITUDES'].astype(np.int64)

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
    #print(color)
    #color=color.to_json()
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
layer_oficinas = FeatureGroup(name='Directorio de Oficinas', show=False)
layer_capacitacion = FeatureGroup(name='Capacitaciones y Talleres', show=False)
layer_reuniones = FeatureGroup(name='Reuniones', show=False)
layer_revistas = FeatureGroup(name='Publicaciones de revistas', show=False)
layer_sesiones = FeatureGroup(name='Sesiones Virtuales', show=False)
layer_programastv = FeatureGroup(name='Programas de TV', show=False)
layer_otros = FeatureGroup(name='Otras Actividades', show=False)

#Definimos marcadores de las actividades
from folium.plugins import MarkerCluster
mc_oficinas=MarkerCluster()
mc_capacitacion = MarkerCluster()
mc_reuniones = MarkerCluster()
mc_revista = MarkerCluster()
mc_sesiones = MarkerCluster()
mc_programastv = MarkerCluster()
mc_otros = MarkerCluster()

#Definiendo la función para la llamada de datos
def genera_oficinas(df_in, mc):
    # df['Value'] = df.apply(lambda x: "{:,}".format(x['Value']), axis=1)
    for row in df_in.itertuples():
        contenido = tarjeta_oficinas(row)

        popup = folium.Popup(html=contenido, max_width='400')
        icon_Dependencia = folium.features.CustomIcon('images/INVEDEM_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.LAT, row.LON], popup=popup, icon=icon_Dependencia).add_to(
            mc)


def genera_actividades(df_in):

    for row in df_in.itertuples():
        mc = MarkerCluster()
        if row.CAPA=="CAPACITACION":
            mc = mc_capacitacion
        if row.CAPA=="REUNIONES":
            mc = mc_reuniones
        if row.CAPA=="REVISTA":
            mc = mc_revista
        if row.CAPA=="SESIONES VIRTUALES":
            mc = mc_sesiones
        if row.CAPA=="PROGRAMATV":
            mc = mc_programastv
        if row.CAPA=="OTROS":
            mc = mc_otros

        contenidototal = tarjeta_actividades(row)

        popup = folium.Popup(html=contenidototal, max_width='300')
        #Icono de prueba
        icon_Dependencia = folium.features.CustomIcon('images/INVEDEM_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc)


genera_oficinas(df_oficinas,mc_oficinas)
genera_actividades(df_actividades)

mc_oficinas.add_to(layer_oficinas)
mc_capacitacion.add_to(layer_capacitacion)
mc_reuniones.add_to(layer_reuniones)
mc_revista.add_to(layer_revistas)
mc_sesiones.add_to(layer_sesiones)
mc_programastv.add_to(layer_programastv)
mc_otros.add_to(layer_otros)


#Agregamos layers al mapa
layer_oficinas.add_to(m3)
layer_capacitacion.add_to(m3)
layer_reuniones.add_to(m3)
layer_revistas.add_to(m3)
layer_sesiones.add_to(m3)
layer_programastv.add_to(m3)
layer_otros.add_to(m3)

folium.LayerControl(collapsed=False).add_to(m3)
m3.save('INVEDEM2.html')
