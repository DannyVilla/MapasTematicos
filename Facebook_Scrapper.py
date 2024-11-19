import pandas as pd
import datetime
from facebook_scraper import get_posts

log = 'usuario.scrapper.2024@outlook.com'
name = 'prueba12345'
paginas = ["100063610446927"]

def extraer_lista(paginas):
    inicio = datetime.datetime(2024, 7, 3)

    print(paginas)
    for nombre in paginas:
        i = 0
        #df = pd.DataFrame()
        url = []
        descripcion = []
        timestamp = []
        fecha = []

        print('Iniciando generación de publicaciones para: ' + nombre)

        variable = get_posts(nombre, pages=200, credentials=(log, name), timeout=500, options={"allow_extra_requests": False, "posts_per_page": 100})
        print(variable)

        try:
            for post in get_posts(nombre, pages=200, credentials=(log, name), timeout=500, options={"allow_extra_requests": False, "posts_per_page": 100}):
                url.append(post['post_url'])
                descripcion.append(post['post_text'])
                fecha.append(post['time'])

                if (post['time'] < inicio):

                    print('Última publicación registrada:   fecha:' + str(post['time']))
                    list_tuples = list(zip(url, descripcion, fecha))

                    df = pd.DataFrame(list_tuples,
                                      columns=['URL', 'DESCRIPCION', 'FECHA'])
                    df.to_excel("SECRETARIO_2024.xlsx")
                    break
                i = i + 1

            print('Se han registrado: ' + str(i) + 'publicaciones Para: ' + nombre )
        except:
            print("Ha habido una excepción")

extraer_lista(paginas)
