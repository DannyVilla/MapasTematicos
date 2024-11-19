from RS import genera_rs


def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }


def tarjeta_dos(row):
    FOTOS = [str(row.FOTO1), str(row.FOTO2), str(row.FOTO3), str(row.FOTO4), str(row.FOTO5), str(row.FOTO6),
             str(row.FOTO7), str(row.FOTO8), str(row.FOTO9), str(row.FOTO10), str(row.FOTO11), str(row.FOTO12),
             str(row.FOTO13), str(row.FOTO14), str(row.FOTO15), str(row.FOTO16), str(row.FOTO17), str(row.FOTO18),
             str(row.FOTO19), str(row.FOTO20)]
    VIDEOS = [str(row.VIDEO1), str(row.VIDEO2), str(row.VIDEO3), str(row.VIDEO4)]

    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar"></i><strong>ACCIONES: </strong>""" + str(
        row.TRIMESTRE) + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><strong>BENEFICIADOS: </strong>""" + str(row.BENEFICIADOS) + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><strong>APOYOS: </strong>""" + str(row.APOYOS) + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><strong>PROGRAMA: </strong>""" + str(row.PROGRAMA) + """</p>
    """

    carousel_fotos = genera_carousel(FOTOS, "fotos")
    carousel_videos = genera_carousel(VIDEOS, "videos")
    if carousel_fotos[1] or carousel_videos[1]:
        if carousel_fotos:
            texto += carousel_fotos[0]

    texto += """
            </div> 
                <div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("CEJM") + """
                </div>
        </article>
        """

    return texto


def tarjeta_ollas(row):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><strong>Localidad: </strong>""" + str(row.LOCALIDAD) + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><strong>Región: </strong>""" + str(row.REGION) + """</p>

    """

    texto += """
            </div> 
                <div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("CEJM") + """
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
