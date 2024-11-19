from RS import genera_rs


def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }

def genera_actividades(municipio, beneficiados, programa, foto,anio):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + municipio + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i> <strong> ACCIONES """+ anio +""" </strong></p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong>BENEFICIADOS: </strong>""" + beneficiados + """</p>
                <p style="color:#FFFFFF; margin: 0px;">""" + programa + """</p>
        """
    if foto != "0":
        texto += """<img src='""" + foto + """' width='250' height='180'/>"""

    texto += """
                <div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("CEBV") + """
                </div>
            </div>
        </article>
            """
    return texto

def genera_oficinas(municipio, sp, tel, direccion, foto):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + municipio + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DIRECCIÓN: </strong>""" + direccion + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-phone" style = "color:#FAC63A;"></i><strong> TEL: </strong>""" + tel + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class ="fa fa-user" style = "color:#FAC63A;"></i><strong> RESPONSABLE: </strong > """ + sp + """ </p>
        """
    if foto != "0":
        texto += """<img src = '""" + foto + """' width = '250' height = '180'/>"""

    texto += """
                <div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("CEBV") + """
                </div>
            </div>
        </article>
            """

    return texto
