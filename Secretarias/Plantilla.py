
#CLASS POPUP
    #FONDO #900C3F
    #MARGIN 0PX PARA TODO
    #font-family:sans-serif
    #font-size:11px;
    #border-radius: 20px;
    #padding=5px;

#MUNICIPIO
#BENEFICIADOS (POSIBLEMENTE SE ACTUALICE A PARRAFO)
    #CLASE BADGE-DANGER

#CLASIFICACION
#PROGRAMA
#TEXTO
#MÁS INFORMACIÓN
    #PARRAFOS (<p>)

#FOTO
#IFRAMES
    #MEDIDA ESTANDAR WIDTH 250PX Y HEIGHT 180PX

#PLANTILLA GENERAL
def genera_tarjeta(MUNICIPIO,PROGRAMA,FECHA,APOYOS,BENEFICIADOS,CLASIFICACION,TEXTO,FOTO,IFRAME):
    #HEADER
    FOTOS = [str(row.FOTO1), str(row.FOTO2), str(row.FOTO3), str(row.FOTO4), str(row.FOTO5), str(row.FOTO6),
             str(row.FOTO7), str(row.FOTO8), str(row.FOTO9), str(row.FOTO10), str(row.FOTO11), str(row.FOTO12),
             str(row.FOTO13), str(row.FOTO14), str(row.FOTO15), str(row.FOTO16), str(row.FOTO17), str(row.FOTO18),
             str(row.FOTO19), str(row.FOTO20), str(row.VIDEO1), str(row.VIDEO2), str(row.VIDEO3), str(row.VIDEO4)]

    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                <h6><span class="badge badge-danger"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong>BENEFICIADOS: </strong>""" + BENEFICIADOS + """</span></h6>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong>ACCIÓN: </strong>"""+ACCION+"""</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> PROGRAMA: </strong>""" + PROGRAMA +"""</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-list" style = "color:#FAC63A;"></i><strong> CLASIFICACIÓN: </strong>""" + CLASIFICACION +"""</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-globe" style = "color:#FAC63A;"></i><strong> REGIÓN: </strong>""" + REGION + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> FECHA: </strong> """ + FECHA + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DIRECCIÓN: </strong>""" + DIRECCION + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-phone" style = "color:#FAC63A;"></i><strong> TELÉFONO: </strong>""" + TELEFONO + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-at" style = "color:#FAC63A;"></i><strong> CORREO: </strong>""" + str(row.CORREO) + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class ="fa fa-user" style = "color:#FAC63A;"></i><strong> RESPONSABLE: </strong > """ + USUARIO + """ </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class ="fa fa-male" style = "color:#FAC63A;"></i><strong> HOMBRES BENEFICIADOS: </strong > """ + HOMBRE + """ </p>
                <p style="color:#FFFFFF; margin: 0px ;"><i class ="fa fa-female" style = "color:#FAC63A;"></i><strong> MUJERES BENEFICIADAS: </strong > """ + MUJER + """ </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong> COMITÉ INTERDISCIPLINARIO - BENEFICIADOS: """+ BENEFICIADOS +""" </strong></p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-users" style = "color:#FAC63A;"></i><strong> COMITÉ INTERDISCIPLINARIO - BENEFICIADOS: """+ BENEFICIADOS +""" </strong></p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> COMITÉ INTERDISCIPLINARIO - APOYOS: """+ APOYOS1 +""" </strong></p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-bar-chart" style = "color:#FAC63A;"></i><strong> COMITÉ INTERDISCIPLINARIO - APOYOS: """+ PROYECTOS +""" </strong></p>
                 <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;></i><strong> COMITÉ INTERDISCIPLINARIO - APOYOS:  </strong>"""+ CERTIFICACIONES +"""
                <p style="color:#FFFFFF; margi12n: 0px;"><strong>APOYOS: </strong>""" + APOYOS + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><strong>PROGRAMA: </strong>""" + PROGRAMA + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><strong>TEXTO: </strong>""" + TEXTO + """</p>
                
                
                
                <table class="table table-hover table-sm " style="font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;">

        """

    FECHA = FECHA.replace(" 00:00:00", "")

    if FOTOS:
        carousel_fotos = genera_carousel(FOTOS, "mixto")
        if carousel_fotos[1]:
            texto += carousel_fotos[0]


    #ALBUM
    elif "https://flic.kr" or "https://www.flickr.com/photos" in elemento:
        carousel_contenido += """<!-- Slide -->
                    <div class='""" + cl + """' style="height:180;width:250;">
                        <p align = "center" style = "color:white"> Para más información consulta el siguiente enlace:
                        <br>
                            <a href='""" + str(elemento) + """'><img class="postcard__img" src='images/evidencia_foto.png' width='95%' height='15%'/></a>
                        </p>
                        <br>
                    </div>  

    #CONTENT
    texto += """   
            
            <img src='""" + FOTO + """' width='250' height='180'/>
            
                    
            <div align = "center">                            
                                """ + IFRAME + """
            </div> 
    """

    #FOOTER
    texto += """            
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SECTUR") + """
                </div>
            </div>
        </article>
    """

#PLANTILLA DE DIRECTORIO
def content_directorio(MUNICIPIO, DELEGACION, DIRECCION, DELEGADO, TEL, LAT, LON, FOTO):
    texto = """
        <article style="background-color:#900C3F; font-family:sans-serif; font-size:11px;border-radius: 20px;">
            <div class = "card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style= "color:#FFFFFF; margin: 0px;"><strong>DELEGACIÓN: </strong>""" + DELEGACION + """</p>
                <p style= "color:#FFFFFF; margin: 0px;"><strong>DIRECCIÓN: </strong>""" + DIRECCION + """</p>
                <p style= "color:#FFFFFF; margin: 0px;"><strong>NOMBRE: </strong>""" + DELEGADO + """</p>
                <p style= "color:#FFFFFF; margin: 0px;"><strong>TEL: </strong>""" + TEL + """</p>     
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

#Carousel OK que integra fotos,videos,album
#FOTOS = [str(row.FOTO), str(row.VIDEO), str(row.ALBUM)]
#Se debe llamar a la función así: carousel_fotos = genera_carousel(FOTOS, "mixto")

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
    if lista: """
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

