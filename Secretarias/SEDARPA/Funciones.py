from RS import genera_rs

def genera_acciones(MUNICIPIO, TITULO, FECHA, CLASIFICACION, ENLACEPUB, ENLACEFOT1, ENLACEFOT2, URL):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i>""" + FECHA + """  </p>
                <p style="color:#FFFFFF; margin: 0px;">""" + TITULO + """</p>
                <p style="color:#FFFFFF; margin: 0px;">""" + CLASIFICACION + """</p>
                <li><a class = "link" style="background-color:#900C3F;color: #76CFF7; border-radius: 20px; padding=5px;" href=" """ + URL + """ ">Publicación de Facebook</a></li>           
           """
    if ENLACEPUB != "0":
        texto += """
              <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">   
                    <ol class="carousel-indicators">
                        <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                        <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>                   
                    </ol>
                        <div class="carousel-inner">
                            <div class="carousel-item active">                            
                                """ + ENLACEFOT1 + """
                            </div>
                            <div class="carousel-item">                            
                                """ + ENLACEFOT2 + """
                            </div>
                        </div>
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
    texto += """
                    <div align = "center">
                        <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SEDARPA") + """
                    </div>
            </div>
        </article>
        """

    return texto

def tarjeta_agricultura(row):
    FOTOS = [str(row.FOTO1), str(row.FOTO2)]
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <h6 align = "center"><span class="badge badge-light"> Acción del año """ + str(row.ANIO) + """</span></h6>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong> BENEFICIADOS: </strong>""" + str(row.BENEFICIARIOS) + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> APOYOS: </strong>""" + str(row.APOYO1) + """</span></p>
            """

    carousel_fotos = genera_carousel(FOTOS, "fotos")
    if carousel_fotos[1]:
        if carousel_fotos:
            texto += carousel_fotos[0]

    texto += """
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SEDARPA") + """
                </div>
            </div>
        </article>
        """

    return texto

def tarjeta_desarrolloR(row):
    FOTOS = [str(row.FOTO1), str(row.FOTO2)]
    texto = """
            <article class="popup" style="background-color:#900C3F; font-family:sans-serif; font-size:10px;border-radius: 20px;">
                <div class="card-body" >
                    <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                    <h6 align = "center"><span class="badge badge-light">Acción del año """ + str(row.ANIO) + """</span></h6>
                    <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong> BENEFICIADOS: </strong>""" + str(row.BENEFICIADOS) + """</p>
                    <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> PROGRAMA: </strong>""" + str(row.PROGRAMA) +"""</p>
            """
    if row.APOYOS != "0" or 0:
        texto += """<p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> APOYOS: </strong>""" + str(row.APOYOS) + """</p>"""

    carousel_fotos = genera_carousel(FOTOS, "fotos")
    if carousel_fotos[1]:
        if carousel_fotos:
            texto += carousel_fotos[0]

    texto += """
            <div align = "center">
                <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SEDARPA") + """
            </div>
        </div>
    </article>
"""

    return texto

def tarjeta_pesca_acuacultura(row):
    FOTOS = [str(row.FOTO1), str(row.FOTO2)]

    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <h6 align = "center"><span class="badge badge-light"> Acción del año """ + str(row.ANIO) + """</span></h6>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> PROGRAMA: </strong>""" + str(row.PROGRAMA) +"""</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong> BENEFICIADOS: </strong>""" + str(row.BENEFICIADOS) + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> APOYOS: </strong>""" + str(row.APOYOS) + """</p>"""

    carousel_fotos = genera_carousel(FOTOS, "fotos")
    if carousel_fotos[1]:
        if carousel_fotos:
            texto += carousel_fotos[0]

    texto += """
            </div>
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SEDARPA") + """
                </div>
        </article>
        """

    return texto

def tarjeta_infraestructura(row):
    FOTOS = [str(row.FOTO1), str(row.FOTO2)]
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <h6 align = "center"><span class="badge badge-light">Acción del año """ + str(row.ANIO) + """</span></h6>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong> BENEFICIADOS: </strong>""" + str(row.BENEFICIADOS) + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> PROGRAMA: </strong>""" + str(row.PROGRAMA) +"""</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> APOYOS: </strong>""" + str(row.APOYOS) + """</p>                 
        """

    carousel_fotos = genera_carousel(FOTOS, "fotos")
    if carousel_fotos[1]:
        if carousel_fotos:
            texto += carousel_fotos[0]

    texto += """
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SEDARPA") + """
                </div>
            </div>
        </article>
        """

    return texto

def tarjeta_ganaderia(row):
    FOTOS = [str(row.FOTO1), str(row.FOTO2)]
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <h6 align = "center"><span class="badge badge-light">Acción del año """ + str(row.ANIO) + """</span></h6>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong> BENEFICIADOS: </strong>""" + str(row.BENEFICIADOS) + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> PROGRAMA: </strong>""" + str(row.PROGRAMA) +"""</p>
        """
    if str(row.APOYOS1) != "0":
        texto += """
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> Apoyos de Cercos eléctricos: </strong>""" + str(row.APOYOS1) + """</p>"""
    if str(row.APOYOS2) != "0":
        texto += """
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> Apoyos de Bebederos móviles de 500 litros: </strong>""" + str(row.APOYOS2) + """</p>"""
    if str(row.APOYOS3) != "0":
        texto += """
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> Apoyos de Bebederos móviles de 850 litros: </strong>""" + str(row.APOYOS3) + """</p>"""
    if str(row.APOYOS4) != "0":
        texto += """
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> Apoyos de Semilla de Pasto Mejorado: </strong>""" + str(row.APOYOS4) + """</p>"""
    if str(row.APOYOS5) != "0":
        texto += """
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> Apoyos de Paquetes Avícolas: </strong>""" + str(row.APOYOS5) + """</p>"""
    if str(row.APOYOS6) != "0":
        texto += """
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> Apoyos de Herramientas y Equipo de Protección Apícola: </strong>""" + str(row.APOYOS6) + """</p>"""
    if str(row.APOYOS7) != "0":
        texto += """
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> Apoyos de Abeja reina: </strong>""" + str(row.APOYOS7) + """</p>"""
    if str(row.APOYOS8) != "0":
        texto += """
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> Apoyos de Jarabe de Maíz de Alta Fructuosa: </strong>""" + str(row.APOYOS8) + """</p>"""

    carousel_fotos = genera_carousel(FOTOS, "fotos")
    if carousel_fotos[1]:
        if carousel_fotos:
            texto += carousel_fotos[0]

    texto += """
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SEDARPA") + """
                </div>
            </div>
        </article>
    """

    return texto

def tarjeta_agronegocios(row):
    FOTOS = [str(row.FOTO1), str(row.FOTO2)]
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <h6 align = "center"><span class="badge badge-light">Acción del año """ + str(row.ANIO) + """</span></h6>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> PROGRAMA: </strong>""" + str(row.PROGRAMA) +"""</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong> BENEFICIADOS: </strong>""" + str(row.BENEFICIADOS) + """</p>
        """
    if str(row.APOYOS1) != "0":
        texto += """<p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i></i><strong> APOYO: </strong>""" + str(row.APOYOS1) + """</p>"""
    if str(row.APOYOS2) != "0":
        texto += """<p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> APOYO: </strong>""" + str(row.APOYOS2) + """</p>"""
    if str(row.APOYOS3) != "0":
        texto += """<p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> APOYO: </strong>""" + str(row.APOYOS3) + """</p>"""

    carousel_fotos = genera_carousel(FOTOS, "fotos")
    if carousel_fotos[1]:
        if carousel_fotos:
            texto += carousel_fotos[0]

    texto += """
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SEDARPA") + """
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
    carousel[
        0] = carousel_inicio + carousel_indicadores + "</ol>" + carousel_contenido + "</div>" + carousel_controls
    carousel[1] = hay
    return carousel



