from RS import genera_rs


def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }


def genera_rutas(MUNICIPIO, NOMBRE_RUTA, BENEFICIARIOS, LINK):
    texto = """
        <article style="background-color:#900C3F; font-family:sans-serif; font-size:11px;border-radius: 20px;">
           <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>              
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong> BENEFICIADOS: """+ BENEFICIARIOS +""" </strong></p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> NOMBRE DE LA RUTA: </strong>""" + NOMBRE_RUTA + """  </p>
                <a href='""" + LINK + """'><img class="postcard__img" src='images/rutas.png' width='95%' height='30%'/></a>
            """
    texto += """<div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SECTUR") + """
                </div>
        </article>
        """

    return texto


def genera_consejos_mun(MUNICIPIO, FECHA_INST, ACTA):
    FECHA_INST = FECHA_INST.replace(" 00:00:00", "")
    texto = """
        <article style="background-color:#900C3F; font-family:sans-serif; font-size:11px;border-radius: 20px;">
           <div class="card-body">
              <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> INSTALACIÓN: </strong> """ + FECHA_INST + """  </p>
              
            """
    
    if ACTA != "0":
        texto+= """
            <a href='""" + ACTA + """'><img class="postcard__img" src='images/consulta_acta.png' width='95%' height='15%'/></a>
        """

    texto += """<div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SECTUR") + """
                </div>
        </article>
        """

    return texto


def genera_consejos_reg(MUNICIPIO, CONSEJO, INSTALACION, FOTO1, FOTO2, VIDEO):
    texto = """
        <article style="background-color:#900C3F; font-family:sans-serif; font-size:11px;border-radius: 20px;">
           <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><strong>CONSEJO: </strong>""" + CONSEJO + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> INSTALACIÓN: </strong> """ + INSTALACION + """  </p>
           """

    texto += """
        <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
            <div class="carousel-inner">    
    """

    if FOTO1 != "0":
        texto += """
                <div class="carousel-item active">
                    <img class="d-block w-100" src='""" + FOTO1 + """' width='250' height='180'/ alt="First slide">
                </div>    
        """
    if FOTO2 != "0":
        texto += """
                <div class="carousel-item">
                    <img class="d-block w-100" src='""" + FOTO2 + """' width='250' height='180'/ alt="Second slide">
                </div>    
        """

    if VIDEO != "0":
        texto += """ 
                <div align = "center">
                    """ + VIDEO + """
                </div>
          """

    if FOTO1 != "0" and FOTO2 != "0":

        texto += """
                </div>
                  <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="sr-only">Previous</span>
                  </a>
                  <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="sr-only">Next</span>
                  </a>                   
        """

    texto += """
            </div> 
                <div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SECTUR") + """
                </div>
        </article>
        """

    return texto


def genera_paisajes(MUNICIPIO, PROYECTO, ANIO, BENEFICIARIOS, FOTO):
    texto = """
        <article style="background-color:#900C3F; font-family:sans-serif; font-size:11px;border-radius: 20px;">
           <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> AÑO: </strong> """ + ANIO + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-bar-chart" style = "color:#FAC63A;"></i><strong> PROYECTO: </strong>"""+ PROYECTO +""" </p>
        """
    if FOTO != "0":
        texto += """
                <div align = center>
                    <img src='""" + FOTO + """' width='250' height='180'/>
                </div>
        """

    texto += """<div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SECTUR") + """
                </div>
        </article>
        """

    return texto

def genera_turismo(MUNICIPIO, PROGRAMA, ANIO, BENEFICIARIOS, FOTO):
        texto = """
        <article style="background-color:#900C3F; font-family:sans-serif; font-size:11px;border-radius: 20px;">
               <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> AÑO: </strong> """ + ANIO + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong> BENEFICIADOS: """+ BENEFICIARIOS +""" </strong></p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> PROGRAMA: </strong>""" + PROGRAMA +"""</p>
            """
        if FOTO != "0":
            texto += """
                    <div align = "center">
                        <img src='""" + FOTO + """' width='250' height='180'/>
                    </div>    
            """

        texto += """<div align = center>
                        <p style="color:white">Más información: </p> """ + genera_rs("SECTUR") + """
                    </div>
            </article>
            """

        return texto


def genera_servicios(MUNICIPIO, CERTIFICACIONES, ENTREGADAS, CURSO, TOTAL, FOTO1, FOTO2):
    texto = """
        <article style="background-color:#900C3F; font-family:sans-serif; font-size:11px;border-radius: 20px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-square-o" style = "color:#FAC63A;"></i><strong> CERTIFICACIÓN:  </strong>"""+ CERTIFICACIONES +"""</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-square" style = "color:#FAC63A;"></i><strong> ENTREGADAS:  </strong>"""+ ENTREGADAS +"""</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-indent" style = "color:#FAC63A;"></i><strong> CURSO: </strong>""" + CURSO +"""</p>
            """

    texto += """
            <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
                <div class="carousel-inner">    
        """

    if FOTO1 != "0":
        texto += """
                <div class="carousel-item active">
                    <img class="d-block w-100" src='""" + FOTO1 + """' width='250' height='180'/ alt="First slide">
                </div>     
        """
    if FOTO2 != "0":
        texto += """
                <div class="carousel-item">
                    <img class="d-block w-100" src='""" + FOTO2 + """' width='250' height='180'/ alt="Second slide">
                </div>    
        """

    if FOTO1 != "0" and FOTO2 != "0":
        texto += """
                </div>
                  <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="sr-only">Previous</span>
                  </a>
                  <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="sr-only">Next</span>
                  </a>                   
        """

    texto += """
            </div> 
                <div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SECTUR") + """
                </div>
        </article>
        """

    return texto

def genera_ferias_tradiciones(MUNICIPIO,FESTIVAL,FOTO1):
    texto = """
        <article style="background-color:#900C3F; font-family:sans-serif; font-size:11px;border-radius: 20px;">
               <div class="card-body">
                  <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-bar-chart" style = "color:#FAC63A;"></i><strong> FESTIVAL: """+ FESTIVAL +""" </strong></p>
            """

    if FOTO1 != "0":
        texto += """
                <div align = "center">
                   """ + FOTO1 + """
                </div>     
        """

    texto += """<div align = center>
                    <p style="color:white">Más información: </p> """ + genera_rs("SECTUR") + """
                </div>
            </article>
    """

    return texto

def genera_planeaciones_vinculaciones(MUNICIPIO,PROGRAMA,DESCRIPCION,FOTO1,FOTO2):
    texto = """
            <article style="background-color:#900C3F; font-family:sans-serif; font-size:11px;border-radius: 20px;">
                   <div class="card-body">
                      <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-indent" style = "color:#FAC63A;"></i><strong> CURSO: </strong>""" + PROGRAMA +"""</p>
                """
    if DESCRIPCION != "0":
        texto += """
            <p style="color:#FFFFFF; margin: 0px;">""" + DESCRIPCION + """</p>
        """

    texto += """
                <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
                    <div class="carousel-inner">    
            """

    if FOTO1 != "0":
        texto += """
                    <div class="carousel-item active">
                        <img class="d-block w-100" src='""" + FOTO1 + """' width='250' height='180'/ alt="First slide">
                    </div>     
            """
    if FOTO2 != "0":
        texto += """
                    <div class="carousel-item">
                        <img class="d-block w-100" src='""" + FOTO2 + """' width='250' height='180'/ alt="Second slide">
                    </div>    
            """

    if FOTO1 != "0" and FOTO2 != "0":
        texto += """
                    </div>
                      <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="sr-only">Previous</span>
                      </a>
                      <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="sr-only">Next</span>
                      </a>                   
            """

    texto += """
                </div> 
                    <div align = center>
                        <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SECTUR") + """
                    </div>
            </article>
            """

    return texto

def genera_capas(MUNICIPIO,ACTIVIDAD,FECHA,DESCRIPCION,BENEFICIARIOS,FOTO1,FOTO2,VIDEO,OTRO):
    FOTOS = [FOTO1,FOTO2,VIDEO,OTRO]
    FECHA = FECHA.replace(" 00:00:00", "")

    texto = """
            <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
                <div class="card-body">
                    <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                    <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> FECHA: </strong> """ + FECHA + """  </p>               
        """
    if BENEFICIARIOS != "0":
        texto += """ 
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong> BENEFICIADOS: </strong>"""+ BENEFICIARIOS +""" </p>
        """

    texto+="""
                      
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-bar-chart" style = "color:#FAC63A;"></i><strong> ACTIVIDAD: </strong>""" + ACTIVIDAD +"""</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-indent" style = "color:#FAC63A;"></i><strong> DESCRIPCIÓN: </strong>""" + DESCRIPCION +"""</p>
                """

    if FOTOS:
        carousel_fotos = genera_carousel(FOTOS, "mixto")
        if carousel_fotos[1]:
            texto += carousel_fotos[0]

    texto += """
                </div> 
                    <div align = center>
                        <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SECTUR") + """
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
                    elif "iframe src=" in elemento:
                        carousel_contenido += """<!-- Slide -->
                                    <div class='""" + cl + """' style="height:180;width:250;">
                                        <p align = "center" style = "color:white"> Para más información consulta el siguiente enlace:
                                        <br>
                                            """ + str(elemento) + """
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
