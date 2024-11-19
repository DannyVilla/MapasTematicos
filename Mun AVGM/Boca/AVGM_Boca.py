from pathlib import Path

import folium
import geopandas as gpd
import pandas as pd
from folium import FeatureGroup
from folium.plugins import Search

from Funciones import *

# %%


#path_ini = Path("C:/ESyP/Mapas_COESPO/Resources/")
path_ini = Path("/Users/4x/COESPOAX/MapasTematicos/Resources")
pd.options.display.float_format = '{:,.2f}'.format
#pd.set_option('max_columns', None)

df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))

df_regiones = df
df_boca = df_regiones.loc[df_regiones["CVE_MUN"] == "028"]


df_acciones = pd.read_excel("AVGM_Boca.xlsx", sheet_name='ACCIONES')

capa_base = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
capa_base['CVE_MUN'] = capa_base['CVE_MUN'].apply(pd.to_numeric, errors='coerce')

def format(x):
    return "{:,}".format(x)

df_acciones['MUJERES'] = df_acciones['MUJERES'].apply(format)
df_acciones['HOMBRES'] = df_acciones['HOMBRES'].apply(format)
df_acciones['TOTAL'] = df_acciones['TOTAL'].apply(format)

#FORMATO DE HORA Y FECHA

# Se ajustan nombre de la región para desplegar
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

# Se definen colores para cada region
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

from folium.plugins import FloatImage

# df_regiones.loc[df_regiones['CVE_MUN'].isin(['', '', '', '', '', '', '', '', '', '', '']),['Color']]=="#C70039"

LogoCOESPO = ('COESPO_Logo_3.png')
print(df_regiones)

# ---Mapa
from folium.plugins import MarkerCluster

# print(df)
m3 = folium.Map([19.106433009251738, -96.10548234516847], zoom_start=13)


mc_2 = MarkerCluster()


layer_2 = FeatureGroup(name='Acciones por Municipio', show=False)

colores = df_regiones.set_index("CVE_MUN")["Color"]

def style_function(feature):
    #color = colores.get(int(feature["id"][-3:]), None)
    color = "#E2A9F3"
    # print(color)
    # color=color.to_json()
    return {
        "fillOpacity": 0.6,
        "weight": 0,
        "fillColor": color,
        "color": color,
        'line_opacity': 0.3,
    }


def highlight(feature):
    return {
        'weight': 5,
        'opacity': 0.3,
        'fillOpacity': 0.3,
        'line_opacity': 1
    }

mapa = folium.GeoJson(
    df_boca,
    name='Boca del Río',
    highlight_function=highlight,
    style_function=style_function,
    #tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Municipio:', 'Región:']),
).add_to(m3)



# ---Mapa del Estado de Veracruz
statesearch = Search(
    layer=mapa,
    geom_type='Polygon',
    placeholder='Búsqueda de municipio',
    collapsed=False,
    search_label='NOM_MUN',
    weight=5
).add_to(m3)

# print(df_indicadores.dtypes)



def genera_acciones(df_in, mc):
    for row in df_in.itertuples():
        contenido = tarjeta_acciones(row)

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/SEGOB_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.LATITUD, row.LONGITUD], popup=popup, icon=icon_Dependencia).add_to(
            mc)

genera_acciones(df_acciones, mc_2)
mc_2.add_to(layer_2)
layer_2.control = True

layer_2.add_to(m3)

FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m3)
m3.add_child(folium.LayerControl(collapsed=False))
m3.save('AVGM_Boca.html')
