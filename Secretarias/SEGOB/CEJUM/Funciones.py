from RS import genera_rs

def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }

def genera_tarjeta_capa(MUNICIPIO, TEMA, FECHA, DESCIPCION, FOTO1, FOTO2, FOTO3):

    FOTOS = [FOTO1, FOTO2, FOTO3]

    FECHA = FECHA.replace(" 00:00:00", "")

    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-bookmark" style = "color:#FAC63A;"></i><strong> TEMA: </strong>""" + TEMA + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> FECHA: </strong>""" + FECHA + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> DESCRIPCIÓN: </strong>""" + DESCIPCION +"""</p>

        """

    carousel_fotos = genera_carousel(FOTOS, "fotos")
    if carousel_fotos[1] :
        if carousel_fotos:
            texto += carousel_fotos[0]

    texto += """
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("CEJUM") + """
                </div>
            </div>
        </article>      
    """

    return texto


def genera_tarjeta_atencion(MUNICIPIO, BENEFICIADOS, ACCION, APOYO):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-users" style = "color:#FAC63A;"></i><strong> BENEFICIADAS: </strong>""" + BENEFICIADOS + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> ACCIÓN: </strong>""" + ACCION + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> APOYO: </strong>""" + APOYO + """</p>
        """

    texto += """
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("CEJUM") + """
                </div>
            </div>
        </article>      
    """

    return texto


def genera_tarjeta_2022(MUNICIPIO, PROGRAMA, BENEFICIADOS, APOYOS, FOTO1, FOTO2, FOTO3, FOTO4, FOTO5, FOTO6,
             FOTO7, FOTO8, FOTO9, FOTO10, FOTO11, FOTO12, FOTO13, FOTO14, FOTO15, FOTO16, FOTO17, FOTO18,FOTO19, FOTO20,
             VIDEO1, VIDEO2, VIDEO3, VIDEO4):

    FOTOS = [FOTO1, FOTO2, FOTO3, FOTO4, FOTO5, FOTO6,
             FOTO7, FOTO8, FOTO9, FOTO10, FOTO11, FOTO12,
             FOTO13, FOTO14, FOTO15, FOTO16, FOTO17, FOTO18,
             FOTO19, FOTO20]

    VIDEOS = [VIDEO1, VIDEO2, VIDEO3, VIDEO4]

    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong>APOYOS: </strong>""" + APOYOS + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong>BENEFICIARIOS: </strong>""" + BENEFICIADOS + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> PROGRAMA: </strong>""" + PROGRAMA +"""</p>

        """

    carousel_fotos = genera_carousel(FOTOS, "fotos")
    carousel_videos = genera_carousel(VIDEOS, "videos")
    if carousel_fotos[1] or carousel_videos[1]:
        if carousel_fotos:
            texto += carousel_fotos[0]

    texto += """
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("CEJUM") + """
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
            elif tipo == "videos":
                carousel_contenido += """<!-- Slide -->
                                    <div class='""" + cl + """' style="height:180;width:250;">
                                        """ + str(elemento) + """
                                    </div>

                                                       """

        i += 1
    carousel[0] = carousel_inicio + carousel_indicadores + "</ol>" + carousel_contenido + "</div>" + carousel_controls
    carousel[1] = hay
    return carousel

