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
from FuncionesPoblacion import *
from folium import FeatureGroup, LayerControl, Map, Marker

# %%
path_ini = Path("C:/ESyP/Mapas_COESPO/Resources/")
#path_ini = Path("/Users/4x/COESPOAX/MapasTematicos/Resources/")

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
df_traslado = pd.read_excel("DGAM_OK.xlsx", sheet_name='TRASLADO DE PERSONAS')
df_actas = pd.read_excel("DGAM_OK.xlsx", sheet_name='GESTION DE ACTAS DE R.C.')
df_constancia = pd.read_excel("DGAM_OK.xlsx", sheet_name='CONTANCIA DE IDENTIDAD')
df_localizacion = pd.read_excel("DGAM_OK.xlsx", sheet_name='LOCALIZACION DE PERSONAS')
df_detenidos = pd.read_excel("DGAM_OK.xlsx", sheet_name='DETENIDOS')
df_asesorias = pd.read_excel("DGAM_OK.xlsx", sheet_name='ASESORIAS RAICES VERACRUZANAS')
df_centroamericanos = pd.read_excel("DGAM_OK.xlsx", sheet_name='MIGRANTES CENTROAMERICANOS')
df_albergues = pd.read_excel("DGAM_OK.xlsx", sheet_name='ALBERGUES Y COMEDORES')
df_reunificaciones = pd.read_excel("DGAM_OK.xlsx", sheet_name='REUNIFICACION')
df_pasaportes = pd.read_excel("DGAM_OK.xlsx", sheet_name='PASAPORTES')


df_traslado = pd.merge(df_traslado,df_Localidades,on="CVEGEO")
df_actas = pd.merge(df_actas,df_Localidades,on="CVEGEO")
df_constancia = pd.merge(df_constancia,df_Localidades,on="CVEGEO")
df_localizacion = pd.merge(df_localizacion,df_Localidades,on="CVEGEO")
df_detenidos = pd.merge(df_detenidos,df_Localidades,on="CVEGEO")
df_asesorias = pd.merge(df_asesorias,df_Localidades,on="CVEGEO")
df_asesorias['SOLICITUDES'] = df_asesorias['SOLICITUDES'].astype(np.int64)

df_centroamericanos = pd.merge(df_centroamericanos,df_Localidades,on="CVEGEO")
df_albergues = pd.merge(df_albergues,df_Localidades,on="CVEGEO")
df_reunificaciones = pd.merge(df_reunificaciones,df_Localidades,on="CVEGEO")
df_pasaportes = pd.merge(df_pasaportes,df_Localidades,on="CVEGEO")

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
layer_albergues = FeatureGroup(name='Albergues y Comedores 2021 - 2022',show=False)
layer_asesorias = FeatureGroup(name='Asesorías Raíces Veracruzanas 2021',show=False)
layer_constancia = FeatureGroup(name='Constancia de Identidad 2021 - 2022',show=False)
layer_actas = FeatureGroup(name='Gestión de Actas Reg. Civil 2021 - 2024',show=False)
layer_localizacion = FeatureGroup(name='Localización de Personas 2021 - 2024',show=False)
layer_centroamericanos = FeatureGroup(name='Migrantes Centroamericanos 2021 - 2024',show=False)
layer_detenidos = FeatureGroup(name='Migrantes Detenidos 2021 - 2024',show=False)
layer_traslado = FeatureGroup(name='Traslado de Personas 2021 - 2024',show=False)
layer_reunificaciones = FeatureGroup(name='Reunificación Familiar 2022 - 2024',show=False)
layer_pasaportes = FeatureGroup(name='Pasaportes 2022 - 2024',show=False)

#Definimos marcadores de las actividades
from folium.plugins import MarkerCluster
mc_traslado = MarkerCluster()
mc_actas = MarkerCluster()
mc_constancia = MarkerCluster()
mc_localizacion = MarkerCluster()
mc_detenidos = MarkerCluster()
mc_asesorias = MarkerCluster()
mc_centroamericanos = MarkerCluster()
mc_albergues = MarkerCluster()
mc_reunificaciones = MarkerCluster()
mc_pasaportes = MarkerCluster()

#Definiendo la función para la llamada de datos
def genera(df_in,mc):
    for row in df_in.itertuples():
        contenidototal = genera_contenido(str(row.MUNICIPIO),str(row.DESCRIPCION),str(row.SOLICITUDES),str(row.ANIO))

        popup = folium.Popup(html=contenidototal, max_width='290')
        #Icono de prueba
        icon_Dependencia = folium.features.CustomIcon('images/DGAM_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc)

def genera_albergues(df_in,mc):
    for row in df_in.itertuples():
        contenido = contenido_albergue(str(row.MUNICIPIO),str(row.FOTO),str(row.NOMBRE),str(row.DIRECCION),str(row.TELEFONO),str(row.CORREO),str(row.PAGINA),str(row.FACEBOOK),str(row.DESCRIPCION))

        popup = folium.Popup(html=contenido, max_width='290')
        #Icono de prueba
        icon_Dependencia = folium.features.CustomIcon('images/DGAM_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.LAT, row.LON], popup=popup, icon=icon_Dependencia).add_to(
                mc)

#print(df_asesorias.dtypes)
genera_albergues(df_albergues,mc_albergues)
genera(df_asesorias,mc_asesorias)
genera(df_constancia,mc_constancia)
genera(df_actas,mc_actas)
genera(df_localizacion,mc_localizacion)
genera(df_centroamericanos,mc_centroamericanos)
genera(df_detenidos,mc_detenidos)
genera(df_traslado,mc_traslado)
genera(df_reunificaciones,mc_reunificaciones)
genera(df_pasaportes,mc_pasaportes)

mc_albergues.add_to(layer_albergues)
mc_asesorias.add_to(layer_asesorias)
mc_constancia.add_to(layer_constancia)
mc_actas.add_to(layer_actas)
mc_localizacion.add_to(layer_localizacion)
mc_centroamericanos.add_to(layer_centroamericanos)
mc_detenidos.add_to(layer_detenidos)
mc_traslado.add_to(layer_traslado)
mc_reunificaciones.add_to(layer_reunificaciones)
mc_pasaportes.add_to(layer_pasaportes)

#Agregamos layers al mapa
layer_albergues.add_to(m3)
layer_asesorias.add_to(m3)
layer_constancia.add_to(m3)
layer_actas.add_to(m3)
layer_localizacion.add_to(m3)
layer_centroamericanos.add_to(m3)
layer_detenidos.add_to(m3)
layer_traslado.add_to(m3)
layer_reunificaciones.add_to(m3)
layer_pasaportes.add_to(m3)

folium.LayerControl(collapsed=False).add_to(m3)
m3.save('DGAM.html')
