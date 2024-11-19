from RS import genera_rs


def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }

def genera_tabla_ordinaria(row):
    fila_tabla = " "
    if str(row.Edictos_O) != "0":
        fila_tabla += """
                <tr>
                    <td>Edicto</td>
                    <td>""" + str(row.Edictos_O) + """</td>
                <tr>
        """

    if str(row.Avisos_O) != "0":
        fila_tabla += """
                <tr>
                    <td>Aviso Notarial</td>
                    <td>""" + str(row.Avisos_O) + """</td>
                <tr>
        """

    if str(row.OTROS_O) != "0":
        fila_tabla += """
               <tr>
                    <td>Otros documentos tales como Tarifas, Convenios, Estados Financieros, entre otros. </td>
                    <td>""" + str(row.OTROS_O) + """</td>
               </tr>
        """

    return fila_tabla


def genera_tabla_extraordinaria(row):
    fila_tabla = " "
    if str(row.ACTA_E) != "0":
        fila_tabla += """
                <tr>
                    <td>Acta o Acuerdo</td>
                    <td>""" + str(row.ACTA_E) + """</td>
                <tr>
        """

    if str(row.DN_E) != "0":
        fila_tabla += """
                <tr>
                    <td>Documento Normativo</td>
                    <td>""" + str(row.DN_E) + """</td>
                <tr>
        """

    if str(row.OTROS_E) != "0":
        fila_tabla += """
                <tr>
                    <td>Otros documentos tales como convenios, planes, noombramientos, entre otros. </td>
                    <td>""" + str(row.OTROS_E) + """</td>
                </tr>
        """

    return fila_tabla

def tarjeta_donaciones(row, anio):
    FOTOS = [["foto", str(row.FOTO1)], ["foto", str(row.FOTO2)], ["foto", str(row.FOTO3)],
             ["RS", str(row.RS), row.MUNICIPIO]
             ]


    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
              <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-list" style = "color:#FAC63A;"></i><strong> CLASIFICACIÓN: </strong>""" + str(row.PRODUCTO_EDITORIAL) +"""</p>
              <p style="color:#FFFFFF; margin: 0px;"> CANTIDAD: """ + str(row.CANTIDAD) + """</p>
              """

    if FOTOS:
        carousel_fotos = genera_carousel(FOTOS, "mixto")
        if carousel_fotos[1]:
            texto += carousel_fotos[0]

    texto += """
                </div> 
                    <div align = center>
                        <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("EDITORA") + """
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



def tarjeta_actividades(row, anio):
    FOTOS = [["foto", str(row.FOTO1)], ["foto", str(row.FOTO2)], ["foto", str(row.FOTO3)], ["video", str(row.VIDEO)],
             ["RS", str(row.RS)]
             ]
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> ACCIONES: </strong> """ + anio + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> ACTIVIDAD: </strong>""" + str(row.ACTIVIDAD) +"""</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class ="fa fa-user" style = "color:#FAC63A;"></i><strong> DIRIGIDO A: </strong > """ + str(row.DIRIGIDO) + """ </p>
        """
    if FOTOS:
        carousel_fotos = genera_carousel(FOTOS, "mixto")
        if carousel_fotos[1]:
            texto += carousel_fotos[0]

    texto += """
                </div> 
                    <div align = center>
                        <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("EDITORA") + """
                    </div>
        </article>
        """

    return texto


def tarjeta_decretos(row, anio):
    FOTOS = [["foto", str(row.FOTO)], ["RS", str(row.RS)]]
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> ACCIONES 2021: </strong> </p>
                <p style="color:#FFFFFF; margin: 0px;">""" + str(row.PUBLICACION) + """</p>
        """
    if FOTOS:
        carousel_fotos = genera_carousel(FOTOS, "mixto")
        if carousel_fotos[1]:
            texto += carousel_fotos[0]

    texto += """  
                </div> 
                    <div align = center>
                        <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("EDITORA") + """
                    </div>
        </article>
        """

    return texto


def tarjeta_gaceta_oficial(row, anio):

    inicio_tabla_ordinaria = """
        <table class="table table-hover table-sm" style="font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;">
            <tr align=center style="background-color:#f63434;">
                <td colspan="2" align="center"> GACETA ORDINARIA</td>
            </tr>
            
            <tr align=center>
                <th align="center">CONCEPTO</th>
                <th align="center" >No.</th>
            </tr>
    """

    inicio_tabla_extraordinaria = """
        <table class="table table-hover table-sm" style="font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;">
            <tr align=center style="background-color:#f63434;">
                <td colspan="2" align="center">GACETA EXTRAORDINARIA</td>
            </tr>
            <tr align=center>
                <th>CONCEPTO</th>
                <th>No.</th>
            </tr>
    """

    cierre = """
        </table>
    """

    validar_tabla_ordinaria = genera_tabla_ordinaria(row)
    if validar_tabla_ordinaria != " ":
        validar_tabla_ordinaria = inicio_tabla_ordinaria + validar_tabla_ordinaria + cierre


    validar_tabla_extraordinaria = genera_tabla_extraordinaria(row)
    if validar_tabla_extraordinaria != " ":
        validar_tabla_extraordinaria = inicio_tabla_extraordinaria + validar_tabla_extraordinaria + cierre

    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar"></i> PUBLICACIONES """ + anio +""" </p>
                <p style="color:#FFFFFF; margin: 0px;">PUBLICACIONES TOTALES: """ + str(row.TOTAL_M) + """</p>
                                                
                        <tbody> 
                            """ + validar_tabla_ordinaria + """
                        </tbody>                       
                                                
                        <tbody> 
                            """ + validar_tabla_extraordinaria + """
                        </tbody>   

                """

    texto += """
            </div> 
                <div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("EDITORA") + """
                </div>
        </article>
        """

    return texto


def tarjeta_gaceta_poderes(row, anio):
    texto = """
        <article style="background-color:#900C3F; font-family:sans-serif; font-size:11px;border-radius: 20px;">
           <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> PUBLICACIONES 2021: </strong> </p>
                <p style="color:#FFFFFF; margin: 0px;"> Publicaciones realizadas por los Poderes Estatales, Organismos Autónomos y Gobierno Federal</p>
                    <table class="table table-hover table-sm" style="font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;">
                <tr align=center>
                    <th>PODER U ORGANISMO</th>
                    <th>ACUERDO</th>
                    <th>NORMA</th>
                    <th>OTRO</th>
                    <th>TOTAL</th>
                    
                </tr>
               <tr>
                    <td>PODER JUDICIAL</td>
                    <td>""" + str(row.PJ_Acuerdo) + """ </td>
                    <td>""" + str(row.PJ_Norma) + """ </td>
                    <td>""" + str(row.PJ_Otro) + """ </td>
                    <td>""" + str(row.PJ_TOTAL) + """ </td>
                </tr>
                
                <tr>
                    <td>PODER LEGISLATIVO</td>
                    <td>""" + str(row.PL_Acuerdo) + """ </td>
                    <td>""" + str(row.PL_Norma) + """ </td>
                    <td>""" + str(row.PL_Otro) + """ </td>
                    <td>""" + str(row.PL_TOTAL) + """ </td>
                </tr>
                
                <tr>
                    <td>PODER EJECUTIVO</td>
                    <td>""" + str(row.PE_Acuerdo) + """ </td>
                    <td>""" + str(row.PE_Norma) + """ </td>
                    <td>""" + str(row.PE_Otro) + """ </td>
                    <td>""" + str(row.PE_TOTAL) + """ </td>
                </tr>
                
                <tr>
                    <td>ORGANISMOS AUTÓNOMOS</td>
                    <td>""" + str(row.OA_Acuerdo) + """ </td>
                    <td>""" + str(row.OA_Norma) + """ </td>
                    <td>""" + str(row.OA_Otro) + """ </td>
                    <td>""" + str(row.OA_TOTAL) + """ </td>
                </tr>
                
                <tr>
                    <td>GOBIERNO FEDERAL</td>
                    <td>""" + str(row.GF_Acuerdo) + """ </td>
                    <td>""" + str(row.GF_Norma) + """ </td>
                    <td>""" + str(row.GF_Otro) + """ </td>
                    <td>""" + str(row.GF_TOTAL) + """ </td>
                </tr>
                </table>
                            """

    texto += """
                </div> 
                    <div align = center>
                        <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("EDITORA") + """
                    </div>
        </article>
        """

    return texto
