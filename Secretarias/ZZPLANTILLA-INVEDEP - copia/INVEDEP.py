# %%

import folium
import pandas as pd
import geopandas as gpd
from geopandas import GeoDataFrame
from folium.plugins import Search
import numpy as np
from pathlib import Path


from folium import FeatureGroup, LayerControl, Map, Marker

# %%
path_ini = Path("C:/ESyP/Mapas_COESPO/Resources/")
pd.options.display.float_format = '{:,.2f}'.format

df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
df_regiones = df

df_regiones.loc[df_regiones['region'] == 'Las_Montanas', 'region'] = 'Las Montañas'
df_regiones.loc[df_regiones['region'] == 'Huasteca_Alta', 'region'] = 'Huasteca Alta'
df_regiones.loc[df_regiones['region'] == 'Huasteca_Baja', 'region'] = 'Huasteca Baja'
df_regiones.loc[df_regiones['region'] == 'Los_Tuxtlas', 'region'] = 'Los Tuxtlas'
df_regiones['Color'] = 'grey'
df_regiones.loc[df_regiones['region'] == 'Capital', ['Color']] = '#e8694b'
df_regiones.loc[df_regiones['region'] == 'Huasteca Alta', ['Color']] = '#7cd5a3'
df_regiones.loc[df_regiones['region'] == 'Huasteca Baja', ['Color']] = '#96B921'
df_regiones.loc[df_regiones['region'] == 'Los_Tuxtla', ['Color']] = '#5bbdbf'
df_regiones.loc[df_regiones['region'] == 'Nautla', ['Color']] = '#FDAF3F'
df_regiones.loc[df_regiones['region'] == 'Los Tuxtlas', ['Color']] = '#5bbdbf'
df_regiones.loc[df_regiones['region'] == 'Olmeca', ['Color']] = '#d6ecf8'
df_regiones.loc[df_regiones['region'] == 'Papaloapan', ['Color']] = '#846789'
df_regiones.loc[df_regiones['region'] == 'Sotavento', ['Color']] = '#6e79c1'
df_regiones.loc[df_regiones['region'] == 'Totonaca', ['Color']] = '#D0D108'
df_regiones.loc[df_regiones['region'] == 'Las Montañas', ['Color']] = '#f3b8df'

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

# %%

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

# --- Pobreza Extrema
PE = gpd.read_file(Path.joinpath(path_ini, Path("GIS/PROGOB/Pobreza extrema/Pobreza extrema.shp")), encoding='utf8')
PE = PE.sort_values(by='Pobreza _2', ascending=False)
PE = PE.reset_index(drop=True)
PE['Pobreza _1'] = PE['Pobreza _1'].astype(int).apply(lambda x: "{:,}".format(x))
PE['Pobreza_Extrema'] = PE['Pobreza _2'].astype(float).apply(lambda x: "{:,.2f}%".format(x))
PE_20 = PE.iloc[:20]

# ---- Municipios Prioritarios
dfList = list(PE_20['NOMGEO'])
Municipios = df_regiones.loc[df_regiones['NOM_MUN'].isin(dfList)]

# ---- Pobreza
Pb = gpd.read_file(Path.joinpath(path_ini, "GIS/PROGOB/pobreza/pobreza.shp"), encoding='utf8')
dfList = list(PE_20['CVEGEO'])
Pb['pobreza _1'] = Pb['pobreza _1'].astype(int).apply(lambda x: "{:,}".format(x))
Pb['Pobreza'] = Pb['pobreza _2'].astype(float).apply(lambda x: "{:,.2f}%".format(x))
Pb_2 = Pb.loc[Pb['CVEGEO'].isin(dfList)]

# ---- Acceso Carretero
Carreteras = gpd.read_file(Path.joinpath(path_ini, "GIS/PROGOB/ACCES_CARRETERA/ACCES_CARRETERA/ACCESIBILIDAD_CARRETERA.shp"),encoding='utf8')
Carreteras['ACCES_CARR'] = Carreteras['ACCES_CARR'].str.rstrip('%').astype('float')
Carreteras['Acceso Carretero'] = Carreteras['ACCES_CARR'].astype(float).apply(lambda x: "{:,.2f}%".format(x))
Acceso_2 = Carreteras.loc[Carreteras['CVEGEO'].isin(dfList)]

# ---- Rezago Educativo
RezagoEducativo = gpd.read_file(Path.joinpath(path_ini, "GIS/PROGOB/rezago educativo/Rezago edu.shp"), encoding='utf8')
RezagoEducativo_1 = RezagoEducativo
RezagoEducativo_1 = RezagoEducativo_1.rename(columns={'rezago e_1': 'rezagoe_1', 'rezago e_2': 'rezagoe_2'})
RezagoEducativo_1['rezagoe_2'] = RezagoEducativo_1['rezagoe_2'].astype(int).apply(lambda x: "{:,}".format(x))
RezagoEducativo_1['Rezago_Educativo'] = RezagoEducativo_1['rezagoe_1'].astype(float).apply(
    lambda x: "{:,.2f}%".format(x))
RezagoEducativo_2 = RezagoEducativo_1.loc[RezagoEducativo_1['CVEGEO'].isin(dfList)]

# ---- Rezago Social
IRS_1 = gpd.read_file(Path.joinpath(path_ini, "GIS/PROGOB/IRS 2015 SHP/Indice_Rezago_Social.shp"), encoding='utf8')
IRS_1['IRS_2015'] = IRS_1['IRS_2015'].astype(float)
IRS_1['Rezago_Social'] = IRS_1['IRS_2015'].astype(float).apply(lambda x: "{:,.2f}".format(x))
IRS_2 = IRS_1.loc[IRS_1['CVEGEO'].isin(dfList)]

# ---- Marginación
Marginacion = gpd.read_file(Path.joinpath(path_ini, "GIS/PROGOB/marginacion/Shape de marginación.shp"), encoding='utf8')
Marginacion['Marginacion'] = Marginacion['Marginac_3'].astype(float).apply(lambda x: "{:,.2f}".format(x))
Marginacion_1 = Marginacion.loc[Marginacion['CVEGEO'].isin(dfList)]

from folium.plugins import FloatImage

LogoCOESPO = ('images/COESPO_Logo_3.png')
LogoPROGOB = (Path.joinpath(path_ini, 'GIS/PROGOB/PROGOB_Logo.png'))
Logos = (Path.joinpath(path_ini, 'GIS/PROGOB/Logo_3.png'))

# ---- ColorMap para Acceso Carretero----
from branca.colormap import linear

# cm = linear.YlGnBu_09.scale(
#   Carreteras.ACCES_CARR.min(),
#   Carreteras.ACCES_CARR.max())
# cm

cm_AccesoCarretero = folium.LinearColormap(['green', 'yellow', 'orange', 'red'], vmin=Carreteras.ACCES_CARR.min(),
                                           vmax=Carreteras.ACCES_CARR.max())
# cm_AccesoCarretero

# ---- ColorMap para Acceso Carretero----
from branca.colormap import linear

# cm = linear.YlGnBu_09.scale(
#   Carreteras.ACCES_CARR.min(),
#   Carreteras.ACCES_CARR.max())
# cm

cm_AccesoCarretero2 = folium.LinearColormap(['green', 'yellow', 'orange', 'red'], vmin=Carreteras.ACCES_CARR.min(),
                                            vmax=Carreteras.ACCES_CARR.max())
# cm_AccesoCarretero2

#### ------ ColorMap para Pobreza ---------
from branca.colormap import linear

cm_Pobreza = linear.YlOrRd_09.scale(
    Pb['pobreza _2'].min(),
    Pb['pobreza _2'].max())
# cm_Pobreza

#### ------ ColorMap para Pobreza Extrema ---------
from branca.colormap import linear

cm_PobrezaExtrema = linear.YlOrRd_09.scale(
    PE['Pobreza _2'].min(),
    PE['Pobreza _2'].max())
# cm_PobrezaExtrema

# ------ ColorMap para Rezago Educativo ---------
from branca.colormap import linear

cm_RezagoEducativo = linear.YlGn_09.scale(
    RezagoEducativo_1.rezagoe_1.min(),
    RezagoEducativo_1.rezagoe_1.max())
# cm_RezagoEducativo

# ----- ColorMap para Índice de Rezago Social -----
cm_RezagoSocial = folium.LinearColormap(['blue', 'yellow', 'red'], vmin=IRS_1.IRS_2015.min(), vmax=IRS_1.IRS_2015.max())
# cm_RezagoSocial

#### ------ ColorMap para Marginación ---------
from branca.colormap import linear

cm_Marginacion = linear.YlOrRd_09.scale(
    Marginacion['Marginac_3'].min(),
    Marginacion['Marginac_3'].max())

# %%

df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))

# %%

dfAccion1 = pd.read_csv("Accion1.csv")
df_mapaAccion1 = pd.merge(dfAccion1, df_Localidades, on="CVEGEO")

# %%

dfAccion2 = pd.read_csv("Accion2.csv")
df_mapaAccion2 = pd.merge(dfAccion2, df_Localidades, on="CVEGEO")

# %%

dfAccion3 = pd.read_csv("Accion3.csv")
df_mapaAccion3 = pd.merge(dfAccion3, df_Localidades, on="CVEGEO")

# %%

m = folium.Map(location=[19.8727, -96.1333], zoom_start=7, prefer_canvas=True, tiles='OpenStreetMap')
from folium.plugins import MarkerCluster

LayerAcciones1 = FeatureGroup(name='Caravanas Culturales', show=False)
LayerAcciones2 = FeatureGroup(name='Brigadas Itinerantes', show=False)
LayerAcciones3 = FeatureGroup(name='Capacitaciones', show=False)

# ---- Mapa Base de Veracruz

Veracruz = folium.GeoJson(
    df,
    name='Veracruz',
    control=False,
    style_function=lambda feature: {
        'fillColor': 'grey',
        'color': 'grey',
        'weight': 1,
        'fillOpacity': 0.0,
        'line_opacity': 0.0,
        'line_color': 'grey',
    }, tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Nombre Municipio:', 'Region:']),
).add_to(m)

from folium.plugins import FloatImage

LogoCOESPO = ('COESPO_Logo_3.png')
FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m)

# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster

mc_Accion1 = MarkerCluster()
mc_Accion2 = MarkerCluster()
mc_Accion3 = MarkerCluster()



for row in df_mapaAccion1.itertuples():
    icon_Dependencia = folium.features.CustomIcon('INVEDEP_MARCADOR.png', icon_size=(60, 60), icon_anchor=(22, 59),
                                                  popup_anchor=(3, -54))
    texto_mapa = "<b>Municipio: </b>" + row.nom_mun + "<br><b>Acciones: </b>" + str(row.ACCIONES) \
                 + "<br><b>Personas Atendidas: </b>" + str(row.PERSONAS_ATENDIDAS) \
                 + "<br><b>Cantidad de Peticiones Recibidas: </b>" + str(row.CANTIDAD_DE_PETICIONES_RECIBIDAS) \
                 + "<br><b>Tipo de Peticion más Frecuente: </b>" + str(row.TIPO_DE_PETICION_MAS_FRECUENTE)
    if row.FOTO != "0":
        texto_mapa = texto_mapa + '<br> Evidencia fotográfica en este <a href="' + row.FOTO + '"target="_blank">link</a><br>'
    popup = folium.Popup(html=texto_mapa, max_width='400')
    folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(mc_Accion1)

mc_Accion1.add_to(LayerAcciones1)

for row in df_mapaAccion2.itertuples():
    icon_Dependencia = folium.features.CustomIcon('INVEDEP_MARCADOR.png', icon_size=(60, 60), icon_anchor=(22, 59),
                                                  popup_anchor=(3, -54))
    texto_mapa = "<b>Municipio: </b>" + row.nom_mun + "<br><b>Acciones: </b>" + str(row.ACCIONES) \
                 + "<br><b>Fecha: </b>" + str(row.FECHA) \
                 + "<br><b>Personas Atendidas: </b>" + str(row.PERSONAS_ATENDIDAS) \
                 + "<br><b>Cantidad de Peticiones Recibidas: </b>" + str(row.CANTIDAD_DE_PETICIONES_RECIBIDAS) \
                 + "<br><b>Tipo de Peticion más Frecuente: </b>" + str(row.TIPO_DE_PETICION_MAS_FRECUENTE)
    if row.FOTO != "0":
        texto_mapa = texto_mapa + '<br> Evidencia fotográfica en este <a href="' + row.FOTO + '"target="_blank">link</a><br>'
    popup = folium.Popup(html=texto_mapa, max_width='400')
    folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(mc_Accion2)

mc_Accion2.add_to(LayerAcciones2)

for row in df_mapaAccion3.itertuples():
    icon_Dependencia = folium.features.CustomIcon('INVEDEP_MARCADOR.png', icon_size=(60, 60), icon_anchor=(22, 59),
                                                  popup_anchor=(3, -54))
    texto_mapa = "<b>Municipio: </b>" + row.nom_mun + "<br><b>Acciones: </b>" + str(row.ACCIONES) \
                 + "<br><b>Fecha: </b>" + str(row.FECHA) \
                 + "<br><b>Personas Capacitadas: </b>" + str(row.PERSONAS_CAPACITADAS) \
                 + "<br><b>Sector de Impacto: </b>" + str(row.SECTOR_DE_IMPACTO)
    if row.FOTO != "0":
        texto_mapa = texto_mapa + '<br> Evidencia fotográfica en este <a href="' + row.FOTO + '"target="_blank">link</a><br>'
    popup = folium.Popup(html=texto_mapa, max_width='400')
    folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(mc_Accion3)

mc_Accion3.add_to(LayerAcciones3)

# ---- Botón de Búsqueda de Municipio
statesearch = Search(
    layer=Veracruz,
    geom_type='Polygon',
    placeholder='Búsqueda de municipio',
    collapsed=True,
    search_label='NOM_MUN',
    search_zoom=10,
    weight=3
).add_to(m)

# ---- Control de Capas
# LayerAVGM.add_to(m)
# LayerPVD.add_to(m)
LayerAcciones1.add_to(m)
LayerAcciones2.add_to(m)
LayerAcciones3.add_to(m)

folium.LayerControl().add_to(m)

m.save("INVEDEP_AX.html")

# %%


