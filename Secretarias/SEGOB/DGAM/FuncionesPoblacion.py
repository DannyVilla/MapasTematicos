from RS import genera_rs

def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }

#definiendo función para la llamada de datos dentro de funciones
def genera_contenido(MUNICIPIO,ACCION,SOLICITUDES,ANIO):
    texto = """
         <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> ACCIONES: </strong> """ + ANIO + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong>ACCIÓN: </strong>"""+ACCION+"""</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-bar-chart" style = "color:#FAC63A;"></i><strong> SOLICITUDES: """+ SOLICITUDES +""" </strong></p>
                """
    texto += """
                    </div> 
                            <div align = center>
                                <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGAM") + """
                            </div>
                </article>
            """


    return texto


def contenido_albergue(MUNICIPIO, FOTO, NOMBRE, DIRECCION, TELEFONO, CORREO, PAGINA, FACEBOOK, DESCRIPCION):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class = "card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class ="fa fa-user" style = "color:#FAC63A;"></i><strong> NOMBRE: </strong > """ + NOMBRE + """ </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i> """ +DESCRIPCION+"""</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DIRECCIÓN: </strong>""" + DIRECCION + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-phone" style = "color:#FAC63A;"></i><strong> TELÉFONO: </strong>""" + TELEFONO + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-at" style = "color:#FAC63A;"></i><strong> CORREO: </strong>""" + CORREO + """  </p>
                <p style= "color:#FFFFFF; margin: 0px;"><strong>Facebook:</strong><a class="navbar-brand" target=_blank href='""" + FACEBOOK + """'>
                    <img alt="Brand" src="images/fb3.png" width="30" height="30">
                  </a></p>
                <div align="center">
                    <img src='""" + FOTO + """' align='center' width='250' height='180'/>
                <div>"""

    
    if PAGINA!="0":
            texto+="""
                <p style= "color:#FFFFFF; margin: 0px;"><strong>Página: </strong>""" + PAGINA + """</p>
                """

    texto += """
                </div> 
                        <div align = center>
                            <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGAM") + """
                        </div>
            </article>
        """


    return texto
