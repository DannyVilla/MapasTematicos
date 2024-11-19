from RS import genera_rs


def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }


def tarjeta_oficinas(row):
    texto = """
        <article style="background-color:#900C3F; font-family:sans-serif; font-size:11px;border-radius: 20px;">
            <div class = "card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class ="fa fa-user" style = "color:#FAC63A;"></i><strong> NOMBRE: </strong > """ + str(row.NOMBRE) + """ </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DIRECCIÓN: </strong>""" + str(row.DIRECCION) + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-phone" style = "color:#FAC63A;"></i><strong> TELÉFONO: </strong>""" + str(row.TEL) + """  </p>
              
               <div align = "center">
                 <img src='""" + str(row.FOTO) + """' width='250' height='180'/>
               </div>  
              
              """

    texto += """<div align = "center">
                         <p style= "margin:0px;color:white;">Más información: </p> """ + genera_rs("IVM") + """
                </div>
            </div>   
        </article>
        """

    return texto


def tarjeta_sp(row):
    texto = """
        <article style="background-color:#900C3F; font-family:sans-serif; font-size:11px;border-radius: 20px;">
            <div class = "card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class ="fa fa-user" style = "color:#FAC63A;"></i><strong> NOMBRE: </strong > """ + str(row.NOMBRE) + """ </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DIRECCIÓN: </strong>""" + str(row.DIRECCION) + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-phone" style = "color:#FAC63A;"></i><strong> TELÉFONO: </strong>""" + str(row.TEL) + """  </p>
              """

    texto += """<div align = "center">
                         <p style= "margin:0px;color:white;">Más información: </p> """ + genera_rs("IVM") + """
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
    if lista:
        for elemento in lista:
            if elemento[1] != "0":
                hay = True
                carousel_indicadores += """
                          <li data-target="#carouselExampleIndicators" data-slide-to='""" + str(i) + """' class="active"></li>
                          """
                if i == 0:
                    cl = "carousel-item active"
                else:
                    cl = "carousel-item"

                if elemento[1] != "0":
                    carousel_contenido += """<!-- Slide -->
                                                <div align = "center" class='""" + cl + """'>
                                                    <img src='""" + str(elemento[1]) + """' width='250' height='180'/>
                                                </div>        
                                            """
                elif "video" in elemento[0]:
                    carousel_contenido += """<!-- Slide -->
                                                <div class='""" + cl + """'width='250' height='180'/>
                                                    """ + str(elemento[1]) + """
                                                </div>        
                                           """
                if "RS" in elemento[0]:
                    print(len(elemento))

                    carousel_contenido += """<!-- Slide -->
                                               <div class='""" + cl + """' >
                                                    <p style = "color:white"> Para más información consulta el siguiente enlace:</p>
                                                    <a class="navbar-brand" target=_blank href='""" + str(elemento[1]) + """'>
                                                        <img alt="Brand" src="images/fb3.png" width="30" height="30">
                                                    </a>
                                               </div>        
                            """
                if "ALBUM" in elemento[0]:
                    print(len(elemento))

                    carousel_contenido += """ <!-- Slide -->
                                               <div class='""" + cl + """' >
                                                    <p style = "color:white"> Para más información consulta el siguiente enlace:</p>
                                                    <a class="navbar-brand" target=_blank href='""" + str(elemento[1]) + """'>
                                                        Link del Álbum
                                                    </a>
                                               </div>        
                                               """
                i += 1
        carousel[
            0] = carousel_inicio + carousel_indicadores + "</ol>" + carousel_contenido + "</div>" + carousel_controls
        carousel[1] = hay
    return carousel


def tarjeta_actividades(row, anio):
    FOTOS = [["foto", str(row.FOTO1)], ["foto", str(row.FOTO2)], ["foto", str(row.FOTO3)], ["foto", str(row.FOTO4)],
             ["foto", str(row.FOTO5)], ["foto", str(row.FOTO6)], ["foto", str(row.FOTO7)], ["foto", str(row.FOTO8)],
             ["foto", str(row.FOTO9)], ["foto", str(row.FOTO10)], ["foto", str(row.FOTO11)],["foto", str(row.FOTO12)]]

    texto = """
        <article style="background-color:#900C3F; font-family:sans-serif; font-size:11px;border-radius: 20px;">
            <div class = "card-body">
                  <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> ACCIONES: </strong> """ + anio + """  </p>
    """

    if str(row.APOYOS) != "0" or  0:
        texto += """
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> APOYOS: """+ str(row.APOYOS) +""" </strong></p>
        """

    if str(row.BM) != "0" or 0:
        texto += """
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-female" style = "color:#FAC63A;"></i><strong> MUJERES BENEFICIADAS: </strong>""" + str(row.BM) + """</p>
    """

    if str(row.BH) != "0" or 0:
        texto += """
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-male" style = "color:#FAC63A;"></i><strong> HOMBRES BENEFICIADOS: </strong>""" + str(row.BH) + """</p>
    """

    texto += """
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> ACTIVIDAD: </strong>"""+ str(row.ACTIVIDAD) +"""</p>
            """

    if FOTOS:
        carousel_fotos = genera_carousel(FOTOS, "mixto")
    if carousel_fotos[1]:
        texto += carousel_fotos[0]

    texto += """<div align = "center">
                         <p style= "margin:0px;color:white;">Más información: </p> """ + genera_rs("IVM") + """
                </div>
            </div>
        </article>
        """

    return texto
