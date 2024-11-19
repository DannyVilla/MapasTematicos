from RS import genera_rs


def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }


def tarjeta_oficinas(row):
    FOTOS = [["OFICINA", str(row.FOTO)], ["REGISTRADOR: " + str(row.REGISTRADOR), str(row.FOTOR)],
             ["OFICIAL: " + str(row.OFICIAL), str(row.FOTOO)]]

    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.CABECERA) + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DIRECCIÓN: </strong>""" + str(row.DIRECCION) + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-phone" style = "color:#FAC63A;"></i><strong> TELÉFONO: </strong>""" + str(row.TEL) + """  </p>

              """


    if FOTOS:
        carousel_fotos = genera_carousel(FOTOS, "mixto")
        if carousel_fotos[1]:
            texto += carousel_fotos[0]

    texto += """
                <div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGRPPIAGN") + """
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
                # print(elemento)
                hay = True
                carousel_indicadores += """
                          <li data-target="#carouselExampleIndicators" data-slide-to='""" + str(i) + """' class="active"></li>
                          """
                if i == 0:
                    cl = "carousel-item active"
                else:
                    cl = "carousel-item"
                if "OFICINA" in elemento[0]:
                    ancho = 250
                    alto = 180
                else:
                    ancho = 150
                    alto = 200
                if elemento[0] != "0" and elemento[1] != "0":
                    carousel_contenido += """<!-- Slide -->
                                            <div align = "center" class='""" + cl + """'>
                                                <p style="color:#FFFFFF; margin: 0px;">""" + str(elemento[0]) + """</p>
                                                    <img src='""" + str(elemento[1]) + """' width='""" + str(ancho) + """'
                                                height='""" + str(alto) + """'/>
                                           </div>        
                                           """
            i += 1
        carousel[
            0] = carousel_inicio + carousel_indicadores + "</ol>" + carousel_contenido + "</div>" + carousel_controls
        carousel[1] = hay
    return carousel


def tarjeta_actividades(row,periodo):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.CABECERA) + """</span></h3>
                <p style="color:#FFFFFF; margin: 0px;">""" + str(row.ZONA) + """<strong> ZONA REGISTRAL </strong></p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar"></i> """ + periodo + """</p>

        <table class="table table-hover table-sm" style="font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;">
                <tr align=center>
                    <th>CONCEPTO</th>
                    <th>TOTAL</th>
                </tr>
                <tr align=center>
                            <td>Inscripciones</td>
                            <td>""" + str(row.INSCRIPCIONES) + """</td>
                <tr>
                <tr align=center>
                            <td>Certificados</td>
                            <td>""" + str(row.CERTIFICADOS) + """</td>
                <tr>
                <tr align=center>
                            <td>Oficios</td>
                            <td>""" + str(row.OFICIOS) + """</td>
                <tr>
                <tr align=center>
                            <td>Avisos</td>
                            <td>""" + str(row.AVISOS) + """</td>
                <tr>
                <tr align=center>
                            <td>SIGER</td>
                            <td>""" + str(row.SIGER) + """</td>
                <tr>
                <tr align=center>
                            <td><strong>TOTAL</strong></td>
                            <td>""" + str(row.TOTAL) + """</td>
                <tr>
            </table>
                            """

    texto += """
                <div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGRPPIAGN") + """
                </div>
            </div> 
        </article>
        """

    return texto
