from RS import genera_rs

def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }

def genera_tarjeta_archivos(municipio,programa,foto):
    FOTOS=[foto]
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px; width:290">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + municipio + """</span></h5>
                <p style= "color:#FFFFFF; margin: 0px;">""" + programa + """</p>"""


    texto += """
        <img src='""" + foto + """' width='250' height='180'/>
    """


    texto += """
                    <div align = center>
                        <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("AGEV") + """
                    </div>
              </div> 

            </article>
            """

    return texto

#definiendo función para la llamada de datos dentro de funciones
def genera_contenido(municipio,programa,descripcion,cantidad,foto):
    FOTOS=[foto]
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + municipio + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;">""" + programa + """</p>"""

    if cantidad!="0":
        texto += """
                <p p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong>Cantidad: </strong>""" + cantidad + """</p>"""

    if foto!="0":
        texto += """
            <img src='""" + foto + """' width='250' height='180'/>
        """


    texto += """
                    <div align = center>
                        <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("AGEV") + """
                    </div>
              </div> 

            </article>
            """

    return texto


