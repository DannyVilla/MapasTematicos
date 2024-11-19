import requests
from bs4 import BeautifulSoup
import re
from RS import genera_rs


def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }


def content_secretario(MUNICIPIO, TEXTO, FECHA, CLASIFICACION, FOTO, PUB):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
                <div class="carousel-inner">
                    <div class="carousel-item active">             

                        <div class="card-body">
                            <h5 align = "center" ><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                            <p style= "color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i>""" + FECHA + """</p>
                            <p style= "color:#FFFFFF; margin: 0px;">""" + TEXTO + """</p>

        """

    # Comparacion substring Iframe
    if FOTO != "0":
        html = FOTO
        soup = BeautifulSoup(html, 'html.parser')
        # Encuentra el elemento iframe
        FOTO = soup.find('iframe')
        # Verifica si se encontró el elemento iframe
        if FOTO != "0":
            # Obtiene el valor del atributo src del iframe
            print("Nuevo enlace generado")
        FOTO = FOTO['src']

        # Generación de HTML
        req = requests.get(FOTO)
        content = req.text
        soup = BeautifulSoup(content, 'html.parser')

        # Buscada de elemento en rquests.text
        imagen_height = soup.find_all('img', {'class': 'scaledImageFitHeight img'})
        imagen_width = soup.find_all('img', {'class': 'scaledImageFitWidth img'})
        img_down = soup.find_all('img', {'class': '_46-i img'})
        img_one = soup.find_all('img', {'class': '_1p6f _1p6g img'})

        FOTO = []

        for img in imagen_height:
            newUrl = img['src']
            FOTO.append(newUrl)

        for img in imagen_width:
            newUrl = img['src']
            FOTO.append(newUrl)

        for img in img_down:
            newUrl = img['src']
            FOTO.append(newUrl)

        for img in img_one:
            newUrl = img['src']
            FOTO.append(newUrl)

    if FOTO != "0":
        FOTOS = FOTO
        carousel_fotos = genera_carousel(FOTOS, "fotos")
        if carousel_fotos[1]:
            if carousel_fotos:
                texto += carousel_fotos[0]

    texto += """
                                <div align = "center">
                                     <p style= "margin:0px;color:white;">Más información: </p> """ + genera_rs("SECRETARIO2024") + """
                                </div>
                        </div>
                    </div>
                </article>
            """
    return texto


def content_secretario_2023(MUNICIPIO, TEXTO, FECHA, URL, CLASIFICACION, FOTO, PUB):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
                <div class="carousel-inner">
                    <div class="carousel-item active">             

                        <div class="card-body">
                            <h5 align = "center" ><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                            <p style= "color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i>""" + FECHA + """</p>
                            <p style= "color:#FFFFFF; margin: 0px;">""" + TEXTO + """</p>

        """

    # Comparacion substring Iframe
    if URL != "0":
        # Generación de HTML
        req = requests.get(URL)
        content = req.text
        soup = BeautifulSoup(content, 'html.parser')

        # Buscada de elemento en rquests.text
        URL = [meta['content'] for meta in soup.find_all('meta', content=True) if "https://scontent" in meta['content']]
        print(URL)


    texto += """
        <img class="d-block w-100" src='""" + URL[0] + """' width='250' height='180'/>     
    
    """

    texto += """
                                <div align = "center">
                                     <p style= "margin:0px;color:white;">Más información: </p> """ + genera_rs("SECRETARIO") + """
                                </div>
                        </div>
                    </div>
                </article>
            """
    return texto


def genera_carousel(lista, tipo):
    i = 0
    hay = False
    carousel = [" ", hay]
    carousel_inicio = """ <!-- Carousel container -->
               <div id= "carouselExampleIndicators" class="carousel slide" data-ride="carousel">

               """
    carousel_indicadores = """ <!-- Indicators -->
                   <ol class="carousel-indicators">"""
    carousel_contenido = """
            <!-- Content -->
            <div class="carousel-inner" role="listbox">"""

    carousel_controls = """
            <!-- Previous/Next controls -->
                  <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="sr-only">Previous</span>
                  </a>
                  <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="sr-only">Next</span>
                  </a>         
            </div>
        """

    for elemento in lista:
        if elemento != "0":
            hay = True
            carousel_indicadores += """
                      <li data-target="#carouselExampleIndicators" data-slide-to='""" + str(i) + """' class="active"></li>
                      """
            if i == 0:
                cl = "carousel-item active"
            else:
                cl = "carousel-item"

            if tipo == "fotos":
                carousel_contenido += """<!-- Slide -->
                                    <div class='""" + cl + """'>
                                       <img class="d-block w-100" src='""" + str(elemento) + """' width='250' height='180'/>
                                    </div>        
                                """

        i += 1
        print(elemento)
    carousel[0] = carousel_inicio + carousel_indicadores + "</ol>" + carousel_contenido + "</div>" + carousel_controls
    carousel[1] = hay
    return carousel
