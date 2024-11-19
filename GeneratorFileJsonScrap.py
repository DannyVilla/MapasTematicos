import pandas as pd
import datetime
import json
import os

from facebook_scraper import get_posts

inicio = datetime.datetime(2023, 5, 31)

log = ' '
name = ' '
paginas = ["EricCisnerosB"]

data = {}
data = [ ]


def extraer_lista(paginas):

    for nombre in paginas:
        i = 0
        #df = pd.DataFrame()

        print('Iniciando generación de publicaciones para: ' + nombre)

        for post in get_posts(nombre, pages=1, credentials=(log, name), timeout=120, options={"allow_extra_requests": False, "posts_per_page": 250}):
            data.append(post['post_id'])
            data.append(post['text'])
            data.append(post['post_text'])
            data.append(post['shared_text'])
            data.append(post['original_text'])
#           data.append(post['time'])
            data.append(post['timestamp'])
            data.append(post['image'])
            data.append(post['image_lowquality'])
            data.append(post['images'])
            data.append(post['images_description'])
            data.append(post['images_lowquality'])
            data.append(post['images_lowquality_description'])
            data.append(post['video'])
            data.append(post['video_duration_seconds'])
            data.append(post['video_height'])
            data.append(post['video_id'])
            data.append(post['video_quality'])
            data.append(post['video_size_MB'])
            data.append(post['video_thumbnail'])
            data.append(post['video_watches'])
            data.append(post['video_width'])
            data.append(post['likes'])
            data.append(post['comments'])
            data.append(post['shares'])
            data.append(post['post_url'])
            data.append(post['link'])
            data.append(post['links'])
            data.append(post['user_id'])
            data.append(post['username'])
            data.append(post['user_url'])
            data.append(post['is_live'])
            data.append(post['factcheck'])
            data.append(post['shared_post_id'])
            data.append(post['shared_time'])
            data.append(post['shared_user_id'])
            data.append(post['shared_username'])
            data.append(post['shared_post_url'])
            data.append(post['available'])
            data.append(post['comments_full'])
            data.append(post['reactors'])
            data.append(post['w3_fb_url'])
            data.append(post['reactions'])
            data.append(post['reaction_count'])
            data.append(post['with'])
            data.append(post['page_id'])
            data.append(post['sharers'])

            data.append({

            })

            print('Última publicación registrada:   fecha:' + str(post['time']))

            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)

        print('Se han registrado: ' + str(i) + 'publicaciones Para: ' +nombre +' última fecha:' + str(post['time']))
extraer_lista(paginas)