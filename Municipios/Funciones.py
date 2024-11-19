def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }

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



def tarjeta_capacitaciones(row):
    FOTOS = [str(row.FOTO1), str(row.FOTO2), str(row.VIDEO)]

    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i>""" + str(
        row.FECHA) + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong>TOTAL PERSONAS CAPACITADAS: </strong>""" + str(
        row.TOTAL) + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-female" style = "color:#FAC63A;"></i><strong>MUJERES: </strong>""" + str(
        row.MUJERES) + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-male" style = "color:#FAC63A;"></i><strong>HOMBRES: </strong>""" + str(
        row.HOMBRES) + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><strong>TEMA: </strong>""" + str(row.TEMA) + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><strong>DESCRIPCIÓN: </strong>""" + str(row.DESCRIPCION) + """</p>
        """

    texto += """
        <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
            <div class="carousel-inner">    
    """

    carousel_fotos = genera_carousel(FOTOS, "mixto")
    if carousel_fotos[1] :
        if carousel_fotos:
            texto += carousel_fotos[0]

    return texto


def tarjeta_acciones(row):
    FOTOS = [str(row.FOTO1), str(row.FOTO2), str(row.VIDEO)]

    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i>""" + str(
        row.FECHA) + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong>TOTAL PERSONAS BENEFICIADAS: </strong>""" + str(
        row.TOTAL) + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-female" style = "color:#FAC63A;"></i><strong>MUJERES: </strong>""" + str(
        row.MUJERES) + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-male" style = "color:#FAC63A;"></i><strong>HOMBRES: </strong>""" + str(
        row.HOMBRES) + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><strong>ACCIÓN: </strong>""" + str(row.ACCION) + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><strong>DESCRIPCIÓN: </strong>""" + str(row.DESCRIPCION) + """</p>
        """

    texto += """
        <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
            <div class="carousel-inner">    
    """

    carousel_fotos = genera_carousel(FOTOS, "mixto")
    if carousel_fotos[1] :
        if carousel_fotos:
            texto += carousel_fotos[0]

    return texto

