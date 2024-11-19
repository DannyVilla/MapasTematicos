from RS import genera_rs


def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }


def content_directorio(MUNICIPIO, DELEGACION, DIRECCION, DELEGADO, TEL, LAT, LON, FOTO):
    texto = """
        <article style="background-color:#900C3F; font-family:sans-serif; font-size:11px;border-radius: 20px;">
            <div class = "card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DELEGACIÓN: </strong>""" + DELEGACION + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DIRECCIÓN: </strong>""" + DIRECCION + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class ="fa fa-user" style = "color:#FAC63A;"></i><strong> NOMBRE: </strong > """ + DELEGADO + """ </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-phone" style = "color:#FAC63A;"></i><strong> TELÉFONO: </strong>""" + TEL + """  </p>   
    """

    if ".jpg" in FOTO:
        texto += """
                <div align = "center">            
                    <img align  = "center" src='""" + FOTO + """' width='250' height='180'/>                    
                    <p style= "margin:0px;color:white;">Más información: </p> """ + genera_rs("DGCV") + """                   
                </div>
            """
    else:
        texto += """<div align = "center">
                        <a href='""" + FOTO + """' target="_blank"><i class="fa fa-camera" style="font-family:sans-serif;font-size:11px;color:#FFFFFF;"></i></a>
                         <p style= "margin:0px;color:white;">Más información: </p> """ + genera_rs("DGCV") + """
                    </div>              

            """
        texto += """                
            </article>
            """
    return texto
def genera_digitalizaciones(MUNICIPIO, DELEGACION, ACTUALIZACION, ACCION, DIGITALIZACIONES, FOTO):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
           <div class="card-body">
              <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DELEGACIÓN: </strong>""" + DELEGACION + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i> """ + ACTUALIZACION + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> ACCIÓN: </strong>""" + ACCION +"""</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> DIGITALIZACIONES ENTREGADAS: </strong>""" + DIGITALIZACIONES + """</p>

            """
    if FOTO != "0":
        texto += """
                <div align = "center">            
                    <img align  = "center" src='""" + FOTO + """' width='250' height='180'/>                              
                </div>                
        """

    texto += """<div align = center><p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGCV") + """</div>
        </article>
        """

    return texto


def genera_capacitaciones(municipio, DELEGACION, FECHA, ACCION, spb, ACTUALIZACION, FOTO):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
           <div class="card-body" >
              <h5 align = "center"><span class="badge badge-danger">""" + municipio + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DELEGACIÓN: </strong>""" + DELEGACION + """  </p>
              <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i> """ + ACTUALIZACION + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> ACCIÓN: </strong>""" + ACCION +"""</p>
              <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> SERVIDORES PÚBLICOS ALCANZADOS: </strong>""" + spb + """</p>
            """
    if FOTO != "0":
        texto += """
                <div align = "center">            
                    <img align  = "center" src='""" + FOTO + """' width='250' height='180'/>                              
                </div>                
        """

    texto += """<div align = center><p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGCV") + """</div>
        </article>
        """

    return texto

def genera_promociones(MUNICIPIO, DELEGACION, FECHA, ACCION, ASESORIAS, ACTUALIZACION, FOTO):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
           <div class="card-body">
              <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DELEGACIÓN: </strong>""" + DELEGACION + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i> """ + ACTUALIZACION + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> ACCIÓN: </strong>""" + ACCION +"""</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> ASESORIAS BRINDADAS: </strong>""" + ASESORIAS + """</p>
            """
    if FOTO != "0":
        texto += """
                <div align = "center">            
                    <img align  = "center" src='""" + FOTO + """' width='250' height='180'/>                              
                </div>                
        """

    texto += """<div align = center><p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGCV") + """</div>
        </article>
        """

    return texto

def genera_supervisiones(MUNICIPIO, DELEGACION, FECHA, ACCION, SUPERVISIONES, ACTUALIZACION, FOTO):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
           <div class="card-body" >
              <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DELEGACIÓN: </strong>""" + DELEGACION + """  </p>
              <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i> """ + ACTUALIZACION + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> ACCIÓN: </strong>""" + ACCION +"""</p>
              <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> SUPERVISIONES REALIZADAS: </strong>""" + SUPERVISIONES + """</p>
            """
    if FOTO != "0":
        texto += """
                <div align = "center">            
                    <img align  = "center" src='""" + FOTO + """' width='250' height='180'/>                              
                </div>                
        """

    texto += """<div align = center><p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGCV") + """</div>
        </article>
        """
    return texto

def genera_convenios(MUNICIPIO, DELEGACION, FECHA, ACCION, CONVENIOS, ACTUALIZACION, FOTO):
    ACTUALIZACION = ACTUALIZACION.replace(" 00:00:00", "")
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
           <div class="card-body" >
              <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
              <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DELEGACIÓN: </strong>""" + DELEGACION + """  </p>
              <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i> """ + ACTUALIZACION + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> ACCIÓN: </strong>""" + ACCION +"""</p>
              <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> CONVENIOS FORMALIZADOS: </strong>""" + CONVENIOS + """</p>
            """
    if FOTO != "0":
        texto += """
                <div align = "center">            
                    <img align  = "center" src='""" + FOTO + """' width='250' height='180'/>                              
                </div>                
        """

    texto += """<div align = center><p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGCV") + """</div>
        </article>
        """
    return texto

def genera_tablas(MUNICIPIO, DELEGACION, ACCION, TABLAS, ACTUALIZACION, FOTO):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
           <div class="card-body">
              <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DELEGACIÓN: </strong>""" + DELEGACION + """  </p>
              <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i> """ + ACTUALIZACION + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> ACCIÓN: </strong>""" + ACCION +"""</p>
              <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> TABLAS DE VALORES: </strong>""" + TABLAS + """</p>
            """
    if FOTO != "0":
        texto += """
                <div align = "center">            
                    <img align  = "center" src='""" + FOTO + """' width='250' height='180'/>                              
                </div>                
        """

    texto += """<div align = center><p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGCV") + """</div>
        </article>
        """

    return texto

def genera_avaluos(MUNICIPIO, DELEGACION, ACCION, NUM, BENEFICIADOS, FECHA, FOTO):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
           <div class="card-body">
              <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DELEGACIÓN: </strong>""" + DELEGACION + """  </p>
              <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i> """ + FECHA + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> ACCIÓN: </strong>""" + ACCION +"""</p>
              <p style="color:#FFFFFF; margin: 0px;"><strong>AVALUOS ENTREGADOS: </strong>""" + NUM + """</p>
              <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> DEPENDENCIAS BENEFICIADAS: </strong>""" + BENEFICIADOS + """</p>

            """
    if FOTO != "0":
        texto += """
                <div align = "center">            
                    <img align  = "center" src='""" + FOTO + """' width='250' height='180'/>                              
                </div>                
        """

    texto += """<div align = center><p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGCV") + """</div>
        </article>
        """

    return texto

def genera_tablavalores(MUNICIPIO, DELEGACION, ACCION, FECHA, FOTO):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
           <div class="card-body">
              <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
              <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DELEGACIÓN: </strong>""" + DELEGACION + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> ACCIÓN: </strong>""" + ACCION +"""</p>
              <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i> """ + FECHA + """</p>

            """
    if FOTO != "0":
        texto += """
                <div align = "center">            
                    <img align  = "center" src='""" + FOTO + """' width='250' height='180'/>                              
                </div>                
        """

    texto += """<div align = center><p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGCV") + """</div>
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


def genera_levantamientos(row):
    FOTOS = [str(row.FOTO1), str(row.FOTO2),str(row.FOTO3),str(row.FOTO4)]

    ACTUALIZACION = str(row.ACTUALIZACION).replace(" 00:00:00", "")

    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
           <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DELEGACIÓN: </strong>""" + str(row.DELEGACION) + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> ACCIÓN: </strong>""" + str(row.ACCION) +"""</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> LEVANTAMIENTOS REALIZADOS: </strong>"""+str(row.NUM)+"""</p>
                <p style="color:#FFFFFF; margin: 0px;"><strong><i class="fa fa-calendar" style = "color:#FAC63A;"></i> FECHA DE ACTUALIZACION: </strong>"""+ ACTUALIZACION +"""</p>
              """

    if FOTOS:
        carousel_fotos = genera_carousel(FOTOS, "mixto")
        if carousel_fotos[1]:
            texto += carousel_fotos[0]

    texto += """
                <div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGCV") + """
                </div> 
            </div>
        </article>
        """

    return texto


