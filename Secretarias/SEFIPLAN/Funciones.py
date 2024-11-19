from RS import genera_rs
def genera_tarjeta(MUNICIPIO, DIRECCION, TELEFONO, FOTO):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DIRECCIÓN: </strong>""" + DIRECCION + """  </p>
        """
    if TELEFONO != "0":
        texto += """
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-phone" style = "color:#FAC63A;"></i><strong> TELÉFONO: </strong>""" + TELEFONO + """  </p>
        """
    texto += """
                <p align = "center" style="color:#FFFFFF; margin: 0px;"><strong> UBICACIÓN: </strong></p>
                    <div style="margin: 0px; text-align: center;">    
                        <a href='""" + FOTO + """' target="_blank"><i class="fa fa-map-marker fa-2x" style = "color:#99E88A;"></i></a>
                    </div>
        """
    texto += """
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SEFIPLAN") + """
                </div>
            </div>
        </article>
        """

    return texto


def genera_acciones(MUNICIPIO,TITULO, FECHA, ENLACEPUB, ENLACEFOT1, ENLACEFOT2, URL):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i>""" + FECHA + """  </p>
                <p style="color:#FFFFFF; margin: 0px;">""" + TITULO + """</p>
                <li><a style="color:#D6EAF8; padding=5px;"href=" """ + URL + """ ">Publicación de Facebook</a></li>
        """
    if ENLACEPUB != "0":
        texto += """
                """+ENLACEFOT1+"""
        """

    texto += """
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SEFIPLAN") + """
                </div>
            </div>
        </article>
        """
    return texto
