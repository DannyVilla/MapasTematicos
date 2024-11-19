
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
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <h6><span class="badge badge-danger">BENEFICIADOS: """ + BENEFICIADOS + """</span></h6>
                <p style="color:#FFFFFF; margin: 0px;">""" + PROGRAMA + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar"></i>""" + FECHA + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><strong>APOYOS: </strong>""" + APOYOS + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><strong>PROGRAMA: </strong>""" + PROGRAMA + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><strong>TEXTO: </strong>""" + TEXTO + """</p>
        """

    #CONTENT
    texto += """   
            
            <img src='""" + FOTO + """' width='250' height='180'/>
            
                    
            <div align = "center">                            
                                """ + IFRAME + """
            </div> 
    """

    #FOOTER
    texto += """
            </div> 
                    <div align = center>
                        <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SECTUR") + """
                    </div>
        </article>
    """


#PLANTILLA CON CAROUSEL
def genera_consejos_reg(MUNICIPIO, CONSEJO, INSTALACION, FOTO1, FOTO2, VIDEO):
    texto = """
        <article style="background-color:#900C3F; font-family:sans-serif; font-size:11px;border-radius: 20px;">
           <div class="card-body">
              <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
              <h6><span class="badge badge-danger">Consejo: """ + CONSEJO + """</span></h6>
              <h6><span class="badge badge-danger"><i class="fa fa-calendar"></i>Fecha de Instalación: """ + INSTALACION + """</span></h6>
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
