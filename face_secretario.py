import pandas as pd
import datetime

from facebook_scraper import get_posts

inicio = datetime.datetime(2024, 1, 1)

log='usuario.scrapper.2024@outlook.com'
passwd='prueba12345'
paginas = ["CuitlahuacGarciaJimenez"]

def una(pagina):
    df = pd.DataFrame()
    url = []
    descripcion = []
    timestamp = []
    fecha = []
    i=0

    for post in get_posts(pagina, pages=10, timeout=120,cookies="from_browser",
                          options={"allow_extra_requests": True, "posts_per_page": 200}):
        url.append(post['post_url'])
        descripcion.append(post['post_text'])
        timestamp.append(post['timestamp'])
        fecha.append(post['time'])

        if (post['time'] < inicio):
            print('Última publicación registrada:   fecha:' + str(post['time']))
            list_tuples = list(zip(url, descripcion, timestamp, fecha))

            df = pd.DataFrame(list_tuples,
                              columns=['URL', 'Descripción', 'Timestamp', 'Fecha', 'Images', 'Image', 'w3_fb_url'])
            df.to_excel(pagina + "_Enero-Junio_UNA.xlsx")
            break
        i = i + 1
    print('Se han registrado: ' + str(i) + 'publicaciones Para: ' + pagina + ' última fecha:' + str(post['time']))


def extraer_lista(paginas):

    for nombre in paginas:
        i = 0
        #df = pd.DataFrame()
        url = []
        descripcion = []
        timestamp = []
        fecha = []
        print('Iniciando generación de publicaciones para:' + nombre)

        for post in get_posts(nombre, pages=150, credentials=(log, passwd), timeout=120, options={"allow_extra_requests": False, "posts_per_page": 50}):
            url.append(post['post_url'])
            descripcion.append(post['post_text'])
            timestamp.append(post['timestamp'])
            fecha.append(post['time'])

            if(post['time'] < inicio):
                list_tuples = list(zip(url, descripcion, timestamp, fecha))

                df = pd.DataFrame(list_tuples, columns=['URL', 'Descripción', 'Timestamp', 'Fecha'])
                df.to_excel(nombre+"_mayo-julio_2022.xlsx")
                break
            i = i+1
        print('Se han registrado: ' + str(i) + 'publicaciones Para: ' +nombre +' última fecha:' + str(post['time']))

una("EricCisnerosB")
