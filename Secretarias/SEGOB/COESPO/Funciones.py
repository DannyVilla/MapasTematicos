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


def content_COMUPOS(MUNICIPIO, REGION, PRESIDENTEMUNICIPAL, FECHA, FOTO):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
                <div class="carousel-inner">
                    <div class="carousel-item active">             

                        <div class="card-body" style: width='250'>
                            <h5 align = "center" ><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                            <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-globe" style = "color:#FAC63A;"></i><strong> REGIÓN: </strong>""" + REGION + """  </p>
                            <p style= "color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i>Fecha de Instalación: """ + FECHA + """</p>
                            <p style= "color:#FFFFFF; margin: 0px;"><i class="fa fa-user" style = "color:#FAC63A;"></i>Presidente Municipal: """ + PRESIDENTEMUNICIPAL + """</p>
        """

    # Comparacion substring Iframe
    if "iframe" in FOTO:
        if FOTO != "0":
            html = FOTO
            soup = BeautifulSoup(html, 'html.parser')
            # Encuentra el elemento iframe
            FOTO = soup.find('iframe')
            # Verifica si se encontró el elemento iframe
            if FOTO !="0":
                # Obtiene el valor del atributo src del iframe
                print("Nuevo enlace generado")
            FOTO = FOTO['src']

            # Generación de HTML
            req = requests.get(FOTO)
            content = req.text
            soup = BeautifulSoup(content, 'html.parser')

            #Buscada de elemento en rquests.text
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
                                     <p style= "margin:0px;color:white;">Más información: </p> """ + genera_rs(
        "COESPO") + """
                                </div>
                        </div>
                    </div>
                </article>
            """
    return texto

###############################################################################################
def content_GIPEAMS(MUNICIPIO, REGION, ANIO, FOTO):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
                <div class="carousel-inner">
                    <div class="carousel-item active">             

                        <div class="card-body" style: width='250'>
                            <h5 align = "center" ><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                            <p align = "center" style= "color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i>AÑO: """ + ANIO + """</p>
                            <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-globe" style = "color:#FAC63A;"></i><strong> REGIÓN: </strong>""" + REGION + """  </p>
        """

    if "https://live." in FOTO:
        texto+= """
                            <img class="d-block w-100" src='""" + FOTO + """' width='250' height='180'/>
        """

    # Comparacion substring Iframe
    if "iframe" in FOTO:
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
                                     <p style= "margin:0px;color:white;">Más información: </p> """ + genera_rs(
        "COESPO") + """
                                </div>
                        </div>
                    </div>
                </article>
            """
    return texto

#######################################################################################


def content_JORNADAS(MUNICIPIO, REGION, MUJERES, HOMBRES, TOTAL,
                                    GRUPOS, ANIO, FECHA, FOTO):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
                <div class="carousel-inner">
                    <div class="carousel-item active">             

                        <div class="card-body" style: width='250'>
                            <h5 align = "center" ><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                            
                            <p align = "center" style= "color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i>AÑO: """ + ANIO + """</p>
                            <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-globe" style = "color:#FAC63A;"></i><strong> REGIÓN: </strong>""" + REGION + """  </p>
                            <p style= "color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i>FECHA DE ATENCIÓN: """ + FECHA + """</p>
                            
        """
    if HOMBRES != "0" or 0:
        texto += """
                            <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-male" style = "color:#FAC63A;"></i><strong> HOMBRES BENEFICIADOS: </strong > """ + HOMBRES + """ </p>
            """

    if MUJERES != "0" or 0:
        texto += """
                            <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-female" style = "color:#FAC63A;"></i><strong> MUJERES BENEFICIADOS: </strong > """ + MUJERES + """ </p>
            """

    if TOTAL != "0" or 0:
        texto += """
                            <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-users" style = "color:#FAC63A;"></i><strong> TOTAL BENEFICIADOS: """+ TOTAL +""" </strong></p>
            """

    if GRUPOS != "0" or 0:
        texto += """
                            <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong> GRUPOS: """+ GRUPOS +""" </strong></p>
            """

    if "https://live." in FOTO:
        texto+= """
                            <img class="d-block w-100" src='""" + FOTO + """' width='250' height='180'/>
        """

    # Comparacion substring Iframe
    if "iframe" in FOTO:
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
                                     <p style= "margin:0px;color:white;">Más información: </p> """ + genera_rs(
        "COESPO") + """
                                </div>
                        </div>
                    </div>
                </article>
            """
    return texto


def content_FOCALIZADOS(REGION, MUNICIPIO, NACIMIENTOS_10_14, NACIMIENTOS_15_19, NACIMIENOS_TOTAL, TFF_10_14, TEF_15_19, anio):
    texto = """
            <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
                <div class="card-body">
                    <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                    <h6 align = "center"><span class="badge badge-secondary"><i class="fa fa-calendar" style = "color:#FAC63A;"></i> Año """ + anio + """<span></h6>
                    <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-globe" style = "color:#FAC63A;"></i><strong> REGIÓN: </strong>""" + REGION + """  </p>
                    <p style="color:#FFFFFF; margin: 0px;"> En la siguiente tabla se muestra el número de nacimientos de hijos nacidos vivos de madres adolescentes de 10-14 años,
                     de 15-19 años y el total de nacimientos de madres de 10-19 años ocurridos en el municipio. Así como, la Tasa de Fecundidad Forzada en niñas de 10-14 años y la
                      Tasa Especifica de Fecundidad en madres de 15-19 años. Las Tasas representan el número de nacimientos por cada mil mujeres, de acuerdo a cada rango de edad. </p>

            """

    texto += """           
                    <table class="table table-hover table-sm " style=" font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;">
                    <tr align = "center">
                        <td>Cantidad de Hijos Nacidos Vivos de Madres de 10-14 Años</td>
                        <td >""" + NACIMIENTOS_10_14 + """</td>
                    </tr>
                    
                    <tr align = "center">
                        <td>Cantidad de Hijos Nacidos Vivos de Madres de 15-19 AÑOS</td>
                        <td>""" + NACIMIENTOS_15_19 + """</td>
                    </tr align = "center">
                    
                    <tr align = "center">
                        <td>Nacimientos Totales</td>
                        <td>""" + NACIMIENOS_TOTAL + """</td>
                    </tr> 
                    
                    <tr align = "center">
                        <td>Tasa Especifica de Fecundidad</td>
                        <td>""" + TEF_15_19 + """</td>
                    </tr>                    
                """

    if TFF_10_14 != "0":
        texto+= """
                    <tr align = "center">
                        <td>Tasa de Fecundidad Forzada</td>
                        <td>""" + TFF_10_14 + """</td>
                    </tr>
                    
                    
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

                if "https://live." in elemento:
                    carousel_contenido += """        <!-- Slide -->
                                <div class='""" + cl + """'>
                                   <img class="d-block w-100" src='""" + str(elemento) + """' width='250' height='180'/>
                                </div>  
            """

        i += 1
        print(elemento)
    carousel[0] = carousel_inicio + carousel_indicadores + "</ol>" + carousel_contenido + "</div>" + carousel_controls
    carousel[1] = hay
    return carousel
