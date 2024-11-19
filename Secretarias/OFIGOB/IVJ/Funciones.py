from RS import genera_rs

def content_tarjeta(MUNICIPIO, BENEFICIADOS, ACCION, APOYO, FOTO):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
            """
    if BENEFICIADOS != "0":
        texto += """
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong>BENEFICIADOS: </strong>""" + BENEFICIADOS + """</p>
        """

    if APOYO != "0":
        texto += """
                <p style="color:#FFFFFF; margin: 0px;"><strong>APOYOS: </strong>""" + APOYO + """</p>
        """
    texto += """
                <p style="color:#FFFFFF; margin: 0px;"><strong>ACCION: </strong>""" + ACCION + """</p>
    """
    if FOTO != "0":
        texto += """
                <img src='""" + FOTO + """' width='250' height='180'/>
            """

    texto += """            
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("IVJ") + """
                </div>
            </div>
        </article>
    """

    return texto

