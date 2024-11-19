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
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
    """
    if str(row.DIRECCION) != "0":
        texto += """<p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DIRECCIÓN: </strong>""" + str(row.DIRECCION) + """  </p>"""

    texto += """   
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-phone" style = "color:#FAC63A;"></i><strong> TELÉFONO: </strong>""" + str(row.TEL) + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class ="fa fa-user" style = "color:#FAC63A;"></i><strong> TITULAR: </strong > """ + str(row.NOMBRE) + """ </p>

              """

    if str(row.FOTO) != "0":
        texto += """
                <img class="d-block w-100" src='""" + str(row.FOTO) + """' width='250' height='180'/>
    
        """

    texto += """
                <div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SIPINNA") + """
                </div>
            </div>
        </article>
        """

    return texto

def tarjeta_procuradores(row):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class ="fa fa-user" style = "color:#FAC63A;"></i><strong> TITULAR: </strong > """ + str(row.TITULAR) + """ </p>
    """
    if str(row.TEL) != "0":
        texto += """<p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> TELEFONO: </strong>""" + str(row.TEL) + """  </p>"""

    texto += """
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-at" style = "color:#FAC63A;"></i><strong> CORREO: </strong>""" + str(row.CORREO) + """  </p>
              """


    texto += """
                <div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SIPINNA") + """
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
               <div id='""" + tipo + """' class="carousel slide" data-ride="carousel" style="display:inline-block;margin:auto;">

               """
    carousel_indicadores = """ <!-- Indicators -->
                   <ol class="carousel-indicators">"""
    carousel_contenido = """
            <!-- Content -->
            <div class="carousel-inner" role="listbox">"""

    carousel_controls = """
            <!-- Previous/Next controls -->
            <a class="left carousel-control" href="#""" + tipo + """" role="button" data-slide="prev">
            <span class="icon-prev" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
            </a>
            <a class="right carousel-control" href="#""" + tipo + """" role="button" data-slide="next">
                <span class="icon-next" aria-hidden="true"></span>
                <span class="sr-only">Next</span>
            </a>
            </div>
        """
    if lista:
        for elemento in lista:
            if elemento[1] != "0":
                # print(elemento)
                hay = True
                carousel_indicadores += """
                          <li data-target="#""" + tipo + """" data-slide-to='""" + str(i) + """' class="active"></li>
                          """
                if i == 0:
                    cl = "item active"
                else:
                    cl = "item"
                if "Oficina" in elemento[0]:
                    ancho = 300
                    alto = 200
                else:
                    ancho = 300
                    alto = 300
                if "foto" in elemento[0]:

                    if elemento[1] != "0":
                        carousel_contenido += """ <!-- Slide -->
                                             <div class='""" + cl + """'>
                                                  <img src='""" + str(elemento[1]) + """' width='""" + str(
                            ancho) + """' height='""" + str(alto) + """'/>
                                                                   </div>        
                                                                   """
                    else:
                        print(elemento[1])
                if "video" in elemento[0]:
                    # print(elemento)

                    carousel_contenido += """        <!-- Slide -->
                                            <div class='""" + cl + """'>
                                             """ + str(elemento[1]) + """
                                           </div>        
                                           """
                    # print(carousel_contenido)

                if "RS" in elemento[0]:
                    print(len(elemento))

                    carousel_contenido += """        <!-- Slide -->
                                               <div class='""" + cl + """' >
                                                    <p style = "color:white"> Para más información consulta el siguiente enlace:</p>
                                                    <a class="navbar-brand" target=_blank href='""" + str(elemento[1]) + """'>
                                                        <img alt="Brand" src="images/fb3.png" width="30" height="30">
                                                    </a>
                                             </div>        
                                               """
                if "ALBUM" in elemento[0]:
                    print(len(elemento))

                    carousel_contenido += """        <!-- Slide -->
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


def tarjeta_capacitaciones(row):

    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> FECHA: </strong>""" + str(row.FECHA) + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong> TOTAL PERSONAS CAPACITADAS: </strong>""" + str(row.TOTAL) + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-female" style = "color:#FAC63A;"></i><strong> MUJERES: </strong>""" + str(row.MUJERES) + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-male" style = "color:#FAC63A;"></i><strong> HOMBRES: </strong>""" + str(row.HOMBRES) + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> COMITÉ INTERDISCIPLINARIO - APOYOS: """+ str(row.MODALIDAD) +""" </strong></p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> MODALIDAD: </strong>""" + str(row.TEMA) +"""</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class ="fa fa-user" style = "color:#FAC63A;"></i><strong> DIRIGIDO A: </strong > """ + str(row.DIRIGIDO) + """ </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> DESCRIPCIÓN: </strong>""" + str(row.DESCRIPCION) +"""</p>
        """

    if str(row.FOTO) != "0" or 0:
        texto+="""
            <div>
                 <img src='""" + str(row.FOTO) + """' width='250' height='180'/>
            </div> 
        """

    texto += """
                <div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SIPINNA") + """
                </div>
            </div>
        </article>
        """

    return texto
