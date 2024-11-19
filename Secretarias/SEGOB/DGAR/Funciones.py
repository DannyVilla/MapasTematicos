from RS import genera_rs
def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }

def tarjeta_contenido(row,anio):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> ACCIONES """ + anio + """ </strong></p>
    """
    if str(row.BENEFICIADOS) != "0":
        texto += """
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong> BENEFICIARIOS: </strong> """ + str(row.BENEFICIADOS) + """</p>
                """
    texto += """              
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> ACTIVIDAD: </strong>""" + str(row.ACTIVIDAD) +"""</p>
    """

    if str(row.FOTO) != "0" or 0:
        texto += """
                <img src='""" + str(row.FOTO) + """' width='250' height='180'/>
        """

    texto += """
            </div> 
                <div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGAR") + """
                </div>
        </article>
        """

    return texto


