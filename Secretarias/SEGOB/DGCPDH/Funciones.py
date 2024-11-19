from RS import genera_rs


def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }


def tarjeta_cine(row):
    FOTOS = [str(row.FOTO), str(row.VIDEO), str(row.ALBUM)]

    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-user"></i><strong> PERSONAS ASISTENTES: </strong>""" + str(row.PERSONAS) + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> ACCIÓN: </strong>"""+str(row.ACCION)+"""</p>
                <p style="color:#FFFFFF; margin: 0px;">""" + str(row.DESCRIPCION) + """</p>
    """

    if FOTOS:
        carousel_fotos = genera_carousel(FOTOS, "mixto")
        if carousel_fotos[1]:
            texto += carousel_fotos[0]

    texto += """<div align = center>
                        <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGCPDH") + """
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
            if elemento != "0":
                hay = True
                carousel_indicadores += """
                      <li data-target="#carouselExampleIndicators" data-slide-to='""" + str(i) + """' class="active"></li>
                          """
                if i == 0:
                    cl = "carousel-item active"
                else:
                    cl = "carousel-item"
                if tipo == "mixto":
                    if "https://live." in elemento:
                        carousel_contenido += """        <!-- Slide -->
                                    <div class='""" + cl + """'>
                                       <img class="d-block w-100" src='""" + str(elemento) + """' width='250' height='180'/>
                                    </div>        
                                               """
                    elif "https://flic.kr" in elemento:
                        carousel_contenido += """<!-- Slide -->
                                    <div class='""" + cl + """' style="height:180;width:250;">
                                        <p align = "center" style = "color:white"> Para más información consulta el siguiente enlace:
                                        <br>
                                            <a href='""" + str(elemento) + """' target="_blank"><strong>Link del Álbum </strong></a>
                                        </p>
                                        <br>
                                    </div>
                            
                                """

                    elif "https://flic.kr" or "https://www.flickr.com/photos" in elemento:
                        carousel_contenido += """<!-- Slide -->
                                    <div class='""" + cl + """' style="height:180;width:250;">
                                        <p align = "center" style = "color:white"> Para más información consulta el siguiente enlace:
                                        <br>
                                            <a href='""" + str(elemento) + """'><img class="postcard__img" src='images/evidencia_foto.png' width='95%' height='15%'/></a>
                                        </p>
                                        <br>
                                    </div>   
                        """
                        
                    else:
                        carousel_contenido += """        <!-- Slide -->
                                    <div class='""" + cl + """' style="height:180;width:250;">
                                        """ + str(elemento) + """
                                    </div>
                            """
            i += 1
        carousel[
            0] = carousel_inicio + carousel_indicadores + "</ol>" + carousel_contenido + "</div>" + carousel_controls
        carousel[1] = hay
    return carousel


def tarjeta_cursos_y_capacitaciones(row):
    FOTOS = [str(row.FOTO), str(row.ALBUM)]

    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
           <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-users" style = "color:#FAC63A;"></i><strong> PERSONAS ASISTENTES: </strong>""" + str(row.TOTAL) + """</p>
                <p style="color:#FFFFFF; margin: 0px"><i class ="fa fa-female" style = "color:#FAC63A;"></i><strong> MUJERES BENEFICIADAS: </strong >""" + str(row.MUJERES) + """</p>
                <p style="color:#FFFFFF; margin: 0px"><i class ="fa fa-male" style = "color:#FAC63A;"></i><strong> HOMBRES BENEFICIADOS: </strong > """ + str(row.HOMBRES) + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> TEMA: </strong>"""+str(row.TEMA)+"""</p>
                <p style="color:#FFFFFF; margin: 0px"><strong>DESCRIPCIÓN: </strong>""" + str(row.DESCRIPCION) + """</p>
              """

    if FOTOS:
        carousel_fotos = genera_carousel(FOTOS, "mixto")
        if carousel_fotos[1]:
            texto += carousel_fotos[0]

    texto += """<div align = center>
                        <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGCPDH") + """
                </div>
            </div>
        </article>
        """

    return texto

def tarjeta_otros(row):
    FOTOS = [str(row.FOTO), str(row.VIDEO), str(row.ALBUM)]

    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
           <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-users" style = "color:#FAC63A;"></i><strong> PERSONAS ASISTENTES: </strong>""" + str(row.TOTAL) + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> TEMA: </strong>"""+str(row.TEMA)+"""</p>
                <p style="color:#FFFFFF; margin: 0px;">""" + str(row.DESCRIPCION) + """</p>
              """

    if FOTOS:
        carousel_fotos = genera_carousel(FOTOS, "mixto")
        if carousel_fotos[1]:
            texto += carousel_fotos[0]

    texto += """
                <div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGCPDH") + """
                </div> 
            </div>
        </article>
        """

    return texto

def genera_tabla_sexo(row):
    fila_tabla = " "
    if str(row.HOMBRES) != "0":
        fila_tabla += """           
                    <tr>
                        <td> Hombres </td>
                        <td><p style="color:#FFFFFF; margin: 0px;">""" + str(row.HOMBRES) + """</p></td>
                    </tr>
                 """
    if str(row.MUJERES) != "0":
        fila_tabla += """           
                                <tr>
                                    <td> Mujeres </td>
                                    <td><p style="color:#FFFFFF; margin: 0px;">""" + str(row.MUJERES) + """</p></td>
                                </tr>
                 """
    return fila_tabla

def genera_tabla(row):
    fila_tabla = " "
    if str(row.PREESCOLAR) != "0":
        fila_tabla += """           
                                <tr>
                                    <td> Preescolar </td>
                                    <td><p style="color:#FFFFFF; margin: 0px;">""" + str(row.PREESCOLAR) + """</p></td>
                                </tr>
                 """

    if str(row.PRIMARIA) != "0":
        fila_tabla += """           
                                <tr>
                                    <td> Primaria </td>
                                    <td><p style="color:#FFFFFF; margin: 0px;">""" + str(row.PRIMARIA) + """</p></td>
                                </tr>
                 """

    if str(row.SECUNDARIA) != "0":
        fila_tabla += """           
                                <tr>
                                    <td> Secundaria </td>
                                    <td><p style="color:#FFFFFF; margin: 0px;">""" + str(row.SECUNDARIA) + """</p></td>
                                </tr>
                 """

    if str(row.BACHILLERATO) != "0":
        fila_tabla += """           
                                <tr>
                                    <td> Bachillerato </td>
                                    <td><p style="color:#FFFFFF; margin: 0px;">""" + str(row.BACHILLERATO) + """</p></td>
                                </tr>
                 """

    if str(row.LICENCIATURA) != "0":
        fila_tabla += """           
                                <tr>
                                    <td> Licenciatura </td>
                                    <td><p style="color:#FFFFFF; margin: 0px;">""" + str(row.LICENCIATURA) + """</p></td>
                                </tr>
                 """


    if str(row.POSGRADO) != "0":
        fila_tabla += """           
                                <tr>
                                    <td> Posgrado </td>
                                    <td><p style="color:#FFFFFF; margin: 0px;">""" + str(row.POSGRADO) + """</p></td>
                                </tr>
                 """
    if str(row.TOTAL) != "0":
        fila_tabla += """           
                                <tr>
                                    <td> Total </td>
                                    <td><p style="color:#FFFFFF; margin: 0px;">""" + str(row.TOTAL) + """</p></td>
                                </tr>
                 """

    return fila_tabla

def tarjeta_becas(row):

    validar_tabla_sexo = genera_tabla_sexo(row)
    validar_tabla = genera_tabla(row)

    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <p align = "center" style="color:#FFFFFF; margin: 0px; width: 200px;"><strong> Becas de Atención Especial de Derechos Humanos (2020)</strong></p>
                    <table id=defunciones class="table table-hover table-sm " style="font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;">
                        <tbody> 
                        """ + validar_tabla_sexo + """
                        </tbody>
        
                    </table>
                    <table id=defunciones class="table table-hover table-sm " style="font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;">
                        <tbody> 
                        """ + validar_tabla + """
                        </tbody>
        
                    </table>
    """

    texto += """
                <div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGCPDH") + """
                </div> 
            </div>
        </article>
    """

    return texto

def tarjeta_revista_y_presentaciones(row):
    FOTOS = [str(row.FOTO), str(row.VIDEO), str(row.ALBUM)]

    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
              <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
              <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-users" style = "color:#FAC63A;"></i><strong> PERSONAS ASISTENTES: </strong>""" + str(row.PERSONAS) + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> ACCIÓN: </strong>"""+str(row.ACCION)+"""</p>
              <p style="color:#FFFFFF; margin: 0px;">""" + str(row.DESCRIPCION) + """</p>
    """

    if FOTOS:
        carousel_fotos = genera_carousel(FOTOS, "mixto")
        if carousel_fotos[1]:
            texto += carousel_fotos[0]

    texto += """<div align = center>
                        <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGCPDH") + """
                </div>
            </div>
        </article>
        """

    return texto

def tarjeta_mesas(row):
    FOTOS = [str(row.FOTO), str(row.VIDEO), str(row.ALBUM)]

    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-users" style = "color:#FAC63A;"></i><strong> PERSONAS ASISTENTES: </strong>""" + str(row.ASISTENTES) + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> CURSO: </strong>"""+str(row.CURSO)+"""</p>
    """

    if FOTOS:
        carousel_fotos = genera_carousel(FOTOS, "mixto")
        if carousel_fotos[1]:
            texto += carousel_fotos[0]

    texto += """<div align = center>
                        <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGCPDH") + """
                </div>
            </div>
        </article>
        """

    return texto


def tarjeta_mesas_trabajo(row):
    FOTOS = [str(row.FOTO), str(row.ALBUM)]

    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> TEMA: </strong>"""+str(row.TEMA)+"""</p>
                <p style="color:#FFFFFF; margin: 0px;">""" + str(row.DESCRIPCION) + """</p>
    """

    if FOTOS:
        carousel_fotos = genera_carousel(FOTOS, "mixto")
        if carousel_fotos[1]:
            texto += carousel_fotos[0]

    texto += """<div align = center>
                        <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGCPDH") + """
                </div>
            </div>
        </article>
        """

    return texto
