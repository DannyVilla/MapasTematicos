from RS import genera_rs


def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }


# definiendo función para la llamada de datos dentro de funciones
def genera_cont_reuniones(municipio, reuniones, fecha, descripcion, foto1, foto2,anio):
    FOTOS = [foto1, foto2]
    fecha = fecha.replace(" 00:00:00", "")
    texto = """
            <article style="background-color:#900C3F; font-family:sans-serif; font-size:11px;border-radius: 20px;">
            <div class = "card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + municipio + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-list" style = "color:#FAC63A;"></i><strong> REUNIONES: </strong>""" + reuniones +"""</p>
            """
    if fecha != "0":
        texto += """
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> FECHAS: </strong> """ + fecha + """  </p>
                """
    texto += """
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> DESCRIPCIÓN: </strong>"""+descripcion+"""</p>
                """

    carousel_fotos = genera_carousel(FOTOS, "fotos")
    if carousel_fotos[1]:
        if carousel_fotos:
            texto += carousel_fotos[0]

    texto += """
                    <div align = center>
                        <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGG") + """
                    </div>
              </div> 

            </article>
            """

    return texto


def contenido_oficina(municipio, encargado, area, foto, direccion, telefono):
    texto = """
            <article style="background-color:#900C3F; font-family:sans-serif; font-size:11px;border-radius: 20px;">
            <div class = "card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + municipio + """</span></h5>
                <p style= "color:#FFFFFF; margin: 0px;font-family:sans-serif; font-size:13px;"><strong>""" + area + """</strong></p>        
                <p style="color:#FFFFFF; margin: 0px;"><i class ="fa fa-user" style = "color:#FAC63A;"></i><strong> RESPONSABLE: </strong > """ + encargado + """ </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DIRECCIÓN: </strong>""" + direccion + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-phone" style = "color:#FAC63A;"></i><strong> TELÉFONO: </strong>""" + telefono + """  </p>
                """

    if foto != "0":
        texto += """
                <div align="center">
                    <img src='""" + foto + """' align='center' width='250' height='180'/>
                <div>
                """

    texto += """
                       <div align = center>
                           <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGG") + """
                       </div>
                 </div> 

               </article>
               """

    return texto


def genera_cont_slyp(cvegeo, municipio, descripcion, cantidad, foto1, foto2, anio):
    FOTOS = [foto1, foto2]

    texto = """
            <article style="background-color:#900C3F; font-family:sans-serif; font-size:11px;border-radius: 20px;">
            <div class = "card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + municipio + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> AÑO: </strong> """ + anio + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> DESCRIPCIÓN: </strong>"""+descripcion+"""</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> TOTAL DE DOCUMENTOS: """+ cantidad +""" </strong></p>
                """

    carousel_fotos = genera_carousel(FOTOS, "fotos")
    if carousel_fotos[1]:
        if carousel_fotos:
            texto += carousel_fotos[0]
                

    texto += """
                       <div align = center>
                           <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGG") + """
                       </div>
                 </div> 

               </article>
               """

    return texto


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
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar"></i><strong> ACCIONES: </strong>""" + str(
        row.TRIMESTRE) + """</p>
                <h6><span class="badge badge-danger"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong> BENEFICIADOS: </strong>""" + str(row.BENEFICIADOS) + """</span></h6>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> APOYOS: """+ str(row.APOYOS) +""" </strong></p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> PROGRAMA: </strong>""" + str(row.PROGRAMA) +"""</p>
    """

    carousel_fotos = genera_carousel(FOTOS, "fotos")
    carousel_videos = genera_carousel(VIDEOS, "videos")
    if carousel_fotos[1] or carousel_videos[1]:
        if carousel_fotos:
            texto += carousel_fotos[0]

    texto += """
            </div> 
                <div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGG") + """
                </div>
        </article>
        """

    return texto


def contenido_tramites(municipio, descripcion, inf, ges_lab, prog_soc, sind, viv, regu, agra, trans, elec, salud,
                       med_amb, agua, edu, ssp, otros, total, foto1, foto2, anio):

    FOTOS = [foto1, foto2]

    texto = """
    <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + municipio + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> AÑO: </strong> """ + anio + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> DESCRIPCIÓN: </strong>"""+descripcion+"""</p>
        """

    carousel_fotos = genera_carousel(FOTOS, "fotos")
    if carousel_fotos[1]:
        if carousel_fotos:
            texto += carousel_fotos[0]

    contenido_tabla = """
        <div class="card-body">   
                    <table id=aplicaciones class="table table-hover table-sm table-responsive" style="font-family:sans-serif; font-size:12px;color:#FFFFFF; background-color:#f64668; alt="First slide;"> 
                        <tr align="center">
                            <th>Tema tratado</th>
                            <th>Cantidad</th>          
                        </tr>
        """
    contenido_tabla += genera_tabla(inf, ges_lab, prog_soc, sind, viv, regu, agra, trans, elec, salud,
                                    med_amb, agua, edu, ssp, otros, total)
    cierre = """
                    </table>
                 """
    texto += contenido_tabla + cierre
    texto += """
                       <div align = center>
                           <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGG") + """
                       </div>
                 </div> 

               </article>
               """

    return texto


def genera_tabla(inf, ges_lab, prog_soc, sind, viv, regu, agra, trans, elec, salud,
                 med_amb, agua, edu, ssp, otros, total):
    texto_tabla = ""
    if inf != "0":
        texto_tabla += """
                <tr> 
                            <td>    
                                Infraestructura                  
                            </td>                     
                            <td align="center">""" + inf + """</td>
               </tr>                
            """
    if ges_lab != "0":
        texto_tabla += """
                <tr> 
                            <td>    
                                Gestiones Laborales                  
                            </td>                     
                            <td align="center">""" + ges_lab + """</td>
               </tr>                
            """

    if prog_soc != "0":
        texto_tabla += """
                <tr> 
                            <td>    
                                Programas Sociales                  
                            </td>                     
                            <td align="center">""" + prog_soc + """</td>
               </tr>                
            """

    if sind != "0":
        texto_tabla += """
                <tr> 
                            <td>    
                                Sindicatos                  
                            </td>                     
                            <td align="center">""" + sind + """</td>
               </tr>                
            """

    if viv != "0":
        texto_tabla += """
                <tr> 
                            <td>    
                                Vivienda                  
                            </td>                     
                            <td align="center">""" + viv + """</td>
               </tr>                
            """

    if regu != "0":
        texto_tabla += """
                <tr> 
                            <td>    
                                Regularización                  
                            </td>                     
                            <td align="center">""" + regu + """</td>
               </tr>                
            """

    if agra != "0":
        texto_tabla += """
                <tr> 
                            <td>    
                                Agrario                  
                            </td>                     
                            <td align="center">""" + agra + """</td>
               </tr>                
            """

    if trans != "0":
        texto_tabla += """
                <tr> 
                            <td>    
                                Servicios de Transporte                  
                            </td>                     
                            <td align="center">""" + trans + """</td>
               </tr>                
            """

    if elec != "0":
        texto_tabla += """
                <tr> 
                            <td>    
                                Electrificación                  
                            </td>                     
                            <td align="center">""" + elec + """</td>
               </tr>                
            """

    if salud != "0":
        texto_tabla += """
                <tr> 
                            <td>    
                                Salud                  
                            </td>                     
                            <td align="center">""" + salud + """</td>
               </tr>                
            """

    if med_amb != "0":
        texto_tabla += """
                <tr> 
                            <td>    
                                Medio Ambiente                  
                            </td>                     
                            <td align="center">""" + med_amb + """</td>
               </tr>                
            """

    if agua != "0":
        texto_tabla += """
                <tr> 
                            <td>    
                                Agua                  
                            </td>                     
                            <td align="center">""" + agua + """</td>
               </tr>                
            """

    if edu != "0":
        texto_tabla += """
                <tr> 
                            <td>    
                                Educación                  
                            </td>                     
                            <td align="center">""" + edu + """</td>
               </tr>                
            """

    if ssp != "0":
        texto_tabla += """
                <tr> 
                            <td>    
                                SSP                  
                            </td>                     
                            <td align="center">""" + ssp + """</td>
               </tr>                
            """

    if otros != "0":
        texto_tabla += """
                <tr> 
                            <td>    
                                Otros                  
                            </td>                     
                            <td align="center">""" + otros + """</td>
               </tr>                
            """

    if total != "0":
        texto_tabla += """
                <tr> 
                            <td>    
                                Total                  
                            </td>                     
                            <td align="center">""" + total + """</td>
               </tr>                
            """
    return texto_tabla


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



