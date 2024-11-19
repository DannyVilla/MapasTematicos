import folium
import pandas as pd
import geopandas as gpd
from folium.plugins import Search
import branca
from pathlib import Path
from Funciones import *

from folium import FeatureGroup

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
LogoCOESPO = ('images/COESPO_Logo_3.png')

# %%  LECTURA DE DATAFRAMES
df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))

#df_agronegocios2021 = pd.read_excel("SEDARPA_AGRONEGOCIO_OK.xlsx", sheet_name='2021')
#df_agronegocios2022 = pd.read_excel("SEDARPA_AGRONEGOCIO_OK.xlsx", sheet_name='2022')
df_agronegocios21a22 = pd.read_excel("SEDARPA_AGRONEGOCIO_OK.xlsx", sheet_name='2021-2023')
#df_agricultura19 = pd.read_excel("SEDARPA_AGRICULTURA_OK.xlsx", sheet_name='2019')
#df_agricultura20 = pd.read_excel("SEDARPA_AGRICULTURA_OK.xlsx", sheet_name='2020')
#df_agricultura21 = pd.read_excel("SEDARPA_AGRICULTURA_OK.xlsx", sheet_name='2021') NO SE REPORTARON ACCIONES
#df_agricultura22 = pd.read_excel("SEDARPA_AGRICULTURA_OK.xlsx", sheet_name='2022')
df_agricultura19a22 = pd.read_excel("SEDARPA_AGRICULTURA_OK.xlsx", sheet_name='2019-2023')
#df_desarrollo19 = pd.read_excel("SEDARPA_DESARROLLO_RURAL_OK.xlsx", sheet_name='2019')
#df_desarrollo20 = pd.read_excel("SEDARPA_DESARROLLO_RURAL_OK.xlsx", sheet_name='2020')
#df_desarrollo21 = pd.read_excel("SEDARPA_DESARROLLO_RURAL_OK.xlsx", sheet_name='2021')
#df_desarrollo22 = pd.read_excel("SEDARPA_DESARROLLO_RURAL_OK.xlsx", sheet_name='2022')
df_DesarrolloR19a22 = pd.read_excel("SEDARPA_DESARROLLO_RURAL_OK.xlsx", sheet_name='2019-2023')
#df_ganaderia19 = pd.read_excel("SEDARPA_GANADERIA 2019_2020_OK.xlsx", sheet_name='2019')
#df_ganaderia20 = pd.read_excel("SEDARPA_GANADERIA 2019_2020_OK.xlsx", sheet_name='2020')
#df_ganaderia21 = pd.read_excel("SEDARPA_GANADERIA 2019_2020_OK.xlsx", sheet_name='2021')
df_ganaderia19a22 = pd.read_excel("SEDARPA_GANADERIA 2019_2020_OK.xlsx", sheet_name='2019-2023')
#df_infraestructura19 = pd.read_excel("SEDARPA_INFRAESTRUCTURA RURAL2019_2020_OK.xlsx", sheet_name='2019')
#df_infraestructura20 = pd.read_excel("SEDARPA_INFRAESTRUCTURA RURAL2019_2020_OK.xlsx", sheet_name='2020')
#df_infraestructura21 = pd.read_excel("SEDARPA_INFRAESTRUCTURA RURAL2019_2020_OK.xlsx", sheet_name='2021')
df_infraestructura19a22 = pd.read_excel("SEDARPA_INFRAESTRUCTURA RURAL2019_2020_OK.xlsx", sheet_name='2019-2023')
#df_pesca19 = pd.read_excel("SEDARPA_PESCA Y ACUACULTURA_OK.xlsx", sheet_name='2019')
#df_pesca20 = pd.read_excel("SEDARPA_PESCA Y ACUACULTURA_OK.xlsx", sheet_name='2020')
#df_pesca21 = pd.read_excel("SEDARPA_PESCA Y ACUACULTURA_OK.xlsx", sheet_name='2021') NO SE REPORTARON ACCIONES
#df_pesca22 = pd.read_excel("SEDARPA_PESCA Y ACUACULTURA_OK.xlsx", sheet_name='2022')
df_pesca19a22 = pd.read_excel("SEDARPA_PESCA Y ACUACULTURA_OK.xlsx", sheet_name='2019-2023')

#Acciones 2021
df_acciones2021 = pd.read_excel("SEDARPA_ACCIONES_2021.xlsx", sheet_name='SEDARPA 2021')
df_acciones2021 = pd.merge(df_acciones2021, df_Localidades, on="CVEGEO")

# se agregan lat y long a los datos
#df_agronegocios2021 = pd.merge(df_agronegocios2021, df_Localidades, on="CVEGEO")
#df_agronegocios2022 = pd.merge(df_agronegocios2022, df_Localidades, on="CVEGEO")
df_agronegocios21a22 = pd.merge(df_agronegocios21a22, df_Localidades, on="CVEGEO")
#df_agricultura19 = pd.merge(df_agricultura19, df_Localidades, on="CVEGEO")
#df_agricultura20 = pd.merge(df_agricultura20, df_Localidades, on="CVEGEO")
#df_agricultura22 = pd.merge(df_agricultura22, df_Localidades, on="CVEGEO")
df_agricultura19a22 = pd.merge(df_agricultura19a22, df_Localidades, on="CVEGEO")
#df_desarrollo19 = pd.merge(df_desarrollo19, df_Localidades, on="CVEGEO")
#df_desarrollo20 = pd.merge(df_desarrollo20, df_Localidades, on="CVEGEO")
#df_desarrollo21 = pd.merge(df_desarrollo21, df_Localidades, on="CVEGEO")
#df_desarrollo22 = pd.merge(df_desarrollo22, df_Localidades, on="CVEGEO")
df_DesarrolloR19a22 = pd.merge(df_DesarrolloR19a22, df_Localidades, on="CVEGEO")
#df_ganaderia19 = pd.merge(df_ganaderia19, df_Localidades, on="CVEGEO")
#df_ganaderia20 = pd.merge(df_ganaderia20, df_Localidades, on="CVEGEO")
#df_ganaderia21 = pd.merge(df_ganaderia21, df_Localidades, on="CVEGEO")
df_ganaderia19a22 = pd.merge(df_ganaderia19a22, df_Localidades, on="CVEGEO")
#df_infraestructura19 = pd.merge(df_infraestructura19, df_Localidades, on="CVEGEO")
#df_infraestructura20 = pd.merge(df_infraestructura20, df_Localidades, on="CVEGEO")
#df_infraestructura21 = pd.merge(df_infraestructura21, df_Localidades, on="CVEGEO")
df_infraestructura19a22 = pd.merge(df_infraestructura19a22, df_Localidades, on="CVEGEO")
#df_pesca19 = pd.merge(df_pesca19, df_Localidades, on="CVEGEO")
#df_pesca20 = pd.merge(df_pesca20, df_Localidades, on="CVEGEO")
#df_pesca22 = pd.merge(df_pesca22, df_Localidades, on="CVEGEO")
df_pesca19a22 = pd.merge(df_pesca19a22, df_Localidades, on="CVEGEO")

# Se modifican los textos
df.loc[df['region'] == 'Las_Montanas', 'region'] = 'Las Montañas'
df.loc[df['region'] == 'Huasteca_Alta', 'region'] = 'Huasteca Alta'
df.loc[df['region'] == 'Huasteca_Baja', 'region'] = 'Huasteca Baja'
df.loc[df['region'] == 'Los_Tuxtlas', 'region'] = 'Los Tuxtlas'
pd.set_option('max_columns', None)

# Se definen colores para cada region
df.loc[df['region'] == 'Capital', ['Color']] = '#e8694b'
df.loc[df['region'] == 'Huasteca Alta', ['Color']] = '#7cd5a3'
df.loc[df['region'] == 'Huasteca Baja', ['Color']] = '#96B921'
df.loc[df['region'] == 'Los_Tuxtla', ['Color']] = '#5bbdbf'
df.loc[df['region'] == 'Nautla', ['Color']] = '#FDAF3F'
df.loc[df['region'] == 'Los Tuxtlas', ['Color']] = '#5bbdbf'
df.loc[df['region'] == 'Olmeca', ['Color']] = '#4f46FF'
df.loc[df['region'] == 'Papaloapan', ['Color']] = '#846789'
df.loc[df['region'] == 'Sotavento', ['Color']] = '#6e79c1'
df.loc[df['region'] == 'Totonaca', ['Color']] = '#D0D108'
df.loc[df['region'] == 'Las Montañas', ['Color']] = '#f3b8df'

m = folium.Map(location=[19.8727, -96.1333], zoom_start=7, prefer_canvas=True, tiles='OpenStreetMap')

# ---- Mapa Base de Veracruz
colores = df.set_index("CVE_MUN")["Color"]

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
    df,
    name='Base',
    highlight_function=highlight,
    style_function=style_function,
    control=False,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'region'], aliases=['Nombre Municipio:', 'Región:']),
).add_to(m)

# ---- Imagen inferior izquierda logo COESPO
from folium.plugins import FloatImage

FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m)

# ---- Capas
#layer_agronegocios_2021 = FeatureGroup(name='Agronegocios 2021', show=False)
#layer_agronegocios_2022 = FeatureGroup(name='Agronegocios 2022', show=False)
layer_agronegocios_21_22 = FeatureGroup(name='Agronegocios 2021-2024', show=False)
#layer_agricultura_2019 = FeatureGroup(name='Agricultura 2019', show=False)
#layer_agricultura_2020 = FeatureGroup(name='Agricultura 2020', show=False)
#layer_agricultura_2022 = FeatureGroup(name='Agricultura 2022', show=False)
layer_Agricultura_19_22 = FeatureGroup(name='Agricultura 2019-2024', show=False)
#layer_DesarrolloR_2019 = FeatureGroup(name='Desarrollo Rural 2019', show=False)
#layer_DesarrolloR_2020 = FeatureGroup(name='Desarrollo Rural 2020', show=False)
#layer_DesarrolloR_2021 = FeatureGroup(name='Desarrollo Rural 2021', show=False)
#layer_DesarrolloR_2022 = FeatureGroup(name='Desarrollo Rural 2022', show=False)
layer_DesarrolloR_19_22 = FeatureGroup(name='Desarrollo Rural 2019-2024', show=False)
#layer_Ganaderia_2019 = FeatureGroup(name='Ganadería 2019', show=False)
#layer_Ganaderia_2020 = FeatureGroup(name='Ganadería 2020', show=False)
#layer_Ganaderia_2021 = FeatureGroup(name='Ganadería 2021', show=False)
layer_Ganaderia_19_22 = FeatureGroup(name='Ganadería 2019-2024', show=False)
#layer_Infraestructura_2019 = FeatureGroup(name='Infraestructura Rural 2019', show=False)
#layer_Infraestructura_2020 = FeatureGroup(name='Infraestructura Rural 2020', show=False)
#layer_Infraestructura_2021 = FeatureGroup(name='Infraestructura Rural 2021', show=False)
layer_Infraestructura_19_22 = FeatureGroup(name='Infraestructura Rural 2019-2024', show=False)
#layer_Pesca_2019 = FeatureGroup(name='Pesca y Acuaculturar 2019', show=False)
#layer_Pesca_2020 = FeatureGroup(name='Pesca y Acuaculturar 2020', show=False)
#layer_Pesca_2022 = FeatureGroup(name='Pesca y Acuaculturar 2022', show=False)
layer_Pesca_19_22 = FeatureGroup(name='Pesca y Acuacultura 2019-2024', show=False)

layer_Acciones = FeatureGroup(name='Acciones SEDARPA 2021', show=False)

pd.set_option('display.max_columns', None)

# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster

#mc_agricultura19 = MarkerCluster()
#mc_agricultura20 = MarkerCluster()
#mc_agricultura22 = MarkerCluster()
mc_agricultura19_22 = MarkerCluster()
#mc_desarrolloR19 = MarkerCluster()
#mc_desarrolloR20 = MarkerCluster()
#mc_desarrolloR21 = MarkerCluster()
#mc_desarrolloR22 = MarkerCluster()
mc_DesarrolloR19_22 = MarkerCluster()
#mc_ganaderia19 = MarkerCluster()
#mc_ganaderia20 = MarkerCluster()
#mc_ganaderia21 = MarkerCluster()
mc_ganaderia19_22 = MarkerCluster()
#mc_infraestructura19 = MarkerCluster()
#mc_infraestructura20 = MarkerCluster()
#mc_infraestructura21 = MarkerCluster()
mc_infraestructura19_22 = MarkerCluster()
#mc_pesca19 = MarkerCluster()
#mc_pesca20 = MarkerCluster()
#mc_pesca22 = MarkerCluster()
mc_pesca19_22 = MarkerCluster()
#mc_agronegocios21 = MarkerCluster()
#mc_agronegocios22 = MarkerCluster()
mc_agronegocios21_22 = MarkerCluster()

mc_acciones21 = MarkerCluster()

def funcion(df_in):

    for row in df_in.itertuples():
        contenido = genera_acciones(str (row.MUNICIPIO), str(row.TITULO), str(row.FECHA), str(row.CLASIFICACION),
                                      str(row.ENLACEPUB),str(row.ENLACEFOT1),str(row.ENLACEFOT2),str(row.URL))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/SEDARPA_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_acciones21)
funcion(df_acciones2021)

def genera_agricultura(df_in, mc):

    for row in df_in.itertuples():
        contenido = tarjeta_agricultura(row)
        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/SEDARPA_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)
genera_agricultura(df_agricultura19a22, mc_agricultura19_22)
#genera_agricultura(df_agricultura19, '2019')
#genera_agricultura(df_agricultura20, '2020')
#genera_agricultura(df_agricultura22, '2022')

def genera_DesarrolloR(df_in, mc):

    for row in df_in.itertuples():
        contenido = tarjeta_desarrolloR(row)

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/SEDARPA_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)
#genera_capa(df_desarrollo19, '2019', mc_desarrolloR19)
#genera_capa(df_desarrollo20, '2020', mc_desarrolloR20)
#genera_capa(df_desarrollo21, '2021', mc_desarrolloR21)
#genera_capa(df_desarrollo22, '2022', mc_desarrolloR22)
genera_DesarrolloR(df_DesarrolloR19a22, mc_DesarrolloR19_22)

def genera_pesca_acuacultura(df_in, mc):

    for row in df_in.itertuples():
        contenido = tarjeta_pesca_acuacultura(row)

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/SEDARPA_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
            mc)
#genera_capa(df_pesca19, '2019', mc_pesca19)
#genera_capa(df_pesca20, '2020', mc_pesca20)
#genera_capa(df_pesca22, '2022', mc_pesca22)
genera_pesca_acuacultura(df_pesca19a22, mc_pesca19_22)

def genera_infraestructura(df_in, mc):
    for row in df_in.itertuples():
        contenido = tarjeta_infraestructura(row)

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/SEDARPA_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
        mc)
#genera_capa(df_infraestructura19, '2019', mc_infraestructura19)
#genera_capa(df_infraestructura20, '2020', mc_infraestructura20)
genera_infraestructura(df_infraestructura19a22, mc_infraestructura19_22)

def genera_ganaderia(df_in, mc):
    for row in df_in.itertuples():
        contenido = tarjeta_ganaderia(row)

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/SEDARPA_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),

                                                      popup_anchor=(3, -54))

        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
        mc)
#genera_ganaderia(df_ganaderia19, '2019', mc_ganaderia19)
#genera_ganaderia(df_ganaderia20, '2020', mc_ganaderia20)
#genera_ganaderia(df_ganaderia21, '2021', mc_ganaderia21)
genera_ganaderia(df_ganaderia19a22, mc_ganaderia19_22)

def genera_agronegocios(df_in, mc):
    for row in df_in.itertuples():
        contenido = tarjeta_agronegocios(row)

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/SEDARPA_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
        mc)
#genera_Agronegocios(df_agronegocios2021, mc_agronegocios21, '2021')
#genera_Agronegocios(df_agronegocios2022, mc_agronegocios22, '2022')
genera_agronegocios(df_agronegocios21a22, mc_agronegocios21_22)


#mc_agronegocios21.add_to(layer_agronegocios_2021)
#mc_agronegocios22.add_to(layer_agronegocios_2022)
mc_agronegocios21_22.add_to(layer_agronegocios_21_22)
#mc_agricultura19.add_to(layer_agricultura_2019)
#mc_agricultura20.add_to(layer_agricultura_2020)
#mc_agricultura22.add_to(layer_agricultura_2022)
mc_agricultura19_22.add_to(layer_Agricultura_19_22)
#mc_desarrolloR19.add_to(layer_DesarrolloR_2019)
#mc_desarrolloR20.add_to(layer_DesarrolloR_2020)
#mc_desarrolloR21.add_to(layer_DesarrolloR_2021)
#mc_desarrolloR22.add_to(layer_DesarrolloR_2022)
mc_DesarrolloR19_22.add_to(layer_DesarrolloR_19_22)
#mc_ganaderia19.add_to(layer_Ganaderia_2019)
#mc_ganaderia20.add_to(layer_Ganaderia_2020)
#mc_ganaderia21.add_to(layer_Ganaderia_2021)
mc_ganaderia19_22.add_to(layer_Ganaderia_19_22)
#mc_infraestructura19.add_to(layer_Infraestructura_2019)
#mc_infraestructura20.add_to(layer_Infraestructura_2020)
#mc_infraestructura21.add_to(layer_Infraestructura_2021)
mc_infraestructura19_22.add_to(layer_Infraestructura_19_22)
#mc_pesca19.add_to(layer_Pesca_2019)
#mc_pesca20.add_to(layer_Pesca_2020)
#mc_pesca22.add_to(layer_Pesca_2022)
mc_pesca19_22.add_to(layer_Pesca_19_22)



#layer_agronegocios_2021.add_to(m)
#layer_agronegocios_2022.add_to(m)
layer_agronegocios_21_22.add_to(m)
#mc_acciones21.add_to(layer_Acciones)
#layer_agricultura_2019.add_to(m)
#layer_agricultura_2020.add_to(m)
#layer_agricultura_2022.add_to(m)
layer_Agricultura_19_22.add_to(m)
#layer_DesarrolloR_2019.add_to(m)
#layer_DesarrolloR_2020.add_to(m)
#layer_DesarrolloR_2021.add_to(m)
#layer_DesarrolloR_2022.add_to(m)
layer_DesarrolloR_19_22.add_to(m)
#layer_Ganaderia_2019.add_to(m)
#layer_Ganaderia_2020.add_to(m)
#layer_Ganaderia_2021.add_to(m)
layer_Ganaderia_19_22.add_to(m)
#layer_Infraestructura_2019.add_to(m)
#layer_Infraestructura_2020.add_to(m)
#layer_Infraestructura_2021.add_to(m)
layer_Infraestructura_19_22.add_to(m)
#layer_Pesca_2019.add_to(m)
#layer_Pesca_2020.add_to(m)
#layer_Pesca_2022.add_to(m)
layer_Pesca_19_22.add_to(m)

#layer_Acciones.add_to(m)

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
m.save("SEDARPA.html")

