from RS import genera_rs

def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }

def genera_tarjeta(MUNICIPIO,FECHA, MECANISMO,PERSONAS, ACCIONES,FOTO1,ALBUM,COMENTARIO):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong>Fecha: </strong>""" + FECHA + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i>""" + MECANISMO + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class ="fa fa-user" style = "color:#FAC63A;"></i><strong> Personas capacitadas: </strong>""" + PERSONAS + """</p>
                <p style="color:#FFFFFF; margin: 0px;">""" + ACCIONES + """</p>
        """
    if FOTO1 != "0":
        texto += """
                        <img src='""" + FOTO1 + """' width='250' height='180'/>
                """
    if COMENTARIO != "0":
        texto+="""
             <p style="color:#FFFFFF; margin: 0px;">"""+COMENTARIO+"""</p>"""
    texto += """
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SEDEMA") + """
                </div>
            </div>
        </article>
        """

    return texto


