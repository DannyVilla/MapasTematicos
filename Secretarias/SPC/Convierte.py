# %%

import pandas as pd

# %%

# %%  LECTURA DE DATAFRAMES

df_refugios = pd.read_excel("REFUGIOS.xlsx", sheet_name='CONVERTIR')


def conversion(old):
    direction = {'N': -1, 'S': 1, 'E': -1, 'W': 1}
    new = old.replace(u'°', ' ').replace('\'', ' ').replace('"', ' ')
    new = new.split()
    new_dir = new.pop()
    new.extend([0, 0, 0])
    return (int(new[0]) + int(new[1]) / 60.0 + float(new[2]) / 3600.0) * direction[new_dir]


def refugio(df_in):
    # latitudes = [u'''19°0'4"N''', u'''18°54'25"N''', u'''19°0'4"N''', u'''19°0'45"N''', u'''18°55'42"N''',
    #              u'''18°53'41"N''', u'''18°57'6"N''', u'''18°56'40"N''', u'''18°55'42"N''', u'''21°11'14.90"N''',
    #              u'''21°11'02.01"N''', u'''21°11'58.46"N''', u'''19°0'54"N''', u'''18°58'28"N''', u'''21°17'28.8"N''',
    #              u'''21°17'02.6"N''', u'''21°16'46.54"N''', u'''21°15'29.51"N''', u'''21°25'78.54"N''']
    # for lat in latitudes:
    #     print(conversion(lat))
    latitudes = []
    longitudes = []

    for row in df_in.itertuples():
        lat = str(row.LAT)
        lon = str(row.LON)
        latitud = conversion(str(row.LAT))
        longitud = conversion(str(row.LON))
        latitudes.append(latitud)
        longitudes.append(longitudes)
        print(longitud)

        # contenido = genera_refugio(str(row.MUNICIPIO), str(row.NOMBRE), str(row.DIRECCION),
        #                            str(row.CAPACIDAD), str(row.FOTO))
        #
        # popup = folium.Popup(html=contenido, max_width='400')
        # icon_Dependencia = folium.features.CustomIcon('images/PC_marcador.png', icon_size=(60, 60),
        #                                               icon_anchor=(22, 59),
        #                                               popup_anchor=(3, -54))
        # folium.Marker(location=[row.LAT, row.LON], popup=popup, icon=icon_Dependencia).add_to(
        #     mc)


refugio(df_refugios)

# lat, lon = u'''0°25'30"S, 91°7'W'''.split(', ')
