from pathlib import Path
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

df['CVEGEO'] = df.apply(lambda row: row.CVE_ENT + row.CVE_MUN, axis=1)
df['CVEGEO'] = df['CVEGEO'].apply(pd.to_numeric, errors='coerce')
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

LogoCOESPO = ('images/COESPO_Logo_3.png')
LogoPROGOB = (Path.joinpath(path_ini, 'GIS/PROGOB/PROGOB_Logo.png'))
Logos = (Path.joinpath(path_ini, 'GIS/PROGOB/Logo_3.png'))

df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))

df_capacitaciones = pd.read_csv("SSP_OK.csv", encoding='UTF8')
df_capacitaciones = pd.merge(df_capacitaciones, df_Localidades, on="CVEGEO")
df_c4 = pd.read_excel("directorio_SSP_OK.xlsx", sheet_name='C4')
df_dgt_oficinas = pd.read_excel("directorio_SSP_OK.xlsx", sheet_name='DGT-OFICINAS')
df_centros = pd.read_excel("directorio_SSP_OK.xlsx", sheet_name='CENTROS_PENITENCIARIOS')
df_licencias = pd.read_excel("directorio_SSP_OK.xlsx", sheet_name='DGT_MOD_LIC')
df_cobertura_del = pd.read_excel("directorio_SSP_OK.xlsx", sheet_name='COBERTURA_DELEG')
df_cobertura_c4 = pd.read_excel("directorio_SSP_OK.xlsx", sheet_name='COBERTURA_C4')
df_acciones_2022 = pd.read_excel("ACCIONES_2022.xlsx", sheet_name='2022')

df_cobertura_del = pd.merge(df, df_cobertura_del, on="CVEGEO")
df_cobertura_c4 = pd.merge(df, df_cobertura_c4, on="CVEGEO")
df_acciones_2022 = pd.merge(df_acciones_2022, df_Localidades, on="CVEGEO")

#Quitar time a date y se convierte en datatime
df_acciones_2022['FECHA'] = df_acciones_2022['FECHA'].dt.strftime('%d/%m/%Y')

# %% CAMBIAR TIPO DE STR A NUMERO PARA LATITUD Y LONGITUD
df_dgt_oficinas['LAT'] = df_dgt_oficinas['LAT'].apply(pd.to_numeric, errors='coerce')
df_dgt_oficinas['LON'] = df_dgt_oficinas['LON'].apply(pd.to_numeric, errors='coerce')

m = folium.Map(location=[19.8727, -96.1333], zoom_start=7, prefer_canvas=True, tiles='OpenStreetMap')

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

## ---- Mapa # ---Cobertura delegaciones de tránsito
colores = df_cobertura_del.set_index("CVE_MUN")["COLOR"]

def colorscale(color):
    return '"' + color + '"'

def style_function(feature):
    color = colores.get(int(feature["id"][-3:]), None)
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
    df_cobertura_del,
    name='Cobertura por Delegaciones de Tránsito',
    highlight_function=highlight,
    style_function=style_function,
    control=True,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'DELEGACION'],
                                           aliases=['Nombre Municipio:', 'Delegación:']),
).add_to(m)



colores_c4 = df_cobertura_c4.set_index("CVE_MUN")["COLOR"]
def colorscale(color):
    return '"' + color + '"'

def style_function_c4(feature):
    color = colores_c4.get(int(feature["id"][-3:]), None)
    return {
        "fillOpacity": 0.6,
        "weight": 0,
        "fillColor": color,
        "color": color,
        'line_opacity': 0.2,
    }

# ---- Imagen inferior izquierda logo COESPO
from folium.plugins import FloatImage

LogoCOESPO = ('images/COESPO_Logo_3.png')
FloatImage(LogoCOESPO, bottom=3, left=0).add_to(m)
# ---- Capas
Layer2019 = FeatureGroup(name='Capacitaciones 2019', show=False)
Layer2020 = FeatureGroup(name='Capacitacones 2020', show=False)
LayerC4 = FeatureGroup(name='Centro y Subcentros C4', show=False)
LayerDGT_OFICINAS = FeatureGroup(name='Directorio Oficinas Tránsito', show=False)
LayerCENTROS_PENITENCIARIOS = FeatureGroup(name='Directorio Centros Penitenciarios', show=False)
LayerDGT_MOD_LIC = FeatureGroup(name='Módulos de Licencias', show=False)
LayerActividades_2022 = FeatureGroup(name='Acciones 2022', show=False)

# ---- Marcadores de las actividades
from folium.plugins import MarkerCluster

mc_cap2019 = MarkerCluster()
mc_cap2020 = MarkerCluster()
mc_C4 = MarkerCluster()
mc_DGT_OFICINAS = MarkerCluster()
mc_CENTROS_PENITENCIARIOS = MarkerCluster()
mc_DGT_MOD_LIC = MarkerCluster()
mc_acciones = MarkerCluster()

def genera_capacitaciones(df_in):
    for row in df_in.itertuples():
        icon_Dependencia = folium.features.CustomIcon('images/' + str(row.MARCADOR) + '.PNG', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))
        contenido = content_capacitaciones(str(row.MUNICIPIO), str(row.TEMA), str(row.H),
                                           str(row.M), str(row.T))

        if row.ANIO == 2019:
            popup = folium.Popup(html=contenido,max_width='290')
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_cap2019)
        if row.ANIO == 2020:
            popup = folium.Popup(html=contenido,max_width='290')
            folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_cap2020)

def genera_tarjeta(df_in, mc):
    for reg in df_in.itertuples():
        contenido = content_tarjeta(str(reg.MUNICIPIO), str(reg.DIRECCION), str(reg.TEL),
                                    str(reg.FOTO))
        icon_Dependencia = folium.features.CustomIcon('images/SSP_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        popup = folium.Popup(html=contenido)
        folium.Marker(location=[reg.LAT, reg.LON], popup=popup, icon=icon_Dependencia).add_to(
            mc)


def genera_licencias(df_in, mc):
    for reg in df_in.itertuples():
        contenido = content_licencias(str(reg.MUNICIPIO), str(reg.DIRECCION), str(reg.TEL),
                                      str(reg.FOTO))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/SSP_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))


        folium.Marker(location=[reg.LAT, reg.LON], popup=popup, icon=icon_Dependencia).add_to(
            mc)


def genera_acciones(df_in):
    for row in df_in.itertuples():
        contenido = genera_acciones_2022(str (row.MUNICIPIO), str(row.TITULO), str(row.FECHA),
                                      str(row.ENLACEPUB),str(row.ENLACEFOT))

        popup = folium.Popup(html=contenido, max_width='290')
        icon_Dependencia = folium.features.CustomIcon('images/SSP_Marcador.png', icon_size=(60, 60),
                                                      icon_anchor=(22, 59),
                                                      popup_anchor=(3, -54))

        folium.Marker(location=[row.lat_decimal, row.lon_decimal], popup=popup, icon=icon_Dependencia).add_to(
                mc_acciones)

genera_capacitaciones(df_capacitaciones)
genera_tarjeta(df_c4, mc_C4)
genera_tarjeta(df_dgt_oficinas, mc_DGT_OFICINAS)
genera_tarjeta(df_centros, mc_CENTROS_PENITENCIARIOS)
genera_licencias(df_licencias, mc_DGT_MOD_LIC)
genera_acciones(df_acciones_2022)

mc_cap2019.add_to(Layer2019)
mc_cap2020.add_to(Layer2020)

mapa_c4 = folium.GeoJson(
    df_cobertura_c4,
    name='Cobertura Centros C4',
    highlight_function=highlight,
    style_function=style_function_c4,
    control=True,
    tooltip=folium.features.GeoJsonTooltip(fields=['NOM_MUN', 'SUBCENTRO'],
                                           aliases=['Nombre del Municipio:', 'Subcentro:']),
).add_to(m)
mc_C4.add_to(LayerC4)
mc_DGT_OFICINAS.add_to(LayerDGT_OFICINAS)
mc_CENTROS_PENITENCIARIOS.add_to(LayerCENTROS_PENITENCIARIOS)
mc_DGT_MOD_LIC.add_to(LayerDGT_MOD_LIC)
mc_acciones.add_to(LayerActividades_2022)

#Layer2019.add_to(m)
#Layer2020.add_to(m)
LayerC4.add_to(m)
LayerDGT_OFICINAS.add_to(m)
LayerCENTROS_PENITENCIARIOS.add_to(m)
LayerDGT_MOD_LIC.add_to(m)
#LayerActividades_2022.add_to(m)

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
m.save("SSP.html")
