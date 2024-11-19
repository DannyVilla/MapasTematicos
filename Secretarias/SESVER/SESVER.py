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

df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))

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

df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))


df_2019 = pd.read_excel("SESVER_COMPLETO.xlsx", sheet_name='2019')
df_2020 = pd.read_excel("SESVER_COMPLETO.xlsx", sheet_name='2020')
df_2021 = pd.read_excel("SESVER_COMPLETO.xlsx", sheet_name='2021')
df_2022 = pd.read_excel("SESVER_COMPLETO.xlsx", sheet_name='2022')
df_unidades = pd.read_excel("SESVER_COMPLETO.xlsx", sheet_name='UNIDADES_MEDICAS')
df_intervenidas = pd.read_excel("SESVER_COMPLETO.xlsx", sheet_name='UNIDADES_INTERVENIDAS')
df_jur = pd.read_excel("SESVER_COMPLETO.xlsx", sheet_name='JUR')
df_obras = pd.read_excel("SESVER_COMPLETO.xlsx", sheet_name='OBRAS')

localidades = Path("C:/ESyP/Mapas_COESPO/Resources/")

df2019 = pd.merge(df_2019, df_Localidades, on="CVEGEO")
df2020 = pd.merge(df_2020, df_Localidades, on="CVEGEO")
df2021 = pd.merge(df_2021, df_Localidades, on="CVEGEO")
df2022 = pd.merge(df_2022, df_Localidades, on="CVEGEO")

df_intervenidas = pd.merge(df_intervenidas, df_Localidades, on="CVEGEO")

# df['CVEGEO']=str(df['CVE_ENT']+df['CVE_MUN'])
df['CVEGEO'] = df.apply(lambda row: row.CVE_ENT + row.CVE_MUN, axis=1)
df_jur['CVEGEO'] = df_jur['CVEGEO'].astype(str)  # ESTABA COMO FLOAT.set_option('max_columns', None)
df_jur2 = pd.merge(df, df_jur, on=["CVEGEO", "CVEGEO"])

# Cambiar formato a columnas
cols = ['DEFUNCIONES', 'EDAS', 'IRAS', 'BCG', 'PENTA', 'HB', 'RV5', 'NC', 'RV1', 'HEX', 'HIP', 'OBE', 'DIS', 'TUB',
        'LEP', 'BRU', 'EPOC', 'LEPTO', 'CH', 'IMC', 'VIH', 'UAA', 'MANT', 'PREV', 'PART', 'PARTC', 'ELAB', 'TRAT',
        'CIRU', 'CONSUL', 'ANTIRR', 'ITS', 'LEHIS'
        ]

def format(x):
    return "{:,}".format(x)

#Dataframe 2019 Delimitador por comas en miles
df2019['DEFUNCIONES'] = df2019['DEFUNCIONES'].apply(format)
df2019['EDAS'] = df2019['EDAS'].apply(format)
df2019['IRAS'] = df2019['IRAS'].apply(format)
df2019['BCG'] = df2019['BCG'].apply(format)
df2019['PENTA'] = df2019['PENTA'].apply(format)
df2019['HB'] = df2019['HB'].apply(format)
df2019['RV5'] = df2019['RV5'].apply(format)
df2019['NC'] = df2019['NC'].apply(format)
df2019['RV1'] = df2019['RV1'].apply(format)
df2019['HEX'] = df2019['HEX'].apply(format)
df2019['HIP'] = df2019['HIP'].apply(format)
df2019['OBE'] = df2019['OBE'].apply(format)
df2019['DIS'] = df2019['DIS'].apply(format)
df2019['TUB'] = df2019['TUB'].apply(format)
df2019['LEP'] = df2019['LEP'].apply(format)
df2019['BRU'] = df2019['BRU'].apply(format)
df2019['EPOC'] = df2019['EPOC'].apply(format)
df2019['CH'] = df2019['CH'].apply(format)
df2019['IMC'] = df2019['IMC'].apply(format)
df2019['VIH'] = df2019['VIH'].apply(format)
df2019['UAA'] = df2019['UAA'].apply(format)
df2019['MANT'] = df2019['MANT'].apply(format)
df2019['PREV'] = df2019['PREV'].apply(format)
df2019['PART'] = df2019['PART'].apply(format)
df2019['PARTC'] = df2019['PARTC'].apply(format)
df2019['ELAB'] = df2019['ELAB'].apply(format)
df2019['TRAT'] = df2019['TRAT'].apply(format)
df2019['CIRU'] = df2019['CIRU'].apply(format)
df2019['CONSUL'] = df2019['CONSUL'].apply(format)
df2019['ANTIRR'] = df2019['ANTIRR'].apply(format)
df2019['ITS'] = df2019['ITS'].apply(format)
df2019['LEHIS'] = df2019['LEHIS'].apply(format)

#Dataframe 2020 Delimitador por comas en miles
df2020['DEFUNCIONES'] = df2020['DEFUNCIONES'].apply(format)
df2020['EDAS'] = df2020['EDAS'].apply(format)
df2020['IRAS'] = df2020['IRAS'].apply(format)
df2020['BCG'] = df2020['BCG'].apply(format)
df2020['PENTA'] = df2020['PENTA'].apply(format)
df2020['HB'] = df2020['HB'].apply(format)
df2020['RV5'] = df2020['RV5'].apply(format)
df2020['NC'] = df2020['NC'].apply(format)
df2020['RV1'] = df2020['RV1'].apply(format)
df2020['HEX'] = df2020['HEX'].apply(format)
df2020['HIP'] = df2020['HIP'].apply(format)
df2020['OBE'] = df2020['OBE'].apply(format)
df2020['DIS'] = df2020['DIS'].apply(format)
df2020['TUB'] = df2020['TUB'].apply(format)
df2020['LEP'] = df2020['LEP'].apply(format)
df2020['BRU'] = df2020['BRU'].apply(format)
df2020['EPOC'] = df2020['EPOC'].apply(format)
df2020['CH'] = df2020['CH'].apply(format)
df2020['IMC'] = df2020['IMC'].apply(format)
df2020['VIH'] = df2020['VIH'].apply(format)
df2020['UAA'] = df2020['UAA'].apply(format)
df2020['MANT'] = df2020['MANT'].apply(format)
df2020['PREV'] = df2020['PREV'].apply(format)
df2020['PART'] = df2020['PART'].apply(format)
df2020['PARTC'] = df2020['PARTC'].apply(format)
df2020['ELAB'] = df2020['ELAB'].apply(format)
df2020['TRAT'] = df2020['TRAT'].apply(format)
df2020['CIRU'] = df2020['CIRU'].apply(format)
df2020['CONSUL'] = df2020['CONSUL'].apply(format)
df2020['ANTIRR'] = df2020['ANTIRR'].apply(format)
df2020['ITS'] = df2020['ITS'].apply(format)
df2020['LEHIS'] = df2020['LEHIS'].apply(format)

#Dataframe 2021 Delimitador por comas en miles
df2022['DEFUNCIONES'] = df2022['DEFUNCIONES'].apply(format)
df2022['EDAS'] = df2022['EDAS'].apply(format)
df2022['IRAS'] = df2022['IRAS'].apply(format)
df2022['BCG'] = df2022['BCG'].apply(format)
df2022['PENTA'] = df2022['PENTA'].apply(format)
df2022['HB'] = df2022['HB'].apply(format)
df2022['RV5'] = df2022['RV5'].apply(format)
df2022['NC'] = df2022['NC'].apply(format)
df2022['RV1'] = df2022['RV1'].apply(format)
df2022['HEX'] = df2022['HEX'].apply(format)
df2022['HIP'] = df2022['HIP'].apply(format)
df2022['OBE'] = df2022['OBE'].apply(format)
df2022['DIS'] = df2022['DIS'].apply(format)
df2022['TUB'] = df2022['TUB'].apply(format)
df2022['LEP'] = df2022['LEP'].apply(format)
df2022['BRU'] = df2022['BRU'].apply(format)
df2022['EPOC'] = df2022['EPOC'].apply(format)
df2022['CH'] = df2022['CH'].apply(format)
df2022['IMC'] = df2022['IMC'].apply(format)
df2022['VIH'] = df2022['VIH'].apply(format)
df2022['UAA'] = df2022['UAA'].apply(format)
df2022['MANT'] = df2022['MANT'].apply(format)
df2022['PREV'] = df2022['PREV'].apply(format)
df2022['PART'] = df2022['PART'].apply(format)
df2022['PARTC'] = df2022['PARTC'].apply(format)
df2022['ELAB'] = df2022['ELAB'].apply(format)
df2022['TRAT'] = df2022['TRAT'].apply(format)
df2022['CIRU'] = df2022['CIRU'].apply(format)
df2022['CONSUL'] = df2022['CONSUL'].apply(format)
df2022['ANTIRR'] = df2022['ANTIRR'].apply(format)
df2022['ITS'] = df2022['ITS'].apply(format)
df2022['LEHIS'] = df2022['LEHIS'].apply(format)

m = folium.Map(location=[19.8727, -96.1333], zoom_start=7, prefer_canvas=True, tiles='OpenStreetMap')

# ---- Mapa Base de Veracruz
colores = df_jur2.set_index("CVE_MUN")["COLOR"]

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


Veracruz = folium.GeoJson(
    df_jur2,
    name='Jurisdicciones',
    control=True,
    highlight_function=highlight,
    style_function=style_function,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'JUR'], aliases=['Nombre Municipio:', 'Jurisdicción:']),
).add_to(m)

# ---- Imagen inferior izquierda logo COESPO
from folium.plugins import FloatImage

LogoCOESPO = ('images/COESPO_Logo_3.png')
FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m)
# ---- Capas
layer_2019 = FeatureGroup(name='Acciones 2019', show=False)
layer_2020 = FeatureGroup(name='Acciones 2020', show=False)
layer_2021 = FeatureGroup(name='Acciones 2021', show=False)
layer_2022 = FeatureGroup(name='Acciones 2022', show=False)
layer_unidades = FeatureGroup(name='Unidades Médicas', show=False)
layer_intervenidas = FeatureGroup(name='Unidades Médicas Intervenidas', show=False)
layer_obras = FeatureGroup(name='Obras Unidades Medicas (Actualización 2022)', show=False)
# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster

mc_2019 = MarkerCluster()
mc_2020 = MarkerCluster()
mc_2021 = MarkerCluster()
mc_2022 = MarkerCluster()
mc_unidades = MarkerCluster()
mc_intervenidas = MarkerCluster()
mc_obras = MarkerCluster()

pd.set_option('display.max_columns', None)

def genera(df_in, mc):
    for row in df_in.itertuples():
        contenido = genera_tarjeta(str(row.MUNICIPIO), str(row.JUR), str(row.DEFUNCIONES), str(row.EDAS), str(row.IRAS),
                                   str(row.BCG), str(row.PENTA), str(row.HB), str(row.RV5), str(row.NC),
                                   str(row.RV1), str(row.HEX), str(row.HIP), str(row.OBE), str(row.DIS), str(row.TUB),
                                   str(row.LEP), str(row.BRU), str(row.EPOC), str(row.LEPTO), str(row.CH), str(row.IMC),
                                   str(row.VIH), str(row.UAA), str(row.MANT), str(row.PREV), str(row.PART),
                                   str(row.PARTC),
                                   str(row.ELAB), str(row.TRAT), str(row.LEP), str(row.CONSUL), str(row.ANTIRR),
                                   str(row.ITS), str(row.LEHIS))
        popup = folium.Popup(html=contenido, max_width='500')
        icon_Dependencia = folium.features.CustomIcon('images/SS_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

genera(df2019, mc_2019)
genera(df2020, mc_2020)
genera(df2021, mc_2021)
genera(df2022, mc_2022)
# print(df_unidades)

for row in df_unidades.itertuples():
    contenido = content_unidades(str(row.NOMBRE), str(row.MUNICIPIO), str(row.LOCALIDAD), str(row.TIPO),
                                 str(row.DIRECCIÓN))
    icon_Dependencia = folium.features.CustomIcon('images/SS_Marcador.png', icon_size=(60, 60),
                                                  icon_anchor=(22, 59),
                                                  popup_anchor=(3, -54))

    popup = folium.Popup(html=contenido, max_width='350')
    folium.Marker(location=[row.LATITUD, row.LONGITUD], popup=popup, icon=icon_Dependencia).add_to(
        mc_unidades)

for row in df_obras.itertuples():
    contenido = content_unidades_2022(str(row.MUNICIPIO), str(row.LOCALIDAD), str(row.TIPO),
                                 str(row.NOMBRE),str(row.ANIO_INTERVENCION),str(row.TIPO_INTERVENCION))

    icon_Dependencia = folium.features.CustomIcon('images/SS_Marcador.png', icon_size=(60, 60),
                                                  icon_anchor=(22, 59),
                                                  popup_anchor=(3, -54))

    popup = folium.Popup(html=contenido, max_width='350')
    folium.Marker(location=[row.LATITUD, row.LONGITUD], popup=popup, icon=icon_Dependencia).add_to(
        mc_obras)

def genera_intervencion(df_in, mc):
    for row in df_in.itertuples():
        contenido = genera_tarjeta_intervencion(str(row.MUNICIPIO), str(row.JUR), str(row.CLUES), str(row.LOCALIDAD), str(row.TIPO_UNIDAD),
                                   str(row.NOMBRE_UNIDAD), str(row.ANIO_INTERVENCION), str(row.TIPO_INTERVENCION), str(row.POBLACION))
        popup = folium.Popup(html=contenido, max_width='500')
        icon_Dependencia = folium.features.CustomIcon('images/SS_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)

genera_intervencion(df_intervenidas,mc_intervenidas)

mc_2019.add_to(layer_2019)
mc_2020.add_to(layer_2020)
mc_2021.add_to(layer_2021)
mc_2022.add_to(layer_2022)
mc_unidades.add_to(layer_unidades)
mc_obras.add_to(layer_obras)
mc_intervenidas.add_to(layer_intervenidas)

layer_2019.add_to(m)
layer_2020.add_to(m)
layer_2021.add_to(m)
layer_2022.add_to(m)
layer_unidades.add_to(m)
layer_obras.add_to(m)
layer_intervenidas.add_to(m)

# ---- Botón de Búsqueda de Municipio
statesearch = Search(
    layer=Veracruz,
    geom_type='Polygon',
    placeholder='Búsqueda de municipio',
    collapsed=False,
    search_label='NOM_MUN',
    search_zoom=10,
    weight=3
).add_to(m)
folium.LayerControl(collapsed=False).add_to(m)
m.save("SESVER.html")
