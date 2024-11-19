# %%

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
        """)  # noqa

# %%  IMAGEN FLOTANTE
LogoCOESPO = ('images/COESPO_Logo_3.png')

# %%  LECTURA DE DATAFRAMES
df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
df['CVEGEO']=df['CVE_ENT']+df['CVE_MUN']
df['CVEGEO']=df['CVEGEO'].astype(int64)#ESTABA COMO FLOAT

df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))

df_rutas19 = pd.read_excel("SECTUR_OK.xlsx", sheet_name='RUTAS2019')
df_rutas20 = pd.read_excel("SECTUR_OK.xlsx", sheet_name='RUTAS2020')
df_ccr = pd.read_excel("SECTUR_OK.xlsx", sheet_name='CCR')
df_cosejos_mun = pd.read_excel("SECTUR_OK.xlsx", sheet_name='CONSEJOS_MUN')
df_mip = pd.read_excel("SECTUR_OK.xlsx", sheet_name='MIP')
df_TD = pd.read_excel("SECTUR_OK.xlsx", sheet_name='TD')
df_ST = pd.read_excel("SECTUR_OK.xlsx", sheet_name='ST')
df_FT = pd.read_excel("SECTUR_OK.xlsx", sheet_name='FT')
df_planeacion = pd.read_excel("SECTUR_OK.xlsx", sheet_name='PLANEACION')
df_vinculacion = pd.read_excel("SECTUR_OK.xlsx", sheet_name='VINCULACION')

#-----------------Integración capas 2022----------------------------
df_convenios = pd.read_excel("SECTUR_OK.xlsx", sheet_name='CONVENIOS')
df_capacitaciones = pd.read_excel("SECTUR_OK.xlsx", sheet_name='CAPACITACIONES')
df_eventos = pd.read_excel("SECTUR_OK.xlsx", sheet_name='EVENTOS')
df_cinematografia = pd.read_excel("SECTUR_OK.xlsx", sheet_name='CINEMATOGRAFIA')
df_unidadgenero = pd.read_excel("SECTUR_OK.xlsx", sheet_name='UNIDADGENERO')
df_apoyos = pd.read_excel("SECTUR_OK.xlsx", sheet_name='APOYOS')


#--------2023-------
df_ccr_2023 = pd.read_excel("SECTUR_OK.xlsx", sheet_name='CCR_2023')
df_cosejos_mun_2023 = pd.read_excel("SECTUR_OK.xlsx", sheet_name='CONSEJOS_MUN_2023')
df_convenios_2023 = pd.read_excel("SECTUR_OK.xlsx", sheet_name='CONVENIOS_2023')
df_capacitaciones_2023 = pd.read_excel("SECTUR_OK.xlsx", sheet_name='CAPACITACIONES_2023')
df_eventos_2023 = pd.read_excel("SECTUR_OK.xlsx", sheet_name='EVENTOS_2023')
df_cinematografia_2023 = pd.read_excel("SECTUR_OK.xlsx", sheet_name='CINEMATOGRAFIA_2023')
df_unidadgenero_2023 = pd.read_excel("SECTUR_OK.xlsx", sheet_name='UNIDADGENERO_2023')
df_apoyos_2023 = pd.read_excel("SECTUR_OK.xlsx", sheet_name='APOYOS_2023')
df_sellos_2023 = pd.read_excel("SECTUR_OK.xlsx", sheet_name='SELLOS_2023')
df_ferias_2023 = pd.read_excel("SECTUR_OK.xlsx", sheet_name='FERIAS_2023')


#--------2024-------
df_convenios_2024 = pd.read_excel("SECTUR_OK.xlsx", sheet_name='CONVENIOS_2024')
df_capacitaciones_2024 = pd.read_excel("SECTUR_OK.xlsx", sheet_name='CAPACITACIONES_2024')
df_eventos_2024 = pd.read_excel("SECTUR_OK.xlsx", sheet_name='EVENTOS_2024')
df_cinematografia_2024 = pd.read_excel("SECTUR_OK.xlsx", sheet_name='CINEMATOGRAFIA_2024')
df_unidadgenero_2024 = pd.read_excel("SECTUR_OK.xlsx", sheet_name='UNIDADGENERO_2024')
df_sellos_2024 = pd.read_excel("SECTUR_OK.xlsx", sheet_name='SELLOS_2024')
df_ferias_2024 = pd.read_excel("SECTUR_OK.xlsx", sheet_name='FERIAS_2024')


#---------MERGE-------------
dfrutas19 = pd.merge(df_rutas19, df_Localidades, on="CVEGEO")
dfrutas19['BENEFICIARIOS'] = dfrutas19['BENEFICIARIOS'].apply(pd.to_numeric, errors='coerce')
dfrutas19['BENEFICIARIOS'] = dfrutas19.apply(lambda x: "{:,}".format(x['BENEFICIARIOS']), axis=1)

dfrutas20 = pd.merge(df_rutas20, df_Localidades, on="CVEGEO")
df_ccr = pd.merge(df_ccr,df_Localidades, on="CVEGEO")
df_ccrb=pd.merge(df,df_ccr,on='CVEGEO',how='left')
dfcosejos_mun = pd.merge(df_cosejos_mun, df_Localidades, on="CVEGEO")
dfmip = pd.merge(df_mip, df_Localidades, on="CVEGEO")
dfTD = pd.merge(df_TD, df_Localidades, on="CVEGEO")
dfST = pd.merge(df_ST, df_Localidades, on="CVEGEO")
dfFT = pd.merge(df_FT, df_Localidades, on="CVEGEO")
dfplaneacion = pd.merge(df_planeacion, df_Localidades, on="CVEGEO")
dfvinculacion = pd.merge(df_vinculacion, df_Localidades, on="CVEGEO")
#----------Merge Capas 2022-----------
df_convenios = pd.merge(df_convenios, df_Localidades, on="CVEGEO")
df_capacitaciones = pd.merge(df_capacitaciones, df_Localidades, on="CVEGEO")
df_eventos = pd.merge(df_eventos, df_Localidades, on="CVEGEO")
df_cinematografia = pd.merge(df_cinematografia, df_Localidades, on="CVEGEO")
df_unidadgenero = pd.merge(df_unidadgenero, df_Localidades, on="CVEGEO")
df_apoyos = pd.merge(df_apoyos, df_Localidades, on="CVEGEO")

#-----------MERGE 2023----------
df_ccr_2023 = pd.merge(df_ccr_2023, df_Localidades, on="CVEGEO")
df_cosejos_mun_2023 = pd.merge(df_cosejos_mun_2023, df_Localidades, on="CVEGEO")
df_convenios_2023 = pd.merge(df_convenios_2023, df_Localidades, on="CVEGEO")
df_capacitaciones_2023 = pd.merge(df_capacitaciones_2023, df_Localidades, on="CVEGEO")
df_eventos_2023 = pd.merge(df_eventos_2023, df_Localidades, on="CVEGEO")
df_cinematografia_2023 = pd.merge(df_cinematografia_2023, df_Localidades, on="CVEGEO")
df_unidadgenero_2023 = pd.merge(df_unidadgenero_2023, df_Localidades, on="CVEGEO")
df_apoyos_2023 = pd.merge(df_apoyos_2023, df_Localidades, on="CVEGEO")
df_sellos_2023 = pd.merge(df_sellos_2023, df_Localidades, on="CVEGEO")
df_ferias_2023 = pd.merge(df_ferias_2023, df_Localidades, on="CVEGEO")


#-----------MERGE 2024----------
df_convenios_2024 = pd.merge(df_convenios_2024, df_Localidades, on="CVEGEO")
df_capacitaciones_2024 = pd.merge(df_capacitaciones_2024, df_Localidades, on="CVEGEO")
df_eventos_2024 = pd.merge(df_eventos_2024, df_Localidades, on="CVEGEO")
df_cinematografia_2024 = pd.merge(df_cinematografia_2024, df_Localidades, on="CVEGEO")
df_unidadgenero_2024 = pd.merge(df_unidadgenero_2024, df_Localidades, on="CVEGEO")
df_sellos_2024 = pd.merge(df_sellos_2024, df_Localidades, on="CVEGEO")
df_ferias_2024 = pd.merge(df_ferias_2024, df_Localidades, on="CVEGEO")


def format(x):
    return "{:,}".format(x)
#df_convenios['BENEFICIARIOS'] = df_convenios['BENEFICIARIOS'].apply(format)
#df_capacitaciones['BENEFICIARIOS'] = df_capacitaciones['BENEFICIARIOS'].apply(format)
#df_eventos['BENEFICIARIOS'] = df_eventos['BENEFICIARIOS'].apply(format)
#df_cinematografia['BENEFICIARIOS'] = df_cinematografia['BENEFICIARIOS'].apply(format)
#df_unidadgenero['BENEFICIARIOS'] = df_unidadgenero['BENEFICIARIOS'].apply(format)
#df_apoyos['BENEFICIARIOS'] = df_apoyos['BENEFICIARIOS'].apply(format)

df.loc[df['region'] == 'Las_Montanas', 'region'] = 'Las Montañas'
df.loc[df['region'] == 'Huasteca_Alta', 'region'] = 'Huasteca Alta'
df.loc[df['region'] == 'Huasteca_Baja', 'region'] = 'Huasteca Baja'
df.loc[df['region'] == 'Los_Tuxtlas', 'region'] = 'Los Tuxtlas'
df_ccrb['COLORB']=df_ccrb['COLORB'].fillna('#F5DBB4')

pd.set_option('max_columns', None)
m = folium.Map(location=[19.8727, -96.1333], zoom_start=7, prefer_canvas=True, tiles='OpenStreetMap')

# ---- Mapa Base de Veracruz
colores = df_ccrb.set_index("CVE_MUN")["COLORB"]

def colorscale(color):
    return '"'+color+'"'

def style_function(feature):
    color = colores.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.8,
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
# ---Mapa de clasificacion 2020
df_ccrb['CONSEJO']=df_ccrb['CONSEJO'].fillna('No')
mapa20 = folium.GeoJson(
    df_ccrb,
    name='Consejos',
    highlight_function=highlight,
    control=False,
    style_function=style_function, tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region','CONSEJO'], aliases=['Nombre Municipio:', 'Región:','Consejo Consultivo Regional:']),
).add_to(m)
# ---- Imagen inferior izquierda logo COESPO
from folium.plugins import FloatImage

FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m)
# ---- Capas

layer_1=FeatureGroup(name='Rutas Turísticas 2019',show=False)
layer_2=FeatureGroup(name='Rutas Turísticas 2020',show=False)
layer_3=FeatureGroup(name='Consejos Municipales 2019 - 2022',show=False)
layer_4=FeatureGroup(name='Consejos Consultivos Regionales 2020 - 2022',show=False)
layer_5=FeatureGroup(name='Manejo Integrado de Paisajes 2021',show=False)
layer_6=FeatureGroup(name='Turismo Deportivo 2021',show=False)
layer_7=FeatureGroup(name='Servicios Turisticos 2021',show=False)
layer_8=FeatureGroup(name='Ferias y Tradiciones 2022',show=False)
layer_9=FeatureGroup(name='Planeaciónes 2022',show=False)
layer_10=FeatureGroup(name='Vinculaciónes 2021',show=False)
layer_11=FeatureGroup(name='Convenios 2022',show=False)
layer_12=FeatureGroup(name='Capacitaciones 2022',show=False)
layer_13=FeatureGroup(name='Eventos 2022',show=False)
layer_14=FeatureGroup(name='Cinematografía 2022',show=False)
layer_15=FeatureGroup(name='Unidad de Genero 2022',show=False)
layer_16=FeatureGroup(name='Apoyos 2022',show=False)

layer_ccm_2023=FeatureGroup(name='Consejos Municipales 2023',show=False)
layer_ccr_2023=FeatureGroup(name='Consejos Consultivos Regionales 2023',show=False)
layer_convenios_2023=FeatureGroup(name='Convenios 2023',show=False)
layer_capacitaciones_2023=FeatureGroup(name='Capacitaciones 2023',show=False)
layer_eventos_2023=FeatureGroup(name='Eventos 2023',show=False)
layer_cinematografia_2023=FeatureGroup(name='Cinematografía 2023',show=False)
layer_unidad_2023=FeatureGroup(name='Unidad de Genero 2023',show=False)
layer_apoyos_2023=FeatureGroup(name='Apoyos 2023',show=False)
layer_sellos_2023=FeatureGroup(name='Sellos y Distintivos 2023',show=False)
layer_ferias_2023=FeatureGroup(name='Ferias y Tradiciones 2023',show=False)

layer_convenios_2024=FeatureGroup(name='Convenios 2024',show=False)
layer_capacitaciones_2024=FeatureGroup(name='Capacitaciones 2024',show=False)
layer_eventos_2024=FeatureGroup(name='Eventos 2024',show=False)
layer_cinematografia_2024=FeatureGroup(name='Cinematografía 2024',show=False)
layer_unidad_2024=FeatureGroup(name='Unidad de Genero 2024',show=False)
layer_sellos_2024=FeatureGroup(name='Sellos y Distintivos 2024',show=False)
layer_ferias_2024=FeatureGroup(name='Ferias y Tradiciones 2024',show=False)

# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster
mc_1=MarkerCluster()
mc_2=MarkerCluster()
mc_tabla20=MarkerCluster()
mc_tabla21=MarkerCluster()
mc_3=MarkerCluster()
mc_4=MarkerCluster()
mc_5=MarkerCluster()
mc_6=MarkerCluster()
mc_7=MarkerCluster()
mc_8=MarkerCluster()
mc_9=MarkerCluster()
mc_10=MarkerCluster()
mc_11=MarkerCluster()
mc_12=MarkerCluster()
mc_13=MarkerCluster()
mc_14=MarkerCluster()
mc_15=MarkerCluster()
mc_16=MarkerCluster()

#2023-------------
mc_ccm_2023=MarkerCluster()
mc_ccr_2023=MarkerCluster()
mc_convenios_2023=MarkerCluster()
mc_capacitaciones_2023=MarkerCluster()
mc_eventos_2023=MarkerCluster()
mc_cinematografia_2023=MarkerCluster()
mc_unidad_2023=MarkerCluster()
mc_apoyos_2023=MarkerCluster()
mc_sellos_2023=MarkerCluster()
mc_ferias_2023=MarkerCluster()

#2024-------------
mc_convenios_2024=MarkerCluster()
mc_capacitaciones_2024=MarkerCluster()
mc_eventos_2024=MarkerCluster()
mc_cinematografia_2024=MarkerCluster()
mc_unidad_2024=MarkerCluster()
mc_sellos_2024=MarkerCluster()
mc_ferias_2024=MarkerCluster()

def rutas(df_in):
    for row in df_in.itertuples():
        contenido = genera_rutas( str(row.nom_mun), str(row.NOMBRE_RUTA), str(row.BENEFICIARIOS), str(row.LINK))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/SECTUR__marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        if row.CAPA == 2019:

            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_1)

        if row.CAPA == 2020:
                folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_2)

rutas(dfrutas19)
rutas(dfrutas20)

def consejos_mun(df_in,mc):
        for row in df_in.itertuples():
            contenido = genera_consejos_mun(str(row.nom_mun), str(row.FECHA_INST), str(row.ACTA))

            popup = folium.Popup(html=contenido, max_width='290')
            icon_Dependencia = folium.features.CustomIcon('images/SECTUR__marcador.png', icon_size=(60, 60),
                                                          icon_anchor=(22, 59),
                                                          popup_anchor=(3, -54))

            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                        mc)

consejos_mun(dfcosejos_mun,mc_3)
consejos_mun(df_cosejos_mun_2023,mc_ccm_2023)

def consejos_regionales(df_in,mc):
    for row in df_in.itertuples():
        contenido = genera_consejos_reg(str(row.nom_mun), str(row.CONSEJO), str(row.INSTALACION), str(row.FOTO1), str(row.FOTO2), str(row.VIDEO))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/SECTUR__marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

consejos_regionales(df_ccr,mc_4)
consejos_regionales(df_ccr_2023,mc_ccr_2023)

def manejo_paisajes(df_in):
    for row in df_in.itertuples():
        contenido = genera_paisajes(str(row.nom_mun), str(row.PROYECTO), str(row.ANIO), str(row.BENEFICIARIOS), str(row.FOTO))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/SECTUR__marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_5)

manejo_paisajes(dfmip)

def turismo_deportivo(df_in):
    for row in df_in.itertuples():
        contenido = genera_turismo(str(row.nom_mun), str(row.PROGRAMA), str(row.ANIO), str(row.BENEFICIARIOS), str(row.FOTO))
        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/SECTUR__marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_6)

turismo_deportivo(dfTD)

def servicios_turisticos(df_in):
    for row in df_in.itertuples():
        contenido = genera_servicios(str(row.MUNICIPIO), str(row.CERTIFICACIONES), str(row.ENTREGADAS),
                                     str(row.CURSO), str(row.TOTAL), str(row.FOTO1), str(row.FOTO2))
        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/SECTUR__marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_7)

servicios_turisticos(dfST)

def ferias_y_tradiciones(df_in):
    for row in df_in.itertuples():
        contenido = genera_ferias_tradiciones(str(row.MUNICIPIO), str(row.FESTIVAL), str(row.FOTO1))
        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/SECTUR__marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc_8)

ferias_y_tradiciones(dfFT)

def planeaciones_vinculaciones(df_in,mc):
    for row in df_in.itertuples():
        contenido = genera_planeaciones_vinculaciones(str(row.MUNICIPIO), str(row.PROGRAMA), str(row.DESCRIPCION),
                                              str(row.FOTO1),str(row.FOTO2))
        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/SECTUR__marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

planeaciones_vinculaciones(dfplaneacion,mc_9)
planeaciones_vinculaciones(dfvinculacion,mc_10)


def capasImplementadas(df_in,mc):
    for row in df_in.itertuples():
        contenido = genera_capas(str(row.MUNICIPIO), str(row.ACTIVIDAD), str(row.FECHA), str(row.DESCRIPCION), str(row.BENEFICIARIOS),
                                              str(row.FOTO1),str(row.FOTO2),str(row.VIDEO),str(row.OTRO))
        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/SECTUR__marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

capasImplementadas(df_convenios,mc_11)
capasImplementadas(df_capacitaciones,mc_12)
capasImplementadas(df_eventos,mc_13)
capasImplementadas(df_cinematografia,mc_14)
capasImplementadas(df_unidadgenero,mc_15)
capasImplementadas(df_apoyos,mc_16)

capasImplementadas(df_convenios_2023,mc_convenios_2023)
capasImplementadas(df_capacitaciones_2023,mc_capacitaciones_2023)
capasImplementadas(df_eventos_2023,mc_eventos_2023)
capasImplementadas(df_cinematografia_2023,mc_cinematografia_2023)
capasImplementadas(df_unidadgenero_2023,mc_unidad_2023)
capasImplementadas(df_apoyos_2023,mc_apoyos_2023)
capasImplementadas(df_ferias_2023,mc_ferias_2023)
capasImplementadas(df_sellos_2023,mc_sellos_2023)

capasImplementadas(df_convenios_2024,mc_convenios_2024)
capasImplementadas(df_capacitaciones_2024,mc_capacitaciones_2024)
capasImplementadas(df_eventos_2024,mc_eventos_2024)
capasImplementadas(df_cinematografia_2024,mc_cinematografia_2024)
capasImplementadas(df_unidadgenero_2024,mc_unidad_2024)
capasImplementadas(df_ferias_2024,mc_ferias_2024)
capasImplementadas(df_sellos_2024,mc_sellos_2024)


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
mc_11.add_to(layer_11)
mc_12.add_to(layer_12)
mc_13.add_to(layer_13)
mc_14.add_to(layer_14)
mc_15.add_to(layer_15)
mc_16.add_to(layer_16)

mc_ccm_2023.add_to(layer_ccm_2023)
mc_ccr_2023.add_to(layer_ccr_2023)
mc_convenios_2023.add_to(layer_convenios_2023)
mc_capacitaciones_2023.add_to(layer_capacitaciones_2023)
mc_eventos_2023.add_to(layer_eventos_2023)
mc_cinematografia_2023.add_to(layer_cinematografia_2023)
mc_unidad_2023.add_to(layer_unidad_2023)
mc_apoyos_2023.add_to(layer_apoyos_2023)
mc_sellos_2023.add_to(layer_sellos_2023)
mc_ferias_2023.add_to(layer_ferias_2023)

mc_convenios_2024.add_to(layer_convenios_2024)
mc_capacitaciones_2024.add_to(layer_capacitaciones_2024)
mc_eventos_2024.add_to(layer_eventos_2024)
mc_cinematografia_2024.add_to(layer_cinematografia_2024)
mc_unidad_2024.add_to(layer_unidad_2024)
mc_sellos_2024.add_to(layer_sellos_2024)
mc_ferias_2024.add_to(layer_ferias_2024)



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
layer_11.add_to(m)
layer_12.add_to(m)
layer_13.add_to(m)
layer_14.add_to(m)
layer_15.add_to(m)
layer_16.add_to(m)

layer_ccm_2023.add_to(m)
layer_ccr_2023.add_to(m)
layer_convenios_2023.add_to(m)
layer_capacitaciones_2023.add_to(m)
layer_eventos_2023.add_to(m)
layer_cinematografia_2023.add_to(m)
layer_unidad_2023.add_to(m)
layer_apoyos_2023.add_to(m)
layer_sellos_2023.add_to(m)
layer_ferias_2023.add_to(m)


layer_convenios_2024.add_to(m)
layer_capacitaciones_2024.add_to(m)
layer_eventos_2024.add_to(m)
layer_cinematografia_2024.add_to(m)
layer_unidad_2024.add_to(m)
layer_sellos_2024.add_to(m)
layer_ferias_2024.add_to(m)


# ---- Botón de Búsqueda de Municipio
statesearch = Search(
    layer=mapa20,
    geom_type='Polygon',
    placeholder='Búsqueda de municipio',
    collapsed=False,
    search_label='NOM_MUN',
    search_zoom=10,
    weight=3
).add_to(m)

folium.LayerControl(collapsed=False).add_to(m)

m.save("SECTUR.html")

