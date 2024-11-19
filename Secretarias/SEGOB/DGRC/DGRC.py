import folium
import pandas as pd
import geopandas as gpd
from folium.plugins import Search
from pathlib import Path
from numpy import int64
from Funciones import *
from folium import FeatureGroup

from folium.plugins import MarkerCluster

# %%
path_ini = Path("C:/ESyP/Mapas_COESPO/Resources/")
#path_ini = Path("/Users/4x/COESPOAX/MapasTematicos/Resources")
pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('max_columns', None)
LogoCOESPO = ('images/COESPO_Logo_3.png')

df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))

df_regiones = df
df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))

df_directorio = pd.read_excel("DIRECTORIO COESPO_orig.xlsx", sheet_name='DATOS DIRECTORIO')
df_actas_2021 = pd.read_excel("DGRC_OK.xlsx", sheet_name='2021')
df_actas_2022 = pd.read_excel("DGRC_OK.xlsx", sheet_name='2022')
df_actas_2023 = pd.read_excel("DGRC_OK.xlsx", sheet_name='2023')
df_actas_2024 = pd.read_excel("DGRC_OK.xlsx", sheet_name='2024')
df_brigadas = pd.read_excel("DGRC_OK.xlsx", sheet_name='BRIGADAS')
df_capa2 = pd.read_excel("DGRC_OK.xlsx", sheet_name='BRIGADAS')

capa_base = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
capa_base['CVE_MUN'] = capa_base['CVE_MUN'].apply(pd.to_numeric, errors='coerce')
df_capa2 = pd.merge(capa_base, df_capa2, on="CVE_MUN")

df_directorio = pd.merge(df_directorio,df_Localidades, on='CVEGEO')
df_actas_2021 = pd.merge(df_actas_2021,df_Localidades, on='CVEGEO')
df_actas_2022 = pd.merge(df_actas_2022,df_Localidades, on='CVEGEO')
df_actas_2023 = pd.merge(df_actas_2023,df_Localidades, on='CVEGEO')
df_actas_2024 = pd.merge(df_actas_2024,df_Localidades, on='CVEGEO')
df_brigadas = pd.merge(df_brigadas,df_Localidades, on='CVEGEO')

def format(x):
    return "{:,}".format(x)
df_actas_2021['NACIMIENTO'] = df_actas_2021['NACIMIENTO'].apply(format)
df_actas_2021['MATRIMONIO'] = df_actas_2021['MATRIMONIO'].apply(format)
df_actas_2021['DIVORCIO'] = df_actas_2021['DIVORCIO'].apply(format)
df_actas_2021['DEFUNCION'] = df_actas_2021['DEFUNCION'].apply(format)
df_actas_2021['SENTENCIA'] = df_actas_2021['SENTENCIA'].apply(format)
df_actas_2021['TOTAL'] = df_actas_2021['TOTAL'].apply(format)

df_actas_2022['NACIMIENTO'] = df_actas_2022['NACIMIENTO'].apply(format)
df_actas_2022['MATRIMONIO'] = df_actas_2022['MATRIMONIO'].apply(format)
df_actas_2022['DIVORCIO'] = df_actas_2022['DIVORCIO'].apply(format)
df_actas_2022['DEFUNCION'] = df_actas_2022['DEFUNCION'].apply(format)
df_actas_2022['SENTENCIA'] = df_actas_2022['SENTENCIA'].apply(format)
df_actas_2022['TOTAL'] = df_actas_2022['TOTAL'].apply(format)

df_actas_2023['NACIMIENTO'] = df_actas_2023['NACIMIENTO'].apply(format)
df_actas_2023['MATRIMONIO'] = df_actas_2023['MATRIMONIO'].apply(format)
df_actas_2023['DIVORCIO'] = df_actas_2023['DIVORCIO'].apply(format)
df_actas_2023['DEFUNCION'] = df_actas_2023['DEFUNCION'].apply(format)
df_actas_2023['SENTENCIA'] = df_actas_2023['SENTENCIA'].apply(format)
df_actas_2023['TOTAL'] = df_actas_2023['TOTAL'].apply(format)

df_actas_2024['NACIMIENTO'] = df_actas_2024['NACIMIENTO'].apply(format)
df_actas_2024['MATRIMONIO'] = df_actas_2024['MATRIMONIO'].apply(format)
df_actas_2024['DIVORCIO'] = df_actas_2024['DIVORCIO'].apply(format)
df_actas_2024['DEFUNCION'] = df_actas_2024['DEFUNCION'].apply(format)
df_actas_2024['SENTENCIA'] = df_actas_2024['SENTENCIA'].apply(format)
df_actas_2024['TOTAL'] = df_actas_2024['TOTAL'].apply(format)

df.loc[df['region'] == 'Las_Montanas', 'region'] = 'Las Montañas'
df.loc[df['region'] == 'Huasteca_Alta', 'region'] = 'Huasteca Alta'
df.loc[df['region'] == 'Huasteca_Baja', 'region'] = 'Huasteca Baja'
df.loc[df['region'] == 'Los_Tuxtlas', 'region'] = 'Los Tuxtlas'

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
m3 = folium.Map([19.5426, -96.91], zoom_start=7, prefer_canvas=True, titles='OpenStreetMap')

from folium.plugins import FloatImage
FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m3)

mc_Directorio = MarkerCluster()
mc_actas_2021 = MarkerCluster()
mc_actas_2022 = MarkerCluster()
mc_actas_2023 = MarkerCluster()
mc_actas_2024 = MarkerCluster()
mc_brigadas=MarkerCluster()

#Definimos los layers
layer_directorio = FeatureGroup(name='Directorio', show=False)
layer_total2021=FeatureGroup(name='Actas 2021',show=False)
layer_total2022=FeatureGroup(name='Actas 2022',show=False)
layer_total2023=FeatureGroup(name='Actas 2023',show=False)
layer_total2024=FeatureGroup(name='Actas 2024',show=False)
layer_brigadas=FeatureGroup(name='Brigadas 2022',show=False)

colores = df_regiones.set_index("CVE_MUN")["Color"]
colores_avgm = df_capa2.set_index("id")["COLOR_MP"]

def style_function(feature):
    color = colores.get(int(feature["id"][-3:]), None)
    # print(color)
    # color=color.to_json()
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
    df_regiones,
    name='Regiones Veracruz',
    highlight_function=highlight,
    style_function=style_function,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Municipio:', 'Región:']),
).add_to(m3)

def style_function_brigadas(feature):
    #color_avgm = colores_avgm.get(int(feature["id"][-3:]), None)
    color_brigadas = "#800000"
    # print(color)
    # color=color.to_json()
    return {
        "fillOpacity": 0.9,
        "weight": 0,
        "fillColor": color_brigadas,
        "color": color_brigadas,
        'line_opacity': 0.2,
    }


def highlight_brigadas(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }

mapa_brigadas = folium.GeoJson(
    df_capa2,
    name='Brigadas 2022',
    show=False,
    highlight_function=highlight_brigadas,
    style_function=style_function_brigadas,
    tooltip=folium.features.GeoJsonTooltip(fields=['MUNICIPIO', 'REGION'], aliases=['Municipio:', 'Región:']),
).add_to(m3)

def directorio(df_in):
    for row in df_in.itertuples():
        contenidototal = genera_directorio(str(row.MUNICIPIO), str(row.OFICIAL), str(row.COORDINACION), str(row.DIRECCION),
                                      str(row.TELEFONO), str(row.CORREO))

        popup = folium.Popup(html=contenidototal, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/DGRC_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_Directorio)

directorio(df_directorio)

def actastotales(df_in,mc,anio):
    for row in df_in.itertuples():
        contenidototal = genera_total(str(row.MUNICIPIO), str(row.DIRECCION),  str(row.TELEFONO), str(row.NACIMIENTO), str(row.MATRIMONIO),
                                      str(row.DIVORCIO),str(row.DEFUNCION),str(row.SENTENCIA),str(row.TOTAL),anio)

        popup = folium.Popup(html=contenidototal, max_width='290')
        #Icono de prueba
        icon_Dependencia = folium.features.CustomIcon('images/DGRC_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

actastotales(df_actas_2021,mc_actas_2021,"2021")
actastotales(df_actas_2022,mc_actas_2022,"2022")
actastotales(df_actas_2023,mc_actas_2023,"2023")
actastotales(df_actas_2024,mc_actas_2024,"2024")

def brigadas_f(df_in):
    for row in df_in.itertuples():
        contenido_brigadas = genera_brigadas(str(row.id), str(row.MUNICIPIO), str(row.FECHA),  str(row.BENEFICIARIOS), str(row.COLOR_MP))

        popup = folium.Popup(html=contenido_brigadas, max_width='290')

        icon_Dependencia = folium.features.CustomIcon('images/DGRC_marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_brigadas)

brigadas_f(df_brigadas)

mc_Directorio.add_to(layer_directorio)
mc_actas_2021.add_to(layer_total2021)
mc_actas_2022.add_to(layer_total2022)
mc_actas_2023.add_to(layer_total2023)
mc_actas_2024.add_to(layer_total2024)
mc_brigadas.add_to(mapa_brigadas)

#Agregamos layers al mapa
layer_directorio.add_to(m3)
layer_total2021.add_to(m3)
layer_total2022.add_to(m3)
layer_total2023.add_to(m3)
layer_total2024.add_to(m3)
mapa_brigadas.add_to(m3)

statesearch = Search(
     layer=mapa,
     geom_type='Polygon',
     placeholder='Búsqueda de municipio',
     collapsed=False,
     search_label='NOM_MUN',
     weight=5
).add_to(m3)
folium.LayerControl(collapsed=False).add_to(m3)
m3.save('DGRC.html')
