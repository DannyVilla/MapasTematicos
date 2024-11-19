def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }


def genera_trabajadores_movilidad(MUNICIPIO, BENEFICIADOS, ACCION, FOTO, AÑO):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> ACCIONES: </strong> """ + AÑO + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong> BENEFICIADOS: """+ BENEFICIADOS +""" </strong></p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> TIPO DE EVENTO: </strong>"""+ ACCION +"""</p>
           """

    if FOTO != "0" or 0:
        texto += """
            <div>
                 <img src='""" + FOTO + """' width='250' height='180'/>
            </div> 
        """

    return texto

def genera_tarjeta(MUNICIPIO, BENEFICIADOS, TEMA, FOTO, AÑO):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> ACCIONES: </strong> """ + AÑO + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong> BENEFICIADOS: """+ BENEFICIADOS +""" </strong></p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> TEMA: </strong>"""+ TEMA +"""</p>
    """

    if FOTO != "0" or 0:
        texto += """
            <div>
                 <img src='""" + FOTO + """' width='250' height='180'/>
            </div> 
        """

    return texto

def genera_feria(MUNICIPIO, APOYO, BENEFICIADOS, FOTO, AÑO):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> ACCIONES: </strong> """ + AÑO + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong> BENEFICIADOS: """+ BENEFICIADOS +""" </strong></p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> TIPO DE EVENTO: </strong>"""+ APOYO +"""</p>
           """

    if FOTO != "0" or 0:
        texto += """
            <div>
                 <img src='""" + FOTO + """' width='250' height='180'/>
            </div> 
        """

    return texto


def genera_icatver(MUNICIPIO, FECHA, ACCION, BENEFICIADOS, FOTO):
    FECHA = FECHA.replace(" 00:00:00", "")

    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> FECHA: </strong> """ + FECHA + """  </p>          
                """
    if BENEFICIADOS != "0" or 0:
        texto += """
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong> BENEFICIADOS: """+ BENEFICIADOS +""" </strong></p>
            """
    texto += """
            <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> ACCIÓN: </strong>"""+ACCION+"""</p>
        """

    if FOTO != "0" or 0:
        texto += """
            <div>
                 <img src='""" + FOTO + """' width='250' height='180'/>
            </div> 
        """

    return texto


def genera_cclv(DELEGACION, NOMBRE, DIRECCION, JURISDICCION, EMAIL, TEL, FOTO):

    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + DELEGACION + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class ="fa fa-user" style = "color:#FAC63A;"></i><strong> RESPONSABLE: </strong > """ + NOMBRE + """ </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DIRECCIÓN: </strong>""" + DIRECCION + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> JURISDICCION: </strong>""" + JURISDICCION + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-at" style = "color:#FAC63A;"></i><strong> CORREO: </strong>""" + EMAIL + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-phone" style = "color:#FAC63A;"></i><strong> TELÉFONO: </strong>""" + TEL + """  </p>
        """

    if FOTO != "0" or 0:
        texto += """
            <div align = "center" >
                 <img src='""" + FOTO + """' width='150' height='180'/>
            </div> 
        """

    return texto


def conversion(old):
    direction = {'N': -1, 'S': 1, 'E': -1, 'W': 1}
    new = old.replace(u'°', ' ').replace('\'', ' ').replace('"', ' ')
    new = new.split()
    new_dir = new.pop()
    new.extend([0, 0, 0])
    return (int(new[0]) + int(new[1]) / 60.0 + float(new[2]) / 3600.0) * direction[new_dir]

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
        carousel[
            0] = carousel_inicio + carousel_indicadores + "</ol>" + carousel_contenido + "</div>" + carousel_controls
        carousel[1] = hay
        return carousel

