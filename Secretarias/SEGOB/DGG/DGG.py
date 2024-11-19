    import folium
import pandas as pd
import geopandas as gpd
from folium.plugins import Search
from pathlib import Path
from numpy import int64
from Funciones import *
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
df_oficinas = pd.read_excel("DIRECTORIO_OFICINAS_OK.xlsx", sheet_name='OFICINAS')
df_SCP_2021_2023 = pd.read_excel("REUNIONES_OK.xlsx", sheet_name='SCP_2021_2023')
df_reuniones_2024 = pd.read_excel("REUNIONES_OK.xlsx", sheet_name='SCP_2024')
df_tram_scp_2021_2023 = pd.read_excel("TRAMITES_OK.xlsx", sheet_name='SCP_2021_2023')
df_tram_scp_2024 = pd.read_excel("TRAMITES_OK.xlsx", sheet_name='SCP_2024')
df_tram_sac_2021_2023 = pd.read_excel("TRAMITES_OK.xlsx", sheet_name='SAC_2021_2023')
df_tram_sac_2024 = pd.read_excel("TRAMITES_OK.xlsx", sheet_name='SAC_2024')
df_tram_slyp_2021_2023 = pd.read_excel("TRAMITES_OK.xlsx", sheet_name='SLYP_2021_2023')
df_tram_slyp_2024 = pd.read_excel("TRAMITES_OK.xlsx", sheet_name='SLPY_2024')

df_SCP_2021_2023 = pd.merge(df_SCP_2021_2023, df_Localidades, on="CVEGEO")
df_reuniones_2024 = pd.merge(df_reuniones_2024,df_Localidades,on="CVEGEO")
df_tram_scp_2021_2023 = pd.merge(df_tram_scp_2021_2023, df_Localidades, on="CVEGEO")
df_tram_scp_2024 = pd.merge(df_tram_scp_2024,df_Localidades,on="CVEGEO")
df_tram_sac_2021_2023 = pd.merge(df_tram_sac_2021_2023, df_Localidades, on="CVEGEO")
df_tram_sac_2024 = pd.merge(df_tram_sac_2024,df_Localidades,on="CVEGEO")
df_tram_slyp_2021_2023 = pd.merge(df_tram_slyp_2021_2023, df_Localidades, on="CVEGEO")
df_tram_slyp_2024 = pd.merge(df_tram_slyp_2024,df_Localidades,on="CVEGEO")

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
layer_oficinas = FeatureGroup(name='Directorio de Oficinas (Actualización 2024)',show=False)
layer_reuniones_2021_2023 = FeatureGroup(name='Reuniones realizadas 2021 - 2023', show=False)
layer_reuniones_2024 = FeatureGroup(name='Reuniones realizadas 2024 (1er y 2do Trimestre)',show=False)
layer_tramites_scp_2021_2023 = FeatureGroup(name='Trámites Subdirección de Concertación Política 2021 - 2023', show=False)
layer_tramites_scp_2024 = FeatureGroup(name='Trámites Subdirección de Concertación Política 2024 (1er y 2do Trimestre)',show=False)
layer_tramites_sac_2021_2023 = FeatureGroup(name='Trámites Subdireción de Atención Ciudadana 2021 - 2023', show=False)
layer_tramites_sac_2024 = FeatureGroup(name='Trámites Subdireción de Atención Ciudadana 2024 (1er y 2do Trimestre)',show=False)
layer_tramites_slyp_2021_2023 = FeatureGroup(name='Trámites Subdirección de Legalización y Permisos 2021 - 2023', show=False)
layer_tramites_slyp_2024 = FeatureGroup(name='Trámites Subdirección de Legalización y Permisos 2024 (1er y 2do Trimestre)',show=False)

#Definimos marcadores de las actividades
from folium.plugins import MarkerCluster
mc_oficinas = MarkerCluster()
mc_reuniones_2021_2023 = MarkerCluster()
mc_reuniones_2024 = MarkerCluster()
mc_tramites_scp_2021_2023 = MarkerCluster()
mc_tramites_scp_2024 = MarkerCluster()
mc_tramites_sac_2021_2023 = MarkerCluster()
mc_tramites_sac_2024 = MarkerCluster()
mc_tramites_slyp_2021_2023 = MarkerCluster()
mc_tramites_slyp_2024 = MarkerCluster()

#Definiendo la función para la llamada de datos
def genera_reuniones(df_in,mc, anio):
    for row in df_in.itertuples():
        contenidototal = genera_cont_reuniones(str(row.MUNICIPIO),str(row.REUNIONES),str(row.FECHA),str(row.DESCRIPCION),str(row.FOTO1),str(row.FOTO2), anio)

        popup = folium.Popup(html=contenidototal, max_width='290')
        #Icono de prueba
        icon_Dependencia = folium.features.CustomIcon('images/DGG_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc)

def genera_oficinas(df_in,mc):
    for row in df_in.itertuples():
        contenido = contenido_oficina(str(row.MUNICIPIO),str(row.ENCARGADO), str(row.AREA),str(row.FOTO),str(row.DIRECCION),str(row.TELEFONO))

        popup = folium.Popup(html=contenido, max_width='290')
        #Icono de prueba
        icon_Dependencia = folium.features.CustomIcon('images/DGG_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.LATITUD, row.LONGITUD], popup=popup, icon=icon_Dependencia).add_to(
                mc)


def genera_tramites(df_in,mc, anio):
    for row in df_in.itertuples():
        contenido = contenido_tramites(str(row.MUNICIPIO),str(row.DESCRIPCION),str(row.INF),str(row.GES_LAB),
                                       str(row.PROG_SOC),str(row.SIND),str(row.VIV),str(row.REGU),str(row.AGRA),
                                       str(row.TRANS),str(row.ELEC),str(row.SALUD ),str(row.MED_AMB),str(row.AGUA),
                                       str(row.EDU),str(row.SSP),str(row.OTROS ),str(row.TOTAL),str(row.FOTO1),
                                       str(row.FOTO2), anio)

        popup = folium.Popup(html=contenido, max_width='290')
        #Icono del marcador
        icon_Dependencia = folium.features.CustomIcon('images/DGG_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc)

def genera_tramites_slyp(df_in,mc,anio):
    for row in df_in.itertuples():
        contenidototal = genera_cont_slyp(str(row.CVEGEO),str(row.MUNICIPIO),str(row.DESCRIPCION),str(row.CANTIDAD), str(row.FOTO1), str(row.FOTO2), anio)

        popup = folium.Popup(html=contenidototal, max_width='290')
        #Icono de prueba
        icon_Dependencia = folium.features.CustomIcon('images/DGG_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc)

genera_oficinas(df_oficinas,mc_oficinas)
genera_reuniones(df_SCP_2021_2023, mc_reuniones_2021_2023, "2021")
genera_reuniones(df_reuniones_2024,mc_reuniones_2024,"2024")
genera_tramites(df_tram_scp_2021_2023, mc_tramites_scp_2021_2023, "2021")
genera_tramites(df_tram_scp_2024,mc_tramites_scp_2024,"2024")
genera_tramites(df_tram_sac_2021_2023, mc_tramites_sac_2021_2023, "2021")
genera_tramites(df_tram_sac_2024,mc_tramites_sac_2024,"2024")
genera_tramites_slyp(df_tram_slyp_2021_2023, mc_tramites_slyp_2021_2023, "2021")
genera_tramites_slyp(df_tram_slyp_2024,mc_tramites_slyp_2024,"2024")

mc_oficinas.add_to(layer_oficinas)
mc_reuniones_2021_2023.add_to(layer_reuniones_2021_2023)
mc_reuniones_2024.add_to(layer_reuniones_2024)
mc_tramites_scp_2021_2023.add_to(layer_tramites_scp_2021_2023)
mc_tramites_scp_2024.add_to(layer_tramites_scp_2024)
mc_tramites_sac_2021_2023.add_to(layer_tramites_sac_2021_2023)
mc_tramites_sac_2024.add_to(layer_tramites_sac_2024)
mc_tramites_slyp_2021_2023.add_to(layer_tramites_slyp_2021_2023)
mc_tramites_slyp_2024.add_to(layer_tramites_slyp_2024)

#Agregamos layers al mapa
layer_oficinas.add_to(m3)
layer_reuniones_2021_2023.add_to(m3)
layer_reuniones_2024.add_to(m3)
layer_tramites_scp_2021_2023.add_to(m3)
layer_tramites_scp_2024.add_to(m3)
layer_tramites_sac_2021_2023.add_to(m3)
layer_tramites_sac_2024.add_to(m3)
layer_tramites_slyp_2021_2023.add_to(m3)
layer_tramites_slyp_2024.add_to(m3)

folium.LayerControl(collapsed=False).add_to(m3)
m3.save('DGG.html')
