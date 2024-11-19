import requests
import time

# %%
from pathlib import Path
import geopandas as gpd
import pandas as pd

path_ini = Path("C:/ESyP/Mapas_COESPO/Resources/")
#path_ini = Path("/Users/4x/COESPOAX/MapasTematicos/Resources")
pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('max_columns', None)
df = gpd.read_file(Path.joinpath(path_ini, Path("Veracruz/Veracruz_Shape1.shp")))
#print(df)
df_Localidades = pd.read_csv(Path.joinpath(path_ini, "cabeceras (localidades).csv"))



df_actividades_2023= pd.read_excel("SECRETARIO_SCRAPP.xlsx", sheet_name='SECRETARIO_2022')


tst=" "
url2= "https://www.facebook.com/plugins/post.php?href=https%3A%2F%2F"

#credentials = {"user": "username", "pass": "password"}
#response = requests.get(url, auth=("_DEMOPOC", "Demo123S"), headers=headers)


for index, row in df_actividades_2023.interrows():
    print(row['ObjectID'])
    x = requests.post(url2,data={
        'ObjectID': row['ObjectID']
    })

    time.sleep(1)
    if x.status_code == 200:
        print("Correcto ".format(row['ObjectID']))
    else:
        print("Falló")



