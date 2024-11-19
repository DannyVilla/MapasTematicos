from pathlib import Path

import folium
import geopandas as gpd
import pandas as pd
from folium import FeatureGroup
from folium.plugins import Search

#Directorio MAC
path_ini = Path("/Users/4x/COESPOAX/MapasTematicos/Resources/")


df_centros = pd.read_excel("directorio_SSP_OK.xlsx", sheet_name='CENTROS_PENITENCIARIOS')

#Quitar time a date y se convierte en datatime
df['Value'] = df['Value'].dt.strftime('%d/%m/%Y')

# , a miles
def format(x):
    return "{:,}".format(x)
df_obras2019['BENEFICIADOS'] = df_obras2019['BENEFICIADOS'].apply(format)

# Cambiar formato de columna
df['Value'] = df.apply(lambda x: "{:,}".format(x['Value']), axis=1)
df['Value'] = df.apply(lambda x: "${:,}".format(x['Value']), axis=1)


def format(x):
    return "${:.1f}K".format(x / 1000)


df = pd.DataFrame(
    {'A': ['A', 'B', 'C', 'D'],
     'C': [12355.00, 12555.67, 640.00, 7000]
     })
df['C'] = df['C'].apply(format)

print(df)

# imprimir tipo de campos
print(df.dtypes)

#Cambiar tipo a varias columnas
cols = ['DEFUNCIONES', 'EDAS', 'IRAS', 'BCG', 'PENTA', 'HB', 'RV5', 'NC', 'RV1', 'HEX', 'HIP', 'OBE', 'DIS', 'TUB',
        'LEP', 'BRU', 'EPOC', 'LEPTO', 'CH', 'IMC', 'VIH', 'UAA', 'MANT', 'PREV', 'PART', 'PARTC', 'ELAB', 'TRAT',
        'CIRU', 'CONSUL', 'ANTIRR', 'ITS', 'LEHIS',
        ]
df[cols] = df[cols].applymap(np.int64)

#Guardar DataFrame a Excel
df.to_excel("Veracruz.xlsx")

#Cambiar tipo de columna OBJ a numerico
print(df.dtypes)
df['CVEGEO'] = df['CVEGEO'].apply(pd.to_numeric, errors='coerce')
print(df.dtypes)

Botstrap 3.2

# iCONO TELEFONO glyphicon glyphicon-earphone
# icono Usuario glyphicon glyphicon-user

Bootstrap 4.0 +
# iCONO TELEFONO fa fa-earphone
# icono Usuario fa fa-user

#Estilo de tablas en Bootstrap 4.0 +
	<table id=aplicaciones class="table table-hover table-sm" style="font-family:sans-serif; font-size:11px;color:#FFFFFF; background-color:#984063;"> 


#DIMENCIONES VIDEO YOUTUBE <iframe width="250" height="150">

#FORMATO DE HORA Y FECHA
df['FECHA'] = df['FECHA'].dt.strftime('%d/%m/%Y')

#FORMATOS PARA LOGOS (iconos fa fa , antes glyplicons)
<i class="fa fa-calendar"></i> #FECHA
<i class="fa fa-home"></i> #DIRECCIÓN
<i class="fa fa-phone"></i> #TELEFONO
<i class="fa fa-user"></i> #USUARIO

# filter data frame
New_df = df.loc[df["DOB"] >= "1999-02-5"]






inicio = datetime.datetime(2023, 5, 28)

log = ' '
name = ' '
paginas = ["EricCisnerosB"]

def extraer_lista(paginas):

    for nombre in paginas:
        i = 0
        #df = pd.DataFrame()
        url = []
        photo = []
        images = []
        descripcion = []
        timestamp = []
        fecha = []

        print('Iniciando generación de publicaciones para: ' + nombre)

        for post in get_posts(nombre, pages=10, credentials=(log, name), timeout=120, options={"allow_extra_requests": False, "posts_per_page": 250}):
            url.append(post['post_url'])
            photo.append(post['image_lowquality'])
            images.append(post['images_lowquality'])
            descripcion.append(post['post_text'])
            timestamp.append(post['timestamp'])
            fecha.append(post['time'])

            if (post['time'] < inicio):
                print('Última publicación registrada:   fecha:' + str(post['time']))
                list_tuples = list(zip(url, photo, images, descripcion, timestamp, fecha))

                df = pd.DataFrame(list_tuples,
                                  columns=['URL', 'FOTO', 'IMAGENES', 'DESCRIPCION','TIME', 'FECHA'])
                df.to_excel("Scraper.xlsx")
                break
            i = i + 1

        print('Se han registrado: ' + str(i) + 'publicaciones Para: ' +nombre +' última fecha:' + str(post['time']))


extraer_lista(paginas)